# Platform patterns

Read the section that matches the actual product. These are design considerations, not permission to introduce new features or platforms.

## Websites and marketing surfaces

Build the narrative around the visitor's next decision. Make the offering, intended audience, and useful action understandable from real content. Let the visual structure follow that narrative rather than automatically adding hero, logo strip, feature cards, testimonials, pricing, and FAQ.

Give sections different roles and appropriate proportions. Use imagery, typography, whitespace, and contrast to vary pacing while keeping a coherent system. Use proof supplied by the project; do not manufacture social proof or conversion statistics.

Design responsive behaviour as a change in composition. Reconsider image crops, ordering, headline breaks, navigation, and calls to action. Do not merely shrink a desktop layout. Check the narrowest supported viewport, intermediate widths, and a wide screen when relevant. Avoid accidental horizontal overflow while retaining deliberate scrolling regions such as data tables.

Use semantic HTML and native controls where suitable. Ensure keyboard access, visible focus, useful labels, meaningful links, and accessible form feedback. Check zoom and content expansion. Touch controls should meet the relevant platform's target-size requirements and remain comfortably separated; there is no single unit or minimum that applies to every platform.

Respect performance budgets. Reserve media dimensions, load assets appropriately, and keep motion from delaying content. Do not add a heavy animation library for an effect already supported by the existing stack.

## Web, mobile, and desktop applications

Prioritise task completion, predictable structure, and legibility over presentation-only spectacle. Identify the primary workspace, repeated actions, persistent navigation, and information that must remain visible during the task.

Use a density appropriate to the audience. A professional table may benefit from compact rows and aligned numeric columns; a touch-first flow may need larger controls and staged disclosure. Do not replace useful structured data with large decorative cards without a task-based reason.

Preserve platform conventions for navigation, back behaviour, selection, dismissal, focus, and input. Native applications should use their framework's accessibility and layout mechanisms. Inspect the actual framework before proposing web-specific CSS or libraries.

Handle the states the affected flow needs: loading, empty, error, success, validation, long content, missing media, and partial data. Explain an empty state with a useful next action. Keep errors close to the cause and preserve entered data. Do not add every possible state to an unrelated cosmetic task.

Check resizing, safe areas, text scaling, keyboard presentation, and the intended input devices. On desktop, consider window minimums and keyboard workflows. On mobile, check thumb reach and small-screen composition. In responsive web apps, verify that sticky regions and menus do not obscure content or focus.

Use coherent tokens and components across related screens. Reuse the existing design system and extend it sparingly. Check that a token change does not make secondary screens unreadable or disturb unrelated products in a shared repository.

## Game interfaces and HUDs

Start with the gameplay loop, camera, target devices, input methods, engine, and information priorities. Separate always-needed telemetry, contextual actions, temporary feedback, and menus. Ask which information must be understood in a glance and which can wait until a pause.

Protect the action area. Keep panels away from targets, characters, reticles, subtitles, objective markers, and other critical content. Avoid obstructive decorations in central or high-attention regions. Use peripheral placement and visual grouping according to gameplay and player expectations; a fixed corner is not universally correct.

Test legibility over representative bright, dark, detailed, and moving scenes. Use backing surfaces, outlines, or controlled contrast where necessary. Do not depend on blur alone. Scale critical values and state changes by importance; health, ammunition, and cooldowns should not compete equally with an incidental notification.

Convey urgent state through more than colour. Pair changes with clear symbols, labels, shape, or appropriate feedback. Avoid rapid flashing and constant motion that distracts from play. Respect reduced-motion and accessibility settings supported by the game.

Account for supported aspect ratios, safe areas, resolution scaling, localisation, and UI scale settings. Inspect narrow and ultrawide layouts when supported. Use the engine's responsive anchors and constraints rather than assuming CSS, device pixels, or a universal screen size.

Match controller, keyboard/mouse, and touch interaction to the supported devices. Menus need a visible focus path and predictable selection. Show input prompts that match the active device when the product already supports device switching. Do not redesign a combat overlay into a website navigation system.

Keep the visual system consistent with the world without sacrificing clarity. Diegetic treatment is an option, not an obligation. Fancy framing, particles, and translucency must earn their rendering cost; measure or explicitly leave performance unverified when instrumentation is unavailable.
