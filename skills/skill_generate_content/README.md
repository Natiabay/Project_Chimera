# Skill: Generate Multimodal Content

## SRS Reference: FR 3.0, FR 3.1, FR 3.2

## Purpose
Create text, image, and video content with character consistency.

## Input Contract

```json
{
  "content_type": "text | image | video_tier1 | video_tier2",
  "theme": "string",
  "persona_id": "string (references SOUL.md)",
  "character_reference_id": "string (for image consistency)",
  "budget_allocation": "float (USDC)"
}
```

## Output Contract

```json
{
  "content_url": "string (CDN link)",
  "generation_cost": "float (USDC)",
  "consistency_score": "float 0-1 (Judge validated)",
  "disclosure_flag": "boolean (AI label required)"
}
```

## MCP Dependencies
- **mcp-server-ideogram**: Image generation
- **mcp-server-runway**: Video generation
- **mcp-server-gemini**: Text generation

## Special Rules
- Image generation MUST include character_reference_id (FR 3.1)
- Video tier selection based on budget (FR 3.2)
- Judge validates consistency before publishing
