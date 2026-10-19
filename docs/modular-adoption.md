# Modular Adoption Guide

This framework is a reusable contract policy, not a shared runtime. Keep it independent of a product's language, deployment, tenancy, and cloud account.

## Ownership boundary

| Artifact | Owner | Rule |
|---|---|---|
| Framework profile, templates, reusable validator | this repository | Portable, public-safe, no environment values |
| OpenAPI contract, product adapter, implementation and tests | owning product | Versioned with the product and its consumers |
| Credentials, tenancy/topology, provider receipts, deployment state | local secure systems | Never commit here or into an adapter |

## Adopt in four small steps

1. Copy [`../templates/api-profile.yaml`](../templates/api-profile.yaml) into the product's architecture/configuration area or reference it from a product policy document.
2. Copy [`../templates/product-api-adapter.yaml`](../templates/product-api-adapter.yaml) into the product and replace only the declared, non-sensitive placeholders. One adapter may cover one bounded API surface; add another instead of creating a monolith.
3. Make the adapter point to the product's canonical OpenAPI document. Keep resource schemas, HTTP routing, and implementation-specific configuration in product modules.
4. Add the framework validator to product CI: `sh ./scripts/check-contract.sh path/to/openapi.json`. For YAML contracts, use the product's chosen parser/linter to emit or validate an equivalent JSON artifact, then run this baseline guard plus a full OpenAPI linter.

## Adapter convention

An adapter is declarative and intentionally narrow. It records:

- API owner, audience, stability, and contract location;
- module boundaries and resource/action namespaces;
- verified identity/tenant context and policy location, never secrets;
- implementation option (FastAPI, another ASGI/server runtime, or gateway) without making that option the contract;
- compatibility window, evidence level, and links to product-owned tests.

An adapter must not embed routes from other products, arbitrary provider URLs, profile names, OCIDs, tokens, customer names, deployment manifests, or runtime receipts.

## Modular product layout

```text
product/
  api/
    contracts/openapi.json       # canonical transport contract
    adapters/<surface>.yaml      # framework-to-product binding
    modules/<domain>/            # resource/action implementation
    tests/contracts/             # positive, negative, compatibility tests
```

Keep cross-cutting request context, error mapping, audit/redaction, and authorization as shared product modules. Keep domain resources and custom actions in separately testable modules. Do not use a generic proxy or a single agent endpoint to bypass these boundaries.

## Validation layers

`check-contract.sh` is a dependency-free baseline guard for JSON OpenAPI 3.x documents. It checks parseability, version, metadata, paths, response descriptions, and that a reusable safe error schema is present. It is not a substitute for an OpenAPI semantic linter, authenticated integration tests, authorization tests, compatibility diffs, or release acceptance.

Run the full product gate in this order:

1. Framework docs and baseline contract guard.
2. Product schema/lint and generated-client checks.
3. Unit and authenticated positive/negative tests, including cross-tenant denial.
4. Compatibility diff against the released contract and consumer rollout evidence.
5. Target-bound provider and release checks only when separately authorized.

## Minimal CI pattern

```sh
sh ./scripts/check-contract.sh api/contracts/openapi.json
# product-owned: OpenAPI linter, implementation tests, authenticated tests
```

The example contract is illustrative only. It is not a deployed endpoint, a tenant model, or authorization evidence.
