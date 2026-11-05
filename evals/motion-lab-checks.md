# Motion lab checks — 2026-11-05

Scope: the original [self-contained browser example](../skills/ui-art-director/assets/motion-lab.html), not model-generated outputs for all evaluation cases.

Environment: connected in-app browser with a Windows development host. The browser engine version was not recorded. Checks used UI actions, accessibility snapshots, DOM state, and sampled screenshots.

| Check | Observed result |
| --- | --- |
| Initial content | The heading and all list content are present without waiting for an entrance |
| Replay controls | Heading and list replays execute; no captured console warnings or errors |
| Panel opening | Expanded state, visible content, and interactive content agree |
| Keyboard closing | Tab from the toggle reaches the inner close control; Enter closes the panel and returns focus to the toggle |
| Interrupted reversal | A double click reverses and reopens the panel; the final state remains expanded with its temporary height cleared |
| Reduced-motion control | Enabling the control after replay preserves complete content and the chosen panel state |
| Collapsed content | The settled panel is hidden and inert |
| Resizing | The expanded panel settles coherently; no horizontal document overflow at requested 375 px and 768 px widths or the default view |

To reproduce, open the HTML file in a modern browser, exercise its labelled controls, repeat the toggle quickly, close using the keyboard, enable reduced motion during replay, and resize the window. Confirm the final state after each action.

Limits: no frame-time benchmark, exact-curve measurement, assistive-technology session, native app test, or game-engine test was performed. The operating-system reduced-motion setting was not separately emulated; the page's live preference control was exercised. Screenshots and DOM checks do not prove perceptual smoothness across devices. The fourteen agent evaluation briefs remain unexecuted as a comparative benchmark.
