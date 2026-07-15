# Tool Capability Graph

Select tools by required capability and production-system fit, not by name recognition or repository popularity.

## Capability Record

For every candidate tool record:

- invocation: CLI, API, MCP, SDK, Agent Skill, GUI bridge
- modalities
- operation granularity: file, document, layer, clip, frame, component, state
- source of truth: code, timeline, project file, database, prompt, remote service
- state readability by the agent
- partial editability
- reproducibility and determinism
- parameterization and batch support
- preview and intermediate inspection
- automatic evaluation surfaces
- human handoff and round-trip behavior
- OS, hardware, network, cost, account, license, and data constraints
- rollback, retry, idempotency, and failure recovery
- version and last verification date

Use `assets/templates/tool-capability-registry.json`.

## Capability-First Selection

1. Decompose the desired output into required operations.
2. Mark hard constraints and human approval points.
3. Search for tools that expose the required operations to the agent.
4. Verify current first-party interfaces, license, and environment constraints.
5. Compare candidates against source-of-truth and editing-model needs.
6. Assign one primary tool and a fallback per critical capability, or record a concrete manual fallback with an owner and procedure.
7. Record unsupported non-required capabilities separately. A required capability cannot pass complete validation while unsupported.

## Tool Choice Changes The System

Tool selection is not merely implementation. It constrains grammar, revision style, reproducibility, and agency. Record those effects in the grammar and doctrine compatibility fields.

## Evidence Roles

- Official documentation and code: current capabilities and constraints.
- Maintained repository tests and examples: executable evidence.
- Issues and discussions: failure and recovery evidence.
- Papers and benchmarks: method and generalization evidence.
- X, Reddit, and blogs: discovery and practitioner hypotheses that must be traced to stronger evidence.

Re-verify temporally unstable tool claims before compiling them into an active system.
