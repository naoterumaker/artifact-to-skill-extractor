# Text Modality

Represent text primarily in annotated Markdown. Use structured data only for stable metadata, variables, constraints, or evaluator handoffs.

## Observation Views

### Move Map

Segment the text by functional move rather than paragraph length:

```markdown
## Move 1: <functional name>
- Source span:
- Surface action:
- Reader state before:
- Intended change:
- Evidence status: observed | inferred
```

Useful move labels include:

- establish relevance
- interrupt an assumption
- state a claim
- define stakes
- provide mechanism
- provide evidence
- concretize through an example
- handle an objection
- derive a practical rule
- request or enable action

Do not force every text into the same sequence.

### Argument Graph

Record relations such as:

```text
claim -> reason -> evidence -> implication
problem -> mechanism -> intervention -> expected result
scene -> tension -> interpretation -> lesson
```

### Voice Profile

Capture observable properties separately from inferred personality:

- sentence length and rhythm
- certainty and qualification
- concrete versus abstract ratio
- relationship to the reader
- use of examples, analogy, humor, and contrast
- emotional temperature
- vocabulary and prohibited expressions

## Abstraction

Candidate invariants should describe relations, not exact phrasing. For example:

```text
unsupported contrarian opening       -> not an invariant
reversal followed by causal support  -> candidate invariant
```

Variables may include audience belief, thesis, evidence, example, domain, voice, and call to action. Constraints define which combinations preserve the text's function.

## Generation

Generate in this order:

1. reader-state change
2. move sequence
3. evidence placement
4. voice and rhythm
5. platform adaptation
6. final wording

Evaluate copied phrase structure, repetitive AI cadence, unsupported certainty, and mismatch between opening promise and delivered value.
