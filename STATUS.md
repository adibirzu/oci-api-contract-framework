# API Framework Status

| Item | Status | Evidence | Next action |
|---|---|---|---|
| Framework contract and security profile | code-backed | Docs and template in this repository | Review with product owners |
| OCI-DEMO adapter plan | proposed | Router/component mapping guidance only | Produce read-only API inventory per router |
| OCI-DEMO implementation | not started | No product source changed here | Authorize PRD execution by migration wave |
| Documentation validation CI | code-backed | Read-only GitHub Actions workflow runs `./scripts/check-docs.sh` on pull requests and `main` | Verify the workflow from an authorized GitHub event |
| Shared lint/contract CI | proposed | No tool dependency selected | Evaluate Spectral/OpenAPI tooling per product |
| Modular adoption package | code-backed | Product adapter template, JSON OpenAPI example, and dependency-free baseline validator | Adopt in one product and add its chosen full OpenAPI linter and authenticated tests |
| OCI-DEMO contract baseline | code-backed | `docs/migration/oci-demo-adapter.md`, `templates/oci-demo-api-profile.yaml`, `./scripts/check-docs.sh`, and `sh ./scripts/check-contract.sh examples/components.openapi.json` on 2026-10-19; commands verify this framework only | Obtain OCI-DEMO product-owned validation and authenticated integration evidence before claiming a migrated or deployed API |

## Update rule

Use one of: `proposed`, `code-backed`, `locally verified`, `provider verified`, `release accepted`, `blocked`. Record a dated, reproducible receipt or link for any status change. Do not replace an unresolved risk with a favorable status.
