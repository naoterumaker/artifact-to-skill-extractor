# Artifact To Skill Extractor v0.2

`artifact-to-skill-extractor` is a Codex skill-construction harness. It turns real artifacts, examples, expert practice, research, and failed outputs into a reusable skill, then tests that skill on a new output through a Generator/Evaluator repair loop.

## What Changed In v0.2

- Starts with a capability contract and evidence plan.
- Routes text, image, video, research, process, and tool artifacts to native representations.
- Separates observations, inferences, hypotheses, invariants, variables, and constraints.
- Treats YAML as a representation format, not abstraction by itself.
- Composes production function, modality, platform, objective, and audience context.
- Freezes a weighted rubric before generation.
- Generates a real test output and repairs the lowest responsible layer for up to three rounds.
- Keeps mutable evidence and evaluations in an auditable project workspace.
- Adds measured transfer, failure harvesting, lifecycle status, and cost-aware extraction.

## Core Flow

```text
interview
  -> evidence plan
  -> native observation
  -> generative abstraction
  -> frozen rubric
  -> skill package
  -> test output
  -> evaluator
  -> targeted repair
  -> promotion or scoped experimental status
```

## Repository Layout

```text
artifact-to-skill-extractor/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── modalities/
│   ├── platforms/
│   ├── objectives/
│   ├── research/
│   └── worked-example-*.md
├── assets/
│   ├── templates/
│   └── examples/
├── scripts/
└── tests/
```

## Initialize A Project

```bash
python3 scripts/init_project.py my-skill-project --output /path/to/work
python3 scripts/validate_project.py /path/to/work/my-skill-project
python3 scripts/estimate_extraction.py /path/to/artifacts
```

The project keeps intake, corpus, observations, patterns, rubric, generated skill, outputs, evaluations, and harvested failures in separate stages. It is intentionally outside the installed skill so run-specific evidence does not pollute reusable instructions.

## Worked Tests

- **X article:** an actual public X Article is reduced to a functional move map, converted into a candidate generative pattern, and tested by producing a different article about evaluation-driven skill design.
- **Image:** a CC0 Paris travel poster is represented as image observations, abstracted into functional relationships, and tested by producing a materially different Hokkaido poster.
- **Self-extraction:** the v0.2 harness audits its own missing transfer, failure-harvest, lifecycle, and cost layers, then repairs and re-scores itself.

The examples preserve source URLs, rights notes, scoring records, and repair decisions. They do not claim that pre-publication scores guarantee impressions or other platform outcomes.

## Verify v0.2

```bash
python3 scripts/validate_skill.py . --strict
python3 -m unittest discover -s tests -v
python3 scripts/run_test_prompts.py assets/test-prompts-template.json
python3 scripts/score_evaluation.py \
  assets/examples/x-article/evaluation-rubric.json \
  assets/examples/x-article/evaluation-round-2.json
python3 scripts/score_evaluation.py \
  assets/examples/image/evaluation-rubric.json \
  assets/examples/image/evaluation-round-2.json
python3 scripts/score_evaluation.py \
  assets/examples/self-extraction/evaluation-rubric.json \
  assets/examples/self-extraction/evaluation-round-2.json
```

`score_evaluation.py` exits with `0` for pass, `2` for revise, and `1` for malformed inputs.

## Install For Codex

```bash
mkdir -p ~/.codex/skills
cp -R artifact-to-skill-extractor ~/.codex/skills/
```

Start a new Codex task after installation so the updated skill metadata is discovered.
