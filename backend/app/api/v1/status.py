"""Task Status Routes"""
from fastapi import APIRouter, HTTPException
from app.core.celery_app import celery_app
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/task/{task_id}")
async def get_task_status(task_id: str):
    """Get status of a Celery task"""
    try:
        task = celery_app.AsyncResult(task_id)
        
        response = {
            "task_id": task_id,
            "status": task.state,
            "result": None
        }
        
        if task.state == "SUCCESS":
            response["result"] = task.result
        elif task.state == "FAILURE":
            response["error"] = str(task.info)
        elif task.state == "PROGRESS":
            response["progress"] = task.info
        
        return response
    except Exception as e:
        logger.error(f"Task status error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
