# Evaluation And Tests

This is the compatibility entry point for v0.2 evaluation. Read `rubric-design.md`, `evaluator-protocol.md`, and `repair-routing.md` for the operative method.

## Test Surfaces

Every generated skill needs four prompt-test classes and at least one forward test.

| Surface | Minimum | Purpose |
|---|---:|---|
| Should trigger | 5 | Confirm realistic activation language |
| Should not trigger | 5 | Detect broad or ambiguous activation |
| Boundary | 3 | Confirm clarification, refusal, or routing behavior |
| Functional | 3 | Confirm required artifacts and decisions |
| Forward output | 1 | Test the skill on an unseen related input |

Prompt tests alone do not establish output quality. The forward output must be evaluated.

## Frozen Rubric

Create the rubric before generation using `assets/templates/evaluation-rubric.json`. Weights must total 100.

Default contract:

```text
total score >= 80
each critical dimension >= 60
all hard gates pass
maximum 3 rounds
```

Use `scripts/score_evaluation.py` to calculate the decision. The script validates arithmetic and gates; the evaluator remains responsible for evidence-backed judgments.

## Evaluation Record

Use `assets/templates/evaluation-result.json`. Each score requires observable evidence. Each issue must name:

- severity
- artifact location
- violated criterion
- evidence
- lowest responsible layer
- required repair

Do not award a passing score based on confidence or fluency alone.

## Regression From Feedback

When the user corrects an output:

1. Preserve the correction as evidence.
2. Classify the defect.
3. Add a case that reproduces it.
4. Locate the lowest responsible layer.
5. Patch only that layer.
6. Re-run affected tests and at least one prior passing case.

Common failure labels:

- `trigger-too-broad`
- `trigger-too-narrow`
- `surface-copying`
- `generic-output`
- `representation-mismatch`
- `unsupported-inference`
- `missing-boundary`
- `missing-source-check`
- `wrong-resource-placement`
- `rubric-mismatch`
- `copyright-or-privacy-risk`

## Performance Claims

For platform outcomes such as impressions, retention, conversion, or revenue, pre-publication evaluation is only a proxy. Record actual analytics when available, compare them with the prediction, and use the discrepancy as new evidence. Never convert a rubric score into a guaranteed real-world result.
