# PRD-002: API Foundation and Security

## Goal

Provide common versioning, request context, error, audit, redaction, validation, and authorization foundations for a product's API surface.

## Scope

- Introduce `/api/v1` contract boundary and safe legacy coexistence.
- Implement verified principal/tenant context; resource/action-level authorization; standardized error envelope; request IDs; audit and redaction.
- Add body/rate/concurrency limits, idempotency policy, exact CORS, and CSRF controls for cookie-authenticated mutations.

## Acceptance criteria

- Cross-tenant, wrong-role, unauthenticated, malformed-input, and sensitive-error negative tests pass.
- OpenAPI contract documents security requirements, errors, schemas, and version.
- Logs/traces/audit records correlate safely without secrets or raw tool payloads.

## Rollback

Feature-gate v1 routing while legacy routes stay intact; keep policy decisions observable and revertible. Do not fall back to weaker authorization on errors.
