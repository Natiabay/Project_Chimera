"""
Blockchain transaction SQLAlchemy model for Project Chimera.
"""
from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from app.models.base import Base, generate_uuid


class Transaction(Base):
    """Blockchain transaction model."""
    __tablename__ = "transactions"

    id = Column(String, primary_key=True, default=generate_uuid)
    agent_id = Column(String, ForeignKey("agents.id"), nullable=False)

    transaction_type = Column(String, nullable=False)
    network = Column(String, default="base")
    token_symbol = Column(String, default="USDC")

    amount = Column(Float, nullable=False)
    gas_used = Column(Float)
    gas_price = Column(Float)

    from_address = Column(String)
    to_address = Column(String)
    contract_address = Column(String)

    transaction_hash = Column(String, unique=True)
    block_number = Column(Integer)
    status = Column(String, default="pending")

    cfo_approved = Column(Boolean, default=False)
    budget_check_passed = Column(Boolean, default=False)
    anomaly_detected = Column(Boolean, default=False)

    purpose = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)
    confirmed_at = Column(DateTime)

    agent = relationship("Agent", back_populates="transactions")
