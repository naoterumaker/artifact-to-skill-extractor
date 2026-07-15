# Source Selection

Research sources according to the claim being supported. Do not use one universal ranking for every domain.

## Default Priority

1. Current first-party or official documentation
2. Primary data, analytics, experiments, and maintained source code
3. Public artifacts with observable outcomes and known context
4. Practitioner postmortems and detailed case studies
5. Reddit, X, forums, note, Zenn, Qiita, and blogs for practice signals and failure discovery
6. Aggregations and summaries for discovery only

## Source Score

Score 0-5 on:

- relevance to the exact research question
- directness of evidence
- creator or repository credibility
- observable methodology or data
- recency appropriate to the claim
- reproducibility
- maintenance and adoption
- rights and accessibility

For GitHub, consider stars, but also recent commits, contributor activity, issue quality, documentation, tests, releases, and real-world adoption. A high-star repository can still be irrelevant or stale.

## Community Sources

Use Reddit and X to discover:

- concrete workflows
- failures and counterexamples
- current vocabulary and emerging practices
- links to primary evidence

Do not convert engagement counts or confident language into factual authority. Record claims as reported until independently supported.

## Channel Roles

| Channel | Primary role |
|---|---|
| Official documentation | current interfaces, constraints, policies, and supported behavior |
| GitHub source and tests | implementation, schemas, executable workflows, and recovery behavior |
| arXiv, OpenReview, proceedings | induction method, evaluation design, limitations, and generalization evidence |
| GitHub Issues and Discussions | operational failures, granularity problems, and maintenance evidence |
| Reddit and X | vocabulary, emerging tools, practitioner hypotheses, and links to stronger sources |
| note | Japanese operational practice, tacit knowledge, and workflow narratives |
| Zenn and Qiita | implementation details, Agent Skill structure, and engineering operations |

Trace discovery posts back to code, official documentation, papers, actual artifacts, or measurable outcomes before treating them as evidence.

## Tool Research

Research required capabilities before tool names. For each candidate, verify invocation interface, granularity, source of truth, state readability, editability, reproducibility, batch behavior, preview, evaluation support, human round-trip, license, OS/hardware/network constraints, and recovery. Record version and verification date because these claims change.

## Minimum Evidence

For a reusable production rule, prefer at least two independent supporting sources or one strong primary source plus a successful transfer test. Otherwise retain the rule as a hypothesis.
