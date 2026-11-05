# Visual language

Use this reference to choose or repair a visual direction. It offers decision criteria, not a preset aesthetic. Preserve an established brand when the task is an incremental improvement.

## Start with a composition that works without decoration

Decide what the viewer should notice first, second, and third. Give those elements different visual weights. Use size, contrast, position, grouping, and whitespace together; do not make every element compete through saturation or bold type.

Judge the first viewport as a composition. Is the focal point clear? Does the main content occupy an appropriate proportion of the screen? Does alignment create a readable path? Are sections meaningfully different, or just repeated boxes? In a dense tool, the primary workspace may deserve the largest area. In a portfolio, a single image may lead. Do not force every product into a centred headline and a grid of cards.

Use proximity to express relationships. Separate sections more strongly than elements within a section. Repeated spacing should create rhythm, with purposeful exceptions around focal content. Keep long lines readable and short labels visually attached to their values.

Negative space is an allocation of attention. Excessive padding can make a working application inefficient; insufficient space can make a marketing page feel cheap. Choose density from the task rather than fashion.

## Make typography carry the design

Assign roles before selecting fonts: display, heading, body, label, data, and code where needed. Establish a visible hierarchy through size, weight, line height, width, and colour. Start with a restrained type system, then add variety only for a clear role.

Judge actual words. Refine awkward heading wraps, orphaned words, uneven label baselines, and number alignment. Use tabular numerals for changing values or columns where they improve scanning. All-caps may suit a small HUD label; it rarely suits a paragraph.

Respect available font weights, language coverage, loading behaviour, and the project's distribution constraints. A distinctive system font treatment can be stronger than an unnecessary external font dependency. Avoid shrinking essential text to solve a layout problem; solve the layout.

## Give colour a job

Define colours by role: canvas, surface, foreground, muted text, border, accent, and semantic states. Vary visual emphasis deliberately. Reserve high salience for the main action and genuinely important information.

Choose hue, value, and saturation together. Colourful interfaces need quiet areas; restrained interfaces still need enough contrast and differentiation. Light and dark themes require separate judgement of surfaces, borders, images, and text, rather than mechanical inversion.

Readability outranks a fashionable palette. For WCAG-targeted web work, check the relevant current contrast criteria: ordinary text generally needs 4.5:1, large text 3:1, and qualifying interface graphics 3:1. Consult the W3C explanations of [text contrast](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) and [non-text contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html) for definitions and exceptions. These are scoped checks, not proof of overall accessibility compliance. Use redundant labels, shapes, or symbols for semantic meaning.

## Choose materials and assets deliberately

Use elevation, borders, texture, and translucency to explain grouping or layering. A border may be clearer and cheaper than a large shadow. A translucent HUD may need a backing plate or scrim so text survives a bright moving scene.

Match icon family, stroke weight, optical size, and alignment. Prefer the project's icon system over mixing libraries. Use icon-only controls only when their meaning and accessible naming are clear.

Treat imagery as part of the layout: subject, crop, focal point, aspect ratio, and colour relationship matter. Reserve layout space to avoid shifting content when images load. Do not use irrelevant stock images simply to fill a gap. Avoid rendering essential UI text inside an image when editable, accessible text is appropriate.

## Give the product a signature

Derive a distinctive motif from its content or task: a precise numeric rhythm for an operations tool, a strong editorial grid for a publication, a material vocabulary for a crafting game, or a recognisable framing treatment for a portfolio.

Carry that decision through relevant components instead of adding unrelated decoration to every section. The signature should survive removal of a logo and still belong to the product.

Common generated patterns become weak when chosen automatically: generic gradient headlines, identical rounded cards, excessive pills, ornamental charts, empty “premium” copy, and motion without a purpose. These elements can be appropriate when the brief supports them. Diagnose the mismatch rather than banning a style universally.

## Make interaction and motion part of the same language

Use states to explain what can be acted on, what is selected, what changed, and whether an action succeeded. Keep focus, hover, pressed, selected, loading, disabled, and error states distinct where relevant. Do not use disabled styling for content that remains actionable.

Choose motion according to distance, importance, and input. Small feedback should feel prompt; a large spatial transition may need more time. Preserve continuity when a panel opens or an object changes position. Support reduced-motion preferences and avoid hiding essential content behind delayed animation.

Prototype the costly visual effect before spreading it across the interface. A beautiful effect that breaks scrolling or game frame time has failed its context.
