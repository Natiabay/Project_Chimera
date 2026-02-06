"""
Project Chimera: Trends API (real skill_fetch_trends integration)
"""
from fastapi import APIRouter, HTTPException, Query
from typing import Optional

router = APIRouter()


@router.get("")
@router.get("/")
async def list_trends(
    niche: str = Query(..., description="Topic e.g. fashion, crypto"),
    time_window: str = Query("24h", description="4h, 24h, 7d, 30d"),
    location: Optional[str] = Query(None, description="Country code e.g. US"),
):
    """Fetch real trends via NewsData.io and cache."""
    try:
        from skills.skill_fetch_trends import fetch_trends
        result = await fetch_trends(niche=niche, time_window=time_window, location=location)
        return result
    except Exception as e:
        raise HTTPException(status_code=503, detail=str(e))


@router.get("/{niche}")
async def get_trends_by_niche(
    niche: str,
    time_window: str = Query("24h"),
    location: Optional[str] = None,
):
    """Fetch trends for a niche (path version)."""
    try:
        from skills.skill_fetch_trends import fetch_trends
        result = await fetch_trends(niche=niche, time_window=time_window, location=location)
        return result
    except Exception as e:
        raise HTTPException(status_code=503, detail=str(e))
