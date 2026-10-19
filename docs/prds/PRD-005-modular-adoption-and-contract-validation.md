# PRD-005: Modular Adoption and Contract Validation

## Status

Code-backed framework package. Product adoption remains proposed until an owning product supplies its own evidence.

## Problem

Products need a small, repeatable way to adopt the shared API profile without coupling their runtime, deployment state, credentials, or product-specific resource model to this repository.

## Outcomes

- A non-sensitive product adapter convention records the framework-to-product boundary.
- A JSON OpenAPI example and dependency-free baseline validator give every product a reproducible starting command.
- Documentation defines what the baseline check does not prove and routes full linting, authorization tests, compatibility checks, and release evidence to the owning product.

## Non-goals

- Selecting a universal OpenAPI linter, runtime, gateway, authentication provider, or deployment tool.
- Validating a live endpoint, provider target, tenant, or release.
- Publishing product contracts, credentials, customer data, topology, or operational receipts.

## Acceptance criteria

1. `templates/product-api-adapter.yaml` contains only declarative, non-sensitive placeholders.
2. `sh scripts/check-contract.sh examples/components.openapi.json` succeeds using Python standard library JSON parsing.
3. The validator rejects missing OpenAPI metadata, paths, response descriptions, or shared `Error` schema.
4. `./scripts/check-docs.sh` invokes the example validation and passes.

## Evidence and next action

Framework evidence is local documentation/validator evidence. A product must add a canonical OpenAPI artifact, its selected semantic linter, implementation tests, authenticated negative tests, and compatibility receipt before any stronger claim.
