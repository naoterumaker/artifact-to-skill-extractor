# Workflow Design

This is the full artifact-to-skill pipeline.

## Phase 0: Scope And Source Gate

1. Confirm the desired output: analysis report, new skill, skill update, or library design.
2. Confirm source artifacts and access paths.
3. Identify confidentiality, copyright, or quoting limits.
4. Define the target future user: who will invoke the skill, for what task, in what environment.

Stop and ask for source material if the user wants grounded extraction but provided none.

## Phase 1: Source Reading

Read all supplied material before naming a final workflow. Build a source inventory first.

For large sources:

- Sample structure first: table of contents, headings, README, sitemap, transcript timestamps, tests.
- Extract high-signal zones: openings, endings, examples, errors, corrections, evaluation sections.
- Track what was not read so assumptions are visible.

## Phase 2: Functional Decomposition

Create element rows with the extraction schema.

Ask these questions repeatedly:

- What does this element make possible?
- What would break if it were removed?
- What input did the creator need to decide this?
- What alternative could have been chosen?
- What makes this artifact-specific versus reusable?

## Phase 3: Candidate Unit Design

Group elements into candidate units. Use this decision table:

| Signal | Action |
|---|---|
| Same function appears across multiple sources | Create or strengthen a unit |
| One source has a strong named method | Create a unit if transfer passes |
| Element is useful only inside a larger workflow | Keep as step or example |
| Element is generic advice | Demote to supporting note |
| Element requires exact commands or transforms | Consider script-backed skill |
| Several units share inputs and output | Merge into one workflow skill |

## Phase 4: Verification

Run the gates from `extraction-schema.md`. At minimum:

1. Evidence: cite the source rows.
2. Transfer: test a novel scenario.
3. Specificity: explain why the rule is not generic.
4. Trigger: write should-trigger and should-not-trigger prompts.
5. Executability: list required inputs and done criteria.
6. Boundary: list non-use cases.

## Phase 5: Skill Architecture

Choose structure:

| Situation | Structure |
|---|---|
| One coherent workflow | One skill with references |
| Multiple independent methods | Skill set with index |
| Heavy source knowledge | Lean `SKILL.md` plus on-demand references |
| Deterministic transform | Add scripts |
| Reusable output format | Add assets/templates |
| Many related skills | Add relation map: depends-on, composes-with, contrasts-with |

## Phase 6: Skill Writing

Write in this order:

1. Name: kebab-case, action-oriented.
2. Description: triggering conditions only; include non-triggers when needed.
3. Core principle: one or two sentences.
4. Workflow decision tree or modes.
5. Steps with input, action, output, completion standard.
6. Boundaries and failure modes.
7. References/resources.
8. Tests and rubric.

Avoid putting a long theory essay in `SKILL.md`. The agent needs a way to act.

## Phase 7: Evaluation

Use four layers:

- Trigger tests: does the agent load the skill at the right time?
- Functional tests: does the workflow produce the expected artifact?
- Boundary tests: does the agent refuse or defer when the skill should not apply?
- Update tests: does the skill improve after feedback without breaking its original cases?

## Phase 8: Delivery

For a new skill, deliver:

- Skill folder path
- Source inventory and extraction report
- Files created
- Validation performed
- Known assumptions
- Next test prompts

For a skill update, deliver:

- Evidence for change
- Files changed
- Old failure and new guardrail
- Regression prompts

## Anti-Patterns During Workflow Design

- Treating media as the method: "X writing skill" instead of "compressed thesis construction skill"
- Producing a prompt library without triggers or boundaries
- Turning every section into its own skill
- Writing advice that cannot be tested
- Removing all source-specific texture and leaving generic strategy words
