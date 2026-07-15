# Transfer Protocol

Use transfer tests to distinguish a reusable production rule from a source-specific description. A different concrete inside the same platform is a **forward test**. A changed platform, modality, audience, or production function is a **cross-domain test**.

## Test Record

```yaml
transfer_test:
  pattern_id: pattern-001
  source_domain: "X Article"
  source_artifacts: [src-001, src-002]
  target_domain: "LP first view"
  target_artifacts: [target-001, target-002, target-003]
  baseline: "same generator without the candidate pattern"
  evaluator: "blind or independent where feasible"
  scoring:
    reproducibility: 1-5
    improvement_over_baseline: 1-5
    target_constraint_preservation: 1-5
    anti_clone_independence: 1-5
    evidence_traceability: 1-5
  decision: promote | narrow | revise | reject
```

## Corpus Rules

- Use unseen target artifacts or tasks.
- Use at least three target cases for promotion. One case is a smoke test only.
- Include one difficult or negative case when available.
- Keep the target's native constraints; do not force source-platform structure onto it.
- Compare against a baseline when claiming improvement.
- Prevent the evaluator from seeing the intended conclusion when independent evaluation is possible.

## Decision Thresholds

Promote when:

- average dimension score is at least `4.0`
- no dimension is below `3.0`
- all rights, safety, and anti-clone hard gates pass
- no target-specific constraint is materially damaged

Use `narrow` when the pattern works only for the source domain or a named subset. Use `revise` when the production function appears valid but variables or constraints are incomplete. Use `reject` when the pattern does not outperform the baseline, breaks target constraints, or merely reproduces source expression.

## Interpreting The Bundled Examples

The X and image examples in this repository each use one unseen test output. They establish forward execution and anti-clone behavior, but they do not meet the three-case promotion threshold. Their generated skills therefore remain `experimental`.

## Real-World Outcomes

If the capability targets impressions, retention, conversion, revenue, error reduction, or another external outcome, pre-publication scoring is only a proxy. Record actual outcomes and compare them with the evaluator prediction. A pattern should be narrowed or demoted when proxy scores repeatedly fail to predict observed performance.
