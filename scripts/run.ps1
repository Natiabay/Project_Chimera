# Start Project Chimera API (PowerShell) — run from repo root
Set-Location (Join-Path $PSScriptRoot "..")
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
