# DOCP Backend - PowerShell starter
# Run from ANY directory - paths are resolved relative to this script
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$python = Join-Path $root ".venv\Scripts\python.exe"
$uvicorn = Join-Path $root ".venv\Scripts\uvicorn.exe"

Write-Host "============================================" -ForegroundColor Cyan
Write-Host " DOCP Backend Starter" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan

# Verify venv exists
if (-not (Test-Path $python)) {
    Write-Host "ERROR: .venv not found at $root\.venv" -ForegroundColor Red
    Write-Host "Run: python -m venv .venv && .venv\Scripts\pip install -r requirements.txt" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "`n[1/2] Loading demo documents (skips if already loaded)..." -ForegroundColor Yellow
& $python (Join-Path $root "load_demo_docs.py")

Write-Host "`n[2/2] Starting backend on http://localhost:8000 ..." -ForegroundColor Green
Write-Host "Keep this window open while using the app.`n" -ForegroundColor Gray
Set-Location $root
& $uvicorn app.main:app --port 8000
