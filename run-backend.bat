@echo off
cd backend
call venv\Scripts\activate
echo Starting Backend Server...
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
