# Extraction Schema

Use this schema to convert concrete evidence into reusable production knowledge. Keep source evidence separate from inferred rules.

## Source Inventory

| Field | Purpose |
|---|---|
| `source_id` | Stable id, e.g. `src-001` |
| `source_type` | Artifact, process trace, expert note, comparative set, feedback |
| `artifact_type` | Post, article, video, LP, ad, deck, book, UI, repo, runbook, transcript, code, prompt, etc. |
| `location` | File path, URL, timestamp, section, line, or page |
| `creator_context` | Who made it, for whom, and under what constraints |
| `intended_outcome` | What the artifact tries to make happen |
| `evidence_strength` | Strong, medium, weak, or hypothesis |
| `rights_note` | Any copying, quoting, privacy, or confidentiality constraint |

## Element Extraction

Use one row per meaningful element.

| Field | Question |
|---|---|
| `element_id` | Stable id, e.g. `el-014` |
| `surface` | What is visibly present? |
| `sequence_position` | Where does it occur in the artifact or workflow? |
| `production_function` | What job does this element perform? |
| `audience_or_user_state` | What does the recipient/user likely know, feel, need, or fear here? |
| `decision_rule` | Why this move instead of a plausible alternative? |
| `required_inputs` | What future input is needed to reproduce the move? |
| `constraints` | Medium, format, tool, legal, timing, cost, tone, data, or audience limits |
| `proof_or_feedback` | What shows this move works or matters? |
| `failure_modes` | How does this fail when copied blindly? |
| `transferability` | High, medium, low, or source-specific |
| `candidate_skill_unit` | Which reusable unit might this feed? |

## Candidate Skill Unit

```yaml
id: unit-001
title: concise production capability
source_elements: [el-001, el-004]
problem_solved: what recurring situation this handles
trigger_language:
  - user phrasing that should activate the skill
non_triggers:
  - similar phrasing that should not activate it
inputs:
  required: []
  optional: []
workflow:
  - step: action
    completion_standard: how to know this is done
decision_rules:
  - if/when rule
boundaries:
  - when not to use
failure_modes:
  - likely error and prevention
rubric:
  - quality criterion
resources_needed:
  scripts: []
  references: []
  assets: []
status: verified | hypothesis | rejected
```

## Verification Record

```yaml
unit_id: unit-001
evidence_gate:
  status: pass | weak | fail
  notes: source-backed reason
transfer_gate:
  status: pass | weak | fail
  novel_case: short unseen scenario
  expected_guidance: what the unit would tell the agent to do
specificity_gate:
  status: pass | weak | fail
  why_not_generic: explanation
trigger_gate:
  status: pass | weak | fail
  should_trigger: []
  should_not_trigger: []
executability_gate:
  status: pass | weak | fail
  missing_inputs: []
boundary_gate:
  status: pass | weak | fail
  non_use_cases: []
decision: package | merge | demote | reject
```

## Function Labels

Prefer precise function labels over medium-specific labels.

| Broad Function | More Useful Labels |
|---|---|
| Attention | interrupt assumption, create curiosity gap, compress stakes, signal relevance |
| Explanation | define term, sequence logic, compare alternatives, expose mechanism |
| Trust | cite evidence, show process, demonstrate constraint awareness, handle objection |
| Conversion | reduce friction, clarify next action, justify timing, make commitment reversible |
| Execution | validate input, transform data, choose branch, recover from failure, verify output |
| Learning | extract framework, define boundary, create analogy, generate practice case |
| Evaluation | define rubric, compare output to target, identify failure, propose repair |

## Minimal Extraction Report

When time is short, capture only:

1. Source inventory
2. Top 5 reusable functions
3. Candidate skill units
4. Verification decisions
5. Proposed skill package structure
