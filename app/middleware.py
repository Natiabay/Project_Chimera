"""
Project Chimera: Request logging and metrics middleware
"""
import time
import logging
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

from app.metrics import request_counter, response_time_histogram

logger = logging.getLogger(__name__)


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    """Log requests and record Prometheus metrics."""

    async def dispatch(self, request: Request, call_next):
        start = time.perf_counter()
        method = request.method
        path = request.url.path or "/"
        # Normalize path for metrics (avoid high cardinality)
        endpoint = path if path.startswith("/api/") else path.split("/")[1] or "root"
        if endpoint and endpoint[0] != "/":
            endpoint = "/" + endpoint
        status = 500
        try:
            response = await call_next(request)
            status = response.status_code
            return response
        finally:
            duration = time.perf_counter() - start
            request_counter.labels(method=method, endpoint=endpoint, status=status).inc()
            response_time_histogram.labels(method=method, endpoint=endpoint).observe(duration)
            logger.info("%s %s %s %.3fs", method, path, status, duration)
