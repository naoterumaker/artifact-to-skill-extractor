# Freshness Policy

Classify knowledge before deciding whether stored references are sufficient.

| Class | Examples | Default Action |
|---|---|---|
| Stable | composition principles, argument relations | reuse and periodically review |
| Versioned | API, CLI, file format | verify installed/current version |
| Volatile | platform ranking, product behavior, policies | research at execution time |
| Event-driven | trends, current discourse, prices | research immediately |

## Evidence Metadata

Record:

```yaml
published_at:
observed_at:
last_verified_at:
valid_for:
supersedes:
confidence:
```

Do not write volatile platform claims as timeless production rules. Store the durable decision framework in the skill and current findings in the project evidence corpus.
