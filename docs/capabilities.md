# Capability Catalogue

| Capability | Required behavior | Validation evidence |
|---|---|---|
| Contract publication | OpenAPI document with schemas, examples, tags, security, error responses | Spec parse and contract test |
| Resources | stable names, standard CRUD where applicable | positive/negative API tests |
| Actions | explicit `:verb`, policy and audit classification | authorization and audit tests |
| Async work | operation/job state, result/error, cancellation semantics | polling, terminal-error, cancellation tests |
| Tenant isolation | verified tenant context and cross-tenant deny | two-tenant negative test |
| Authorization | scope/role/resource policy checked before use | unauthenticated, wrong-role, wrong-resource tests |
| Idempotency | documented replay key, retention, conflict behavior | duplicate mutation test |
| Queries | bounded pagination/filter/order and opaque tokens | limit, malformed-token, auth-change tests |
| Safe errors | stable code/message/details; no sensitive leakage | malformed/provider-failure tests |
| Agent/MCP tools | typed allowlist, limits, policy, audit, approval when needed | unknown-tool and hostile-input tests |
| Observability | request, operation, actor, tenant, component, trace correlation; redaction | trace/audit inspection |
| Compatibility | additive evolution, consumer inventory, deprecation/rollback | old/new contract regression suite |
