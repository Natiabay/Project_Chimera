# News MCP Server (Runtime)

Runtime MCP for trend monitoring. Conforms to [specs/mcp_interface_schema.json](../../specs/mcp_interface_schema.json).

- **Tools:** `fetch_headlines`, `analyze_trends`
- **Resources:** `news://[niche]/latest`
- **Env:** `NEWSDATA_API_KEY` (optional; stub works without)

Run: `uv run python server.py` (from this directory) or via MCP config.
