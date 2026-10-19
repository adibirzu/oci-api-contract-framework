# OCI API Contract Framework

A compact, reusable API strategy for OCI-oriented and multicloud products. It turns an API inventory into versioned, secure, observable contracts and staged migrations. It does **not** ship an API gateway, authentication provider, SDK, or cloud policy.

## Use it

1. Inventory endpoints, consumers, data classes, mutation risk, tenant behavior, and evidence.
2. Adopt the shared profile in [`templates/api-profile.yaml`](templates/api-profile.yaml), then create one product-owned adapter from [`templates/product-api-adapter.yaml`](templates/product-api-adapter.yaml).
3. Keep the canonical OpenAPI document and its implementation in the owning product. The framework stays product-neutral.
4. Validate an OpenAPI JSON artifact locally with `sh ./scripts/check-contract.sh path/to/openapi.json`; see the safe example in [`examples/components.openapi.json`](examples/components.openapi.json).
5. Plan the work with [`docs/prds/`](docs/prds/) and track it in [`STATUS.md`](STATUS.md). Validate documentation with `./scripts/check-docs.sh`; GitHub Actions also runs this check on pull requests and pushes to `main`.

For the product/adapter boundary, implementation choices, and a minimal CI pattern, read the [modular adoption guide](docs/modular-adoption.md).

## Architecture

The framework has five portable layers:

| Layer | Responsibility | Primary reference |
|---|---|---|
| Contract | resources, actions, schemas, versions | [architecture](docs/architecture.md) |
| Security | identity, tenant isolation, authorization, audit | [security profile](docs/architecture.md#security-profile) |
| Operations | pagination, idempotency, jobs, errors, observability | [capabilities](docs/capabilities.md) |
| Migration | inventory, compatibility, consumer rollout, rollback | [migration playbook](docs/migration/oci-demo-adapter.md) |
| Governance | PRDs, evidence, decision records, roadmap | [roadmap](docs/roadmap.md) |

Products consume the framework through a small adapter. A product adapter names its contract location, resource vocabulary, authentication boundary, implementation choice, and evidence; it does not copy credentials, deployment topology, provider receipts, or other operational state into this repository.

## AIP-informed, not AIP-dependent

Google API Improvement Proposals are useful public design guidance. This framework borrows their resource-oriented vocabulary and topics such as standard methods, custom methods, operations, errors, pagination, filtering, field masks, request IDs, and compatibility. It does not assert Google endorsement, use of Google infrastructure, or full AIP conformance. Products may document approved deviations.

## FastAPI and OpenAPI: complementary

FastAPI is a Python web framework that can implement validation, dependencies, routing, and generate an OpenAPI document. OpenAPI is a language-neutral contract format for describing HTTP APIs and enabling documentation, linting, clients, gateways, and compatibility checks. A product may use FastAPI to serve an OpenAPI-defined contract; other products may use another framework while retaining the same contract rules. See [the comparison](docs/fastapi-openapi.md).

## Scope and evidence

This repository is currently **proposed/code-backed documentation only**. It makes no claim that a product has deployed the profile. Each product migration must show its own local, provider, and release evidence.
