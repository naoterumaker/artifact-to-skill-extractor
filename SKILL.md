---
name: artifact-to-skill-extractor
description: Use when the user wants to turn concrete artifacts, content examples, finished outputs, books, transcripts, runbooks, process logs, repositories, prompts, SOPs, or expert practice into reusable AI agent skills. Trigger on requests to extract production knowledge, reverse-engineer a workflow from examples, convert examples into a skill/SOP/playbook, build a Codex or Claude Skill from real work, formalize tacit knowledge, generate evaluation rubrics from outputs, or update an existing skill from feedback. Not for simple summaries or one-off content generation.
---

# Artifact To Skill Extractor

## Core Principle

Extract structure, not summaries. The goal is to transform concrete artifacts into reusable production knowledge: triggers, inputs, decisions, workflow steps, boundaries, failure modes, rubrics, and tests that an agent can use later.

This skill treats an artifact as evidence of hidden production decisions. Do not copy its surface form unless the surface itself is the reusable mechanism.

## Operating Modes

Choose the smallest mode that satisfies the request:

| Mode | Use When | Output |
|---|---|---|
| Analyze only | User wants research, extraction, or a map before creating files | Extraction report |
| Skill package | User wants a usable skill or SOP | Skill folder with `SKILL.md` and resources |
| Skill update | User has an existing skill plus feedback or new examples | Patch plan or edited skill files |
| Library design | User has many examples/domains and wants a system | Skill taxonomy, relation map, rollout plan |

If the user gives no artifact, ask for one. Do not invent the source evidence. If they ask for a speculative first draft, mark all ungrounded rules as hypotheses.

## Workflow

### 1. Inventory The Evidence

List every source before interpreting it. Classify each item using `references/artifact-type-routing.md`:

- Finished artifacts: posts, LPs, ads, videos, docs, decks, UI, code, books, emails, courses
- Process traces: transcripts, session logs, terminal runs, edit histories, review comments
- Knowledge sources: expert notes, frameworks, manuals, examples, policies
- Comparative sets: winners/losers, before/after, alternatives, feedback

Capture source id, artifact type, audience/user, purpose, context, and reliability. Use `references/extraction-schema.md` for fields.

### 2. Decompose By Function

For each artifact, separate:

- **Surface**: what is visible, such as headline, section order, command, slide, step, UI control
- **Function**: what that element does in the workflow
- **Decision**: why this choice was made instead of plausible alternatives
- **Input needed**: what future users must provide to reproduce it
- **Constraint**: medium, tool, audience, compliance, cost, time, format, or environment limit
- **Failure mode**: how this breaks when copied blindly

Never stop at labels like "hook", "CTA", "summary", or "research". Translate them into operational roles.

### 3. Extract Candidate Skill Units

Create candidate units only when they are reusable, modular, and teach something the base model may not reliably infer.

Use these lenses:

- **Example -> Pattern**: repeated structure across examples
- **Artifact -> Workflow**: finished output implies a production sequence
- **Expert Practice -> SOP**: human judgment becomes decision rules
- **Tacit Knowledge -> Explicit Rules**: unstated criteria become checks and boundaries
- **Prompt -> Skill**: a one-off prompt becomes durable instructions plus tests
- **Workflow -> Agent Skill**: human steps become agent-executable actions
- **Cases -> Playbook**: multiple cases become a scenario map
- **Output -> Rubric**: good outputs reveal evaluation criteria
- **Feedback -> Skill Update**: corrections become guardrails and examples

Avoid over-fragmenting. If several steps only work as one coherent workflow, keep them as one skill and move substeps to references.

### 4. Verify The Extraction

Run these gates before packaging:

| Gate | Question |
|---|---|
| Evidence | Is the rule grounded in source artifacts, not model taste? |
| Transfer | Can it guide a new but related case? |
| Specificity | Is it more useful than generic advice? |
| Trigger | Can an agent know when to load it and when not to? |
| Executability | Are inputs, steps, outputs, and stop conditions clear? |
| Boundary | Are non-use cases and failure modes explicit? |

If a rule fails evidence but seems valuable, keep it as a hypothesis. If it fails transfer or specificity, demote it to an example.

### 5. Package The Skill

Use `references/skill-packaging.md`.

Default structure:

```text
skill-name/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── workflow.md
│   ├── rubric.md
│   └── examples.md
└── assets/
    └── templates...
```

Keep `SKILL.md` lean: trigger, core principle, decision tree, workflow, and references. Put detailed schemas, examples, rubrics, and variant-specific guidance in `references/`. Put reusable output templates in `assets/`.

### 6. Test And Iterate

Use `references/evaluation-and-tests.md`.

At minimum produce:

- 5 should-trigger prompts
- 5 should-not-trigger near misses
- 3 boundary prompts
- 3 realistic execution cases
- A rubric covering output quality and misuse risk

If updating an existing skill, preserve what already works. Add the smallest rule, example, or boundary that prevents the observed failure.

## Output Formats

For analyze-only work, use `assets/extraction-report-template.md`.

For a new skill, produce:

1. Extraction report with source trace
2. Proposed skill name and trigger description
3. Skill folder files
4. Evaluation prompts and rubric
5. Remaining assumptions

For skill updates, produce:

1. Observed failure or new source evidence
2. Proposed change
3. Files changed
4. Tests or prompts that would catch the old behavior

## Quality Rules

- Preserve exact names for named frameworks, methods, commands, and domain terms.
- Write rules in operational language: when, input, action, output, stop condition.
- Keep evidence and synthesis separate.
- Prefer one durable workflow over many brittle mini-skills.
- Do not make universal rules from a single weak example.
- Do not let a platform label such as X, note, YouTube, LP, GitHub, or book become the abstraction. The abstraction is the production function.

## References

- `references/extraction-schema.md` - canonical extraction fields
- `references/artifact-type-routing.md` - how to read different artifact types
- `references/workflow-design.md` - full extraction pipeline
- `references/skill-packaging.md` - converting extraction to skill files
- `references/evaluation-and-tests.md` - rubrics and prompt tests
- `references/failure-modes.md` - common abstraction errors
- `references/source-influences.md` - design influences from reviewed projects
