import logging
import google.generativeai as genai
from app.config import settings
import json

genai.configure(api_key=settings.gemini_api_key)


model = genai.GenerativeModel("gemini-2.5-flash")


async def generate_project_summary(total_tasks, completed, in_progress, pending, task_list):
    prompt = f"""
    You are an expert technical project manager analyzing a project's health.
    
    Project metrics:
    - Total: {total_tasks} | Completed: {completed} | In Progress: {in_progress} | Pending: {pending}
    
    Recent/Active Tasks Context:
    {task_list}
    
    Task: Write a concise executive summary (maximum 3 sentences). 
    Focus on the overall progress, highlight any high-priority tasks that are pending or stuck, and suggest a quick next step.
    """
    
    try:
        
        response = await model.generate_content_async(prompt)
        return response.text.strip()
    except Exception as e:
        
        logging.error(f"Failed to generate AI summary: {str(e)}")
        return "AI summary is currently unavailable. Please refer to the raw metrics."
    

async def generate_project_tasks(project_prompt: str, available_users: str):
    prompt = f"""
    You are an expert Technical Project Manager.
    A user wants to add this feature: "{project_prompt}"
    
    Break this down into 3 to 6 actionable tasks.
    
    AVAILABLE TEAM MEMBERS:
    {available_users}
    
    RULES:
    1. Respond STRICTLY with a valid JSON array of objects.
    2. Distribute the workload evenly among the available team members.
    3. Each object MUST have these exact keys: 
       - "title" (string)
       - "description" (string)
       - "priority" ("low", "medium", or "high")
       - "assigned_to" (integer - MUST be one of the IDs from the team members list above).
    """
    
    try:
        response = await model.generate_content_async(
            prompt,
            generation_config={"response_mime_type": "application/json"}
        )
        return json.loads(response.text.strip())
    except Exception as e:
        logging.error(f"AI generation failed: {str(e)}")
        return None
    
async def assign_task_with_ai(task_title: str, task_desc: str, users_context: str):
    """
    Asks Gemini to match a task to the best user based on their skills.
    """
    prompt = f"""
    You are an intelligent Engineering Manager routing tasks to the best team member.
    
    TASK TO ASSIGN:
    Title: {task_title}
    Description: {task_desc}
    
    AVAILABLE TEAM MEMBERS:
    {users_context}
    
    RULES:
    1. Analyze the task and match it to the team member whose "Role" and "Skills" best fit the technical requirements.
    2. Respond STRICTLY with a valid JSON object.
    3. The JSON MUST contain exactly two keys:
       - "assigned_to": (integer) The exact ID of the chosen team member.
       - "reason": (string) A short 1-sentence explanation of why they were chosen based on their tech stack.
    """
    
    try:
        response = await model.generate_content_async(
            prompt,
            generation_config={"response_mime_type": "application/json"}
        )
        return json.loads(response.text.strip())
    except Exception as e:
        logging.error(f"AI task routing failed: {str(e)}")
        return None