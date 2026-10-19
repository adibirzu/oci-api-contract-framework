# OCI-DEMO Migration Adapter

This is a planning adapter for OCI-DEMO's FastAPI control plane, not evidence that its endpoints already meet this framework.

## Read-only discovery

Start from `control_plane/api/main.py`, its included routers, `components.yaml`, Pydantic schemas, client callers, and deployment manifests. For every route, record:

- component and source owner;
- HTTP method/path/current schema and consumer;
- tenant/authentication/authorization behavior actually present;
- data class and external side effect;
- synchronous vs asynchronous execution;
- compatibility risk and observability fields;
- evidence class and migration wave.

Do not infer a deployed component, reachable provider, or effective policy from a router import alone.

## Wave plan

| Wave | Scope | Exit evidence |
|---|---|---|
| 0: inventory | all included routers and consumers | reviewed inventory and threat model |
| 1: cross-cutting | request context, error envelope, OpenAPI CI, audit/redaction | local unit and contract tests |
| 2: high-risk | coordinator, MCP/tools, remediation, compliance, detections, access | authenticated positive and negative tests |
| 3: async | scans, batches, pipelines, reports | operation lifecycle and retry tests |
| 4: remaining APIs | integrations and read models | compatibility and consumer migration evidence |
| 5: retirement | deprecated legacy routes | consumer telemetry, rollback drill, release approval |

## Mapping rules

- Keep ordinary reads/creates/updates/deletes as resources where a durable domain object exists.
- Preserve chat and streaming as purpose-specific interaction endpoints; give them typed messages, tenant-aware quotas, cancellation semantics, audit, and safe error behavior.
- Map `execute`, `scan`, `reconnect`, and batch operations to explicit custom actions. Long work must expose an operation/job rather than hold an HTTP request open.
- Place `/api/v1` beside legacy `/api` routes; use adapters, not a flag-day rewrite. New clients use v1; legacy traffic is measured and sunset by a published schedule.

## OCI evidence gates

Local route tests, generated OpenAPI, and mocked provider responses are local evidence only. OCI/provider validation additionally requires the exact tenancy/account, region, compartment, resource, authorization boundary, target, action, cost/blast-radius approval, and sanitized receipt. Release acceptance remains separate.

## Current OCI-DEMO source artifacts

OCI-DEMO now supplies these product-owned, locally verified sources. The
framework does not import them and does not operate OCI resources.

| Surface | Product-owned artifact | Evidence |
|---|---|---|
| Route inventory | `scripts/generate_api_route_inventory.py` | locally verified |
| API profile and OpenAPI baseline | `docs/architecture/api/` | locally verified |
| Principal and tenant policy | `control_plane/api/authorization.py` | locally verified |
| Tool policy | `control_plane/api/tool_security.py` | locally verified |
| Legacy compatibility | `control_plane/api/legacy_adapter.py` | locally verified |

The listed source artifacts do not replace the OCI evidence gates above. An
authenticated positive and negative request, cloud tool invocation, deployment,
or legacy-route retirement needs OCI-DEMO's separately authorized,
target-bound receipt.
