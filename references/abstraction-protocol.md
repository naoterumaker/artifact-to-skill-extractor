# Abstraction Protocol

Abstraction is the semantic operation that turns artifact-specific observations into reusable production logic. Serialization is not abstraction.

## Evidence Status

Label every extracted claim:

| Status | Meaning |
|---|---|
| `observed` | directly visible in the artifact |
| `inferred` | plausible explanation of the observation |
| `user-confirmed` | creator or user confirmed the rule |
| `hypothesis` | useful candidate requiring testing |
| `verified` | passed comparison or transfer testing |

## Abstraction Steps

1. Describe the actual element without interpretation.
2. Name the function the element appears to perform.
3. Identify the relation that makes the function work.
4. Generate plausible alternatives and ask what can change.
5. Mark remaining relations as candidate invariants.
6. Define variables and their valid ranges.
7. Define constraints among variables.
8. Add selection rules, anti-patterns, and anti-clone rules.
9. Instantiate a materially different case.
10. Evaluate whether function survived without expression being copied.

## Pattern Shape

```yaml
pattern_id: pattern-001
intent: desired user or system change
source_elements: []
invariants: []
variables: {}
constraints: []
selection_rules: []
anti_patterns: []
anti_clone: []
evidence_status: hypothesis
transfer_tests: []
```

## Promotion Rules

- One example: candidate only.
- Multiple independent examples: stronger hypothesis.
- User confirmation: valid for the user's domain, not automatically universal.
- Successful unseen instantiation: transfer-supported.
- Repeated successful use with no critical regressions: verified pattern.

## Anti-Clone Test

The generated output must satisfy both:

1. Functional fidelity: the intended production mechanism remains.
2. Expressive distance: protected expression, unique composition, wording, subject, and source-specific details are not reproduced.

Changing nouns while preserving the entire original structure is not sufficient abstraction.
