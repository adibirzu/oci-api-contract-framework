# OCI API Contract Framework

A compact, reusable API strategy for OCI-oriented and multicloud products. It turns an API inventory into versioned, secure, observable contracts and staged migrations. It does **not** ship an API gateway, authentication provider, SDK, or cloud policy.

## Use it

1. Inventory endpoints, consumers, data classes, mutation risk, tenant behavior, and evidence.
2. Adopt the profile in [`templates/api-profile.yaml`](templates/api-profile.yaml).
3. Plan the work with [`docs/prds/`](docs/prds/) and track it in [`STATUS.md`](STATUS.md).
4. Validate documentation with `./scripts/check-docs.sh`; GitHub Actions also runs this check on pull requests and pushes to `main`. Validate implementations in their owning product.

## Architecture

The framework has five portable layers:

| Layer | Responsibility | Primary reference |
|---|---|---|
| Contract | resources, actions, schemas, versions | [architecture](docs/architecture.md) |
| Security | identity, tenant isolation, authorization, audit | [security profile](docs/architecture.md#security-profile) |
| Operations | pagination, idempotency, jobs, errors, observability | [capabilities](docs/capabilities.md) |
| Migration | inventory, compatibility, consumer rollout, rollback | [migration playbook](docs/migration/oci-demo-adapter.md) |
| Governance | PRDs, evidence, decision records, roadmap | [roadmap](docs/roadmap.md) |

## AIP-informed, not AIP-dependent

Google API Improvement Proposals are useful public design guidance. This framework borrows their resource-oriented vocabulary and topics such as standard methods, custom methods, operations, errors, pagination, filtering, field masks, request IDs, and compatibility. It does not assert Google endorsement, use of Google infrastructure, or full AIP conformance. Products may document approved deviations.

## FastAPI and OpenAPI: complementary

FastAPI is a Python web framework that can implement validation, dependencies, routing, and generate an OpenAPI document. OpenAPI is a language-neutral contract format for describing HTTP APIs and enabling documentation, linting, clients, gateways, and compatibility checks. A product may use FastAPI to serve an OpenAPI-defined contract; other products may use another framework while retaining the same contract rules. See [the comparison](docs/fastapi-openapi.md).

## Scope and evidence

This repository is currently **proposed/code-backed documentation only**. It makes no claim that a product has deployed the profile. Each product migration must show its own local, provider, and release evidence.
