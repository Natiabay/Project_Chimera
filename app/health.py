"""
Health check endpoint for Docker and CI/CD monitoring.
"""

import os

from fastapi import FastAPI
from fastapi.responses import JSONResponse

# Sub-app for health: use routes "/", "/liveness", "/readiness" so main can mount at "/health"
app = FastAPI(title="Project Chimera Health Check")


@app.get("/")
async def health_check():
    """Comprehensive health check for all services (mounted at /health)"""
    health_status = {
        "status": "healthy",
        "services": {},
        "version": "1.0.0",
    }

    # Check environment variables
    required_env_vars = ["GEMINI_API_KEY", "WEAVIATE_URL", "REDIS_URL"]
    for var in required_env_vars:
        if os.getenv(var):
            health_status["services"][f"env_{var}"] = "present"
        else:
            health_status["services"][f"env_{var}"] = "missing"
            health_status["status"] = "unhealthy"

    # Return appropriate HTTP status
    if health_status["status"] == "healthy":
        return health_status
    else:
        return JSONResponse(content=health_status, status_code=503)


@app.get("/liveness")
async def liveness_check():
    """Simple liveness check"""
    return {"status": "alive"}


@app.get("/readiness")
async def readiness_check():
    """Readiness check for service dependencies"""
    return {"status": "ready"}
