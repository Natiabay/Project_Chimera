# OpenClaw Integration Plan

**Executable protocol definitions (JSON Schema):** [openclaw_protocols.json](openclaw_protocols.json) — Identity, Capability Advertisement, Reputation Oracle, Negotiation, Secure Data Exchange.

---

## Identity Protocol
- Use agent's wallet address (from Coinbase AgentKit) as DID
- Cryptographic verification of principal owner

## Capability Advertisement
- Publish MCP resource: `mcp://chimera/[agent_id]/capabilities`
- Structured signal format: JSON with intent schema

## Reputation Oracle
- Query decentralized ledger for counterparty history
- Share successful transaction outcomes
- Flag protocol violations

## Negotiation Protocol
- Smart contract templates for agent deals
- CFO Judge validates all external contracts
- On-chain escrow for high-value agreements

## Secure Data Exchange
- Permissioned information sharing
- Usage constraints and expiration
- Governed by SOUL.md directives

## Implementation Phases
1. **Now**: Internal swarm only (closed beta)
2. **Q2 2026**: Broadcast capabilities to trusted network
3. **Q4 2026**: Full inter-agent commerce with OpenClaw v2
