#!/usr/bin/env python3
"""
Generate OpenAPI schema from FastAPI app. Output: specs/openapi.yaml
Linked from specs/technical.md for Executable Spec Fidelity.
"""
import json
import sys
from pathlib import Path

# Project root
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

def main():
    from app.main import app
    schema = app.openapi()
    out = ROOT / "specs" / "openapi.json"
    with open(out, "w") as f:
        json.dump(schema, f, indent=2)
    print(f"Wrote {out}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
