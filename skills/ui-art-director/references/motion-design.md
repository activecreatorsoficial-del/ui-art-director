# UI motion design

Use when animation or transitions matter to the assignment. Build motion around the product's task, brand, input methods, and runtime. An edited video can inspire a treatment without supplying the behaviour of an interactive application.

## Define the movement before implementing it

For a significant interaction, establish a compact contract:

- Trigger and purpose: what action or state change causes it, and what it explains.
- Start and end states: visible properties and the actual application state.
- Choreography: which element leads, which follows, and what remains stable.
- Pacing: duration, delay, acceleration, and any intentional overshoot.
- Interruption: the response to repeated input, reversal, resize, or dismissal.
- Access: focus, keyboard/touch/controller equivalents, reduced motion, and content availability.

Describe a curve by what it achieves before selecting a preset: a prompt response that settles gently, a restrained elastic response, or a constant progression. Do not claim to have measured a tutorial's easing from its narration or sparse frames.

## Choose the appropriate motion role

| Role | Typical use | Direction |
| --- | --- | --- |
| Immediate feedback | Press, selection, toggle | Acknowledge the action promptly; do not delay the actual response |
| State transition | Panel, menu, tab, record update | Preserve spatial continuity and a clear final state |
| Presentation | Introductory heading, product reveal | Support the intended reading order without delaying the task |

For an original prototype, useful starting points might be 120-180 ms for small feedback, 180-280 ms for local transitions, and 360-600 ms for a deliberate presentation. These are adjustable design hypotheses, not standards or measurements from the reference videos. Tune distance, device, input, repetition, and the user's brief. Essential information should not wait for a decorative timeline.

## Compose with stable anchors

Keep enough of the interface stable to explain the change. A selected item can lead into its detail; related content can move as a group. Reuse semantic identity when changing a representation, and keep labels and values truthful during the transition.

A masked text reveal combines movement with a clipping region. Give glyphs enough space to avoid cutting accents and descenders in the final state. A stagger separates related entries slightly to guide attention. Limit the total delay and preserve complete accessible text; do not make a screen reader announce a heading one animated word at a time.

For a restrained presentation inspired by the supplied Apple-style tutorial, consider a quiet background, deliberate whitespace, compact typography, eased movement, and limited layering. Use this only when it fits the brief. Centre alignment, rounded corners, glass, and particular fonts remain optional choices.

## Handle interruption as normal input

The latest valid user intent should win. Cancel, reverse, or retarget the active transition according to the interaction. Start from the current visible state when a restart would cause a jump. Clean up old callbacks and animation objects so a cancelled closing transition cannot hide a newly opened panel.

Define the settled state independently of the animation. After cancellation, navigation, or reduced-motion changes, elements must remain visible, correctly selected, and usable. Avoid relying on a delayed callback to establish important application state.

Use springs when their response suits the interaction. Tune settling and overshoot in context rather than adding bounce to every component. A dragging object and a confirmation message need different behaviour. Keep the implementation within the existing framework or engine.

## Implement in the actual runtime

Prefer the project's existing motion mechanisms. For small web effects, native CSS or the Web Animations API may be sufficient; larger choreography may justify an existing animation library. In a native app or game, use its own layout, tweening, and input mechanisms. Do not translate After Effects layer names into nonexistent runtime APIs.

On the web, movement and opacity are useful starting choices for visual-only transitions. Genuine resizing may need layout animation or a measured layout technique; verify its cost and behaviour rather than prohibiting it universally. Avoid unnecessary layout work on each frame and oversized layers with expensive blur or shadows.

If inspecting platform details, consult current primary documentation. Useful web references include [Element.animate](https://developer.mozilla.org/en-US/docs/Web/API/Element/animate) and [matchMedia](https://developer.mozilla.org/en-US/docs/Web/API/Window/matchMedia). Use the browser's accessibility semantics as well as visual states. A modal's focus behaviour follows the [WAI dialog pattern](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/).

## Preserve access and function

Respect the system's reduced-motion preference and relevant product settings. Provide an equivalent settled or quieter state, including when the preference changes during movement. Do not hide controls until an entrance completes. Check clipped content, focus indicators, larger text, and supported window sizes.

For HUDs, keep current critical telemetry readable while a secondary effect communicates change. A delayed damage trail should not delay the actual health value. Keep decorative effects away from the action area and respect the game's supported accessibility settings. Add sound only when the product calls for it and respect the relevant sound controls.

## Verify time, not only appearance

Replay the interaction at normal speed, then inspect intermediate frames when useful. Exercise rapid repeated input, reversal before completion, keyboard access, resize, and reduced motion. Check the final state after every interruption. Record the device, viewport, motion setting, and what was actually observed.

Look for unexpected jumps, awkward pauses, overlapping sequences, excessive delay, clipped text, abandoned focus, and accumulating animations. Use runtime profiling when performance matters. A sample capture can show a defect; it does not establish frame-time performance on untested devices.

The original [motion lab](../assets/motion-lab.html) demonstrates three small browser interactions without external libraries. Its source is illustrative and its checks do not establish support across native frameworks or game engines.
