# Compiler Architecture

The compiler has two boundaries:

```text
artifacts, demonstrations, revisions, traces
  -> production-system intermediate representation
  -> agent-callable package and new concrete output
```

## Induction Modules

1. **Corpus Builder:** collect comparable artifacts, revisions, failures, explanations, traces, outcomes, and rights.
2. **Artifact Analyzer:** produce modality-native observations and functional decomposition.
3. **Comparative Aligner:** align opportunities, choices, alternatives, contexts, and outcomes.
4. **Doctrine Inducer:** recover scoped value priorities and anti-goals when evidence permits.
5. **Grammar Inducer:** recover conditional composition and expression rules.
6. **Decision Compiler:** create executable decision units with provenance and confidence.
7. **Tool Scout:** build and verify a capability registry.
8. **Capability Planner:** assign agency and compile an execution graph.
9. **Package Compiler:** emit skills, references, assets, scripts, adapters, and evaluators.
10. **Evaluator:** test technical quality, output quality, doctrine consistency, prediction, transfer, and failure recovery.

## Representation Routing

- Doctrine and rationale: Markdown with evidence and counterexamples.
- Comparative evidence: CSV, SQLite, or JSONL depending scale.
- Stable interfaces: JSON or typed schemas.
- Visual or media observations: structured records plus interpretive Markdown.
- Executable workflow: DAG, code, CLI scripts, adapters.
- Agent activation: lean `SKILL.md`.
- Mutable run state: external project workspace.

## Package Profiles

Minimal procedural package:

```text
SKILL.md + decision units + workflow + verifier + tests
```

Creative or hybrid system:

```text
doctrine/
grammar/
evidence/
decision-units/
toolchain/
workflows/
skills/
evals/
```

Compile only supported layers. An explicitly absent doctrine is better than fabricated philosophy.
