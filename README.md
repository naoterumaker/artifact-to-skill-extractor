# Artifact To Skill Extractor v0.3

`artifact-to-skill-extractor` is an evidence-aware production-system compiler for Codex. It turns artifacts, demonstrations, revisions, failures, traces, and creator evidence into scoped doctrine, grammar, executable decisions, tool assignments, workflows, skills, and evaluators. It then runs the compiled system on a new concrete case and repairs the lowest responsible layer.

This is broader than a content-template extractor. It supports procedural systems such as research or operations, creative systems such as text and image production, and hybrid systems whose output depends on agent-callable tools.

## What Changed In v0.3

- Introduces `procedural`, `creative`, and `hybrid` compilation profiles.
- Enforces an evidence ceiling: one artifact supports observations and candidate grammar, not verified creator doctrine.
- Separates recovered creator doctrine, user-confirmed project doctrine, platform constraints, and model preference.
- Aligns multiple artifacts, revisions, accepted/rejected alternatives, and failures before inducing principles.
- Compiles function labels into executable `WHEN / IF / DO / VERIFY / ELSE` decision units.
- Represents toolchains as capability registries and execution graphs, with agency, state, retries, provenance, and fallbacks.
- Routes each knowledge role to an appropriate format instead of forcing all artifacts into YAML.
- Adds deterministic v0.3 project and intermediate-representation validation.
- Upgrades the X Article and image tests into complete creative-system examples.

## Compiler Flow

```text
capability contract
  -> corpus and evidence ceiling
  -> modality-native observations
  -> cross-case comparison
  -> doctrine + grammar + decision units
  -> capability registry + execution graph
  -> frozen evaluation contract
  -> agent-callable package
  -> unseen concrete output
  -> evaluation, repair, and lifecycle decision
```

`SKILL.md` is the activation and orchestration layer. Detailed production knowledge lives in references, reusable output resources live in assets, deterministic behavior lives in scripts, and mutable run evidence lives in an external project workspace.

## Profiles

| Profile | Use when | Minimum system |
|---|---|---|
| `procedural` | correctness depends on steps, branches, state, and recovery | decision units, workflow, verifier, fallback |
| `creative` | quality depends on values, expression, medium, and taste | project or recovered doctrine, grammar, decision units, evaluators |
| `hybrid` | creative work also depends on an automated or stateful toolchain | creative system plus capability registry, execution graph, and adapters |

## Representation Policy

YAML is not the abstraction. A detailed image YAML is still a concrete description of one image.

- Text uses annotated Markdown, argument/evidence maps, and language patterns.
- Images use spatial or scene records plus interpretive prose.
- Video uses timelines, shot maps, and audiovisual relations.
- Doctrine uses evidence-backed Markdown conflict rules.
- Decisions use validated JSON contracts.
- Tool capabilities use JSON registries.
- Execution uses DAGs, scripts, CLIs, APIs, MCPs, or SDK adapters as required.

## Initialize A Project

```bash
python3 scripts/init_project.py my-system \
  --profile creative \
  --output /path/to/work
python3 scripts/validate_project.py /path/to/work/my-system
python3 scripts/validate_system_ir.py /path/to/work/my-system --complete
```

The initializer creates separate stages for intake, corpus, observations, comparisons, doctrine, grammar, decision units, toolchain, evaluation, execution graphs, generated system, outputs, and failures. Structural validation may pass while templates are still empty; `--complete` must pass before promotion.

## Worked Tests

### X Article: creative profile

A permitted public article is represented as an annotated move map. The example explicitly refuses to recover the source creator's philosophy from one article, uses user-confirmed project doctrine instead, compiles an evidence-proportionate claim decision, and generates a materially different article. The score improves from `75.2` to `87.9`; live X performance remains unknown.

### Image: hybrid profile

A CC0 Paris poster is observed with spatial YAML and interpretive Markdown. The concrete observation is then abstracted into candidate grammar and an executable composition decision. HTML/CSS, Playwright, and SIPS are recorded by capability rather than name alone. A different Hokkaido poster improves from `75.0` to `88.2` after full-size and thumbnail evaluation.

### Self-extraction

The repository is treated as its own artifact. The v0.3 owner reviews expose that v0.2 recovered patterns and workflows but did not explicitly compile production doctrine, grammar, agency, and tool capability. Those corrections are preserved as user-confirmed compiler doctrine and structural regression tests. The prior `88.2` self-audit remains diagnostic, not independent promotion evidence.

## Verify v0.3

```bash
python3 scripts/validate_skill.py . --strict
python3 scripts/validate_system_ir.py \
  assets/examples/x-article/creative-system --complete
python3 scripts/validate_system_ir.py \
  assets/examples/image/creative-system --complete
python3 -m unittest discover -s tests -v
python3 scripts/run_test_prompts.py assets/test-prompts-template.json
python3 scripts/score_evaluation.py \
  assets/examples/x-article/evaluation-rubric.json \
  assets/examples/x-article/evaluation-round-2.json
python3 scripts/score_evaluation.py \
  assets/examples/image/evaluation-rubric.json \
  assets/examples/image/evaluation-round-2.json
```

`score_evaluation.py` exits with `0` for pass, `2` for revise, and `1` for malformed inputs. Passing structural and example tests does not prove universal transfer, creator-doctrine recovery, or platform performance; lifecycle status remains `experimental`.

## Install For Codex

```bash
rsync -a --delete \
  --exclude .git --exclude __pycache__ --exclude '*.pyc' \
  artifact-to-skill-extractor/ \
  ~/.codex/skills/artifact-to-skill-extractor/
```

Start a new Codex task after installation so updated metadata is discovered.
