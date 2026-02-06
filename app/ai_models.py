"""
DEPRECATED: Use app.models.ai_models instead.
Re-export for backward compatibility. Will be removed in a future release.
"""
from app.models.ai_models import load_models, check_model_health

__all__ = ["load_models", "check_model_health"]
