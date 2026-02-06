# Tooling Strategy

**Runtime MCP interface contract:** [specs/mcp_interface_schema.json](../specs/mcp_interface_schema.json) — all Runtime MCP servers (weaviate, news, coinbase, twitter) conform to this schema.

## Developer MCP Servers (For YOU)
1. **git-mcp**: Version control automation
   - Auto-commit after successful tests
   - Branch management for feature development

2. **filesystem-mcp**: File operations
   - Create/read/update spec files
   - Manage skill directories

3. **docker-mcp**: Container management
   - Build/test Docker images
   - Local Kubernetes simulation

## Runtime MCP Servers (For Agents)
1. **mcp-server-twitter**: Social media integration
   - Tools: post_tweet, get_mentions, like_post
   - Resources: twitter://mentions/recent

2. **mcp-server-weaviate**: Memory management
   - Tools: search_memory, store_memory
   - Resources: memory://agent/[id]/episodic

3. **mcp-server-coinbase**: Financial operations
   - Tools: transfer_asset, get_balance
   - Resources: wallet://balance/latest

4. **mcp-server-news**: Trend monitoring
   - Tools: fetch_headlines, analyze_trends
   - Resources: news://[niche]/latest

## Skill vs Tool Distinction
- **Skills**: Reusable Python modules that agents call internally
- **MCP Tools**: External capabilities exposed via MCP Servers
- **Rule**: Skills USE Tools, but are not Tools themselves
