# PRD-003: Actions, Operations, and Agent/Tool Security

## Goal

Make high-risk actions, long-running work, MCP, and agent tool execution explicit, controlled, and auditable.

## Scope

- Convert operational verbs to `:action` contracts with typed schemas and effect classification.
- Model long-running work as operation/job resources.
- Register MCP/tools through typed allowlists with least-privilege credentials, limits, approvals, and audit.

## Acceptance criteria

- Unknown tools and unapproved effects fail closed.
- Duplicate mutation and operation-state tests prove idempotency and terminal behavior.
- Malicious URL/shell/provider-profile/secret-reference inputs are rejected or safely neutralized.
- Cancellation and retry behavior is documented and tested where supported.
