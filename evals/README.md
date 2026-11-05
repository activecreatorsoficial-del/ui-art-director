# Behavioural evaluation

The cases in [cases.json](cases.json) are reusable task briefs and observable criteria. They are not completed evaluations and the structural validator does not execute an agent or score visual quality.

To run a case, supply a suitable shareable starting project, freeze its revision and representative data, and use the same starting state for the baseline and candidate. For a new interface, freeze the brief, assets, framework, and device constraints instead. Keep generated work outside the skill source tree.

Record the case ID, skill revision, model if known, tools, starting revision, platform, target devices and viewports, actual changes, inspected screens and interactions, check results, and limitations. Keep baseline and candidate screenshots comparable and retain any necessary asset attribution.

Evaluate task completion, hierarchy, fit to brief, visual consistency, legibility, responsiveness, interaction, and regressions. Explain each judgement with an observable example. Prefer a blinded human comparison when feasible; do not invent an objective beauty score.

For broad changes, include a website, an application, a HUD, a narrow polish task, and an existing-brand task. Include negative routing cases to confirm the skill is not being used for unrelated work. The screenshot-only case checks honest handling of unavailable source and runtime.

Agent benchmark results are not bundled yet. The original [motion lab](../skills/ui-art-director/assets/motion-lab.html) is a small browser example, not the result of running all evaluation cases. For motion tasks, retain temporal evidence and exercise interruption, focus, resizing, and live reduced-motion changes. Contributions should label a run as incomplete when artifacts or observations are missing and must not include private project content without permission.
