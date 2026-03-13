import logging
import google.generativeai as genai
from app.config import settings

genai.configure(api_key=settings.gemini_api_key)

# UPDATE: Make sure to use the latest active model to avoid 404 errors!
model = genai.GenerativeModel("gemini-2.5-flash")

# UPDATE: Added 'async' keyword
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
        # UPDATE: Use the async generation method so it doesn't block FastAPI
        response = await model.generate_content_async(prompt)
        return response.text.strip()
    except Exception as e:
        # Log the actual error for your debugging, but return a safe string to the user
        logging.error(f"Failed to generate AI summary: {str(e)}")
        return "AI summary is currently unavailable. Please refer to the raw metrics."