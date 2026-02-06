"""
Project Chimera: AI model loading and health checks.
"""
import logging
from typing import Any, Dict

logger = logging.getLogger(__name__)


async def load_models():
    """Load or verify AI model clients (Gemini, etc.)."""
    import os
    if os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY"):
        logger.info("AI model config present (Gemini)")
    else:
        logger.warning("No GEMINI_API_KEY / GOOGLE_API_KEY set")


async def check_model_health() -> Dict[str, Any]:
    """Check AI model API availability."""
    import os
    key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if key and not key.startswith("test_") and "xxx" not in key.lower():
        return {"status": "configured", "provider": "gemini"}
    return {"status": "not_configured", "message": "Set GEMINI_API_KEY or GOOGLE_API_KEY"}
