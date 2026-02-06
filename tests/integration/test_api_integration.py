"""
API integration tests: FastAPI endpoints with real or test client.
Ref: specs/functional.md, NFR (health, root). TDD: contract for API shape.
"""
import pytest
from httpx import ASGITransport, AsyncClient

# Import app after env is ready
pytestmark = pytest.mark.asyncio


async def test_health_endpoint():
    """Health endpoint returns 200 and status."""
    from app.main import app
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test",
    ) as client:
        r = await client.get("/health")
    assert r.status_code in (200, 503)
    data = r.json()
    assert "status" in data
    assert "services" in data


async def test_root_endpoint():
    """Root returns service info."""
    from app.main import app
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test",
    ) as client:
        r = await client.get("/")
    assert r.status_code == 200
    data = r.json()
    assert data.get("service") == "Project Chimera"
    assert "status" in data
