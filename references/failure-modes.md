# Failure Modes

Use this list when reviewing extraction reports and generated skills.

## Abstraction Failures

| Failure | Symptom | Fix |
|---|---|---|
| Surface copying | The skill says "use a contrarian hook" but not why or when | Extract function, audience state, and decision rule |
| Generic abstraction | Output says "understand the audience" and "provide value" | Add concrete inputs, checks, examples, and stop conditions |
| Medium trap | The skill becomes "X skill" or "YouTube skill" without transferable logic | Rename around production function |
| One-example universal rule | A single artifact becomes a law | Mark hypothesis or require more evidence |
| Over-fragmentation | Every section becomes a separate skill | Merge steps that share trigger and outcome |
| Under-fragmentation | One massive skill handles unrelated tasks | Split by trigger and output |

## Skill Packaging Failures

| Failure | Symptom | Fix |
|---|---|---|
| Trigger too broad | Activates for any "content" or "skill" request | Add non-triggers and specific source conditions |
| Trigger too narrow | Only activates for one platform or phrasing | Add synonyms and artifact types |
| Workflow in description | Agent acts from frontmatter and skips body | Keep description to when-to-use |
| No boundary | Skill is used where it should not apply | Add non-use cases and near misses |
| No tests | Cannot tell if the skill works | Add trigger, boundary, and functional prompts |
| Wrong resource placement | SKILL.md is huge or assets contain reasoning docs | Move detail to references; templates to assets |

## Evidence Failures

| Failure | Symptom | Fix |
|---|---|---|
| No source trace | Rules cannot be traced back | Add source ids and element ids |
| Quote-heavy output | Skill copies artifact text | Paraphrase structure; quote minimally only when needed |
| Missing creator context | Decisions are misread without audience/constraints | Capture context before extraction |
| Ignoring failures | Only successful examples are analyzed | Include rejected, edited, or low-performing artifacts if available |

## Execution Failures

| Failure | Symptom | Fix |
|---|---|---|
| Unclear input | Future agent asks the same intake questions every time | Define required and optional inputs |
| No done condition | Agent keeps improving forever | Add completion standards |
| No fallback | Tool or source unavailable breaks workflow | Add recovery or ask-user branch |
| Human-only judgment | Skill says "use taste" or "make it good" | Convert taste into rubric signals |

## Review Heuristic

If a future agent could produce the same output from common sense without the skill, the extraction is not specific enough.
