#!/usr/bin/env sh
set -eu

root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
required="AGENTS.md CLAUDE.md README.md STATUS.md docs/architecture.md docs/capabilities.md docs/fastapi-openapi.md docs/migration/oci-demo-adapter.md docs/roadmap.md templates/api-profile.yaml templates/openapi-security-snippet.yaml"

for file in $required; do
  test -s "$root/$file" || { echo "missing or empty: $file" >&2; exit 1; }
done

test "$(cat "$root/CLAUDE.md")" = "@AGENTS.md" || { echo "CLAUDE.md must point to AGENTS.md" >&2; exit 1; }

for prd in "$root"/docs/prds/PRD-*.md; do
  test -s "$prd" || { echo "missing PRD" >&2; exit 1; }
  grep -q '^# PRD-' "$prd" || { echo "invalid PRD heading: $prd" >&2; exit 1; }
done

grep -q 'aip_conformance_claimed: false' "$root/templates/api-profile.yaml"
grep -q 'Python ASGI web framework' "$root/docs/fastapi-openapi.md"
grep -q 'MCP/tool endpoints are not generic proxy endpoints' "$root/docs/architecture.md"
echo "documentation checks passed"
