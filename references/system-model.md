# System Model

The compiler reconstructs a production system, not merely a sequence of steps. Select the smallest profile that matches the target capability.

## Profiles

| Profile | Typical targets | Required intermediate representations |
|---|---|---|
| `procedural` | research, operations, code maintenance, support, analysis | evidence map, decision units, workflow, verifier, fallback |
| `creative` | text, image, video, slides, UI, campaigns, courses | doctrine, grammar, decision units, medium constraints, evaluators, explicit capability gaps |
| `hybrid` | data-driven content, interactive tools, automated media systems | all relevant procedural and creative representations |

Do not force philosophy or a toolchain into a narrow deterministic transform. Do not reduce a creative system to a prompt template when its quality depends on values, grammar, medium, and tool affordances.

## Production-System Layers

| Layer | Question | Output |
|---|---|---|
| Intended change | How should the recipient or system change? | understanding, emotion, action, relationship, system state |
| Doctrine | What is treated as right, valuable, honest, or beautiful? | philosophy, priorities, tensions, anti-goals |
| Audience relationship | How is the recipient treated? | teacher, partner, challenger, buyer, operator |
| Epistemology | What counts as a reason to believe? | data, demonstration, authority, comparison, experience, narrative |
| Experience design | What should unfold over time? | attention, tension, release, comprehension, confidence, aftertaste |
| Grammar | Which elements and relations repeatedly create the experience? | composition, narrative, visual, sonic, interaction, component rules |
| Medium materiality | What can this medium uniquely do or not do? | duration, frame, interaction, density, latency, editability |
| Decision logic | What is inspected, chosen, rejected, or repaired? | executable decision units |
| Agency allocation | Who or what owns each judgment? | human, model, rule, tool, approval boundary |
| Toolchain | Which capabilities make the system executable? | capability registry, adapters, constraints |
| Quality doctrine | What counts as good and what is unacceptable? | rubric, hard gates, tolerances |
| Distribution context | Where, by whom, and for how long is it consumed? | platform, update, derivative, and lifecycle rules |

## Evidence Eligibility

Evidence type limits what may be induced:

| Evidence | Maximum defensible output |
|---|---|
| One finished artifact | observations, functional decomposition, candidate grammar |
| Multiple comparable artifacts | recurring patterns and conditional variation |
| Positive and negative examples | success conditions, boundaries, anti-patterns |
| Revisions or accepted/rejected alternatives | decision criteria and value priorities |
| Execution traces or tool logs | actual procedure, branches, recovery, agency |
| Creator explanation plus outcomes | stronger intent, doctrine, and effectiveness claims |
| Longitudinal corpus | doctrine hypotheses and signature behavior |

A lower evidence tier may generate hypotheses for a higher layer, but it cannot verify them.

## Compiler Output

The full creative or hybrid package is:

```text
evidence and provenance
  + doctrine
  + grammar
  + executable decision units
  + tool capability graph
  + execution graph and adapters
  + skill activation layer
  + technical, expressive, and doctrine evaluators
```

`SKILL.md` activates and orchestrates the package. It is not the whole production system.
