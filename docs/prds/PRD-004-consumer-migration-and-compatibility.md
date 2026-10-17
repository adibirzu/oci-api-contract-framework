# PRD-004: Consumer Migration and Compatibility

## Goal

Move clients to versioned contracts without a flag-day cutover or unsupported compatibility claim.

## Scope

- Publish migration guide, SDK/client impact matrix, deprecation headers, and telemetry.
- Run old/new contract regression tests and rollback drills.
- Retire legacy endpoints only after evidence-backed consumer readiness and release approval.

## Acceptance criteria

- Each consumer has an owner, target version, migration status, and fallback.
- Contract diff policy blocks unreviewed breaking changes.
- Legacy removal has a date, communication, telemetry, and reversible rollout record.
