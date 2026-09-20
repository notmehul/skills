---
name: product-marketing
description: "Write or update a project's positioning doc at `docs/positioning.md`: who it's for, the problem in their words, the alternatives, why us, proof, and voice. Use on \"positioning\", \"ICP\", \"who is this for\", and at the start of any launch, outreach, content, or copy work on a project that has no positioning doc yet. The other marketing skills read this doc first."
---

# Product marketing

One doc per project, `docs/positioning.md`, next to `architecture.md` and `patterns.md`. Every marketing task on the project reads it first, so nobody re-asks the basics and every piece of copy argues from the same facts.

## Steps

1. **Look for it.** Read `docs/positioning.md`. If it's at an older location (`.agents/product-marketing.md`, `.claude/product-marketing.md`, `product-marketing-context.md`), offer to move it into `docs/`. If it exists, show its version and the last three changelog lines, ask which sections change, and edit only those.
2. **Draft from what exists.** Read the README, the landing page source, `docs/`, pricing config, open issues, and Marshmallow recall for the project. Fill every section of the template below. Mark each line you inferred rather than read as `[inferred]` and each gap as `[unknown]`. Done when every section has a sourced line or a marker.
3. **Get their words.** "In their words" takes verbatim quotes only, each with where it came from (an issue, a DM, a call note, a review) and a date. If there are none, ask the user for them or run `customer-research`. Paraphrase never goes in that section.
4. **Go through it with the user.** Show the draft and ask what's wrong and what's missing, one section at a time where they disagree. Numbers and proof follow unslop rule 32: from a source, or a flagged placeholder.
5. **Save and version.** Bump the version, set today's date (YYYY-MM-DD), and put a new line at the top of the changelog naming the sections touched and why. A typo fix gets no bump.

## Template

```markdown
# Positioning: <project>

Version: v1 · Last updated: YYYY-MM-DD

## One line
What it is and who it's for. It passes the "now you can" test (mehul-voice).

## Category
The shelf people search under when they look for this.

## Who it's for / who it isn't
The person who owns the problem, their company type and stage. Then the anti-persona.

## The problem, in their words
- "verbatim quote" (source, date)

## What they do today
Direct competitors, other approaches, doing nothing, building it themselves. Where each falls short, in their terms.

## Why us
Each differentiator with its proof, or `[unproven]`.

## Switching
Push (what drives them off the current way), pull (what draws them here), habit (what keeps them stuck), anxiety (what worries them about switching).

## Objections
| Objection | Answer | Proof |

## Proof
Metrics, users, quotes, each sourced.

## Voice
Anything published under Mehul's name uses mehul-voice. Otherwise: tone in three words, words to use, words to avoid.

## Goal
The business goal right now and the one action we want a reader to take.

## Changelog
- v1 (YYYY-MM-DD): initial draft from <sources>.
```

Adapted from `product-marketing` in coreyhaines31/marketingskills (MIT). See `~/.agents/NOTICE-marketingskills.md`.
