# Abstraction Protocol

Abstraction turns source-specific observations into scoped production knowledge. Serialization is not abstraction, and a recurring function label is not yet an executable rule.

## Evidence Status

| Status | Meaning |
|---|---|
| `observed` | directly locatable in the artifact or trace |
| `inferred` | plausible explanation supported by observations |
| `user-confirmed` | explicitly owned by the user or creator for the declared scope |
| `hypothesis` | candidate that needs comparison, prediction, or transfer |
| `verified` | passed the declared evidence and evaluation gates |

## From Concrete To Grammar

1. Observe elements in a modality-native representation.
2. Name the production function and intended state change.
3. Align real decision opportunities across eligible cases.
4. Identify repeated relations rather than repeated objects, wording, or styling.
5. Separate invariants, context-linked variables, valid ranges, and constraints.
6. Record selection rules, anti-patterns, anti-clone rules, counterexamples, and scope.
7. Mark the result as candidate unless comparative evidence supports more.

Use `assets/templates/generative-pattern.yaml` only when a stable handoff is useful. Doctrine and rationale normally remain in evidence-backed Markdown.

## From Grammar To Executable Decision

For each judgment that affects the output, compile:

```text
WHEN the context is eligible
IF required evidence and preconditions hold
DO a selected operation with bounded parameters
VERIFY observable criteria
ELSE repair, choose a fallback, or escalate
```

Add provenance, confidence, counterevidence, failure modes, and agency. Use `assets/templates/decision-unit.json` and validate it with `scripts/validate_system_ir.py`.

## Doctrine Boundary

One artifact may suggest values but cannot verify creator doctrine. Use revisions, accepted/rejected alternatives, a longitudinal corpus, creator explanation, and held-out prediction. Keep user-confirmed project doctrine available as a separate input when creator doctrine cannot be recovered.

## Anti-Clone Test

The new concrete must satisfy both:

1. Functional fidelity: supported production relations remain.
2. Expressive distance: protected wording, composition, subject, examples, and source-specific details materially change.

Changing nouns inside the same scene graph or argument skeleton is not sufficient.

## Promotion

- One example: observation, candidate grammar, and low-confidence decisions only.
- Multiple comparable examples: recurring and conditional pattern hypotheses.
- Revisions or positive/negative contrasts: stronger decision and boundary hypotheses.
- User confirmation: project-scoped doctrine, not a universal rule.
- Held-out prediction or unseen execution: evidence for promotion within scope.
- Repeated passing use with independent evaluation: candidate for `active` status.
