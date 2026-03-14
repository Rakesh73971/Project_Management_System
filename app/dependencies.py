from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from . import models, database, oauth2

def get_current_admin(
    project_id: int, 
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(oauth2.get_current_user)
):
    # 1. Find the project to get the Org ID
    project = db.query(models.Project).filter(models.Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    membership = db.query(models.OrganizationMember).filter(
        models.OrganizationMember.user_id == current_user.id,
        models.OrganizationMember.organization_id == project.organizationId
    ).first()

    if not membership or membership.role.lower() != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied: Only Organization Admins can trigger AI operations."
        )
    
    return current_user