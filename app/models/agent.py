"""
AI Agent SQLAlchemy model for Project Chimera.
"""
from sqlalchemy import Column, Integer, String, Float, DateTime, JSON, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime

from app.models.base import Base, generate_uuid


class Agent(Base):
    """AI Agent model."""
    __tablename__ = "agents"

    id = Column(String, primary_key=True, default=generate_uuid)
    name = Column(String, nullable=False)
    persona_id = Column(String, nullable=False)
    wallet_address = Column(String, unique=True)

    soul_md_path = Column(String, nullable=False)
    voice_traits = Column(JSON, default=list)
    directives = Column(JSON, default=list)

    is_active = Column(Boolean, default=True)
    daily_budget = Column(Float, default=50.0)
    spent_today = Column(Float, default=0.0)

    total_posts = Column(Integer, default=0)
    total_engagement = Column(Integer, default=0)
    total_revenue = Column(Float, default=0.0)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    campaigns = relationship("Campaign", back_populates="agent")
    content = relationship("Content", back_populates="agent")
    transactions = relationship("Transaction", back_populates="agent")
