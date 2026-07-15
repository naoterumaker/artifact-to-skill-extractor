# Decision Unit Intermediate Representation

A decision unit is the smallest executable piece of recovered production knowledge. Function labels such as "build trust" or "improve hierarchy" are not executable by themselves.

## Contract

```text
WHEN context applies
IF preconditions and evidence are satisfied
DO a selected action with bounded parameters
VERIFY observable criteria
ELSE use a fallback or escalate
```

## Required Fields

| Field | Purpose |
|---|---|
| `intent` | change the decision is meant to create |
| `context` | situations where the unit is eligible |
| `preconditions` | facts that must already hold |
| `evidence_needed` | information the agent must inspect before deciding |
| `decision_rule` | conditions and selection logic |
| `action` | executable operation and output |
| `parameters` | case-specific values and valid ranges |
| `invariants` | relations that must remain true |
| `verifier` | tests or observations that determine success |
| `fallback` | repair, alternate route, or human escalation |
| `failure_modes` | known breakdowns and prevention |
| `provenance` | source ids, locations, evidence status, and support |
| `confidence` | level, basis, counterevidence, and scope |
| `agency` | judgment owner, executor, approval owner |

Use `assets/templates/decision-unit.json` so deterministic validation can inspect the interface.

## Compilation

Decision units compile into different destinations:

- selection and routing rules in `SKILL.md`
- detailed judgment guidance in `references/`
- reusable parameter contracts in `assets/`
- deterministic operations in `scripts/`
- tool calls and dependencies in an execution graph
- evaluator assertions and fallback cases in `evals/`

Do not compile unsupported inferences into unconditional instructions. Preserve confidence and scope in the executable package.
