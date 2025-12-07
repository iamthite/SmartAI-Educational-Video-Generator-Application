@echo off
cd backend
call venv\Scripts\activate
echo Starting Celery Worker...
celery -A app.core.celery_app worker --loglevel=info
