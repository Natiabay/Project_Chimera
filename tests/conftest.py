import pytest
import os


@pytest.fixture
def sample_soul_md_content():
    """Fixture providing sample SOUL.md content for testing"""
    return """---
name: "Alex Crypto"
id: "influencer_001"
voice_traits: ["witty", "technical", "gen-z"]
directives: ["Never discuss politics", "Always disclose AI nature", "Sustainability-focused"]
---

## Backstory
A crypto-native virtual influencer created in 2025.
Expert in Web3 trends and sustainable fashion.
Speaks 5 languages and connects with global youth culture.
"""


@pytest.fixture
def mock_mcp_server():
    """Fixture to mock MCP server responses"""
    return {
        "tools": ["post_content", "get_mentions", "search_memory"],
        "resources": ["twitter://mentions/recent", "news://latest"],
    }
