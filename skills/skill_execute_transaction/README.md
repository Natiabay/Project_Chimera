# Skill: Execute On-Chain Transaction

## SRS Reference: FR 5.0, FR 5.1, FR 5.2

## Purpose
Handle autonomous financial transactions with CFO Judge oversight.

## Input Contract

```json
{
  "transaction_type": "native_transfer | deploy_token | get_balance",
  "to_address": "string (optional)",
  "amount_usdc": "float",
  "purpose": "string (e.g., pay_designer, transfer_revenue)",
  "daily_budget_limit": "float (default: 50.0)"
}
```

## Output Contract

```json
{
  "transaction_hash": "string",
  "status": "pending | confirmed | rejected",
  "gas_used": "float",
  "cfp_approval": "boolean",
  "balance_after": "float"
}
```

## MCP Dependencies
- **mcp-server-coinbase**: Coinbase AgentKit integration
- **mcp-server-redis**: For budget tracking

## CFO Judge Rules (FR 5.2)
- Check daily_spend in Redis
- Reject if amount > (limit - daily_spend)
- Flag anomalies for human review
- All transactions logged on-chain
