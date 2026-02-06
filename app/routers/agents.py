"""
Project Chimera: Agents API (stub for production expansion)
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()


class AgentCreate(BaseModel):
    name: str
    persona_id: str
    niche: Optional[str] = None


class AgentResponse(BaseModel):
    id: str
    name: str
    persona_id: str
    status: str = "active"


@router.get("", response_model=List[AgentResponse])
@router.get("/", response_model=List[AgentResponse])
async def list_agents():
    """List agents (stub)."""
    return []


@router.post("", response_model=AgentResponse)
@router.post("/", response_model=AgentResponse)
async def create_agent(body: AgentCreate):
    """Create agent (stub)."""
    return AgentResponse(
        id="stub-1",
        name=body.name,
        persona_id=body.persona_id,
        status="active",
    )


@router.get("/{agent_id}", response_model=AgentResponse)
async def get_agent(agent_id: str):
    """Get agent by id (stub)."""
    raise HTTPException(status_code=404, detail="Not implemented")
