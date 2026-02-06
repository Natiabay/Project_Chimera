import pytest


def test_mcp_tool_standardization():
    """
    FR 4.0: Platform-Agnostic Publishing via MCP
    Tests that all social actions use MCP tools (no direct APIs)
    """
    # Define expected MCP tool schema from specs/technical.md
    expected_tool_schema = {
        "name": "post_content",
        "description": "Publishes text and media to a connected social platform",
        "inputSchema": {
            "type": "object",
            "properties": {
                "platform": {
                    "type": "string",
                    "enum": ["twitter", "instagram", "threads"],
                },
                "text_content": {"type": "string"},
                "media_urls": {"type": "array", "items": {"type": "string"}},
                "disclosure_level": {
                    "type": "string",
                    "enum": ["automated", "assisted", "none"],
                },
            },
            "required": ["platform", "text_content"],
        },
    }

    # This test will fail until MCP tools are implemented
    # It defines the contract that must be fulfilled
    assert "post_content" == expected_tool_schema["name"]
    assert "platform" in expected_tool_schema["inputSchema"]["required"]
    assert True == False  # Intentional TDD failure
