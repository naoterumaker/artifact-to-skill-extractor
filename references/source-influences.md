# Source Influences

This skill borrows design patterns from the following reviewed projects and adapts them for arbitrary artifact-to-skill extraction.

These sources are design influences, not proof that any extracted rule will improve a user's output. The harness still requires source tracing, forward tests, and scoped lifecycle decisions.

## Programmatic Skill Induction And Workflow Memory

Sources:

- https://github.com/zorazrw/agent-skill-induction
- https://github.com/zorazrw/agent-workflow-memory

Useful pattern:

- Induce candidate procedures from execution evidence, validate them, and expose only accepted procedures to later runs.
- Remove example-specific context while preserving executable structure.

Adaptation:

- This skill separates observation from generative abstraction and uses promotion gates rather than treating every extraction as reusable knowledge.

## EvoSkill And MemSkill

Sources:

- https://github.com/sentient-agi/EvoSkill
- https://github.com/ViktorAxelsen/MemSkill

Useful pattern:

- Failed or difficult trajectories expose missing capabilities.
- Skill improvement needs held-out evaluation rather than self-asserted progress.

Adaptation:

- `failure-harvest-loop.md` separates one-run repair from repeated-failure promotion and preserves rejected hypotheses.

## Lenny Skills Database

Source: https://sidbharath.com/blog/building-lenny-skills-database/

Useful pattern:

- Large knowledge corpora benefit from an explicit taxonomy plus a route for genuinely novel categories.
- Unbounded bottom-up framework collection creates duplicate and weakly scoped units.

Adaptation:

- This skill starts from a capability contract and archetype, then allows evidence to challenge that frame. It does not make a fixed content taxonomy the abstraction.

## Evidence-Backed Multi-Agent Extraction

Source: https://github.com/glebis/claude-skills

Useful pattern:

- Parallel extraction is useful when outputs retain evidence locations and can be resumed or reconciled.

Adaptation:

- `cost-aware-extraction.md` permits parallel workers only after a shared schema, evidence labels, and rubric exist, with one contradiction-resolution pass.

## Mind Cloning Engineering

Source: https://github.com/yzfly/Mind-Cloning-Engineering

Useful pattern:

- Separate behavioral layers and express important decisions explicitly rather than relying only on similarity retrieval.

Adaptation:

- The harness separates invariant logic, modality/platform adapters, concrete evidence, assets, and deterministic scripts.

## SkillNet

Source: https://github.com/zjunlp/SkillNet

Useful pattern:

- Create skills from heterogeneous sources such as repositories, documents, logs, and trajectories.
- Evaluate skill quality across safety, completeness, executability, maintainability, and cost.
- Treat skill libraries as graphs with relations such as similar, dependent, and composable.

Adaptation:

- This skill uses heterogeneous source inventory, verification gates, and optional relation mapping.

## Agent Skill Creator

Source: https://github.com/FrancyJGLisboa/agent-skill-creator

Useful pattern:

- Raw material can be vague: workflows, docs, code, PDFs, transcripts, and links.
- The creator should infer implicit requirements, edge cases, and output expectations.
- Generated skills should be validated rather than merely drafted.

Adaptation:

- This skill adds explicit evidence rows and "human said vs artifact implies" separation.

## SkillAnything

Source: https://github.com/AgentSkillOS/SkillAnything

Useful pattern:

- Analyze target, design architecture, implement, generate tests, evaluate, optimize, package.
- Classify target type before choosing analysis strategy.
- Benchmark triggering and functional performance.

Adaptation:

- This skill uses artifact-type routing before extraction and requires trigger/function tests.

## Book-To-Skill And Cangjie Book2Skill

Sources:

- https://www.claudecodehq.com/playbooks/book-to-skill
- https://github.com/kangarooking/cangjie-skill

Useful pattern:

- Extract structure, not summaries.
- Preserve named frameworks and exact terminology.
- Convert frameworks into triggers, executable steps, boundaries, anti-patterns, and test prompts.
- Verify candidate units before making them independent skills.

Adaptation:

- This skill generalizes book extraction to any artifact, content, transcript, workflow, or example set.

## Writing Skills TDD

Source: https://github.com/obra/superpowers/blob/main/skills/writing-skills/SKILL.md

Useful pattern:

- Skills should be tested like process documentation.
- Near-miss trigger tests matter as much as obvious positive tests.
- A skill is reusable technique, not a story about one solved task.

Adaptation:

- This skill requires trigger, boundary, functional, and regression tests for packaged skills.

## OpenAI Skill Creator

Source: https://github.com/openai/skills/blob/main/skills/.system/skill-creator/SKILL.md

Useful pattern:

- Keep `SKILL.md` concise and use progressive disclosure.
- Create references, assets, and scripts only when they directly support execution.
- Validate the skill folder before delivery.

Adaptation:

- This skill uses a lean core file, one-level references, and lightweight reusable assets.

## Skill Studio

Useful pattern:

- Interview-driven discovery can fill missing context.
- Coverage-driven questioning avoids asking what can be inferred.
- Transcript ingestion can become structured design input.

Adaptation:

- This skill asks for artifacts first, then uses focused clarification only for missing target user, context, or output scope.
