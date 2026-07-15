# Worked Example: Image

## Test Question

Can a concrete image be serialized for observation, abstracted beyond that serialization, and used to create a recognizably different image that preserves production function?

## Evidence And Rights

The source is GDJ's `Vintage Travel Poster Paris`, retrieved from Wikimedia Commons with an Open Clip Art origin and a CC0 1.0 Universal dedication. A rasterized local source and rights manifest are stored at:

- `assets/examples/image/source-vintage-travel-poster-paris.png`
- `assets/examples/image/source-manifest.yaml`

CC0 permits worldwide copying, modification, and redistribution to the extent allowed by law. The source is still credited, and anti-clone rules are applied to test whether the abstraction can generate something genuinely new.

## Representation Decision

Image geometry benefits from structured fields, so observed regions, entities, spatial relations, hierarchy, palette, and typography are stored in `assets/examples/image/observation.yaml`. Meaning, taste, and inferred intent are kept in `assets/examples/image/analysis.md` because prose preserves uncertainty better than a rigid scene schema.

The observation YAML is still a concrete representation of one poster. It is not the abstraction.

## Abstraction

Source-specific expression includes FLY TWA/PARIS wording, a central draped figure, a split blue/cream field, a sun face, airplane placement, Paris architecture, produce, and the exact typography.

The candidate invariant is the relationship:

```text
dominant destination identity
  + subordinate place cues
  + integrated naming
  + directional access
  -> recognizable promise
  -> feasible action
```

See `assets/examples/image/pattern.yaml`. Variables include anchor type, subordinate cue set, directional device, verbal sequence, density, and palette. Constraints prevent the variables from being combined arbitrarily.

## Generated Skill And New Concrete

The candidate skill is `assets/examples/image/destination-poster-recomposer/SKILL.md`. Its test output is a contemporary Hokkaido morning-train poster. It changes:

- Paris and air travel to Hokkaido and rail travel
- dense central fashion/city collage to sparse mountain, sun, route, and train
- split blue/cream field to cream/forest/coral masses
- small airplane to a diagonal rail path and train
- interwoven source typography to an asymmetrical title and dedicated footer
- source wording, motifs, and travel promise

The editable output is `assets/examples/image/poster-round-2.html`; the rendered output is `assets/examples/image/poster-round-2.png`.

## Evaluator Loop

The rubric was frozen at `assets/examples/image/evaluation-rubric.json`.

| Round | Score | Decision | Root issue |
|---|---:|---|---|
| 1 | 75.00 | revise | Low-contrast lower copy failed the critical readability dimension |
| 2 | 88.20 | pass | No blocking issue; audience and campaign performance remain untested |

Round 1 changed two layers:

1. The generated skill reference gained mandatory full-size and thumbnail render checks plus a quiet-field requirement for text.
2. The current output gained a dedicated footer hierarchy connecting the promise to the departure action.

## What This Test Establishes

- YAML is useful for exact image observation and handoff.
- A second abstraction step is necessary to produce invariants, variables, constraints, and selection rules.
- A new concrete can preserve functional relationships without becoming nearly equal to the source.
- Visual evaluation must inspect a render, not only HTML, prompts, or YAML.

It does not prove that one extracted pattern generalizes to all posters. The generated skill remains experimental until broader comparative and audience evidence exists.
