# Redesigning an existing UI, and building from a reference image

Read this when the brief is "improve what exists" (a redesign, a restyle, "make it look premium", "it looks AI-made") rather than a new build, or when the brief arrives as a screenshot or a design export.

## Redesign

1. **Decide the mode out loud**: preserve (people use this; new UI explains itself in terms of what they know, and nothing they rely on moves) or overhaul (the owner has said the old one goes). Default to preserve for any product with users. Say which mode you are in before touching a file.
2. **Audit before touching.** Read the codebase for the framework, the styling method and its version (Tailwind v3 or v4 changes the config you edit), and the existing design tokens. Render the current state and measure it: for a public page the lint and inspector in `public-page.md` §8, for an app the review in `polish.md`, and the critique passes in both cases. Write the findings down in the fix order below, with a screenshot reference each. The audit is the deliverable of the first pass; no fixes yet.
3. **Fix in the order that cannot be rescued later**: the idea (does the first screen say what this is and could it belong to anyone else), hierarchy (one dominant element per screen), composition (shared edges, section spacing, holes, variety), typography, imagery, colour, detail (states, focus, alignment), motion last. A font swap is not step one; the weak sites in the study had the same fonts as the strong ones more often than not, and a font change on top of a bad hierarchy is a costume.
4. **Never change silently**: URL structure and slugs, navigation labels, form field names and ids, the wordmark, legal copy, keyboard shortcuts, and any working behaviour. Each of these changes only with a line in the report saying so.
5. **Work in the existing stack.** No framework or styling-library migration inside a redesign; check the dependency file before importing anything; small reviewable changes over a rewrite; run the app after every change (`prove-it-works`), because a redesign that breaks a form is a regression, not a redesign.

### The audit list

Things redesigns usually find, grouped by what they cost the user. Everything here is in addition to the Quick Reference checklist in `SKILL.md`.

- **Reachability**: a skip-to-content link; a visible focus ring on everything interactive; the current page marked in the navigation; a way back from every page; a branded 404; legal links in the footer; a favicon; `<title>`, description and social meta tags.
- **Structure**: semantic elements (`nav`, `main`, `article`, `aside`, `section`) instead of div soup; a z-index scale in the tokens instead of `9999`; relative units instead of hardcoded pixel widths; `min-height: 100dvh` instead of `100vh`; animations on `transform` and `opacity`, never `top`, `left`, `width`, `height`.
- **Collapsed navigation**: a rail of 56 to 72px with one icon per destination keeps its labels in the DOM (visually hidden) and shows them as tooltips on hover and focus; targets stay 44x44px; the control is a button with an accessible name and `aria-expanded`; inactive expanded content is removed from the tab order with `inert`, `hidden` or `display: none`, since `aria-hidden` alone does not; below the tablet breakpoint the rail becomes an off-canvas drawer.
- **Cards side by side**: buttons pinned to the bottom so they form one line regardless of content length; shared elements (title, price, feature list) start at the same y across all cards; allow variable heights or a masonry when content varies instead of forcing equal heights.
- **States**: hover, pressed (`scale(0.96)`, `polish.md`), focus, loading (a skeleton that matches the layout shape, not a generic spinner), empty (a composed first-use view), error (inline, near the field, with the cause and the fix; never `window.alert`), disabled; dead links that go to `#` are either wired or visibly disabled.
- **Content**: no placeholder people ("John Doe"), no round fake numbers (99.99%, $100.00), no placeholder companies; dates and avatars that are not all identical; sentence case; no exclamation marks in success messages; no "Oops"; active voice; no lorem ipsum; no invented proof (`public-page.md` §2).
- **Depth and ornament**: a border used only to fake elevation becomes the shadow-as-border token (`polish.md`) or a tone step; grain and noise overlays, "true glassmorphism", spotlight borders, tinted dramatic shadows and smooth-scroll inertia are the generated look of 2025 and are removed, not added; `backdrop-filter` only on fixed or sticky elements, never on scrolling containers.
- **Placeholders**: a picture that is not there is not replaced with a stock placeholder service; it is the project's own image, a found and credited picture of the subject's world, a drawing of the subject, or type and colour alone (`public-page.md` §6).

## When the brief is an image

A screenshot, a Figma export or a generated comp is a specification, and the failure mode is drifting from it while coding.

1. **Extract before coding.** Read off the reference, into a table: every text string; the type scale (sizes, weights, line heights, tracking) by role; the spacing scale and the margins; the button shapes, sizes and states; the colour values by role; the image ratios and crops; the breakpoints implied.
2. **Build to the table**, tokens first, then the hero at desktop and phone width, then each section.
3. **Anti-drift pass**: put the render and the reference side by side at the same width and walk the table row by row; every deviation is either corrected or written into the report as a deliberate change with a reason.
4. **The first screen must also work on a small laptop** (about 1280x720), not only at the comp's width; and the image is a comp, not a licence: the honesty, proof and licence rules of `public-page.md` still apply to what ends up on the page.

Distilled from taste-skill v2's redesign branch and `image-to-code-skill`, and the structural and accessibility items of its `redesign-skill` (MIT, read 18 Oct 2026). Their ornament advice (grain, glass, tinted shadows, named replacement fonts, placeholder services) was dropped because the same repo's study measures the opposite.
