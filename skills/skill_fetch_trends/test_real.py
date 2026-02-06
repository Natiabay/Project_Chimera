#!/usr/bin/env python3
"""
REAL test that actually runs with environment variables.
Run from project root: uv run python -m skills.skill_fetch_trends.test_real
Or: uv run python skills/skill_fetch_trends/test_real.py
"""
import asyncio
import os
import sys
from pathlib import Path

# Ensure project root is on path
_root = Path(__file__).resolve().parent.parent.parent
if str(_root) not in sys.path:
    sys.path.insert(0, str(_root))

# Load REAL environment variables from project root .env
try:
    from dotenv import load_dotenv
    load_dotenv(_root / ".env")
except ImportError:
    pass


async def real_test() -> None:
    """ACTUAL working test."""
    from skills.skill_fetch_trends import fetch_trends

    print("🔍 Testing REAL trend fetcher...")
    print(f"WEAVIATE_URL: {os.getenv('WEAVIATE_URL', 'Not set')}")
    print(f"NEWSDATA_API_KEY: {'Set' if os.getenv('NEWSDATA_API_KEY') else 'Not set'}")

    try:
        result = await fetch_trends("fashion", "24h", location="US")
        print(f"✅ Test completed: {result.get('status', 'unknown')}")
        trends = result.get("trends", [])
        print(f"📊 Trends found: {len(trends)}")

        if trends:
            print(f"📈 Top trend: {trends[0].get('topic', '')}")
            print(f"   relevance_score: {trends[0].get('relevance_score')}")
        print(f"   trend_alert: {result.get('trend_alert')}")

    except Exception as e:
        print(f"❌ Test failed: {e}")
        print("💡 To fix: Set WEAVIATE_URL and WEAVIATE_API_KEY in .env (optional: NEWSDATA_API_KEY)")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(real_test())
