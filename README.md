# Artifact To Skill Extractor

`artifact-to-skill-extractor` is a Codex skill for turning concrete artifacts into reusable AI agent skills.

It is designed for cases where you have real examples, finished outputs, process logs, transcripts, books, prompts, runbooks, repositories, or expert notes and want to extract the hidden production knowledge behind them.

## What It Produces

- Source inventory
- Functional decomposition of concrete artifacts
- Candidate skill units
- Verification gates for reuse, specificity, triggers, executability, and boundaries
- A packaged AI agent skill structure
- Evaluation prompts and rubrics

## Skill Structure

```text
artifact-to-skill-extractor/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── artifact-type-routing.md
│   ├── evaluation-and-tests.md
│   ├── extraction-schema.md
│   ├── failure-modes.md
│   ├── skill-packaging.md
│   ├── source-influences.md
│   └── workflow-design.md
└── assets/
    ├── extraction-report-template.md
    ├── skill-template.md
    └── test-prompts-template.json
```

## Use Cases

- Convert examples into a reusable Codex or Claude skill
- Reverse-engineer workflows from finished outputs
- Formalize tacit expert knowledge into SOPs
- Turn prompts into durable skill packages
- Extract rubrics from good and bad outputs
- Update existing skills from feedback or failed runs

## Install For Codex

Copy or symlink this folder into a Codex skills directory:

```bash
mkdir -p ~/.codex/skills
cp -R artifact-to-skill-extractor ~/.codex/skills/
```

Then start a new Codex session and ask to use `artifact-to-skill-extractor`.
