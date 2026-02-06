"""
Project Chimera: Content API (stub for production expansion)
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()


class ContentCreate(BaseModel):
    agent_id: str
    content_type: str = "text"
    platform: str = "twitter"
    text_content: Optional[str] = None


class ContentResponse(BaseModel):
    id: str
    agent_id: str
    content_type: str
    platform: str
    status: str = "draft"


@router.get("", response_model=List[ContentResponse])
@router.get("/", response_model=List[ContentResponse])
async def list_content(agent_id: Optional[str] = None):
    """List content (stub)."""
    return []


@router.post("", response_model=ContentResponse)
@router.post("/", response_model=ContentResponse)
async def create_content(body: ContentCreate):
    """Create content (stub)."""
    return ContentResponse(
        id="stub-1",
        agent_id=body.agent_id,
        content_type=body.content_type,
        platform=body.platform,
        status="draft",
    )
