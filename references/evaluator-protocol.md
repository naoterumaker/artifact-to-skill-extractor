# Evaluator Protocol

The Evaluator judges the output produced by the generated skill, not merely whether the skill files look complete.

## Evaluation Inputs

- frozen rubric
- capability contract
- generated skill package
- doctrine, grammar, decision units, and tool/execution graph when applicable
- generated test output
- source-linked patterns and boundaries
- prior evaluation only after round one

## Evaluation Procedure

1. Check hard gates first.
2. Score every dimension using its anchors.
3. Cite concrete evidence from the generated output.
4. Check whether doctrine claims predict held-out choices rather than only explaining known work.
5. Verify capability coverage, agency boundaries, source of truth, and recovery for tool-dependent work.
6. Identify the lowest responsible failure layer.
7. Recommend the smallest patch target.
8. Calculate the weighted total.
9. Decide pass or revise.

## Failure Layers

```yaml
generated_artifact:
decision_unit:
grammar:
doctrine:
tool_assignment:
execution_graph:
skill_instruction:
reference_knowledge:
asset_template:
abstraction_pattern:
source_evidence:
evaluation_rubric:
```

## Evaluator Output

Use `assets/templates/evaluation-result.json`. Each issue must include:

- failed dimension or hard gate
- observable evidence
- root layer
- why that layer caused the defect
- exact patch target
- expected effect of the repair

When a layer is unsupported by the evidence ceiling, the evaluator must not infer or score it as though it existed. Record it as unavailable or use explicit project doctrine instead.

## Round Rules

- Round 1: structural and capability failures.
- Round 2: quality, specificity, and delivery fit.
- Round 3: final regression and boundary check.

Stop immediately if all pass conditions are met. After round three, return the best output and unresolved gaps rather than looping indefinitely.
