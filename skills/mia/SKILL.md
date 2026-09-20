---
name: mia
description: >
  Produces a market-intelligence workbook for an early-stage deal from the
  deal's own materials (Attio record, Fireflies transcripts, Drive documents)
  plus web research: one problem-anchored TAM, trends with headwinds, the
  competitors buyers actually pay for, the founder's claims checked, and the
  questions for the next call, as an xlsx the analyst edits before the
  partner check-in. Use when an analyst asks to run MI, size a market, map
  competitors, check founder claims, or start work on a new deal, or asks to
  add a feature matrix, public sentiment or a bottoms-up cross-check to an
  existing deal workspace.
argument-hint: "[company or deal slug] [basic|full] [add: features|sentiment|bottoms-up]"
allowed-tools: Read, Write, Edit, Grep, Glob, Bash, WebSearch, WebFetch, Agent
---

# MIA: market intelligence

## What the analyst gets

A workbook at `workspace/<slug>/output/<Company>_MI.xlsx` that reads in ten
minutes: a Summary with a six-bullet read, key numbers and two charts; a
Market size tab with one combined TAM, SAM and SOM and the basis for every
line; Trends with the forces that pass the company-specificity test;
Competitors organised by what buyers pay for today; Founder claims checked
one by one with the next-call questions; and a Sources tab. Every number
links to where it came from. The analyst edits it, then takes it to the
partner. Partners run it as a sense check before their own deeper work,
so the default run stays cheap and short.

The workbook is the deliverable. The conversation carries only questions
for the analyst and a short delivery note.

## How a run goes

1. **Workspace.** `workspace/<slug>/` with `brief.md`, `notes/`, `sheet/`,
   `output/`. The slug is the company name in lower-case hyphens. Reuse the
   workspace when the deal already has one; the analyst may be adding a tab.
2. **Intake** (this conversation). Read the deal's materials in the order
   in `references/intake.md`, write `brief.md`, then ask the analyst the
   baseline questions the materials left open, numbered, each with your
   recommended answer. Record the answers in the brief. This is the only
   step that asks a human anything.
3. **Research** (subagents, in parallel, one per thread). Default threads:
   market, trends, competitors, claims. Optional: features, sentiment,
   bottoms-up. Each subagent gets the prompt in the next section, writes
   `notes/<thread>.md`, and returns a summary under 300 words. Read the
   summaries; when one thread's note is missing or thin on what it was
   asked, re-dispatch that thread once with the gap named.
4. **Compose** (one subagent). It reads the brief, the notes,
   `references/compose.md`, `references/sheet-dialect.md` and the exemplar,
   writes `sheet/*.md`, runs the renderer, fixes what `checks.md` fails,
   and returns the path.
5. **Deliver.** One paragraph in chat: the workbook path, the questions for
   the next call, and what was searched for and not found. The analyst
   downloads the xlsx and adds it to the deal's Drive folder; Sheets keeps
   the charts on import.

Run the renderer yourself whenever the analyst edits a tab file and wants
the workbook rebuilt:

```
python3 ${CLAUDE_SKILL_DIR}/scripts/render_sheet.py workspace/<slug>
```

The first run on a machine installs openpyxl into `.venv`:
`bash ${CLAUDE_SKILL_DIR}/scripts/setup.sh`.

## Dispatching a research thread

Send each subagent a self-contained prompt built like this, with the
placeholders filled in:

```
You are researching the <thread> thread for the <Company> deal.

Read, in order:
- <workspace>/brief.md  (the deal brief; the analyst's answers are at the end)
- ${CLAUDE_SKILL_DIR}/references/research.md  (the common section, then the "<Thread>" section)
- ${CLAUDE_SKILL_DIR}/references/sources.md
- <workspace>/notes/  (any notes other threads have already written; cite them rather than repeat them)

Depth is <basic|full>: stop when the pattern stabilises, at about <15|30> sources.
Write your note to <workspace>/notes/<thread>.md in the shape research.md gives.
Then reply with a summary under 300 words: what you found, what you searched
for and did not find, and what you would ask the founder. Questions for the
analyst go in the note, not to me; I cannot relay them mid-run.
```

Dispatch every default thread in one message so they run concurrently. The
claims thread reads the other notes when they exist, so send it after the
first three return when the run is basic, or with them when speed matters
more than cross-referencing.

## Dispatching the composer

```
You are composing the workbook for the <Company> deal.

Read, in order:
- <workspace>/brief.md
- every file in <workspace>/notes/
- ${CLAUDE_SKILL_DIR}/references/compose.md
- ${CLAUDE_SKILL_DIR}/references/sheet-dialect.md
- ${CLAUDE_SKILL_DIR}/references/exemplar/  (a fictional deal showing shape and density)

Write one file per tab into <workspace>/sheet/ using the file names in
compose.md. Tabs in scope: <list>. Then run
  python3 ${CLAUDE_SKILL_DIR}/scripts/render_sheet.py <workspace>
read <workspace>/checks.md, fix every fail in the tab file it names, and
render again until the result is PASS. Reply with the workbook path, the
warnings you left in place and why, and anything in the notes you could not
place.
```

## Judgement calls

- The category anchor decides the comp set and the TAM. When the materials
  straddle two categories, ask at intake; the answer changes every tab.
- One TAM for the problem, with segments combined and overlaps deducted.
  Never a TAM per product.
- Status quo is a competitor on every deal. "What would the buyer do if
  this company did not exist" is the first row of the competitor table.
- Founder statements are claims until an independent source confirms them.
  The claims tab is where they are settled; the other tabs cite them as
  claims.
- Trends without headwinds have not looked hard enough. The strongest
  headwind is named and its power to break the thesis is stated.
- A blank cell with "searched, not found" beside it is correct output. A
  plausible number without a source is not.
- The sizing threshold is an indicator, not a figure: above $1B and growing
  at 10-20% or more is the question the Market size tab answers first.

## Stop when

- The workbook renders with checks at PASS, the delivery note is written,
  and the analyst has the path.
- The analyst asked for a subset (one tab, a re-render, an added tab) and
  that subset is done. Everything else stays untouched.

## Files

- `references/intake.md`: ingestion order, brief template, how to ask.
- `references/research.md`: the common brief and one section per thread.
- `references/compose.md`: tab-by-tab layout and writing rules.
- `references/sheet-dialect.md`: the markdown the renderer understands.
- `references/sources.md`: link format and the credibility model.
- `references/exemplar/`: a fictional deal in the dialect.
- `scripts/render_sheet.py`, `scripts/check_sheet.py`, `scripts/setup.sh`.

---

Vendored from [notmehul/mia](https://github.com/notmehul/mia) @ `e9699a4`, where
it lives as a Claude Code plugin with its tests and design docs. No local
changes: edit it there, then re-copy `skills/mia/` from that repo into this one.
