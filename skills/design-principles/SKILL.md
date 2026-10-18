---
name: design-principles
description: "Reference for a precise, minimal design system: spacing scale, type ramp, restraint rules, the pixel-level decisions a dashboard or admin UI needs. Reached from `ui-ux` when the work needs tightness rather than a style direction."
disable-model-invocation: true
metadata:
  opencode/autoinvoke: "false"
  updated: "2026-10-18"
  source: "own rules; polish values after jakubkrehel/make-interfaces-feel-better (MIT) and type and colour priors after Leonxlnx/taste-skill v2 (MIT), both read 18 Oct 2026"
---

# Design Principles

This skill enforces precise, crafted design for enterprise software, SaaS dashboards, admin interfaces, and web applications. The philosophy is Jony Ive-level precision with intentional personality — every interface is polished, and each is designed for its specific context.

## Design Direction (REQUIRED)

**Before writing any code, commit to a design direction.** Don't default. Think about what this specific product needs to feel like.

### Think About Context

- **What does this product do?** A finance tool needs different energy than a creative tool.
- **Who uses it?** Power users want density. Occasional users want guidance.
- **What's the emotional job?** Trust? Efficiency? Delight? Focus?
- **What would make this memorable?** Every product has a chance to feel distinctive.

### Choose a Personality

Enterprise/SaaS UI has more range than you think. Consider these directions:

**Precision & Density** — Tight spacing, monochrome, information-forward. For power users who live in the tool. Think Linear, Raycast, terminal aesthetics.

**Warmth & Approachability** — Generous spacing, soft shadows, friendly colors. For products that want to feel human. Think Notion, Coda, collaborative tools.

**Sophistication & Trust** — Cool tones, layered depth, financial gravitas. For products handling money or sensitive data. Think Stripe, Mercury, enterprise B2B.

**Boldness & Clarity** — High contrast, dramatic negative space, confident typography. For products that want to feel modern and decisive. Think Vercel, minimal dashboards.

**Utility & Function** — Muted palette, functional density, clear hierarchy. For products where the work matters more than the chrome. Think GitHub, developer tools.

**Data & Analysis** — Chart-optimized, technical but accessible, numbers as first-class citizens. For analytics, metrics, business intelligence.

Pick one. Or blend two. But commit to a direction that fits the product.

### Choose a Color Foundation

**Don't default to warm neutrals.** Consider the product:

- **Warm foundations** (creams, warm grays) — approachable, comfortable, human
- **Cool foundations** (slate, blue-gray) — professional, trustworthy, serious
- **Pure neutrals** (true grays, black/white) — minimal, bold, technical
- **Tinted foundations** (slight color cast) — distinctive, memorable, branded

**Light or dark?** Dark modes aren't just light modes inverted. Dark feels technical, focused, premium. Light feels open, approachable, clean. Choose based on context.

**Accent color** — Pick ONE that means something. Blue for trust. Green for growth. Orange for energy. Violet for creativity. Don't just reach for the same accent every time.

### Choose a Layout Approach

The content should drive the layout:

- **Dense grids** for information-heavy interfaces where users scan and compare
- **Generous spacing** for focused tasks where users need to concentrate
- **Sidebar navigation** for multi-section apps with many destinations
- **Top navigation** for simpler tools with fewer sections
- **Split panels** for list-detail patterns where context matters

### Choose Typography

Typography sets tone. Choose a class for the product, then a face inside it that is not the current default; every published "use this font instead" list becomes the next tell within months, so this skill names classes, not faces:

- **System fonts** — fast, native, invisible (good for utility-focused products)
- **Grotesk, tight or light** — modern, clean, technical; the default class for product UI
- **Geometric sans** — orderly, constructed, slightly cooler
- **Humanist sans or rounded** — warmer, more approachable
- **Monospace as an accent** — code, IDs, hashes and a developer voice; never the running text face

Derive the choice from the product (its users, its voice, its existing brand), load only the weights you use (two or three in total), give a fallback stack of the same kind, and confirm after building that the declared face actually rendered: a fallback makes every visual judgement false.

---

## Core Craft Principles

These apply regardless of design direction. This is the quality floor.

### The 4px Grid
All spacing uses a 4px base grid:
- `4px` - micro spacing (icon gaps)
- `8px` - tight spacing (within components)
- `12px` - standard spacing (between related elements)
- `16px` - comfortable spacing (section padding)
- `24px` - generous spacing (between sections)
- `32px` - major separation

### Padding: symmetrical by default, optical by exception
Start with matching padding on all four sides (16px, or 12px 16px when the horizontal needs room). Then adjust by eye where geometry lies: a button with a trailing icon gets 2px less padding on the icon side; a play triangle shifts about 2px toward its point; a section's bottom padding often needs to be slightly larger than its top to look equal. An optical adjustment is a decision written once in the component, not a different value on every instance.

```css
/* Default */
padding: 16px;
padding: 12px 16px;

/* Optical: icon side = text side - 2px */
padding: 0 14px 0 16px;

/* Accidental */
padding: 24px 16px 12px 16px;
```

### Border Radius Consistency
Stick to the 4px grid. Sharper corners feel technical, rounder corners feel friendly. Pick a system and commit:

- Sharp: 4px, 6px, 8px
- Soft: 8px, 12px
- Minimal: 2px, 4px, 6px

Don't mix systems. Consistency creates coherence. Inside the system, nested radii are concentric: outer radius = inner radius + the padding between them (a 16px card with 8px padding holds an 8px-radius child). Equal radii on parent and child read as pinched; past about 24px of padding, treat the two as separate surfaces and pick each radius on its own. A mixed system is allowed only under a written rule ("buttons pill, cards 12px, inputs 8px").

### Depth & Elevation Strategy

**Match your depth approach to your design direction.** Depth is a tool, not a requirement. Different products need different approaches:

**Borders-only (flat)** — Clean, technical, dense. Works for utility-focused tools where information density matters more than visual lift. Linear, Raycast, and many developer tools use almost no shadows — just subtle borders to define regions. This isn't lazy; it's intentional restraint.

**Subtle single shadows** — Soft lift without complexity. A simple `0 1px 3px rgba(0,0,0,0.08)` can be enough. Works for approachable products that want gentle depth without the weight of layered shadows.

**Layered shadows** — Rich, premium, dimensional. Multiple shadow layers create realistic depth for products that want to feel substantial. Stripe and Mercury use this approach. Best for cards that need to feel like physical objects.

**Surface color shifts** — Background tints establish hierarchy without any shadows. A card one tone step (2 to 6 lightness points) from the ground already feels elevated; one step is enough, and a panel inside a panel is a smell. Shadows can reinforce this, but color does the heavy lifting.

**Shadow as border** — For a card, button or container whose border exists only to fake depth, a layered transparent shadow adapts to any background where a solid border does not. Borders that carry structure or state (dividers, table cells, input outlines, focus and selected states) stay borders.

Choose ONE approach and commit. Mixing flat borders on some cards with heavy shadows on others creates visual inconsistency.

```css
/* Borders-only approach */
--border: rgba(0, 0, 0, 0.08);
--border-subtle: rgba(0, 0, 0, 0.05);
border: 0.5px solid var(--border);

/* Single shadow approach */
--shadow: 0 1px 3px rgba(0, 0, 0, 0.08);

/* Layered shadow approach (when appropriate) */
--shadow-layered:
  0 0 0 0.5px rgba(0, 0, 0, 0.05),
  0 1px 2px rgba(0, 0, 0, 0.04),
  0 2px 4px rgba(0, 0, 0, 0.03),
  0 4px 8px rgba(0, 0, 0, 0.02);

/* Shadow-as-border: a 1px ring, a little lift, ambient depth */
--shadow-border:
  0 0 0 1px oklch(0 0 0 / 0.06),
  0 1px 2px -1px oklch(0 0 0 / 0.06),
  0 2px 4px 0 oklch(0 0 0 / 0.04);
/* dark mode collapses to one ring: 0 0 0 1px oklch(1 0 0 / 0.08) */
```

**The craft is in the choice, not the complexity.** A flat interface with perfect spacing and typography is more polished than a shadow-heavy interface with sloppy details.

### Card Layouts Vary, Surface Treatment Stays Consistent
Monotonous card layouts are lazy design. A metric card doesn't have to look like a plan card doesn't have to look like a settings card. One might have a sparkline, another an avatar stack, another a progress ring, another a two-column split.

Design each card's internal structure for its specific content — but keep the surface treatment consistent: same border weight, shadow depth, corner radius, padding scale, typography. Cohesion comes from the container chrome, not from forcing every card into the same layout template.

### Isolated Controls
UI controls deserve container treatment. Date pickers, filters, dropdowns — these should feel like crafted objects sitting on the page, not plain text with click handlers.

**Native first.** Native `<select>`, `<input type="date">`, checkboxes and radios bring keyboard handling, screen-reader semantics, mobile pickers and the right on-screen keyboard for free; style their container and their trigger and keep them. Build a custom control only when the design needs something a native one cannot do, and then only with full parity: keyboard operation, focus management, ARIA roles and states, and the same behaviour on touch. A custom control that fails any of those is a regression dressed as polish.

- Custom select: trigger button + positioned dropdown menu, `role="listbox"`, arrow keys, typeahead, Escape closes
- Custom date picker: a real input that accepts typing + a calendar popover
- Custom checkbox/radio: the native input stays in the DOM (visually hidden), the styled element mirrors its state

**Custom select triggers must use `display: inline-flex` with `white-space: nowrap`** to keep text and chevron icons on the same row. Without this, flex children can wrap to new lines.

### Typography Hierarchy
- Headlines: 600 weight, tight letter-spacing (-0.02em); size does the hierarchy work before weight does
- Body: 400-500 weight, standard tracking
- Labels: 500 weight, slight positive tracking for uppercase; tiny tracked uppercase labels scattered around a view are a tell, so keep them to table headers and section labels
- Scale: 11px, 12px, 13px, 14px (base), 16px, 18px, 24px, 32px. 13px is the floor for anything meant to be read; 11px and 12px are for metadata nobody must read (timestamps in a dense log, axis ticks), never for body or labels
- `text-wrap: balance` on headings, `pretty` on short paragraphs; `-webkit-font-smoothing: antialiased` once, on the root

### Numbers and Code
Numbers that change (counters, prices, timers, table columns) are set in the text face with `font-variant-numeric: tabular-nums`, so digits line up and nothing shifts. Monospace is for code, IDs, hashes and tokens: things a person copies, not things they read. A monospace label on a number does not make it data; alignment does.

### Iconography
Use **Phosphor Icons** (`@phosphor-icons/react`) as the house set. Icons clarify, not decorate — if removing an icon loses no meaning, remove it.

- One SVG per icon drawn with `currentColor`; hover, selected and disabled come from CSS colour and opacity, never separate assets. Outline is the default; the filled variant marks the active state.
- The stroke matches the text beside it: 1.5px next to regular text, 2px next to medium or semibold, 2.5px next to bold or standalone. One stroke weight per surface; never two icon sets on one surface.
- Test at the smallest render size (usually 16px); use the set's native grid sizes.
- A standalone icon in a toolbar or an empty state may sit in a subtle container for presence. A row of icon-topped feature cards is a marketing-page tell (1% of top sites, 28% of weak ones in the Oct 2026 study), not a dashboard pattern.

### Animation
- 150ms for micro-interactions, 200-250ms for larger transitions; press feedback `scale(0.96)` over 150ms, never below 0.95
- Easing: `cubic-bezier(0.25, 1, 0.5, 1)`, ease-out for entering and exiting (the exit shorter); never ease-in
- CSS transitions for interactive state changes (they retarget mid-flight when the user changes their mind); keyframes only for one-shot sequences
- No bounce or elastic motion in enterprise UI; a spring with bounce 0 is fine, it is just a good ease-out
- Nothing custom on high-frequency interactions (row hover, keystrokes): instant, or a colour or opacity transition at 150ms or less. Motion is never the only feedback channel.
- `references/polish.md` in `ui-ux` carries the rest: concentric radii, optical alignment, image outlines, icon cross-fades, `will-change`, `transition-property`

### Contrast Hierarchy
Build a four-level system: foreground (primary) → secondary → muted → faint. Use all four consistently.

### Color for Meaning Only
Gray builds structure. Color only appears when it communicates: status, action, error, success. Decorative color is noise.

When building data-heavy interfaces, ask whether each use of color is earning its place. Score bars don't need to be color-coded by performance — a single muted color works. Grade badges don't need traffic-light colors — typography can do the hierarchy work. Look at how GitHub renders tables and lists: almost entirely monochrome, with color reserved for status indicators and actionable elements.

---

## Navigation Context

Screens need grounding. A data table floating in space feels like a component demo, not a product. Consider including:

- **Navigation** — sidebar or top nav showing where you are in the app
- **Location indicator** — breadcrumbs, page title, or active nav state
- **User context** — who's logged in, what workspace/org

When building sidebars, consider using the same background as the main content area. Tools like Supabase, Linear, and Vercel rely on a subtle border for separation rather than different background colors. This reduces visual weight and feels more unified.

---

## Dark Mode Considerations

Dark interfaces have different needs:

**Borders over shadows** — Shadows are less visible on dark backgrounds. Lean more on borders for definition. A border at 10-15% white opacity might look nearly invisible but it's doing its job — resist the urge to make it more prominent.

**Adjust semantic colors** — Status colors (success, warning, error) often need to be slightly desaturated or adjusted for dark backgrounds to avoid feeling harsh.

**Same structure, different values** — The hierarchy system (foreground → secondary → muted → faint) still applies, just with inverted values.

---

## Anti-Patterns

### Never Do This
- Dramatic drop shadows (`box-shadow: 0 25px 50px...`)
- Large border radius (16px+) on small elements
- Asymmetric padding without clear reason
- Pure white cards on colored backgrounds
- Thick borders (2px+) for decoration
- Excessive spacing (margins > 48px between sections)
- Spring/bouncy animations
- Gradients for decoration
- Multiple accent colors in one interface

### Always Question
- "Did I think about what this product needs, or did I default?"
- "Does this direction fit the context and users?"
- "Does this element feel crafted?"
- "Is my depth strategy consistent and intentional?"
- "Are all elements on the grid?"

---

## The Standard

Every interface should look designed by a team that obsesses over 1-pixel differences. Not stripped — *crafted*. And designed for its specific context.

Different products want different things. A developer tool wants precision and density. A collaborative product wants warmth and space. A financial product wants trust and sophistication. Let the product context guide the aesthetic.

The goal: intricate minimalism with appropriate personality. Same quality bar, context-driven execution.

<!-- marshmallow:alignment:start -->
## Marshmallow Alignment

Before using this skill, read `~/.marshmallow/overlays/design-principles.md` and apply it as the recall-aware alignment layer.
<!-- marshmallow:alignment:end -->
