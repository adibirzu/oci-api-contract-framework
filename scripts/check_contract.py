#!/usr/bin/env python3
"""Dependency-free baseline structural guard for JSON OpenAPI contracts."""

import json
import sys
from pathlib import Path


def fail(message: str) -> None:
    raise SystemExit(f"invalid OpenAPI contract: {message}")


def main(path: str) -> None:
    try:
        document = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise SystemExit(f"invalid OpenAPI JSON: {error}") from error

    if not isinstance(document, dict):
        fail("root must be an object")
    version = document.get("openapi")
    if not isinstance(version, str) or not version.startswith("3."):
        fail("openapi must be a 3.x version string")
    info = document.get("info")
    if not isinstance(info, dict) or not all(
        isinstance(info.get(key), str) and info[key] for key in ("title", "version")
    ):
        fail("info.title and info.version are required non-empty strings")
    paths = document.get("paths")
    if not isinstance(paths, dict) or not paths:
        fail("paths must be a non-empty object")

    methods = {"get", "put", "post", "delete", "options", "head", "patch", "trace"}
    for path_name, item in paths.items():
        if not isinstance(path_name, str) or not path_name.startswith("/") or not isinstance(item, dict):
            fail("each path must start with / and map to an object")
        for method, operation in item.items():
            if method.lower() not in methods:
                continue
            if not isinstance(operation, dict):
                fail(f"{method.upper()} {path_name} must be an object")
            responses = operation.get("responses")
            if not isinstance(responses, dict) or not responses:
                fail(f"{method.upper()} {path_name} requires responses")
            for status, response in responses.items():
                if (
                    not isinstance(status, str)
                    or not isinstance(response, dict)
                    or not isinstance(response.get("description"), str)
                    or not response["description"]
                ):
                    fail(f"{method.upper()} {path_name} response {status} requires a description")

    schemas = document.get("components", {}).get("schemas", {})
    if not isinstance(schemas, dict) or "Error" not in schemas:
        fail("components.schemas.Error is required for the shared safe error envelope")
    print(f"contract baseline passed: {path}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_contract.py path/to/openapi.json")
    main(sys.argv[1])
