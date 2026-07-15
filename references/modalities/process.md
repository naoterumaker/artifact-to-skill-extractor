# Process Modality

Represent operational work through state, decisions, actions, and recovery rather than narrative summary.

## Representation

- trigger and preconditions
- inputs and authority
- state transitions
- decision table
- tool calls and deterministic steps
- exceptions and recovery
- completion and rollback conditions
- audit trail

## Extraction Priority

Process traces often hide expert checks. Look for pauses, corrections, retries, rejected options, validation commands, and final verification. These reveal more reusable knowledge than the happy path alone.

## Evaluation

Test a normal case, a missing-input case, a tool failure, a boundary case, and a recovery case. A process skill does not pass merely because its documentation is complete.
