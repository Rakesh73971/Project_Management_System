from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app import models
from .ai_service import generate_project_summary

router = APIRouter(
    prefix="/ai",
    tags=["AI"]
)

# UPDATE: Added 'async' to the route definition
@router.get("/project-report/{project_id}")
async def project_report(project_id: int, db: Session = Depends(get_db)):
    
    # Query the database
    tasks = db.query(models.Task).filter(
        models.Task.project_id == project_id
    ).all()

    if not tasks:
        raise HTTPException(status_code=404, detail="No tasks found for this project")

    total_tasks = len(tasks)
    completed = len([t for t in tasks if t.status == "completed"])
    in_progress = len([t for t in tasks if t.status == "in-progress"])
    pending = len([t for t in tasks if t.status == "pending"])
    
    # Prevent division by zero just in case
    progress = int((completed / total_tasks) * 100) if total_tasks > 0 else 0

    # UPDATE: Build a richer task list for the AI, including priority.
    # We also slice it [:50] to ensure we don't overload the prompt if the project is massive.
    task_list = "\n".join([
        f"- [{task.priority.upper()}] {task.title} (Status: {task.status})" 
        for task in tasks[:50]
    ])

    # UPDATE: Added 'await' because our AI function is now async
    ai_summary = await generate_project_summary(
        total_tasks,
        completed,
        in_progress,
        pending,
        task_list
    )

    return {
        "project_id": project_id,
        "metrics": {
            "total_tasks": total_tasks,
            "completed": completed,
            "in_progress": in_progress,
            "pending": pending,
            "progress_percentage": progress
        },
        "ai_summary": ai_summary
    }