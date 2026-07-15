# Representation Router

Choose an intermediate representation that preserves the relationships relevant to the target capability. Do not standardize on YAML merely for consistency.

| Artifact | Primary Representation | Supporting Representation |
|---|---|---|
| Short or long text | annotated Markdown move map | argument graph, voice profile, evidence map |
| Image/poster | scene graph and spatial hierarchy YAML | annotated image, palette and typography notes |
| Video | timeline and shot map | audio/visual relation map, retention moments |
| Audio | time-coded segment map | speaker, energy, music, and semantic layers |
| Research corpus | evidence table | query log, source graph, contradiction map |
| Workflow/log | state machine or flow | decision table, exception and recovery map |
| Code/repository | interface and dependency map | call graph, tests, failure patterns |
| Data/report | schema and metric definitions | transformation lineage and validation rules |

After artifact observation, route induced knowledge by role:

| Knowledge role | Preferred representation |
|---|---|
| doctrine, philosophy, value tensions | Markdown argument with evidence and counterexamples |
| cross-case alignment | CSV, SQLite, or JSONL |
| grammar and style relations | Markdown pattern plus stable typed fields when needed |
| executable decision | validated JSON decision unit |
| tool capabilities | JSON registry or database |
| workflow and handoffs | execution DAG plus adapters or scripts |
| activation and orchestration | lean `SKILL.md` |
| quality | rubric, hard gates, reference comparisons, technical tests |

## Format Rules

- Use Markdown for meaning, rationale, voice, interpretation, and examples.
- Use YAML/JSON for stable fields, variables, constraints, manifests, and stage handoffs.
- Use tables or graphs for relationships, comparisons, sequences, and state transitions.
- Use code only for deterministic behavior that must be enforced.
- Keep the raw artifact or a rights-safe pointer as the source of truth.
- Do not place doctrine, evidence rows, tool capabilities, and executable graphs into one universal YAML document.

## Routing Questions

1. Is the important relationship spatial, temporal, logical, procedural, or evidential?
2. Which details must survive into generation or execution?
3. Which details are merely decorative observations?
4. Will the next stage validate fields mechanically or interpret them semantically?
5. Can the representation link every claim back to a source location?

## Canonical Cross-Archetype Fields

All representations should expose these concepts, even when the concrete format differs:

```yaml
intent:
target_state:
functions:
relationships:
evidence:
constraints:
boundaries:
quality_criteria:
source_links:
```

These fields are the shared semantic interface. They are not a requirement to serialize the entire artifact as YAML.
