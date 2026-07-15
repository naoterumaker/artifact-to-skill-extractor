# Evaluation And Tests

Read `rubric-design.md`, `evaluator-protocol.md`, and `repair-routing.md` for the operative v0.3 method.

## Test Surfaces

| Surface | Minimum | Purpose |
|---|---:|---|
| Should trigger | 5 | confirm realistic activation language |
| Should not trigger | 5 | detect broad or ambiguous activation |
| Boundary | 3 | confirm clarification, refusal, or routing behavior |
| Functional | 3 | confirm required artifacts, decisions, and checks |
| Forward output | 1 | evaluate the compiled system on an unseen related input |
| Recovery | 1 per critical branch | confirm verifier, retry, fallback, and escalation |
| Doctrine prediction | 1 per promoted doctrine hypothesis | test a held-out choice before revealing the actual result |

Prompt tests alone do not establish output quality. Structural validation alone does not establish that decision content is correct. A forward output and evidence-backed evaluation are required.

## Deterministic Validation

Use:

```bash
python3 scripts/validate_skill.py <skill> --strict
python3 scripts/validate_project.py <project>
python3 scripts/validate_system_ir.py <project> --complete
```

`validate_project.py` checks the project schema and managed contracts. `validate_system_ir.py` checks decision units, capability assignments, tool records, execution nodes, bounded cycles, required creative documents, and profile consistency. Passing these checks means the interfaces are complete, not that semantic claims are true.

## Frozen Rubric

Create the output rubric before generation using `assets/templates/evaluation-rubric.json` or the broader `assets/templates/system-evaluation-rubric.json`. Record results with the matching `evaluation-result.json` or `system-evaluation-result.json`. Weights must total 100.

```text
total score >= 80
each critical dimension >= 60
all hard gates pass
maximum 3 rounds
```

For creative or hybrid systems, include supported layers only: intent/doctrine, grammar/medium, decision executability, toolchain/agency, and concrete output quality. Redistribute weights before freezing when a layer is unavailable.

## Evaluation Record

Each score needs observable evidence. Each issue names severity, artifact location, violated criterion, evidence, lowest responsible layer, required repair, and expected effect. Confidence or fluency is not evidence.

When the user corrects an output:

1. preserve the correction as evidence
2. classify the defect and source opportunity
3. add a reproducing case
4. locate the lowest responsible layer
5. patch only that layer
6. rerun affected tests and at least one prior passing case

## Outcome Claims

Pre-publication checks can evaluate structure, readability, packaging, promise alignment, technical integrity, and platform fit. Impressions, CTR, retention, engagement, conversion, and revenue require post-publication analytics. Never convert an internal rubric score into a guaranteed real-world outcome.
