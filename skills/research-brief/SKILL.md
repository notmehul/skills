---
name: research-brief
description: "Research a question against dated sources: 'research X', 'what's the state of', a market or vendor comparison, 'what does the literature say', related work or a reading list, anything that needs citations."
license: MIT
metadata:
  version: "1"
  updated: "2026-10-18"
  harnesses: "claude-code codex opencode"
  source: "research-2026-10/knowledge-and-data-agents.md A6, D10 (Oct 2026); research-2026-10/human-centred-ai-research.md D5 (Oct 2026)"
---

# Research brief

Search results for any technical topic are now dominated by SEO round-ups ("best X in 2026") that contradict each other on dates, licences and prices. A brief treats them as leads and rests every claim on a primary source with a date. The shape every research product converged on by Oct 2026 is an orchestrator, parallel searchers and a synthesiser, with three refinements worth copying: a plan review before spend, structured output with a citation per field, and a budget with a stop condition.

## Steps

1. **Scope in writing before any search.** Six lines: the question, the decision it informs, the audience, the time window, the facts needed, and the sources required per claim. Show the plan and take one round of review when the spend will exceed a few dollars. Done when all six lines are filled and the reviewer has said go, or the spend is trivial and you say so.
2. **Pick the branch.** Related work, citations, a reading list or the literature section of a paper: read `references/literature-review.md` and follow it; the source hierarchy, the conflict rule and the graders below still apply. Everything else continues here.
3. **Fan out.** Split the question into 3 to 6 sub-questions. Each gets a searcher brief: the sub-question, a source-type preference (primary docs, filings, changelogs, papers), a cap on tool calls, and the stop rule under "Budget and stop". Dispatch a subagent per sub-question where the harness offers one; otherwise run them in sequence. Done when every sub-question has a brief and a budget.
4. **Search and read against the source hierarchy.** Open the primary source for every number, date, price and version; the round-up only tells you where to look. Done when every claim in the notes carries a source with a date, or a `(secondary)` or `UNVERIFIED` tag.
5. **Resolve conflicts** with the rule under "Conflict handling". Done when no claim averages two sources.
6. **Synthesise** into the shape under "The brief". Lead with the answer and what changed; then evidence; then open gaps. Date every claim. Done when every section has content or an explicit "nothing found".
7. **Grade the draft** with the four graders. Done when each grader passes or its failure is written into the open gaps.
8. **Hand back** the file on disk and a summary under 300 words in chat.

## Source hierarchy

Primary (official docs, changelogs, filings, papers, repos) over reputable press, over vendor blogs, over SEO round-ups. Every number and date traces to a primary source or carries `(secondary)`. A vendor's own benchmark is a vendor claim; say so.

### UNVERIFIED discipline

A claim you could not confirm against a primary source is written down and tagged `UNVERIFIED`, never dropped and never smoothed into a confident sentence. The reader decides what to do with it; silence takes that decision away from them. Time-bound facts (prices, deadlines, model names) carry "as of <month year>" and "re-check before quoting".

### Conflict handling

When two sources disagree, record both with their dates, prefer the newer primary, and never average. A conflict between two secondaries with no primary in sight is itself an `UNVERIFIED` finding.

## Budget and stop

Cap tool calls per searcher in its brief, with a number agreed at scoping. A searcher stops when the last two searches added no new primary source, or when its cap is reached, whichever comes first. The orchestrator stops the fan-out when every scoped sub-question is answered or marked open.

## Tools, as of Oct 2026

Pick by fit. Public benchmarks disagree about which search API is best (one found four of them statistically indistinguishable), so fit beats leaderboard. Re-check endpoints before building on them; several in this table changed or retired between Feb and Sep 2026.

| Need | Tool | Notes |
| :--- | :--- | :--- |
| Discovery | Exa search | `type: "instant"` for fresh results, `type: "deep-reasoning"` for hard questions; the `/research` endpoint retired 1 Apr 2026; a `publication` category covers over 350M papers |
| Extraction, PDFs, Office files | Firecrawl `/parse` and scrape | Returns markdown; `/agent` runs the fan-out for you with parallel searchers |
| Structured fields with a citation per field | Parallel Task API | Processors `lite` to `ultra8x`; `pro` takes about 10 minutes and the `ultra` tiers up to 2 hours, so use webhooks; its accuracy numbers are vendor claims |
| Fast prototyping | Tavily | Easiest to wire; middling on agentic-search benchmarks `(secondary)` |
| A finished answer with citations | Perplexity Agent API | Routes to third-party frontier models under presets; Sonar migrated here Jul 2026 |
| Papers | Semantic Scholar and OpenAlex APIs | Free; see `references/literature-review.md` |

Harness-native web search and fetch are enough for a brief under a few dollars. Reach for the APIs when the fan-out needs budgets, structured output, or more than a few dozen pages.

## The brief

A file on disk with five sections, in this order. The research briefs this skill was distilled from use this shape.

1. **State**: the state of play inside the time window, by sub-question, every claim dated.
2. **Changed**: what moved since the previous brief or the window start. This is the section readers act on; keep it separate from State.
3. **Defaults**: the lean choices this reader should make, with the reason for each.
4. **Actions**: procedures, checklists and decision rules the reader can lift as they are.
5. **Sources with dates**: one line per source, with the date fetched and the claim it supports.

Open the file with a conventions block: what `(secondary)` and `UNVERIFIED` mean here, and where the search budget ran short.

## The four graders

Run before delivery, in this order. A failure is written into the open gaps, never fixed by deleting the claim.

| Grader | Passes when |
| :--- | :--- |
| Groundedness | Every claim has a source line |
| Coverage | Every scoped sub-question is answered or marked open |
| Source quality | No claim rests only on a round-up or a vendor benchmark |
| Recency | Nothing older than the window without a stated reason |

## Output

- The brief on disk (State / Changed / Defaults / Actions / Sources with dates), with its conventions block.
- A summary under 300 words in chat: the answer, what changed, the open gaps.
- The list of `UNVERIFIED` claims, so the reader can decide which to chase.

What takes over: `unslop` on the prose before it ships; `mehul-voice` when the brief goes out under the user's name; `use-case-discovery` when the question was really "where does AI belong in this process"; `customer-research` when the open gaps are about what users think, which sources cannot answer; `study-design` when an open gap needs an experiment.
