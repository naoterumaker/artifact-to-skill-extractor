# Generator Protocol

The Generator produces both the skill package and a realistic output made by following that skill.

## Inputs

- approved capability contract
- evidence manifest and observations
- verified or clearly labeled hypothesis patterns
- frozen evaluation rubric
- relevant modality, platform, and objective references

## Generation Order

1. Create the skill specification.
2. Choose the minimum file structure needed.
3. Write activation conditions and near-miss boundaries.
4. Write the execution workflow.
5. Place detailed knowledge and examples in references.
6. Place copyable output templates in assets.
7. Add deterministic scripts only where judgment is not required.
8. Generate trigger and functional tests.
9. Use the generated skill to create at least one test output.

## Independence Rules

- Do not copy source wording or composition merely to raise similarity.
- Do not inspect the Evaluator's final diagnosis before producing the first output.
- The Generator may see the frozen rubric because it defines the target.
- Do not alter the rubric during generation.

## Output Trace

Every important generated rule should record one of:

- source observation id
- user-confirmed requirement
- research evidence id
- explicit hypothesis label

If a rule cannot be traced, omit it or mark it as a hypothesis.
