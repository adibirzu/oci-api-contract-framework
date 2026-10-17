# OCI API Contract Framework

Use this repository to define and migrate product API contracts. It is a framework and documentation source, not a production control plane.

## Start here

1. Read `README.md`, then `docs/architecture.md`.
2. For a product migration, read `docs/migration/oci-demo-adapter.md` and the relevant PRD in `docs/prds/`.
3. Copy and tailor `templates/api-profile.yaml`; do not claim a capability is deployed until evidence exists.

## Operating rules

- Google AIPs inform this profile; they are not a mandatory dependency or an assertion of Google conformance.
- OpenAPI describes an API contract; FastAPI is one implementation framework. Use both where appropriate.
- Preserve compatibility: inventory consumers, add versioned contracts, provide deprecation windows, and prove migration before removal.
- Derive tenant, principal, roles, and scopes from verified authentication context—not request payloads.
- Treat MCP and agent tool execution as privileged actions: allowlist, validate typed inputs, least privilege, audit, timeout, redact.
- Classify claims as proposed, code-backed, locally verified, provider verified, or release accepted. Never promote evidence classes.
- Keep secrets, customer data, tokens, topology, and raw operational receipts out of this repository.

## Definition of done

Run `./scripts/check-docs.sh`. Update `STATUS.md` with evidence, risk, and next action. Changes to a product require its own tests, review, and release authority.
