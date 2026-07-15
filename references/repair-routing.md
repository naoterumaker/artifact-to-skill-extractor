# Repair Routing

Repair the lowest layer that can explain the observed failure. Do not convert every bad output into permanent skill instructions.

| Failure Pattern | Patch First | Escalate When |
|---|---|---|
| One wording or rendering defect | current output | defect repeats across outputs |
| Wrong choice despite required evidence being available | decision unit | doctrine or grammar drove the wrong preference |
| Repeated expression relation breaks | grammar | medium or tool affordance invalidates the grammar |
| Output violates an explicit value priority | project doctrine | doctrine was inferred rather than user-confirmed |
| Doctrine fails to predict held-out choices | doctrine hypothesis | comparison corpus is insufficient or scope is wrong |
| Required operation is impossible or opaque | tool assignment | no candidate tool exposes the capability |
| State, handoff, retry, or approval fails | execution graph | underlying tool cannot support recovery |
| Agent skipped or reordered a required step | `SKILL.md` | step requires detailed domain knowledge |
| Missing facts, examples, or domain rules | `references/` | source evidence itself is insufficient |
| Repeated malformed output structure | `assets/` template | template cannot express required variation |
| Function lost across different subjects | abstraction pattern | source observations do not support the invariant |
| Unsupported or contradictory rule | evidence corpus | sources disagree or are stale |
| Evaluator punishes desired variation | rubric | user confirms the target was defined incorrectly |

Do not patch recovered creator doctrine to force the current output to pass. Either correct the evidence-backed hypothesis, narrow its scope, or change the explicitly owned project doctrine.

## Permanent Rule Threshold

Promote a repair into the skill when at least one is true:

- the same defect appears in two independent cases
- the user identifies it as a non-negotiable rule
- a hard safety or rights gate requires it
- a deterministic validator can prevent it reliably

Otherwise, keep the repair local to the current output.

## Regression Requirement

Every permanent skill patch must add a test that would have caught the original failure. Re-run prior passing cases to prevent a repair from narrowing the skill unnecessarily.
