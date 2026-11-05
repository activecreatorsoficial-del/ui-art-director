# UI Art Director

**A portable AI skill for deliberate, distinctive interfaces.**

[Português](README.pt-PT.md) · [The skill](skills/ui-art-director/SKILL.md) · [Evaluation cases](evals/cases.json) · [Contributing](CONTRIBUTING.md) · [MIT](LICENSE)

UI Art Director guides an AI coding agent through art direction, implementation, rendered inspection, and focused refinement. It covers websites, web applications, native mobile and desktop interfaces, and game HUDs without forcing them into the same aesthetic.

The goal is design judgement that fits the product: an expressive portfolio, an efficient operations tool, and a readable combat overlay should look and behave differently.

## What it adds

- A concrete visual direction before a substantial redesign.
- Composition and typography before decorative finishing.
- Platform-specific considerations for websites, apps, and HUDs.
- Review of the actual rendered result when tools permit it.
- Refinement driven by observed defects, with a clear stopping point.
- A process for improving the skill using feedback and comparable evaluations.

It is an instruction-based [Agent Skill](https://agentskills.io/specification), not a UI component library, framework, autonomous background service, or replacement for user testing. Output depends on the model, project context, assets, and tools available. It does not promise perfect design or infinite self-learning.

## Install in Codex

Download or clone this repository, then copy the **entire** `skills/ui-art-director` directory into one of Codex's skill locations:

| Scope | Destination |
| --- | --- |
| Current project | `.agents/skills/ui-art-director/` inside your project |
| All your projects | `~/.agents/skills/ui-art-director/` |

On Windows, the user location is normally `%USERPROFILE%\.agents\skills\ui-art-director`.

Keep `references/`, `agents/`, and the bundled `LICENSE` together with `SKILL.md`. Do not overwrite an existing installation without reviewing it. Codex detects skill changes; restart it if the skill does not appear. These locations and discovery behaviour follow the [official OpenAI documentation](https://learn.chatgpt.com/docs/build-skills).

The same skill files can be used by hosts that support the Agent Skills format. Follow that host's installation instructions; cross-host discovery and rendering tools have not been tested in this initial release. Codex-specific UI metadata lives in `agents/openai.yaml` and the core instructions do not depend on it.

## Use it

Explicit invocation in Codex:

```text
Use $ui-art-director to redesign this dashboard. Preserve its features and
existing stack. Make the hierarchy clearer, keep the data useful, and inspect
the result at the supported desktop and mobile sizes.
```

```text
Use $ui-art-director to improve this game HUD. Keep the crosshair area clear,
make health and cooldowns readable over gameplay, and preserve controller support.
```

```text
Use $ui-art-director to polish this form. Keep the current brand and layout;
fix spacing, labels, focus, and error feedback without redesigning the page.
```

Automatic selection is enabled when the host supports it and the request matches the skill description. Backend-only tasks are outside its scope.

For best results, supply the real project, the main user task, intended devices, brand constraints, and references you have permission to use. The skill can work from incomplete context, but cannot inspect an application or screenshot it has not been given access to.

## Continuous improvement

The workflow is **understand → direct → build → inspect → refine → verify**. Each task ends when its scope is satisfied. Accepted project decisions can inform later work through a project design record. Improvements to the public skill should come from demonstrated failures and comparable evaluations, not an ever-growing list of personal taste rules.

See [continuous-improvement.md](skills/ui-art-director/references/continuous-improvement.md) and the [evaluation guide](evals/README.md).

## Validation and current status

Version **0.1.0** is an initial release. Structural validation checks packaging, metadata, local documentation links, and evaluation-case integrity. It does **not** measure visual quality, prove model compliance, or establish tested support for every framework.

Run the repository checks with Python 3.10 or newer:

```text
python -m pip install -r requirements-dev.txt
python scripts/validate.py
python -m unittest discover -s tests
```

Python and PyYAML are development dependencies for these checks. Using the skill itself requires neither. No network service, telemetry, account, additional skill, or paid design tool is bundled or required by the skill.

The repository includes reproducible evaluation briefs. Real rendered before/after evaluations are still needed; no aesthetic benchmark results are claimed.

## Contribute

Read [CONTRIBUTING.md](CONTRIBUTING.md). Reports with a clear task, shareable starting artifacts, observed outcome, and concrete evidence are especially useful. Keep private work out of public issues.

Licensed under [MIT](LICENSE). Third-party assets used in projects retain their own licences.
