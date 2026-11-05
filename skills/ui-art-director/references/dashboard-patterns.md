# Dashboard patterns

Use for substantial dashboard design or refinement. Preserve existing features; these considerations do not authorise adding a search system, new metrics, or extra workflows.

## Organise the working surface

Name the user's main decision or action. Give it the appropriate position and area. Keep frequently compared information near one another and make visual hierarchy reflect usefulness. Choose a grid from the content rather than fixing every dashboard to the same arrangement.

Use a compact, readable type hierarchy appropriate to repeated use. A marketing headline scale rarely belongs in a table-heavy workspace. Align comparable values, show units and relevant date ranges, and distinguish data from its labels.

## Make navigation predictable

Group destinations by task and make the current location clear. Place global controls consistently; choose sidebar or top-bar placement according to the product. Secondary destinations should not compete equally with daily work.

If navigation collapses, preserve accessible names, selection state, keyboard reachability, and a discoverable way to expand it. A badge should add useful information without obscuring the destination or depending only on colour.

## Make data usable

Use lists for scanning and tables for meaningful comparison. Choose whitespace, dividers, or surface contrast deliberately to separate records. Avoid adding a border around every row when a quieter treatment makes the grouping clearer.

Preserve the search, filtering, sorting, selection, and bulk-action behaviour that the task needs. Contextual actions should appear where selection makes them relevant, with selected records remaining identifiable. Design empty and filtered-empty states differently when their next actions differ.

Charts need truthful data, units, a readable scale, and time context where applicable. Emphasis should help someone identify a value or compare series. Provide equivalent access for supported input methods; do not make important values available only on pointer hover.

## Choose interaction surfaces by task

| Surface | Useful context | Check |
| --- | --- | --- |
| Popover | A short, local option or lightweight contextual detail | Dismissal, naming, input access, and positioning |
| Modal dialog | A bounded task that needs to retain the underlying page context | Initial focus, contained interaction, dismissal, and focus return |
| Separate view | A durable destination, long task, or substantial detail | Navigation, return path, and preservation of relevant state |

Complexity alone does not determine the choice. Consider task duration, persistence, available space, and the need to compare with the underlying content. For web dialogs, use the current [WAI dialog pattern](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/) and suitable native semantics.

## Keep feedback truthful

Use notifications as appropriate feedback alongside the underlying state. Keep validation and recovery instructions near the affected action; a transient toast is insufficient for an important unresolved error.

Optimistic updates can improve perceived responsiveness when the existing application supports them. Show the local pending result appropriately, prevent conflicting duplicate actions, and handle server failure with rollback or recovery. Preserve entered data. A visual-polish task does not authorise changing persistence or transaction behaviour.

For movement, apply [motion-design.md](motion-design.md). A daily-use dashboard should remain efficient when animations are interrupted, reduced, or repeated hundreds of times.
