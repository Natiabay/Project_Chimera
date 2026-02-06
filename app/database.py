"""
Project Chimera: Database connections and health checks
"""
import os
import logging
from typing import Any, Dict

logger = logging.getLogger(__name__)

# Optional SQLAlchemy engine (lazy init)
_engine = None


def get_engine():
    """Create or return SQLAlchemy engine (sync)."""
    global _engine
    if _engine is not None:
        return _engine
    try:
        from sqlalchemy import create_engine
        from app.models import Base
        url = os.getenv("POSTGRES_URL", "postgresql://localhost:5432/chimera")
        _engine = create_engine(url, pool_pre_ping=True)
        return _engine
    except Exception as e:
        logger.warning(f"Database engine not created: {e}")
        return None


async def init_db():
    """Initialize database connections (create tables if needed)."""
    engine = get_engine()
    if engine is None:
        return
    try:
        from app.models import Base
        Base.metadata.create_all(bind=engine)
        logger.info("Database tables ready")
    except Exception as e:
        logger.warning(f"init_db: {e}")


async def close_db():
    """Close database connections."""
    global _engine
    if _engine is not None:
        try:
            _engine.dispose()
        except Exception as e:
            logger.warning(f"close_db: {e}")
        _engine = None


def _check_db_health_sync() -> Dict[str, Any]:
    """Sync database connectivity check (SQLAlchemy 2.0)."""
    from sqlalchemy import text
    engine = get_engine()
    if engine is None:
        return {"status": "unavailable", "error": "no engine"}
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return {"status": "healthy"}
    except Exception as e:
        return {"status": "unhealthy", "error": str(e)}


async def check_db_health() -> Dict[str, Any]:
    """Check database connectivity (async wrapper)."""
    import asyncio
    return await asyncio.to_thread(_check_db_health_sync)
