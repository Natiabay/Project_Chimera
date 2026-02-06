"""
DEPRECATED: Use app.models instead.
Re-export for backward compatibility. Will be removed in a future release.
"""
from app.models import (
    Base,
    generate_uuid,
    Agent,
    Campaign,
    Task,
    Content,
    Transaction,
)

__all__ = ["Base", "generate_uuid", "Agent", "Campaign", "Task", "Content", "Transaction"]
