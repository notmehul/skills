---
name: mi-os
description: "Evaluate a startup, market, or technology as an evidence pack: testable claims, sourced findings, reusable memory. Use for deal evaluation, market sizing, technical due diligence, or building a research dossier."
---

# MI-OS (Market Intelligence / DD)

Turn messy inputs (pitch decks, PDFs, URLs, a company name) into a trustworthy,
reusable intelligence dossier. This is Mehul's own MIA / MI-OS pattern as a
repeatable skill. (Recall-aware: see `biome-impact-and-tooling` in
`~/.marshmallow/`.)

Shape: **worker → orchestrator → memory.** Three outputs per deal/market.

## 1. Testable Claims ("Anti-Feku")

- Decompose the pitch/thesis into discrete, falsifiable claims (market size,
  growth, moat, traction, technical feasibility, competition).
- Each claim gets a status: supported / refuted / unverified, with confidence.
- Flag vague or unfalsifiable assertions explicitly rather than passing them on.

## 2. Sourced Evidence Pack ("Trust Engine")

- Every claim links to its evidence with a source pointer. **No methodology =
  low trust** — score sources, don't treat all equally.
- Separate **data** from **knowledge/insight**; capture the insight, cite the
  data. Use exact figures with year/context (numbers are where retrieval fails).
- For market sizing, prefer primary sources and show the calculation, not a
  single quoted TAM.

## 3. Reusable Memory ("Category Moat")

- Save distilled insights (benchmarks, equations, competitor maps, rejected
  theses) so the next similar deal doesn't restart from zero.
- Record *why* something was dropped, not just that it was.

## Technical DD additions

- Separate what they *have* (hardware/software/IP) from what's *hard* (the real
  technical risk). Name the genuinely non-trivial parts and the failure modes.
- Watch for generic architecture dressed up as proprietary — say so plainly.

## Principles

- Mechanisms beat memory: explicit claim IDs, source pointers, review gates.
- Don't over-constrain the model into rigid prompts (the MIA failure) — give it
  room to reason, then verify against the evidence pack.

## Ask When

- The decision is high-stakes and key claims remain unverified — surface the
  open uncertainties rather than presenting a confident-looking dossier.
