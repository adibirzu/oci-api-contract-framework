#!/usr/bin/env sh
# Dependency-free baseline guard for OpenAPI JSON. It is intentionally not a full semantic linter.
set -eu

if [ "$#" -ne 1 ]; then
  echo "usage: $0 path/to/openapi.json" >&2
  exit 64
fi

contract=$1
test -f "$contract" || { echo "contract not found: $contract" >&2; exit 66; }

root=$(CDPATH='' cd -- "$(dirname -- "$0")" && pwd)
exec python3 "$root/check_contract.py" "$contract"
