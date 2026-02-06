"""
Marketing campaign SQLAlchemy model for Project Chimera.
"""
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from app.models.base import Base, generate_uuid


class Campaign(Base):
    """Marketing campaign model."""
    __tablename__ = "campaigns"

    id = Column(String, primary_key=True, default=generate_uuid)
    agent_id = Column(String, ForeignKey("agents.id"), nullable=False)

    name = Column(String, nullable=False)
    description = Column(String)
    goal = Column(String, nullable=False)
    niche = Column(String, nullable=False)
    location = Column(String)

    total_budget = Column(Float, default=100.0)
    spent_budget = Column(Float, default=0.0)
    start_date = Column(DateTime)
    end_date = Column(DateTime)

    status = Column(String, default="draft")
    confidence_threshold = Column(Float, default=0.75)

    target_impressions = Column(Integer)
    achieved_impressions = Column(Integer, default=0)
    engagement_rate = Column(Float, default=0.0)

    created_at = Column(DateTime, default=datetime.utcnow)

    agent = relationship("Agent", back_populates="campaigns")
    tasks = relationship("Task", back_populates="campaign")
    content = relationship("Content", back_populates="campaign")
