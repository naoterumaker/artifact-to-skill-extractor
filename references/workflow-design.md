# Workflow Design

This is the expanded v0.3 compiler pipeline. `SKILL.md` remains the operative short orchestration layer.

## Phase 0: Capability Contract

Define the desired capability, future user, execution environment, system profile, source of truth, trigger, inputs, outputs, completion standard, authority, quality target, rights, and prohibited behavior. Assume system construction is requested; do not waste a phase debating whether a reusable skill should exist.

## Phase 1: Corpus And Evidence Ceiling

Inventory supplied artifacts before asking questions. Plan the strongest useful mix of finished outputs, comparable works, failures, revisions, accepted/rejected alternatives, traces, creator explanations, and outcomes. Record rights and source locations.

Set the maximum defensible output for each layer. One finished artifact supports observation and candidate grammar, not verified process, causality, or creator doctrine.

## Phase 2: Native Observation

Choose the representation by mechanics and downstream use:

| Evidence | Primary representation |
|---|---|
| Text | annotated Markdown, argument/evidence map, language profile |
| Image | spatial or scene record plus interpretive Markdown |
| Video/audio | timeline, segment/shot map, audiovisual relation map |
| Research | evidence table, query log, contradiction graph |
| Process/trace | state machine, decision table, exception/recovery map |
| Tool/API | interface schema, state model, error/recovery table |

Serialization is not abstraction. Preserve observation, inference, user confirmation, and hypothesis as different statuses.

## Phase 3: Comparative Alignment

Align eligible decision opportunities across works, revisions, creators, accepted/rejected alternatives, and success/failure cases. Compare function, context, available alternatives, observed choice, outcome, and source location.

Repeated presence is an invariant candidate. Context-linked change is a conditional rule. Repeated rejection may reveal an anti-goal. Revision direction may reveal a value priority. Absence counts only when there was a real opportunity to include the element.

## Phase 4: Production-System Induction

Compile supported layers:

1. Doctrine: purpose, value conflicts, audience relationship, epistemology, experience, quality stance, anti-goals, agency, and distribution.
2. Grammar: composition and expression relations conditioned by medium, objective, audience, and tool affordance.
3. Decision units: context, evidence, selection rule, action, parameters, invariants, verifier, fallback, provenance, confidence, and agency.

Keep recovered creator doctrine, user-confirmed project doctrine, external constraints, and model preference separate.

## Phase 5: Capability And Tool Planning

Decompose required operations before naming tools. Evaluate candidate CLI, API, MCP, SDK, skill, or GUI bridge by invocation, modality, granularity, source of truth, state visibility, partial editing, reproducibility, parameterization, batch behavior, preview, evaluation, human round-trip, constraints, license, and recovery.

Assign judgment owner, executor, approval owner, and state owner. Build an execution graph with inspectable handoffs, verifiers, bounded retries, and fallbacks. Record unsupported capabilities explicitly.

## Phase 6: Evaluation Freeze

Freeze the rubric before generation. Combine universal evidence/rights/originality gates with relevant doctrine, grammar, decision, toolchain, modality, platform, objective, and project criteria.

Default contract:

```text
total score >= 80
critical dimensions >= 60
all hard gates pass
maximum 3 rounds
```

Unsupported layers are `not_applicable`, not automatic passes. Recovered doctrine also needs a preregistered held-out prediction.

## Phase 7: Package Compilation

Compile the selected profile into the minimum executable package. Put lean activation and routing in `SKILL.md`, detailed reasoning in references, reusable output material in assets, deterministic operations in scripts or adapters, and mutable evidence outside the installed skill.

Validate the project structure and system intermediate representation before execution.

## Phase 8: New Concrete And Evaluation

Run the package on an unseen related input. Preserve supported production relations while changing source-specific expression. Evaluate the actual output, not only the skill files.

Route each defect to the lowest responsible layer: current output, decision unit, grammar, doctrine, tool assignment, execution graph, skill instruction, reference, asset, abstraction, source evidence, or rubric.

## Phase 9: Repair And Promotion

Patch the smallest responsible layer, regenerate, and re-evaluate for at most three rounds. Promote a permanent rule only when repeated evidence, explicit owner doctrine, a hard gate, or a deterministic validator justifies it.

Promotion requires scoped evidence, traceability, trigger quality, executability, boundaries, output quality, prediction or transfer support, and no critical rights/safety failure. Otherwise retain `experimental`, narrow scope, or reject the candidate.

## Stop Conditions

Stop and surface the gap when evidence cannot be obtained lawfully, a required capability has no viable executor or fallback, a credible evaluation is impossible, three rounds fail, or contradictions require human ownership. Return the best auditable state without inventing certainty.
