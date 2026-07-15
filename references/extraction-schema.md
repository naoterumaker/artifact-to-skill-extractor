# Extraction Schema

Use this schema to convert concrete evidence into reusable production knowledge. It is a conceptual schema, not a requirement to serialize every artifact as YAML. Choose the representation with `representation-router.md` and keep source evidence separate from inferred rules.

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

## Claim Status

Every extracted claim must carry one status:

| Status | Meaning |
|---|---|
| `observed` | Directly present and locatable in the source |
| `inferred` | Plausible production intent supported by observations |
| `user-confirmed` | Explicitly validated by the user or creator |
| `hypothesis` | Useful candidate requiring further evidence or a transfer test |

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

For non-text artifacts, replace `surface` and `sequence_position` with artifact-native fields such as region, timeline, spatial relation, state, or transition. Preserve the same functional questions without forcing the same data shape.

## Production-System Intermediate Representation

Do not jump directly from extracted elements to a monolithic skill template. Route supported knowledge into separate roles:

| Role | Minimum content | Preferred representation |
|---|---|---|
| doctrine | conflict rule, support, counterevidence, scope, confidence, held-out prediction | evidence-backed Markdown |
| grammar | function, elements, relations, variables, constraints, selection rules, anti-patterns | Markdown pattern plus typed fields when needed |
| executable decision | context, evidence, rule, action, verifier, fallback, provenance, agency | `assets/templates/decision-unit.json` |
| capabilities | required operations, candidate tools, assignments, unsupported capabilities | `assets/templates/tool-capability-registry.json` |
| execution | nodes, owners, state, handoffs, retries, verifiers, fallbacks | `assets/templates/execution-graph.json` |
| activation | trigger, non-trigger, short workflow, routing, boundaries | lean `SKILL.md` |

A function label such as `build trust` is only an index. It becomes executable when compiled into:

```text
WHEN the context is eligible
IF required evidence and preconditions hold
DO a bounded operation
VERIFY observable success criteria
ELSE repair, route, or escalate
```

Every decision unit retains source locations, evidence status, scope, counterevidence, confidence, and agency. Unsupported hypotheses must not become unconditional skill instructions.

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

For creative doctrine, add a held-out prediction gate. For hybrid systems, add tool-capability coverage and execution-graph integrity gates. A structurally valid package may remain `experimental` when evidence or independent evaluation is weak.

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

1. Source inventory and evidence ceiling
2. Top 5 production functions
3. Supported doctrine, grammar, and decision candidates
4. Capability gaps and agency boundaries
5. Verification decisions and proposed package profile

The report must also identify which details remain source-specific and which anti-clone rules prevent direct surface reproduction.
