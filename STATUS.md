# API Framework Status

| Item | Status | Evidence | Next action |
|---|---|---|---|
| Framework contract and security profile | code-backed | Docs and template in this repository | Review with product owners |
| OCI-DEMO adapter plan | proposed | Router/component mapping guidance only | Produce read-only API inventory per router |
| OCI-DEMO implementation | not started | No product source changed here | Authorize PRD execution by migration wave |
| Documentation validation CI | code-backed | Read-only GitHub Actions workflow runs `./scripts/check-docs.sh` on pull requests and `main` | Verify the workflow from an authorized GitHub event |
| Shared lint/contract CI | proposed | No tool dependency selected | Evaluate Spectral/OpenAPI tooling per product |

## Update rule

Use one of: `proposed`, `code-backed`, `locally verified`, `provider verified`, `release accepted`, `blocked`. Record a dated, reproducible receipt or link for any status change. Do not replace an unresolved risk with a favorable status.
