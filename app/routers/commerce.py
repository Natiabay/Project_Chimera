"""
Project Chimera: Commerce / transactions API (stub for production expansion)
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()


class TransactionCreate(BaseModel):
    agent_id: str
    transaction_type: str = "transfer"
    amount: float
    to_address: Optional[str] = None
    purpose: Optional[str] = None


class TransactionResponse(BaseModel):
    id: str
    agent_id: str
    transaction_type: str
    amount: float
    status: str = "pending"


@router.get("", response_model=List[TransactionResponse])
@router.get("/", response_model=List[TransactionResponse])
async def list_transactions(agent_id: Optional[str] = None):
    """List transactions (stub)."""
    return []


@router.post("", response_model=TransactionResponse)
@router.post("/", response_model=TransactionResponse)
async def create_transaction(body: TransactionCreate):
    """Create transaction (stub)."""
    return TransactionResponse(
        id="stub-1",
        agent_id=body.agent_id,
        transaction_type=body.transaction_type,
        amount=body.amount,
        status="pending",
    )
