# Rubric Design

Freeze the rubric before the Generator creates the test output. The Evaluator may clarify ambiguous anchors, but must not change the target merely to approve its own output.

## Rubric Layers

| Layer | Purpose | Examples |
|---|---|---|
| Universal | protect evidence, safety, executability, originality | grounding, traceability, anti-clone |
| Archetype | measure the target capability | research credibility, image hierarchy, process recovery |
| Platform/objective | reflect delivery mechanics and KPI proxies | X dwell/readability, YouTube title-thumbnail promise |
| Project-specific | capture the user's taste and constraints | voice, brand, forbidden motifs, required proof |

For creative or hybrid systems, add only the layers supported by the capability contract:

| Layer | Purpose |
|---|---|
| Doctrine consistency | check value priorities, audience relationship, epistemology, and anti-goals |
| Grammar and medium fit | check structural relations and medium affordances |
| Decision executability | check evidence, action, verifier, fallback, and agency |
| Toolchain fit | check capability coverage, source of truth, editability, and recovery |

## Dimension Requirements

Each dimension needs:

```yaml
id: dimension-id
weight: 0-100
critical: true | false
question: what is being judged
anchors:
  0: complete failure
  60: minimally acceptable
  80: production-ready
  100: exceptional and evidence-backed
evidence_required: what the evaluator must cite
```

Weights must total 100. A dimension marked critical must score at least 60.

## Hard Gates

Hard gates do not average into the score:

- required output exists
- source and rights constraints are respected
- no unsupported factual claims when factual grounding is required
- no prohibited action or unsafe execution
- no source-expression cloning

## Pass Contract

```yaml
total_score_minimum: 80
critical_dimension_minimum: 60
all_hard_gates_required: true
maximum_rounds: 3
```

## Platform Performance

Separate pre-publication proxy quality from post-publication outcome quality.

- Pre-publication: structure, packaging, promise alignment, platform fit.
- Post-publication: actual impressions, CTR, retention, engagement, conversion.

Never use an AI-only pre-publication score as proof that real distribution performance is guaranteed.

## Doctrine Prediction

A doctrine evaluator must not only judge whether an output resembles prior work. On a held-out decision opportunity, record the predicted selection or revision direction before revealing the actual choice. Score prediction accuracy, counterexamples, and scope. A retrospective explanation alone cannot promote doctrine.

## Unsupported Layers

If creator doctrine or tool behavior lacks eligible evidence, mark the dimension `not_applicable` and redistribute its weight before freezing the rubric. Do not award a high score for a layer that was never evidenced.
