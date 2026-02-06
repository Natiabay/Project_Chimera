# Project Chimera: AI Agent Instructions

## 🎯 Mission
Build an Autonomous Influencer Network by implementing the specifications in `specs/`.

## 📋 Workflow
1. **Check specs**: Always read `specs/` before writing code
2. **Run failing tests**: Use `make test` to see what needs implementation
3. **Implement skills**: Each skill in `skills/` has a README with contracts
4. **Use MCP**: All external calls must go through MCP servers

## 🚫 Rules
- ❌ Never write direct API calls (use MCP tools only)
- ✅ Follow Pydantic schemas for all data models
- ✅ Write async/await code for I/O operations
- ✅ Include error handling for MCP calls
- ✅ Reference SRS FR numbers in code comments

## 🏁 Getting Started
```bash
./scripts/onboard_ai_agent.sh
```

## 🧪 Testing
- Run `make test` to see failing tests (TDD approach)
- Implement until tests pass
- Run `make spec-check` to ensure spec alignment

## 🛠️ Skill Development
Each skill in `skills/` has:
- A README with input/output contracts
- MCP dependencies listed
- SRS references (FR numbers)

Example: `skills/skill_fetch_trends/README.md`

## 🔌 MCP Integration
- **Tools**: Executable functions (e.g., generate_image)
- **Resources**: Data sources (e.g., news://latest)
- **Prompts**: Reusable templates (e.g., analyze_sentiment)

## ❓ Questions?
Refer to:
- `specs/` - for requirements
- `research/` - for architecture decisions
- `.cursor/rules` - for coding standards
- SRS document - for overall vision
