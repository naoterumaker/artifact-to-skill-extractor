# Cost-Aware Extraction

Estimate before deeply reading a large book, transcript set, repository, image corpus, or video archive. The objective is not to minimize evidence at all costs; it is to spend depth where a skill decision depends on it.

## Depth Levels

| Depth | Use | Typical work |
|---|---|---|
| `minimal` | Scoping, routing, or a narrow update | Inventory, structure scan, high-signal zones, explicit unknowns |
| `standard` | Normal skill construction | Full supplied core, representative comparisons, rubric and forward test |
| `deep` | Large corpus, high stakes, or cross-domain claim | Stratified sampling, negative cases, multiple passes, transfer and regression testing |

Run `scripts/estimate_extraction.py` for a deterministic file and text-size estimate. Token ranges are planning approximations; images, video, OCR, tool calls, and model caching can dominate actual cost.

## Progressive Reading

1. Inventory filenames, types, sizes, dates, and rights.
2. Read structure before body: tables of contents, headings, README files, tests, timelines, or contact sheets.
3. Identify high-signal zones tied to capability decisions.
4. Sample across time, outcome, creator, and failure class.
5. Expand only where evidence remains contradictory or insufficient.
6. Record skipped regions so absence is not mistaken for evidence.

## Large Modalities

- **Books/documents:** index chapters, examples, corrections, definitions, and evaluation sections before full reading.
- **Repositories:** map entry points, tests, public interfaces, failures, and recent maintenance before scanning all code.
- **Video/audio:** obtain duration and transcript coverage; sample openings, transitions, demonstrations, corrections, and endings before frame-level review.
- **Images:** build a contact sheet and stratify by concept, outcome, and composition; do not inspect only the most attractive examples.
- **Logs/traces:** sample successful, failed, retried, and human-corrected runs.

## Parallel Extraction

Parallel workers are useful only after they share a capability contract, representation schema, evidence labels, and rubric. Require source IDs and locations in every returned claim. Reserve a final synthesis pass for contradiction resolution and duplicate pattern control.

## Stop Conditions

Stop collection when each core skill decision has adequate evidence, major contradictions are resolved or documented, the rubric can be frozen, and another source is unlikely to change a decision. Do not use a fixed source count as the only stopping rule.
