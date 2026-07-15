# Workflow Design

This document expands the v0.2 harness in `SKILL.md`. It is retained as a compatibility reference for users of v0.1.

## Pipeline

### Phase 0: Capability Contract

Define the capability, future user, execution environment, trigger, required inputs, output contract, quality target, and prohibited behavior. Assume skill construction is the requested outcome; do not spend a phase debating whether a skill should exist.

### Phase 1: Evidence Plan

Inventory supplied artifacts before asking questions. Separate:

- supplied evidence
- missing evidence
- user knowledge that requires confirmation
- external research axes
- rights and privacy constraints

For research, define the question, preferred source types, minimum evidence, freshness class, and stop condition. Popularity is a discovery signal, not proof of quality.

### Phase 2: Native Observation

Choose the representation by artifact mechanics:

| Artifact | Primary representation |
|---|---|
| Text | Annotated Markdown, move map, argument graph, voice profile |
| Image | Observation YAML or JSON plus interpretive Markdown |
| Video | Timeline, shot map, audio/visual relation map |
| Research | Evidence table, query log, contradiction graph |
| Process | State machine, decision table, exception map |
| Tool/API | Interface schema, state model, error/recovery table |

Serialization is not abstraction. A detailed image YAML can still encode one exact image.

### Phase 3: Evidence-Labeled Inference

Keep claims in separate classes:

- `observed`: directly present in the artifact
- `inferred`: a plausible explanation of the production choice
- `user-confirmed`: explicitly validated by the user or creator
- `hypothesis`: useful but not yet adequately supported

Do not present inferred creator intent as observation.

### Phase 4: Pattern Abstraction

Convert observations into a generative pattern:

1. State the starting and target audience/user state.
2. Name the production function.
3. Separate invariants from variables.
4. Add constraints among variables.
5. Add selection rules for variants.
6. Record anti-patterns and anti-clone rules.
7. Link every candidate invariant to source evidence.

One source yields candidate invariants. Comparative evidence or transfer tests are required before claiming universality.

### Phase 5: Rubric Freeze

Define the rubric before generating the skill or test output. Combine:

- universal quality, rights, and safety
- skill archetype and modality quality
- platform and objective fit
- project-specific taste and constraints

The default pass contract is total score `>= 80`, every critical dimension `>= 60`, all hard gates passing, and at most three rounds.

### Phase 6: Skill Package

Use one coherent skill unless independent triggers or execution environments require separation.

| Knowledge | Destination |
|---|---|
| Trigger, decision routing, core procedure | `SKILL.md` |
| Detailed methods, domain rules, examples | `references/` |
| Templates and files copied into outputs | `assets/` |
| Deterministic transforms and validators | `scripts/` |
| Mutable run evidence and evaluations | Project workspace outside the installed skill |

### Phase 7: Forward Test

Use the generated skill on an unseen but related input. Generate a real output, not only prompt tests. Evaluate that output with the frozen rubric.

### Phase 8: Repair Loop

Route each failure to the lowest responsible layer:

1. current output
2. generated `SKILL.md`
3. reference knowledge
4. asset template
5. abstraction pattern
6. source evidence
7. evaluation rubric

Repair, regenerate, and re-evaluate. Do not permanently modify the skill for a one-off defect unless it reveals a recurring rule.

### Phase 9: Promotion

Promote only when evidence, traceability, specificity, abstraction, anti-clone behavior, trigger quality, executability, boundaries, and output quality pass. Otherwise keep the result experimental, narrow its scope, or request stronger evidence.

## Stop Conditions

Stop and surface the gap when:

- required evidence is unavailable or cannot be used lawfully
- the desired outcome cannot be evaluated even by a credible proxy
- three repair rounds fail the pass contract
- contradictory sources cannot be resolved without a human decision

Deliver the best auditable attempt with unresolved assumptions rather than silently inventing certainty.
