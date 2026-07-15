# Worked Example: X Article

## Test Question

Can one successful X Article be represented without copying it, abstracted into a candidate production pattern, packaged as a skill, and used to produce a materially different article?

## Evidence

The source is a public Japanese X Article about source-led article production. The stored manifest records its URL, creator, publication date, volatile public metrics, rights limits, and unverified claims. The repository deliberately does not store the full body.

Files:

- `assets/examples/x-article/source-manifest.yaml`
- `assets/examples/x-article/move-map.md`

## Representation Decision

The artifact is argumentative text, so the primary representation is an annotated Markdown move map. YAML is used only for the stable corpus and generative-pattern handoff. The move map separates what the article visibly does from interpretations of why those moves may work.

## Abstraction

The source's topic, title formula, metrics, named people, template names, and wording remain source-specific. The candidate reusable relation is:

```text
specific pain
  -> challenge a causal assumption
  -> provide an evidence-grounded replacement mechanism
  -> organize distinct reasoning units
  -> resolve the main objection
  -> preserve provenance and offer one next action
```

See `assets/examples/x-article/pattern.yaml`. Because this comes from one positive example, its promotion status is `experimental`.

## Generated Skill And Transfer Input

The candidate skill is stored at `assets/examples/x-article/source-grounded-x-article/SKILL.md`. It was not tested by rewriting another newsletter. The transfer input was this repository's v0.2 evaluation design, which changes the topic, source type, claims, mechanism, examples, and CTA.

## Evaluator Loop

The rubric was frozen before drafting at `assets/examples/x-article/evaluation-rubric.json`.

| Round | Score | Decision | Root issue |
|---|---:|---|---|
| 1 | 75.20 | revise | Unsupported three-times outcome claim and an over-broad repair rule |
| 2 | 87.90 | pass | No blocking issue; live platform performance remains unknown |

Round 1 caused two different repairs:

1. The generated skill reference gained an evidence ladder and an explicit ban on invented quantitative uplift.
2. The current output replaced the generic "send every failure back to the skill" claim with lowest-responsible-layer routing.

The passing output is `assets/examples/x-article/final-round-2.md`. Its score is a pre-publication proxy, not proof that the article will obtain impressions.

## What This Test Establishes

- Text did not require an image-style YAML decomposition.
- A source-specific surface was separated from a reusable functional relation.
- The new article is not `nearly equal` to the concrete source.
- The evaluator repaired both permanent skill knowledge and one-off output logic at their respective layers.

It does not establish that this one pattern is universal or that it causes X reach. Those claims require broader comparative evidence and post-publication analytics.
