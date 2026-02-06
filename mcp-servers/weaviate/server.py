"""
Project Chimera: Weaviate MCP Server
Connects to Weaviate Cloud and exposes memories as tools and resources.
"""

import asyncio
import json
import os
from datetime import datetime
from typing import Any

from mcp.server.fastmcp import FastMCP
import weaviate
from weaviate.classes.init import Auth

# MCP server instance
mcp = FastMCP(
    "weaviate-server",
    description="Weaviate vector database for agent memories (Project Chimera)",
)

# Collection name for agent memories (SRS FR 1.1)
AGENT_MEMORY_COLLECTION = "AgentMemory"


def _get_weaviate_client() -> weaviate.WeaviateClient:
    """Connect to Weaviate Cloud using env credentials."""
    url = (os.getenv("WEAVIATE_URL") or "").strip()
    if not url:
        raise ValueError("WEAVIATE_URL environment variable is required")
    if not url.startswith("http"):
        url = "https://" + url

    api_key = (os.getenv("WEAVIATE_API_KEY") or "").strip()
    if not api_key:
        raise ValueError("WEAVIATE_API_KEY environment variable is required")

    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=url,
        auth_credentials=Auth.api_key(api_key),
    )
    return client


def _search_memories_sync(query: str, limit: int = 5, agent_id: str | None = None) -> str:
    """Sync semantic search in Weaviate (runs in thread for async)."""
    client = _get_weaviate_client()
    try:
        if not client.is_ready():
            return json.dumps({"error": "Weaviate client not ready"})

        collection = client.collections.get(AGENT_MEMORY_COLLECTION)
        response = collection.query.near_text(query=query, limit=limit)

        items = []
        for obj in response.objects:
            props = dict(obj.properties) if obj.properties else {}
            props["uuid"] = str(obj.uuid)
            if agent_id and props.get("agent_id") != agent_id:
                continue
            items.append(props)

        return json.dumps({"memories": items}, default=str)
    except weaviate.exceptions.WeaviateConnectionError as e:
        return json.dumps({"error": f"Connection failed: {e}"})
    except Exception as e:
        return json.dumps({"error": str(e)})
    finally:
        client.close()


def _fetch_recent_memories_sync(limit: int = 10) -> str:
    """Sync fetch recent memories (runs in thread for async)."""
    client = _get_weaviate_client()
    try:
        if not client.is_ready():
            return json.dumps({"error": "Weaviate client not ready"})

        collection = client.collections.get(AGENT_MEMORY_COLLECTION)
        # Fetch objects; sort by timestamp if available (depends on schema)
        response = collection.query.fetch_objects(limit=limit)

        items = []
        for obj in response.objects:
            props = dict(obj.properties) if obj.properties else {}
            props["uuid"] = str(obj.uuid)
            items.append(props)

        return json.dumps({"memories": items}, default=str)
    except weaviate.exceptions.WeaviateConnectionError as e:
        return json.dumps({"error": f"Connection failed: {e}"})
    except Exception as e:
        return json.dumps({"error": str(e)})
    finally:
        client.close()


def _store_memory_sync(agent_id: str, content: str, memory_type: str = "episodic") -> str:
    """Sync store one memory (runs in thread for async)."""
    client = _get_weaviate_client()
    try:
        if not client.is_ready():
            return json.dumps({"error": "Weaviate client not ready"})

        collection = client.collections.get(AGENT_MEMORY_COLLECTION)
        properties = {
            "agent_id": agent_id,
            "content": content,
            "memory_type": memory_type,
            "timestamp": datetime.utcnow().isoformat() + "Z",
        }
        uuid = collection.data.insert(properties)
        return json.dumps({"status": "ok", "uuid": str(uuid), "agent_id": agent_id})
    except weaviate.exceptions.WeaviateConnectionError as e:
        return json.dumps({"error": f"Connection failed: {e}"})
    except Exception as e:
        return json.dumps({"error": str(e)})
    finally:
        client.close()


# ---- MCP Tools ----


@mcp.tool()
async def search_memories(
    query: str,
    limit: int = 5,
    agent_id: str | None = None,
) -> str:
    """Search agent memories by semantic similarity (Weaviate near_text)."""
    return await asyncio.to_thread(_search_memories_sync, query, limit, agent_id)


@mcp.tool()
async def store_memory(
    agent_id: str,
    content: str,
    memory_type: str = "episodic",
) -> str:
    """Store a new memory for an agent in Weaviate."""
    return await asyncio.to_thread(_store_memory_sync, agent_id, content, memory_type)


# ---- MCP Resource ----


@mcp.resource("weaviate://memories/recent")
async def weaviate_memories_recent() -> str:
    """Recent agent memories from Weaviate (resource for MCP clients)."""
    return await asyncio.to_thread(_fetch_recent_memories_sync, 10)


if __name__ == "__main__":
    # Run with stdio (default for Cursor/IDE MCP)
    mcp.run(transport="stdio")
