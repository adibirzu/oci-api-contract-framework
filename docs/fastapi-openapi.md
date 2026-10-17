# FastAPI and OpenAPI Compared

They address different layers and work well together.

| Concern | OpenAPI | FastAPI |
|---|---|---|
| What it is | Language-neutral HTTP API description standard | Python ASGI web framework |
| Primary value | Contract, docs, client generation, gateway/lint/testing input | Routing, dependency injection, validation, response handling |
| Runtime required | No | Yes, for Python-serving applications |
| Portability | Cross-language and cross-framework | Python-specific |
| Security expression | Declares schemes/requirements; cannot enforce policy alone | Can enforce dependencies/middleware; still needs design and tests |
| Best use here | Canonical contract and compatibility artifact | One valid implementation option for OCI-DEMO services |

## Recommended relationship

1. Define resource/action/error/security behavior in the OpenAPI contract and this profile.
2. Implement the contract in FastAPI when the service is Python-based.
3. Enforce authorization, validation, tenant context, rate limits, and audit in runtime code; generated OpenAPI is evidence of interface shape, not evidence of security.
4. Lint and diff the OpenAPI contract in CI, then run implementation and authenticated integration tests separately.

## Avoid

- Treating generated `/openapi.json` as a complete security review.
- Designing paths around controller names instead of stable resources/actions.
- Assuming FastAPI-generated schemas capture async provider behavior, tenant boundaries, or deprecation commitments without explicit tests and documentation.
