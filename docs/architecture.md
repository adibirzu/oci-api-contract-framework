# Architecture and API Profile

## Contract model

Every public or cross-component API declares an owner, audience, stability level, OpenAPI contract location, authorization policy, tenant behavior, data classification, observability fields, and deprecation policy. Model stable domain objects as resources; use custom actions only when CRUD semantics would conceal operational behavior.

```text
Client -> edge/authentication -> tenant and authorization context -> API handler
       -> resource/action policy -> domain service -> operation/job (when asynchronous)
       -> audit + metrics/logs/traces (redacted, correlated)
```

### Resource APIs

Use plural collection paths and opaque stable identifiers:

```http
GET /api/v1/tenants/{tenant}/components/{component}
GET /api/v1/tenants/{tenant}/components?page_size=50&page_token=...&filter=state%3D%22READY%22
POST /api/v1/tenants/{tenant}/components
PATCH /api/v1/tenants/{tenant}/components/{component}?update_mask=display_name,labels
DELETE /api/v1/tenants/{tenant}/components/{component}
```

Accept `page_size`, `page_token`, `filter`, `order_by`, and `update_mask` only when their semantics and limits are documented. Return an opaque next-page token; do not embed secrets or mutable authorization data in it.

### Custom actions and asynchronous work

Name actions as verbs after `:` and make risk visible:

```http
POST /api/v1/tenants/{tenant}/remediations/{remediation}:execute
POST /api/v1/tenants/{tenant}/scans:run
POST /api/v1/tenants/{tenant}/operations/{operation}:cancel
```

Potentially long or externally side-effecting actions return an operation resource containing `name`, `done`, `metadata`, `result` or safe `error`, actor, tenant, request ID, and timestamps. Expose cancellation only where the underlying work can safely honor it.

## Security profile

1. Verify issuer, audience, signature, expiry, and key lifecycle before using token claims.
2. Construct an immutable request context with verified principal, tenant, roles/scopes, correlation ID, and policy version. Never trust these identities from a body, header, or path alone.
3. Enforce authorization at resource/action level before fetching sensitive data or calling downstream systems. Use least privilege and explicit cross-tenant denial.
4. Require step-up/approval policy for destructive remediation, connector changes, bulk actions, secret access, and agent-controlled effects.
5. Validate typed input at the boundary; limit body size, cardinality, execution duration, output size, and concurrency. Protect browser-cookie flows with CSRF controls and exact CORS origins.
6. Redact secrets, tokens, personal data, tool input/output, provider responses, and customer identifiers from errors, logs, traces, and audit exports.

### MCP and agent tools

MCP/tool endpoints are not generic proxy endpoints. Register each tool with typed schema, required scope, tenant eligibility, effect class, timeout, output cap, audit event, and approval requirement. Default unknown tools to deny. Disallow arbitrary shell commands, URLs, OCI profiles, credential references, and unbounded provider queries from client-controlled arguments.

## Operational contract

Every response carries a request/correlation ID. Mutations accept an idempotency key or request ID with documented retention and conflict behavior. Errors use one safe, stable envelope:

```json
{
  "error": {
    "code": "PERMISSION_DENIED",
    "message": "The caller is not authorized for this action.",
    "details": [{"type": "policy", "reason": "missing_scope"}],
    "request_id": "req_..."
  }
}
```

Map error categories consistently to HTTP status. Do not return stack traces, credentials, raw provider errors, or authorization policy internals.

## Versioning and compatibility

Use an explicit contract major version such as `/api/v1`. Prefer additive, backward-compatible fields and enum expansion handling; do not repurpose fields or alter stable meanings. Publish deprecation dates, migration guidance, and telemetry-defined consumer readiness before retiring an endpoint. Maintain a tested rollback path while both versions are live.
