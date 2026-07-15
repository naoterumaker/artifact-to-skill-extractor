# X Article Move Map

## Source

- Source ID: `x-src-001`
- Format: public X Article
- Observed outcome: 46,722 views and 83 bookmarks at the recorded retrieval point
- Evidence limit: one positive example; metrics do not establish causality

## Reader-State Contract

- Before: the reader posts frequently, sees weak reach, and assumes original writing must begin from a blank page.
- After: the reader sees source-led curation plus AI-assisted transformation as a plausible workflow and has a linked next step.
- Primary objective: gain attention and move interested readers to the attributed source.

## Functional Moves

| Move | Surface action, paraphrased | Functional role | Evidence status |
|---|---|---|---|
| 1. Pain mirror | Opens with the frustration of consistent posting without growth. | Qualify the reader and create immediate self-relevance. | observed |
| 2. Assumption challenge | Questions the need to originate every article from zero. | Create a curiosity gap by attacking the reader's operating assumption. | observed |
| 3. Outcome anchor | Attributes unusually high reach and fast production to another creator's workflow. | Replace abstract possibility with a concrete, high-stakes example. | observed as article content; underlying claim unverified |
| 4. Barrier reduction | Reframes the required input as editorial interest rather than exceptional prose skill. | Lower perceived effort and identity risk. | observed |
| 5. Structure promise | Announces a small numbered set of principles. | Give the reader a reason to continue and a mental index. | observed |
| 6. Context shift | Claims that the platform environment now rewards a different format. | Create urgency and justify changing behavior. | observed as article claim; external truth unverified |
| 7. Mutual-benefit model | Describes benefits for source creator, curator, and reader. | Resolve the objection that curation is extractive or low value. | observed |
| 8. Operational mechanism | Explains a URL-to-draft workflow and several selectable article modes. | Convert inspiration into an executable path. | observed |
| 9. Compressed payoff | Restates low effort and large potential outcome in a short cadence. | Make the promise memorable before the close. | observed |
| 10. Attribution CTA | Names the originating creator and links to the detailed source. | Preserve provenance and route motivated readers onward. | observed |

## Argument Graph

```text
stalled reach
  -> challenge blank-page assumption
  -> show attributed outcome
  -> explain changed context
  -> present mutual-benefit mechanism
  -> reduce execution friction
  -> attribute source and offer next action
```

## Voice Profile

- Sentence rhythm: short assertions alternate with compact explanatory blocks.
- Certainty: high; some externally testable claims are stated more strongly than the artifact alone can support.
- Concrete/abstract balance: numbers and named actors lead, then principles explain the mechanism.
- Relationship to reader: direct second-person challenge followed by practical relief.
- Emotional temperature: urgent and optimistic.
- Repeated devices: rhetorical question, numbered principles, benefit lists, compressed recap.
- Taste exclusions: long preamble, detached summary, or CTA without attribution.

## Candidate Invariants

| Candidate | Evidence | Confidence | Validation needed |
|---|---|---:|---|
| Start from an active pain before teaching the mechanism. | Moves 1-2 | medium | Test on a different topic and audience. |
| Use a small explicit map before the explanatory body. | Move 5 and three titled sections | medium | Compare against an unnumbered article. |
| Pair the mechanism with objection resolution. | Moves 7-8 | medium | Test whether the objection differs by topic. |
| Close with provenance plus a low-friction next action. | Move 10 | medium | Test with non-curation articles. |

## Variables And Constraints

| Variable | Valid range | Constraint |
|---|---|---|
| Opening pain | concrete recurring frustration | Must match the actual target reader, not a generic fear. |
| Assumption challenged | one controllable belief | The article must offer a credible replacement mechanism. |
| Proof anchor | metric, case, demonstration, or implementation | Label source claims and uncertainty; never invent uplift. |
| Principle count | 2-5 | Each principle must advance the mechanism rather than rename it. |
| CTA | source link, repo, checklist, or next action | Must follow naturally from the article's promise. |

## Anti-Clone Rules

- Do not reuse the source's distinctive opening wording, exact section titles, numerical promise, or closing cadence.
- Change the topic, evidence base, mechanism, examples, and CTA in the transfer output.
- Preserve only functional relations such as pain -> reframing -> mechanism -> evidence -> action.
- Treat platform-performance claims as hypotheses unless current independent evidence supports them.
