# Failure Harvest Loop

The per-run repair loop fixes one output. Failure harvesting learns across runs without turning every defect into a permanent rule.

## Failure Record

Store each failure under the project's `09-failures/` directory.

```yaml
failure_id: fail-001
occurred_at: ""
skill_version: ""
case_id: ""
artifact_location: ""
expected: ""
observed: ""
rubric_dimension: ""
severity: critical | major | minor
root_layer: output | skill | reference | asset | pattern | evidence | rubric
repair_applied: ""
repair_result: fixed | partial | unchanged | regression
privacy: public | private | restricted
candidate_cluster: null
```

## Per-Run Handling

1. Record the observable defect and failed criterion.
2. Route it to the lowest responsible layer.
3. Apply the smallest repair.
4. Re-run the failed case and one prior passing case.
5. Preserve the before/after evaluation.

Do not automatically add a permanent skill rule for a single output defect.

## Periodic Harvest

Review failures monthly or after every 20 runs, whichever comes first.

1. Normalize failure labels without deleting source evidence.
2. Cluster by root cause, not by surface wording.
3. Promote clusters with at least five credible cases to a rule hypothesis.
4. Draft the smallest rule, reference addition, asset change, or new skill boundary.
5. Test on held-out failures and prior passing cases.
6. Promote only if the change fixes the cluster without meaningful regression.

The threshold of five is an operational default, not a statistical guarantee. High-severity safety or rights failures can trigger immediate review.

## Frontier

Maintain four queues:

- `unresolved`: no credible root cause yet
- `candidate`: repeated pattern with a hypothesis
- `validating`: change under held-out testing
- `promoted`: validated change linked to a skill version

Close a failure only when its evidence, repair, test, and version link are complete. Keep rejected hypotheses so the same weak fix is not repeatedly proposed.

## Privacy And Rights

Redact secrets and personal data before clustering. Store restricted artifacts outside the public skill repository and retain only non-sensitive failure descriptors or hashes where appropriate.
