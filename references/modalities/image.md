# Image Modality

Use structured scene and composition records because spatial relations are difficult to audit in prose alone. Keep interpretation and aesthetic rationale in Markdown alongside the structured record.

## Observation Layers

1. **Canvas**: dimensions, aspect ratio, frame, margins.
2. **Regions**: foreground, middle ground, background, text zones.
3. **Entities**: people, objects, typography, symbols, environment.
4. **Relations**: overlap, alignment, scale, direction, contrast, gaze, visual vectors.
5. **Hierarchy**: first, second, and third visual attention.
6. **Visual system**: palette, value, texture, typography, negative space.
7. **Meaning**: observed symbols versus inferred emotional or persuasive role.
8. **Delivery context**: platform crop, mobile legibility, thumbnail scale, brand constraints.

Use `assets/templates/image-observation.yaml` for stable fields.

## Separate Observation From Interpretation

```yaml
observation:
  dominant_subject: occupies approximately half the frame
inference:
  claim: monumental scale communicates aspiration
  confidence: medium
```

Do not encode inferred intent as a visual fact.

## Abstraction

Useful invariants are relational:

- dominant symbol overlaps or rises above the environment
- light or directional geometry connects promise and destination
- text hierarchy resolves at the intended viewing size
- palette separates subject from background while preserving mood

Variables may include subject, destination, palette, era, camera, typography, and surface texture. Constraints describe valid relations among them.

## Anti-Clone Requirements

For a new image derived from a source pattern:

- change source-specific subject, location, wording, and unique composition
- preserve only verified functional relationships
- combine multiple evidence sources when possible
- evaluate visual hierarchy and intent, not pixel similarity
- keep license and attribution records for every source asset

## Evaluation

Evaluate at both full size and expected delivery size. Include:

- immediate visual hierarchy
- semantic clarity
- composition stability
- typography legibility
- platform crop resilience
- originality and anti-clone distance
- alignment with intended audience change
