#!/usr/bin/env bash
# Project Chimera — initial setup (development)
set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$ROOT"

echo "Setting up Project Chimera..."
if ! command -v python3 &>/dev/null; then
  echo "Python 3 required. Install from https://python.org"
  exit 1
fi
if ! command -v uv &>/dev/null; then
  pip install uv
fi
uv sync
if [ ! -f .env ]; then
  cp .env.example .env
  echo "Created .env from .env.example — add your API keys."
fi
echo "Run API: uv run uvicorn app.main:app --reload"
echo "Run tests: uv run pytest tests/ -v"
