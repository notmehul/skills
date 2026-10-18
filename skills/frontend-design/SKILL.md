---
name: frontend-design
description: "Reference for frontend work that reads as designed rather than templated: an idea from the subject, type set large with few sizes, one accent, real pictures, one signature move. Reached from `ui-ux` when the brief wants a bold direction."
disable-model-invocation: true
metadata:
  opencode/autoinvoke: "false"
  updated: "2026-10-18"
  source: "forked from Anthropic's frontend-design plugin skill; rewritten with the type, colour, layout, imagery and motion values of Leonxlnx/taste-skill v2 and the polish values of jakubkrehel/make-interfaces-feel-better (both MIT, read 18 Oct 2026)"
---

# Frontend design

Build interfaces that read as designed rather than assembled. The user gives a component, page, application or interface to build, with whatever context exists about purpose, audience and constraints; the output is working code with a clear point of view, refined in every detail. Bold maximalism and refined minimalism both work; the key is intentionality, not intensity. For a public page, `ui-ux/references/public-page.md` carries the full rules and the installed `design-taste-frontend` skill runs the build; for app components, `ui-ux/references/polish.md` carries the craft values. This file is the stance and the numbers behind it.

## Design thinking, before any code

- **Purpose.** What problem does this interface solve, and for whom?
- **Idea.** Inventory what belongs to this subject and to no competitor (its name and what it means, its place, its numbers, the constraint it lives with, its materials, its rituals, the printed things of its world) and write one sentence: "On this page, [something that belongs to the subject] becomes [the device the composition calls for]." Put the nearest competitor in the sentence; if it still works, the idea belongs to the category. In the Oct 2026 study of 247 gallery sites, the pages that won blind tests were built from an item on such a list; the ones that lost had a good composition with a category idea. "Clean and modern" is not an idea.
- **Tone.** Pick a direction and commit: brutally minimal, editorial, luxury, playful, industrial, organic, retro-futuristic, maximalist. Nine idea engines seen on the top-scored sites: the product demonstrates itself; the page is an artefact from the subject's world; the name is the hero; one motif from the subject drives everything; dressed as another category; the place carries it; a fixed stage; one section, one colour; radical understatement.
- **Constraints.** Framework, performance, accessibility, the imagery that truly exists.
- **Differentiation.** The one thing someone remembers an hour later: usually the idea, the signature move, or the live thing the visitor can do.

Match implementation complexity to the vision: a maximalist direction needs elaborate code; a refined one needs restraint, precision and attention to spacing and type. Elegance is executing the vision well.

## Typography

Size contrast is the main lever and the best sites pull it harder; weight is not. The study's 202 measured sites: hero headline median 72px (5.0vw; top sites 6.0vw), largest type on the page 6.4vw median and 8.4vw on top sites against 5.0vw on weak ones, headline ÷ body 4.3 (top 4.7), hero weight regular 48%, medium 18%, bold or heavier 22%.

- **Few sizes, far apart.** Small (13 to 14px), body (17 to 19px), lead (20 to 26px), heading (32 to 64px), display set by the composition. Five is the ceiling; display at least four times body on desktop; nine sizes near each other read as mush.
- **Display settings** for anything over 40px: `line-height: 0.95` (0.85 to 1.05, tighter for capitals and condensed faces), `letter-spacing: -0.035em` (-0.02 to -0.05em, set per step, tighter as size grows), `font-kerning: normal`, `text-wrap: balance`, a `max-width` in `ch`. All caps want 0 to +0.03em and leading about 0.9. A headline starting with O, C, A, T or W is pulled left 0.04 to 0.06em so it aligns optically. No text shadow, outline stroke or gradient fill on display type.
- **Text.** Measure 45 to 75 characters; body leading 1.45 to 1.6; `text-wrap: pretty`; secondary text in a softer ink, not a lighter weight, never under 13px; no centred paragraphs past three lines; no justification; light on dark drops a weight step.
- **Choosing faces.** Choose a class, then a face inside it that is not this season's default; read [`references/type-systems.md`](references/type-systems.md) for 44 free systems by class with the commercial faces each stands in for and the settings that make each work. One family is the safest way to be coherent (a third of strong sites); with two, each has a job and they never swap; no third face for labels, numbers or quotes; no two faces inside one headline; italic for titles and real emphasis, never decoration. A serif display only when the brief names one or the subject is genuinely editorial or heritage, and you can say why. Load only the weights you use, give a fallback of the same kind, and confirm after building that the declared face rendered: a fallback makes every screenshot judgement false.
- **Headlines fit two lines at every width.** About 32 characters (four to six words) survives a phone at a confident size; a statement set large is a paragraph at 36px or less that may run three lines. Author the break; never fix a long headline only by shrinking it. Sentence case; one word styled differently is a tell.
- **Numbers** in the text face with `tabular-nums`; monospace only for code, IDs and hashes.

## Colour

Study: 41% of pages dark, 59% light; buttons neutral on 52%; gradient fills on 22% of top sites against 52% of weak ones and gradient text 2% against 13%; resting shadows 24% against 48%; one site in 246 has a terracotta primary button and none a violet one.

- **Roles**: `--bg`, `--surface` (2 to 6 lightness points from the ground), `--ink`, `--muted`, `--accent`, `--accent-ink`, and per-field inks where sections change ground. Every colour in the build is a token; a raw hex in a component is a second palette starting.
- **Proportion**: ground 70 to 90%; accent under 5% of any screen, on the action and at most one other thing; in five places it stops meaning "here". A headline is ink. Dominant colour with a sharp accent beats a timid, evenly spread palette.
- **Fields over decoration.** A section that changes its whole ground colour replaces dividers, cards and background effects at once; fields meet edge to edge, each with its own ink, neighbours differing in lightness. Depth comes from a tone step; shadows only on what truly floats (a menu, a dialog).
- **Dark pages**: `color-scheme: dark`; a tinted deep ground and a soft light ink, not #fff on #000; check `--muted` at 4.5:1; never a glow.
- **The generated palettes**: cream with terracotta or rust; violet or indigo gradients. Warmth comes from a low-chroma stone or putty ground, a deep green, brown or oxblood ink, photographs, or a full warm field used flat. Warmth is not beige. A brand that owns one of these colours keeps it; say so.
- **Text over a photograph** gets a calm region or a neutral scrim (black or the ink, 30 to 55%, over the text area only), never a coloured wash.

## Composition

- **Margins 16 to 32px, content to the edges.** The centred 1100 to 1300px container is the minority among strong sites and the usual frame of the stock ones; constrain the text measure in `ch`, not the page, and cap the layout around 1760 to 1920px.
- **One anchor line**, off centre, reused for the hero headline, section headings, the price and the footer; two or three on a whole page, six means nothing was decided. Centred is a decision: one axis, wide flanks, one element per screen, never a centred stack of heading, paragraph and two buttons (7% of top sites, 24% of weak).
- **One thing per screen.** Empty space is placed, not left over; the gap between sections (120 to 220px desktop) is clearly larger than any gap inside one; a heading has twice the space above it as below; when a section looks empty, make the main thing bigger or cut it.
- **Sections recomposed, not repeated**, and the idea carried into pricing, FAQ and footer: a distinctive first screen followed by stock blocks is the commonest failure in every score band. Break the system once on purpose. Short pages are fine.
- **Navigation is small furniture**: wordmark, three to five links, one action, no bar; never on top of content at any scroll position. **Endings are a designed scene**, not a link farm.
- **The phone is a second composition**: 390px designed as its own page, line breaks re-authored, images re-cropped, body 16 to 18px, targets 44px.
- **Buttons**: flat, one fill, square-cornered or fully round, decided once (top sites 52% square, 23% pill; the 9 to 16px "soft" radius is the weak-site default). Most strong heroes have no button or one; the primary action keeps one name across the page.

## Imagery

Top pages carry a median of 37 images against 5 on weak ones: the strong sites show, the weak ones tell. On 68% of top sites one piece of media covers at least half the first screen.

- **Order of preference**: the project's own; generated this session as a photographer's brief; real pictures of the subject's world from open collections, credited (`ui-ux/references/public-page.md` §6 for sources, licences and the honesty rule); drawn in code from the subject itself with three levels of detail; generic atmosphere only where honest; type and colour alone, done on purpose.
- **One treatment for the page**, a small set of ratios, images large and touching edges, square corners unless the direction says otherwise, no frames, device mock-ups or browser chrome. Not treatments: colour washes, duotone, blur, grain, vignettes, tilted frames.
- **Never**: a grey box where a picture will go, icons in squares, abstract gradient blobs, isometric clip art, people at laptops, a fake dashboard of grey bars, invented social proof.

## Motion

One signature move done well (a masked headline rising from its baseline, an image opening like a shutter, a wordmark scaling with the scroll, a pinned story, an index whose rows preview their image); an entrance for the parts of each section in reading order, 60 to 90ms apart, rising 16 to 32px with opacity, once; feedback under the hand (press `scale(0.96)`, hover that raises contrast, menus opening from their trigger); one moving picture. Durations: press 100 to 160ms, hover 150 to 200, menus 150 to 250, dialogs 250 to 450, reveals 500 to 900, exits about 70% of enters. Ease-out in and out (`cubic-bezier(0.22, 1, 0.36, 1)`), ease-in-out for things that travel while visible, never ease-in, no bounce. Hidden pre-animation states only under `html.js` so nothing stays invisible when a script fails; hover behind `(hover: hover)`; reduced motion keeps the content and drops the travel. No smooth-scroll library, no scroll hijacking, no custom cursor: they cost usability. CSS first; a motion library only when the project already has one.

## What reads as generated

Violet or indigo gradients and glows; gradient headline text; glass panels and floating pill navigation; a grey shadow under every card; three identical feature cards each with an icon in a rounded square (1% of top sites, 28% of weak); an eyebrow label above every heading; a pill badge above the headline; one italic serif word in a headline; cream and terracotta; a soft serif display as the shortcut to "premium"; broadsheet cosplay with hairlines everywhere; a full sentence at display size over three or four lines; the stock section order; every section the same layout; everything centred; the 12px radius on everything; the same fade-up on every block; a dozen staggered hero entrances; hover lift on every card; pulsing dots and floating shapes; "unlock", "seamless", "elevate", "not just X, it's Y", "Plan. Build. Ship." Removing a tell leaves space: fill it with scale, the full content, a picture made for this subject, or a flat field, never another ornament.

Render it and look at it before calling it done: `ui-ux`'s verify step runs the inspector at three widths and the critique passes on the screenshots.

<!-- marshmallow:alignment:start -->
## Marshmallow Alignment

Before using this skill, read `~/.marshmallow/overlays/frontend-design.md` and apply it as the recall-aware alignment layer.
<!-- marshmallow:alignment:end -->
