"""
Planner-Worker-Judge task SQLAlchemy model for Project Chimera.
"""
from sqlalchemy import Column, Integer, String, Float, DateTime, JSON, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from app.models.base import Base, generate_uuid


class Task(Base):
    """Planner-Worker-Judge task model."""
    __tablename__ = "tasks"

    id = Column(String, primary_key=True, default=generate_uuid)
    campaign_id = Column(String, ForeignKey("campaigns.id"), nullable=False)

    task_type = Column(String, nullable=False)
    priority = Column(String, default="medium")
    status = Column(String, default="pending")

    input_data = Column(JSON)
    output_data = Column(JSON)

    assigned_worker = Column(String)
    started_at = Column(DateTime)
    completed_at = Column(DateTime)

    confidence_score = Column(Float)
    judge_decision = Column(String)
    human_reviewer = Column(String)

    retry_count = Column(Integer, default=0)
    error_message = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    campaign = relationship("Campaign", back_populates="tasks")
