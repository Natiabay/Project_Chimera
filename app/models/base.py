"""
SQLAlchemy declarative base and shared utilities for Project Chimera.
"""
import uuid
from sqlalchemy.orm import declarative_base

Base = declarative_base()


def generate_uuid() -> str:
    """Generate a UUID string for primary keys."""
    return str(uuid.uuid4())
