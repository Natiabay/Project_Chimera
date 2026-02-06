"""
Mock services for Project Chimera - Use when real API keys aren't available.
These provide realistic test data for the 3-Day Challenge.
"""

import os
from typing import Any, Dict, List
from datetime import datetime


class MockWeaviate:
    """Mock Weaviate vector database for testing"""

    @staticmethod
    def search_memory(query: str, limit: int = 5) -> List[Dict]:
        """Mock semantic memory search"""
        return [
            {"id": "1", "content": "Fashion trend: oversized blazers", "score": 0.89},
            {"id": "2", "content": "Summer 2025: pastel colors dominate", "score": 0.76},
            {"id": "3", "content": "Sustainable fashion is trending", "score": 0.92},
            {"id": "4", "content": "Gen-Z prefers vintage styles", "score": 0.81},
            {"id": "5", "content": "Digital fashion shows on rise", "score": 0.67},
        ]


class MockGemini:
    """Mock Gemini API for testing"""

    @staticmethod
    def generate_text(prompt: str) -> str:
        """Mock text generation"""
        responses = {
            "fashion": "Oversized blazers and pastel colors are trending this season.",
            "crypto": "Bitcoin volatility continues as ETF approvals expected.",
            "default": "This is mock generated content for testing purposes.",
        }

        for key in responses:
            if key in prompt.lower():
                return responses[key]
        return responses["default"]


class MockTwitterAPI:
    """Mock Twitter API for testing"""

    @staticmethod
    def get_mentions() -> List[Dict]:
        """Mock recent mentions"""
        return [
            {"id": "1", "user": "@fashion_lover", "text": "Love your style!"},
            {"id": "2", "user": "@crypto_enthusiast", "text": "What do you think about BTC?"},
            {"id": "3", "user": "@tech_guru", "text": "Great content as always!"},
        ]

    @staticmethod
    def post_tweet(text: str, media_urls: List[str] | None = None) -> Dict:
        """Mock tweet posting"""
        return {
            "id": "mock_tweet_123",
            "text": text,
            "posted_at": datetime.now().isoformat(),
            "status": "posted",
        }


class MockCoinbaseAgentKit:
    """Mock Coinbase AgentKit for testing"""

    def __init__(self) -> None:
        self.balance = 100.0  # Mock USDC balance
        self.daily_spent = 0.0

    def get_balance(self) -> float:
        """Mock wallet balance"""
        return self.balance

    def transfer(self, to_address: str, amount: float) -> Dict:
        """Mock transaction"""
        if amount > self.balance:
            return {"status": "failed", "reason": "Insufficient funds"}

        self.balance -= amount
        self.daily_spent += amount

        return {
            "status": "success",
            "transaction_hash": "0x_mock_tx_hash",
            "amount": amount,
            "to": to_address,
        }


def get_env_or_mock(key: str, default: Any = None) -> Any:
    """
    Get environment variable or return mock value for testing.
    This allows real keys when available, mock when not.
    """
    value = os.getenv(key)
    if value and not value.startswith("test_") and "test_key" not in value:
        return value  # Real key found

    # Return mock indicator
    print(f"⚠️  Using mock service for {key} (set real key in .env for production)")
    return f"MOCK_{key}"
