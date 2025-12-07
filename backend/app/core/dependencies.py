"""FastAPI Dependencies"""
from fastapi import Depends, HTTPException, status
from app.database import get_db

async def get_current_user(token: str = None):
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return {"user_id": 1}
