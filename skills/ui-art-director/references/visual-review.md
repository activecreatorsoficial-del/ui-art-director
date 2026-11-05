# Visual review

Use a concrete view, state, and task as evidence. A source diff alone cannot establish that an interface looks good or that a control remains usable.

## Choose representative evidence

For an existing UI, capture a baseline before changes when practical. Compare the same content, viewport, zoom, theme, state, and camera where possible. Note unavoidable differences rather than treating them as improvements.

For a new UI, inspect a representative screen early enough to change the direction cheaply. Include realistic content and the main interaction. Add more screens when they exercise genuinely different patterns.

Use the project's existing browser, emulator, engine, or native preview workflow. Available tools may differ between hosts. Do not install an unrelated capture system or assert access to a browser that is not available. If the runtime cannot be launched, separate code-level checks from visual checks in the delivery.

## Review from large decisions to small details

| Lens | What to inspect | Useful evidence |
| --- | --- | --- |
| Purpose | Main task, primary action, information priority | Can the intended action be located and completed? |
| Composition | Proportions, alignment, grouping, density, balance | Actual first viewport and a representative full screen |
| Typography | Hierarchy, wrapping, line length, weight, numeric alignment | Real strings, long titles, representative data |
| Colour and materials | Readability, semantic states, elevation, imagery | Relevant themes and difficult backgrounds |
| Interaction | Feedback, focus, navigation, state transitions | Exercise the affected controls and main flow |
| Adaptation | Resize, overflow, safe areas, text scaling | Supported narrow, intermediate, and wide layouts as relevant |
| Finish | Optical alignment, crops, icon consistency, rhythm | Close inspection at normal use scale |

Look at the interface at a glance before zooming into details. If everything has equal emphasis, refine the hierarchy. If the interface is visually empty, inspect whether useful content and proportion are missing before adding decoration.

## Use checks that fit the task

- Exercise the primary affected flow and relevant navigation.
- Verify keyboard and other supported input access, visible focus, labels, and feedback.
- Inspect relevant loading, empty, error, selected, and expanded states.
- Check real content expansion and the supported resize range.
- For HUDs, inspect scene contrast, action-area obstruction, and supported devices.
- Run existing build, lint, accessibility, or interaction checks appropriate to the change.

Automated accessibility tools catch some defects, not overall compliance. Do not claim a standard is met without the required scope and evidence. Manual observations are useful but should be identified as such.

## Refine with a stopping condition

Record the few most consequential observations in working notes. Each should name a location, the defect, and why it matters: “At narrow width, the fixed purchase bar covers the final form field,” rather than “mobile needs polish.”

Fix high-impact problems before decorative details. Re-inspect after a change that alters composition, shared tokens, or interaction. Keep a change only if it advances the brief without creating a material regression.

Stop when the requested scope is implemented, identified blockers are resolved or clearly explained, and the relevant checks pass. Do not repeatedly change colours or layouts because the result could be different. An agreed time limit, inaccessible environment, or missing asset may require an explicit handoff with remaining work.

Deliver evidence honestly: name the views and interactions actually inspected and state gaps. Never invent screenshots, usability results, runtime measurements, or a universal design-quality percentage.
