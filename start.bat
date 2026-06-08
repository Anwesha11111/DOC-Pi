@echo off
cd /d "%~dp0"
echo ============================================
echo  DOCP Backend Starter
echo ============================================
echo.
echo [1/2] Loading demo documents...
"%~dp0.venv\Scripts\python.exe" "%~dp0load_demo_docs.py"
echo.
echo [2/2] Starting server on http://localhost:8000
echo  (Keep this window open while using the app)
echo.
"%~dp0.venv\Scripts\uvicorn.exe" app.main:app --port 8000
pause
