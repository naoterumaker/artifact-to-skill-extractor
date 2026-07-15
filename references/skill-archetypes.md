# Skill Archetypes

Classify the target capability before selecting representations, research axes, and tests. A skill may compose multiple archetypes, but choose one primary archetype.

| Archetype | Primary Knowledge To Extract | Typical Test Output |
|---|---|---|
| Content generation | intent, audience shift, structure, proof, voice, delivery constraints | article, post, image, video plan |
| Research | question decomposition, query strategy, source selection, verification, synthesis, stopping | evidence-backed research brief |
| Process | trigger, inputs, steps, branch rules, exceptions, completion | completed runbook scenario |
| Tool/API | interfaces, state, dependencies, safe commands, errors, recovery | successful operation or script |
| Evaluation | dimensions, anchors, thresholds, failure diagnosis, repair | scored artifact and repair plan |
| Decision | criteria, weights, trade-offs, exclusions, escalation | recommendation with decision trace |
| Knowledge application | concepts, retrieval, application conditions, counterexamples | solved novel case |
| Transformation | source representation, mapping rules, validation, output representation | correctly transformed artifact |

## Composition Examples

- X article skill: content generation + research + evaluation
- YouTube growth skill: research + content generation + evaluation
- Competitive research skill: research + decision + knowledge application
- Deployment skill: process + tool/API + evaluation
- Image campaign skill: content generation + transformation + evaluation

## Archetype Decision Rules

- If the core output is expressive, use content generation.
- If the core work is finding and judging evidence, use research.
- If success depends on ordered actions and branches, use process.
- If exact syntax or machine state dominates, use tool/API.
- If the deliverable is a score or critique, use evaluation.
- If the deliverable is a choice under trade-offs, use decision.
- If existing knowledge must be applied to unseen cases, use knowledge application.
- If input and output formats are central, use transformation.

The archetype selects the test. Do not validate a research skill with prose quality alone or an image skill with schema completeness alone.
