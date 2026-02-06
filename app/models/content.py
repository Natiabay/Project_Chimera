"""
Generated content SQLAlchemy model for Project Chimera.
"""
from sqlalchemy import Column, Integer, String, Float, DateTime, JSON, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from app.models.base import Base, generate_uuid


class Content(Base):
    """Generated content model."""
    __tablename__ = "content"

    id = Column(String, primary_key=True, default=generate_uuid)
    agent_id = Column(String, ForeignKey("agents.id"), nullable=False)
    campaign_id = Column(String, ForeignKey("campaigns.id"))

    content_type = Column(String, nullable=False)
    platform = Column(String, nullable=False)
    text_content = Column(String)
    media_urls = Column(JSON, default=list)

    generation_cost = Column(Float, default=0.0)
    model_used = Column(String)
    prompt_tokens = Column(Integer)
    completion_tokens = Column(Integer)

    published_at = Column(DateTime)
    post_id = Column(String)
    disclosure_flag = Column(Boolean, default=True)

    impressions = Column(Integer, default=0)
    likes = Column(Integer, default=0)
    shares = Column(Integer, default=0)
    comments = Column(Integer, default=0)

    consistency_score = Column(Float)
    brand_alignment_score = Column(Float)

    created_at = Column(DateTime, default=datetime.utcnow)

    agent = relationship("Agent", back_populates="content")
    campaign = relationship("Campaign", back_populates="content")
