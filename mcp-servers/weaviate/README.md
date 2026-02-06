# Real Weaviate MCP Server

## Prerequisites

1. Create a **FREE** Weaviate cluster at https://console.weaviate.cloud/
   - Click **"Create Sandbox"** (free for 14 days)
   - Copy **Cluster URL** and **API Key**

2. Set environment variables:

```bash
export WEAVIATE_URL="https://your-cluster.weaviate.network"
export WEAVIATE_API_KEY="your-api-key-here"
export OPENAI_API_KEY="your-openai-key"  # For embeddings
```

## Create the AgentMemory collection

In Weaviate Cloud **Schema**, create a class named **AgentMemory** with at least:

| Property      | Type   | Description              |
|---------------|--------|--------------------------|
| `agent_id`    | string | Agent identifier         |
| `content`     | text   | Memory content           |
| `memory_type` | string | e.g. episodic, semantic  |
| `timestamp`   | date   | When stored              |

Enable a **vectorizer** (e.g. text2vec) so `near_text` search works.

## Run the server

```bash
cd mcp-servers/weaviate
uv run python server.py
```

Or from project root with env from `.env`:

```bash
cd /path/to/Project_Chimera
set -a && source .env && set +a   # Linux/macOS
uv run python mcp-servers/weaviate/server.py
```

**Note:** Default transport is **stdio** (for Cursor/IDE). For HTTP testing on a port, change `server.py` to use `mcp.run(transport="streamable-http")` and connect to the shown URL.

## Test with curl

If the server is run with **streamable-http** on port 3000:

```bash
# List resources
echo '{"jsonrpc":"2.0","method":"resources/list","id":1}' | nc localhost 3000

# Search memories
echo '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"search_memories","arguments":{"query":"fashion trends"}},"id":2}' | nc localhost 3000
```

With **stdio** transport (default), the server does not listen on a port; use the MCP Inspector or Cursor MCP client to test.

## Cursor / IDE

Add to `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "weaviate": {
      "command": "uv",
      "args": ["run", "python", "mcp-servers/weaviate/server.py"],
      "cwd": "<path-to-Project_Chimera>",
      "env": {
        "WEAVIATE_URL": "<your-cluster-url>",
        "WEAVIATE_API_KEY": "<your-api-key>"
      }
    }
  }
}
```

## Deployment

- Can run as **systemd** service
- **Docker** container available
- **Kubernetes** deployment ready
