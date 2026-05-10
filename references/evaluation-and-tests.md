# Evaluation And Tests

Treat a skill like a small product. It needs trigger tests, functional tests, boundary tests, and update tests.

## Trigger Tests

Create realistic prompts, not obvious keyword lists.

Minimum set:

- 5 should-trigger prompts
- 5 should-not-trigger near misses
- 3 boundary prompts where the right action is to ask for clarification or route elsewhere

Good should-trigger examples include:

- user provides artifacts and asks to "turn this into a reusable skill"
- user asks to "extract the hidden workflow from these examples"
- user has a process transcript and wants an SOP
- user wants a rubric from good/bad outputs

Good should-not-trigger examples include:

- user wants a one-off summary
- user wants a single content piece written now
- user asks for generic advice with no artifacts
- user wants to install a finished skill without changing it

## Functional Tests

For each core workflow, define:

```yaml
id: case-001
input_artifacts:
  - type: artifact or transcript
task: what the user asks
expected_outputs:
  - extraction report
  - candidate skill units
  - packaged SKILL.md
assertions:
  - source evidence is cited
  - triggers and non-triggers are included
  - workflow has input/output/completion standards
  - failure modes are named
  - tests are generated
```

## Rubric

Score each dimension 1-5.

| Dimension | 1 | 3 | 5 |
|---|---|---|---|
| Evidence grounding | Unsupported claims | Some source links | Every core rule traced to evidence |
| Transferability | Source-specific | Works for similar cases | Works across novel cases with boundaries |
| Specificity | Generic advice | Some operational rules | Precise decisions and stop conditions |
| Trigger quality | Too broad/vague | Mostly right | Clear trigger, non-trigger, boundary cases |
| Executability | Not actionable | Partially actionable | Inputs, steps, outputs, verification clear |
| Maintainability | Brittle or huge | Usable with edits | Modular, lean, easy to update |
| Safety/copyright | Copies too much or leaks private data | Some caution | Respects privacy and copyright by design |

Block delivery if evidence grounding, executability, or safety/copyright is 1.

## Regression Tests From Feedback

When the user corrects the skill:

1. Quote or summarize the correction.
2. Name the failure type.
3. Add one prompt that reproduces the failure.
4. Add the expected behavior.
5. Patch the smallest section.

Failure types:

- `trigger-too-broad`
- `trigger-too-narrow`
- `surface-copying`
- `generic-output`
- `missing-boundary`
- `missing-source-check`
- `wrong-resource-placement`
- `unsupported-script`
- `copyright-risk`

## Test Prompt JSON Shape

```json
{
  "trigger_tests": [
    {
      "id": "trigger-001",
      "prompt": "I have three high-performing LPs. Extract the reusable workflow and turn it into a Codex skill.",
      "expected": "should_trigger",
      "reason": "Requests example-to-skill extraction from artifacts."
    }
  ],
  "functional_tests": [
    {
      "id": "functional-001",
      "prompt": "Use the attached call transcript to create an intake skill.",
      "expected_outputs": ["source inventory", "candidate units", "SKILL.md", "tests"],
      "assertions": ["cites transcript moments", "includes boundaries"]
    }
  ]
}
```

## Review Questions

Before final delivery, ask internally:

- Would the skill activate for the right future requests?
- Would it avoid nearby wrong requests?
- Can a future agent execute it without asking the user to design the method again?
- Are details loaded only when needed?
- Is the abstraction still connected to the concrete evidence?
