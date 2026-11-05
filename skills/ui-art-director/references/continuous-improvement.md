# Continuous improvement

Read this when evolving the skill itself or when a user explicitly requests an ongoing design-learning process. Ordinary UI edits do not require changes to this skill.

## Keep project memory separate from general guidance

Store accepted project decisions in the existing design record when one is available. For substantial ongoing work without a record, use a compact project-local note when useful. Capture:

- Product context, audience, platforms, and important constraints.
- Accepted direction and the rationale behind consequential decisions.
- Token or component sources of truth.
- Specific feedback and the contexts to which it applies.
- Evidence, unresolved problems, and the next useful validation step.

Do not copy secrets, customer data, or private screenshots into a public skill repository. A project preference is not a universal rule. “This mobile tracker uses quiet transitions” does not imply “all interfaces must avoid expressive animation.”

## Turn observed failures into narrow improvements

Describe the failure in observable terms. Determine whether it came from missing context, unclear instructions, a tool limitation, implementation error, or subjective preference. Fix the relevant cause; do not add a new mandatory checklist item for every isolated dislike.

Before changing a widely applicable instruction, test more than one product context. A correction for a marketing page must not quietly degrade a dense desktop tool or obscure a combat HUD. Preserve explicit user choices and adapt to subsequent feedback.

Do not modify a globally installed skill without authorisation to update it. A request to improve one UI does not authorise changing everyone's design workflow.

## Compare versions using the same task

Use a representative task, frozen starting artifacts, matching environment, and an agreed evaluation scope. Keep baseline and candidate outputs in separate working directories. Record the skill revision, model if known, tool availability, viewport/device, task constraints, and relevant checks.

Compare observable outcomes: task completion, hierarchy, fit to brief, consistency, legibility, adaptation, interaction, and regressions. Side-by-side screenshots support visual judgement; interaction evidence supports behaviour. Prefer a blinded human comparison when feasible. A numerical score is an evaluation aid only when its rubric and evidence are explicit, not proof of universal design quality.

Keep some tasks unchanged as regression checks. Include a narrow change and an existing-brand task, so the skill is not rewarded simply for redesigning everything. Include contexts outside the example that motivated the change.

## Release honestly

Propose the smallest supported instruction change, run structural validation, and repeat the affected behavioural evaluations. Explain the demonstrated improvement and any tradeoff. Publish only examples and assets that can be shared under the repository's terms.

A new version improves a reusable process; it does not change the underlying model, guarantee expert output, or establish automatic learning between sessions. Record actual evidence rather than claiming infinite improvement.
