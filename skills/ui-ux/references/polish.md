# Polish: the details that make an interface feel right

Read this when building or reviewing components, states and motion in an app UI, or when a user says "it feels off", "make it feel better", or asks for a polish pass. Every rule is checkable. Express each fix in the project's existing styling system (Tailwind in a Tailwind project, plain CSS in a CSS project); never add a second one for a polish fix.

When reviewing, slow the interface down: replay motion at 10% speed in the browser's Animations panel and walk every state (hover, focus, active, loading, empty). What feels off at 10% is what is subtly wrong at full speed.

## Surfaces

- **Concentric radius.** Nested rounded elements: outer radius = inner radius + padding (a 16px card with 8px padding holds an 8px-radius child). Equal nested radii read as pinched. Past about 24px of padding, treat the layers as separate surfaces and pick each radius on its own.
- **Optical over geometric.** When centring looks off, adjust by eye: a button with a trailing icon gets 2px less padding on the icon side; a play triangle shifts about 2px right; asymmetric glyphs are fixed in the SVG, not with margins.
- **Shadows for elevation, borders for structure.** A border that exists only to fake depth becomes a layered transparent shadow; borders that carry structure or state (dividers, table cells, form-input outlines, focus and selected states) stay borders. Shadow-as-border token, light mode: `0 0 0 1px oklch(0 0 0 / .06), 0 1px 2px -1px oklch(0 0 0 / .06), 0 2px 4px 0 oklch(0 0 0 / .04)`; hover raises each alpha by about .02. Dark mode collapses to one ring: `0 0 0 1px oklch(1 0 0 / .08)`, hover `.13`.
- **Image outline.** A 1px inset outline on images for consistent depth: `outline: 1px solid oklch(0 0 0 / .1); outline-offset: -1px` in light mode, `oklch(1 0 0 / .1)` in dark. Pure black or white only; a tinted neutral picks up the surface and reads as dirt on the edge.
- **Hit area.** 44x44px for touch, at least 40x40px in dense desktop UI, extended with a pseudo-element when the visible control is smaller. Two hit areas never overlap; shrink the pseudo-element until they do not.

## Typography

- `text-wrap: balance` on headings (browsers apply it only up to about six lines); `text-wrap: pretty` on short and medium text (paragraphs, captions, list items) to stop orphans; neither on long text or code.
- `-webkit-font-smoothing: antialiased` once, on the root, for macOS; per-element use makes weights inconsistent.
- `font-variant-numeric: tabular-nums` on any number that changes (counters, timers, prices, table columns); proportional figures on static or decorative numbers, phone numbers and version strings. Inter widens and centres the digit 1 under this setting; check it.
- These are rendering details. They never justify changing the project's typeface.

## Motion

- **Transitions for interaction, keyframes for one-shot sequences.** A CSS transition retargets mid-flight when the user changes their mind; a keyframe animation restarts. Hover, toggle, open and close are transitions.
- **Enter: split and stagger**, only for an infrequent staged entrance where sequence shows hierarchy (first load of a hero, a success or empty state). Semantic chunks (title, description, actions) about 100ms apart, words in a title about 80ms; each chunk moves on opacity, a 12px rise and a 4px blur. Routine interactions (row hover, keystrokes, tab changes) never stagger.
- **Exit softer than enter.** A fixed small `translateY(-12px)` with opacity and blur, about 150ms against a 300ms enter, `ease-out` both ways. Slide fully out only when spatial context matters (a drawer, a card returning to a list). Remove instantly when motion adds nothing, the interaction repeats often, or reduced motion is set.
- **Contextual icon swap** (play to pause, outline to filled): scale 0.25 to 1, opacity 0 to 1, blur 4px to 0, with a spring of duration 0.3 and bounce 0 when a motion library is installed; otherwise keep both icons in the DOM, one absolutely positioned, and cross-fade with `cubic-bezier(0.2, 0, 0, 1)`. Import from whichever motion package `package.json` already has; never add one for this.
- **Press feedback** is `scale(0.96)` over 150ms as a transition. Never below 0.95. A `static` prop turns it off where it would distract.
- **No enter animation on first paint** for toggles, tabs and icon swaps that have a default state (`initial={false}` on the presence wrapper); keep it for a true page-load entrance, and check a full refresh after changing it.
- **Motion restraint.** No custom animation on high-frequency interactions: instant feedback or a colour or opacity transition at 150ms or less. Motion is never the only feedback channel; every animated state change also has a static cue (colour, icon, label). Reduced motion keeps the cue and drops the travel.

## Icons

- Stroke matches the text beside it: 1.5px next to regular 14 to 16px text, 2px next to medium or semibold, 2.5px next to bold or standalone. One stroke weight per surface; never two icon libraries on one surface.
- One SVG per icon, drawn with `currentColor`; hover, selected and disabled come from CSS colour and opacity, never from separate assets. Outline is the default; the filled variant marks the active state, and the swap is the icon animation above.
- Design at render size: test at 16px, use the set's native grid sizes (16, 20, 24), prefer a simplified glyph to a scaled-down detailed one.
- Right-to-left flips directional glyphs (arrows, chevrons, indent, send) and leaves logos, checkmarks, clocks and playback controls alone. Every icon-only control has an accessible name; decorative icons are hidden from assistive technology.

## Performance

- Never `transition: all`. Name the properties: `transition-property: scale, background-color`. Tailwind's `transition-transform` covers transform, translate, scale and rotate.
- `will-change` only for `transform`, `opacity` and `filter`, only when a first-frame stutter is visible (Safari most often), never `will-change: all`; each layer costs memory.

## Review output

Modes: `quick` covers the primary path and highest-traffic states, reports only HIGH and MEDIUM, caps at 5 findings; `full` covers everything above, caps at 15. Say which mode ran, the exact scope, the framework and styling conventions, and show what was inspected per category (typography, surfaces, motion, icons, performance) with a result of findings, clear, or not reviewed with a reason. Never imply an uninspected surface was reviewed.

Findings as one table per principle: severity, location (`path:line`, or the screen and component when there is no source), before, after, why. HIGH makes an interaction inaccessible, misleading, unreadable or repeatedly disruptive; MEDIUM is a noticeable usability or consistency problem; LOW is isolated polish and appears only in `full`. One row per systemic issue with every affected location listed. No padding to reach the cap.

Then a short "considered but rejected" table (1 to 3 rows in `quick`, 2 to 5 in `full`) of real candidates and why they stayed, a verification list of the commands and interactions actually run (motion at 10% speed when animation is involved; anything not run is marked not verified), and a verdict: `Block` with any HIGH open, `Needs changes` with only MEDIUM or LOW, `Approve` with nothing actionable.

Distilled from jakubkrehel/make-interfaces-feel-better (MIT, read 18 Oct 2026). The values are theirs; the scope notes are ours.
