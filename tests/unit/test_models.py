"""
Unit tests for app.models (SQLAlchemy and domain models).
"""
import pytest
from app.models import Base, generate_uuid, Agent, Campaign, Task, Content, Transaction
from app.models.base import Base as BaseCls


def test_generate_uuid():
    """generate_uuid returns a string UUID."""
    u = generate_uuid()
    assert isinstance(u, str)
    assert len(u) == 36
    assert u.count("-") == 4


def test_base_declarative():
    """Base is SQLAlchemy declarative base."""
    assert Base is not None
    assert BaseCls is Base


def test_agent_table_name():
    """Agent model has correct tablename."""
    assert Agent.__tablename__ == "agents"


def test_campaign_table_name():
    """Campaign model has correct tablename."""
    assert Campaign.__tablename__ == "campaigns"


def test_task_table_name():
    """Task model has correct tablename."""
    assert Task.__tablename__ == "tasks"


def test_content_table_name():
    """Content model has correct tablename."""
    assert Content.__tablename__ == "content"


def test_transaction_table_name():
    """Transaction model has correct tablename."""
    assert Transaction.__tablename__ == "transactions"
