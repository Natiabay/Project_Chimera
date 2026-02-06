# Skill: Fetch Trends

## SRS Reference: FR 2.0, FR 2.2

## Purpose
Monitor MCP Resources for trends and generate Trend Alerts for Planner.

## Input Contract

```json
{
  "niche": "string (e.g., fashion, crypto)",
  "time_window": "4h | 24h | 7d",
  "location": "optional string (e.g., Ethiopia)",
  "relevance_threshold": "float (default: 0.75)"
}
```

## Output Contract

```json
{
  "trends": [
    {
      "topic": "string",
      "volume_change": "float",
      "relevance_score": "float 0-1",
      "source_resources": ["mcp://news/latest", "mcp://twitter/trending"]
    }
  ],
  "trend_alert": "boolean (true if cluster detected)"
}
```

## MCP Dependencies
- **mcp-server-twitter**: For trending topics
- **mcp-server-news**: For news aggregation
- **mcp-server-weaviate**: For semantic trend analysis

## Worker Implementation Notes
- Runs as background process every 4 hours (FR 2.2)
- Uses Gemini 3 Flash for semantic filtering (FR 2.1)
- Only triggers Planner if relevance > threshold
