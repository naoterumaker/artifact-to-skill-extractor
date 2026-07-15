# Lifecycle

Skill status reflects evidence, not enthusiasm.

## States

| State | Meaning | Invocation rule |
|---|---|---|
| `experimental` | Built and runnable, but evidence or transfer coverage is limited | May be used with explicit caveats and evaluation |
| `active` | Current, tested, and suitable for its declared scope | Normal invocation |
| `deprecated` | Superseded, stale, or predictively weak | Do not select for new work; route to successor |
| `archived` | Retained only for history or reproducibility | Never auto-invoke |

## Promotion To Active

Require:

- structural validation passes
- selected profile's complete system-IR validation passes
- trigger, near-miss, boundary, and functional fixtures pass
- at least three forward cases pass the frozen rubric
- recovered doctrine passes a preregistered held-out prediction when doctrine is claimed
- required tool capabilities have current assignments or concrete manual fallbacks
- any cross-domain claim passes `transfer-protocol.md`
- no unresolved critical rights, safety, or privacy failure
- owner, version, validation date, scope, and known limitations are recorded

## Demotion

Move an active skill to `deprecated` when:

- its platform or API assumptions are stale
- a successor covers the same trigger more reliably
- repeated failures show the rubric no longer predicts useful output
- the trigger overlaps another skill and causes material misrouting
- required evidence or dependencies are no longer available

Document a successor or explicit manual route. Do not silently delete the old skill; reproducibility and failure history may depend on it.

Move to `archived` after the deprecation window when no active workflow depends on it.

## Validation Cadence

Use the shortest applicable interval:

- current platform/API behavior: 30-90 days
- stable production method: 6-12 months
- safety, rights, or compliance-sensitive method: on every material policy change
- repeated evaluator failure: immediately

## Status Record

Keep mutable lifecycle metadata in a dedicated status file or skill registry, not in prose scattered across references.

```yaml
skill: skill-name
version: 0.3.0
status: experimental
owner: ""
last_validated: ""
validated_cases: []
known_limits: []
successor: null
```

Deprecated skills may be read for history but must not be invoked as the current solution.
