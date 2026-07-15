# Capability Planning

Capability planning maps production decisions to agent-callable operations and creates an execution graph.

## Decompose Operations

For each required output, identify:

- planning and selection decisions
- content or asset generation
- deterministic transforms
- stateful editing
- preview and human review
- technical validation
- expressive and doctrine evaluation
- packaging, distribution, and update

## Allocate Agency

Assign every node:

- `judgment_owner`: human, model, deterministic rule, or external evaluator
- `executor`: model, script, CLI, API, MCP, SDK, or human
- `approval_owner`: none or named human role
- `state_owner`: file, project, service, database, or timeline

High-impact taste, rights, safety, irreversible publication, and unresolved contradiction normally require human approval. Deterministic transforms and repeatable checks should be automated where practical.

## Build The Graph

Use `assets/templates/execution-graph.json`. Each node needs inputs, outputs, assigned capabilities, tool or model, verifier, retry policy, fallback, and provenance. Edges carry artifacts or state and may include approval gates.

The graph must be acyclic unless an iteration edge has an explicit maximum count and stop condition. Avoid hidden loops such as "improve until good."

## Stack Completeness

Before execution confirm:

- every required capability has an assignment or declared manual fallback
- tool constraints match the runtime
- intermediate state can be inspected
- failures can be localized and retried
- output can be technically and expressively evaluated
- source-of-truth ownership is unambiguous
