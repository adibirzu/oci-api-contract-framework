# PRD-001: API Inventory and Contract Baseline

## Goal

Create a reviewed, machine-readable inventory and baseline OpenAPI posture before changing product endpoints.

## Scope

- Enumerate every server route, caller, component owner, schema, authentication path, tenant behavior, side effect, sensitivity, and evidence class.
- Classify each route: resource, action, interaction/stream, async operation, internal-only, or retire.
- Select contract source-of-truth and contract diff/lint tooling per product.

## Non-goals

No endpoint rewrite, deployment, credential change, or blanket exposure of docs.

## Acceptance criteria

- Every route has an owner and classification, or an explicit unknown/blocker.
- Consumer and compatibility risk are recorded before a retirement date is proposed.
- Inventory is reviewed by API/security owners and linked from the product roadmap.

## Dependencies and risks

Requires router/source access and product ownership. Dynamic/discovered endpoints, undocumented clients, and external consumers remain unknown until evidenced.
