"""
Production FastAPI server for Project Chimera
"""
from contextlib import asynccontextmanager
from datetime import datetime
import logging

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, Response

from app.config import settings
from app.routers import trends, agents, content, commerce
from app.middleware import RequestLoggingMiddleware
from app.database import init_db, close_db, check_db_health
from app.models.ai_models import load_models, check_model_health

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan events for startup/shutdown."""
    logger.info("🚀 Starting Project Chimera API")
    await init_db()
    await load_models()
    yield
    logger.info("🛑 Shutting down Project Chimera API")
    try:
        from skills.skill_fetch_trends import cleanup
        await cleanup()
    except Exception as e:
        logger.warning(f"Skill cleanup: {e}")
    await close_db()


app = FastAPI(
    title="Project Chimera API",
    description="Autonomous Influencer Network Platform",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(RequestLoggingMiddleware)

# Include routers
app.include_router(trends.router, prefix="/api/v1/trends", tags=["trends"])
app.include_router(agents.router, prefix="/api/v1/agents", tags=["agents"])
app.include_router(content.router, prefix="/api/v1/content", tags=["content"])
app.include_router(commerce.router, prefix="/api/v1/commerce", tags=["commerce"])


@app.get("/")
async def root():
    """Root and health info."""
    return {
        "status": "online",
        "service": "Project Chimera",
        "version": "1.0.0",
        "endpoints": {
            "docs": "/docs",
            "health": "/health",
            "trends": "/api/v1/trends",
            "agents": "/api/v1/agents",
            "content": "/api/v1/content",
            "commerce": "/api/v1/commerce",
        },
    }


@app.get("/health")
async def health_check():
    """Comprehensive health check."""
    health_status = {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "services": {},
    }

    db_health = await check_db_health()
    health_status["services"]["database"] = db_health

    model_health = await check_model_health()
    health_status["services"]["ai_models"] = model_health

    try:
        from skills.skill_fetch_trends import get_fetcher
        await get_fetcher()
        health_status["services"]["news_api"] = "connected"
    except Exception as e:
        health_status["services"]["news_api"] = "disconnected"
        health_status["status"] = "degraded"
        health_status["services"]["news_api_error"] = str(e)

    if health_status["status"] != "healthy":
        return JSONResponse(content=health_status, status_code=503)
    return health_status


@app.get("/metrics")
async def metrics():
    """Prometheus metrics endpoint."""
    from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
    return Response(
        content=generate_latest(),
        media_type=CONTENT_TYPE_LATEST,
    )


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(status_code=exc.status_code, content={"error": exc.detail})


@app.exception_handler(Exception)
async def generic_exception_handler(request, exc):
    logger.error("Unhandled exception: %s", exc, exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error"},
    )


__all__ = ["app"]
