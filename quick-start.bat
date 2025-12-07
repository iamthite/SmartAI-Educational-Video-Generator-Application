REM ============================================
REM quick-start.bat - Start Everything
REM ============================================
@echo off
echo ========================================
echo Quick Start - EduVideoGen
echo ========================================
echo.

echo Opening 2 terminal windows:
echo   1. Backend Server
echo   2. Frontend Server
echo.

start "Backend Server" cmd /k "cd backend && venv\Scripts\activate && uvicorn app.main:app --reload --host 0.0.0.0 --port 8000"

timeout /t 3

start "Frontend Server" cmd /k "cd frontend && npm run dev"

echo.
echo Servers starting...
echo Wait 10 seconds, then open: http://localhost:3000
echo.
echo Backend API Docs: http://localhost:8000/docs
echo.
pause