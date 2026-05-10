# Skill Packaging

Package only what a future agent needs to execute the workflow reliably.

## Directory Decision

```text
skill-name/
├── SKILL.md              # required, lean activation + workflow
├── agents/openai.yaml    # Codex UI metadata when relevant
├── references/           # detailed guidance loaded on demand
├── scripts/              # deterministic or fragile operations
├── assets/               # templates or files copied into outputs
└── evals/                # optional test prompts or benchmark fixtures
```

Use `references/` for detail that informs reasoning. Use `assets/` for templates that are copied or adapted into final outputs.

## SKILL.md Rules

### Frontmatter

Use only required fields unless the platform needs more:

```yaml
---
name: skill-name
description: Use when ...
---
```

The description is the activation mechanism. It should answer "when should an agent read this skill?" Do not summarize the internal workflow so heavily that the agent tries to act from the description alone.

Good description shape:

```text
Use when the user wants to convert X into Y, especially when they provide A, B, or C. Trigger on phrases such as ... Not for ...
```

### Body

Recommended sections:

1. Core principle
2. Operating modes
3. Workflow
4. Boundaries
5. Output format
6. Quality rules
7. References

Keep details under progressive disclosure. Put large tables, schemas, and variants in references.

## What Goes Where

| Content | Location |
|---|---|
| Trigger conditions | `SKILL.md` frontmatter |
| Short workflow | `SKILL.md` body |
| Artifact-specific reading guides | `references/` |
| Extraction schemas | `references/` |
| Evaluation rubrics | `references/` or `evals/` |
| Copyable output templates | `assets/` |
| Deterministic parsers or converters | `scripts/` |
| Example source artifacts | `assets/examples/` only if safe and allowed |

## Skill Unit Template

```markdown
---
name: <skill-name>
description: Use when <specific situation>. Trigger on <phrases, artifacts, tasks>. Not for <near misses>.
---

# <Skill Title>

## Core Principle

<One precise sentence.>

## Workflow

1. <Action>
   - Input:
   - Output:
   - Completion standard:

## Decision Rules

| Situation | Do |
|---|---|

## Boundaries

- Do not use when ...
- Ask for clarification when ...

## Quality Check

- ...

## References

- `references/...`
```

## Choosing Scripts

Add scripts when the skill repeatedly needs:

- file parsing
- schema validation
- format conversion
- test generation
- deterministic extraction
- external API calls

Do not add scripts for judgment-heavy tasks where the model needs to reason from context.

## Skill Library Relations

When a project produces many skills, maintain an index:

```yaml
skill: offer-teardown
depends_on: [audience-intake]
composes_with: [lp-builder, ad-brief-builder]
contrasts_with: [copy-polisher]
similar_to: []
```

Relationship types:

- `depends_on`: cannot run well without the other skill
- `composes_with`: often used together
- `contrasts_with`: adjacent but different trigger
- `similar_to`: possible duplicate or variant

## Update Strategy

When feedback arrives:

1. Identify whether the failure is trigger, workflow, boundary, example, rubric, or missing resource.
2. Patch the smallest relevant section.
3. Add a regression prompt that would have caught the old behavior.
4. Re-run validation.
