---
name: knowledge-and-extraction
description: "Answer from documents or extract typed fields: is a knowledge base the answer, which retrieval route, extraction from KYC and income documents, agent memory. Use on 'build a knowledge base', RAG, document extraction, or 'answer from our docs'."
license: MIT
metadata:
  version: "1"
  updated: "2026-10-18"
  harnesses: "claude-code codex opencode"
  source: "research-2026-10/knowledge-and-data-agents.md C, D1-D3, D8, D9, D12 (Oct 2026)"
---

# Knowledge and extraction

The retrieval question became a routing question in 2026. An agent that can grep a folder of Markdown beats a hybrid index on a small corpus (a filesystem agent scored 8.4 correctness to hybrid RAG's 6.4 on five papers in a Jan 2026 benchmark, and lost that edge at 100 and 1,000 documents), live systems want a tool call rather than a copy, and a question over tables is a query, not retrieval. So the work starts with five questions, and an index is what you build when every one of them says no. Extraction follows the same discipline: constrained decoding guarantees the shape, so the effort goes into semantic checks and a per-field accuracy number.

## Steps

1. **Run the pre-flight** under that heading. Done when each of the five questions has an answer and the route it implies.
2. **Route retrieval** with the rule under "Routing". Done when the route and the trigger that would flip it are written down.
3. **Build the index only on that route.** Read `references/knowledge-base.md` for the build checklist and parser selection. Done when the 50-query eval is frozen as a regression suite and recall@10 is reported with and without the reranker.
4. **Extract typed data** with the procedure under "Structured extraction". Done when per-field accuracy on 50 gold documents is reported and the worst field is named.
5. **Give the agent memory** with the procedure under "Memory as files" when the work spans sessions. Done when the memory directory exists, reference material is read-only, and the untrusted-input path cannot write it.

## Pre-flight

1. Could the agent answer this by reading 20 files or fewer directly? → no knowledge base.
2. Is the question really a query over tables ("how many", "which applicants", "trend since")? → `data-analysis`, not retrieval.
3. Does the source change faster than you would re-index (CRM, tickets, calendar)? → a live tool call.
4. Is it "how we do things"? → a skill or SOP file loaded on demand.
5. Does the user need the page citation? → native PDF input plus citations before any chunking.

Only when all five are no does the index get built.

## Routing

```
Answer in order:
1. Who consumes the answer?  agent in the background, able to iterate | human waiting in a UI
2. Corpus size now and in 12 months: documents and total tokens
3. Freshness: static | daily | live system of record
4. Question shape: lookup or explain | aggregate or compare | procedural

Route:
- live system of record              → tool or MCP call against the source; no copy
- aggregate or compare on tables     → DuckDB or warehouse plus a guide file (data-analysis)
- procedural                         → SKILL.md or SOP file loaded on demand
- agent consumer AND under ~1K docs  → parse to Markdown on disk; grep and read tools; no index
- human consumer OR over ~1K docs    → hybrid index (BM25 plus dense, RRF) plus reranker
- one long PDF, Q&A with citations   → native PDF input plus citations (600 pages or fewer)
Record the decision and the trigger that would flip it.
```

Below about 1K documents or about 2M tokens, parse to Markdown and let the agent read; the route works identically in every harness and costs no infrastructure. Add the index when the corpus crosses that line, a UI user waits on the answer, or p95 latency matters. Every current Claude model takes 1M tokens of context, as of Oct 2026, and quality still degrades with input length (the context-rot finding stands), so long context is a route for one document, never a substitute for routing.

## Structured extraction

Running example: a salaried home-loan applicant's three salary slips, six months of bank statements, and a masked PAN.

1. **Define the typed model** with a description on every field (`gross_pay`, `net_pay`, `employer_name`, `pay_month`, `statement_period_start`, `salary_credit_dates[]`). Keep numeric and length constraints on the model; the SDK moves them into descriptions and re-validates locally.
2. **Avoid what the grammar rejects**: recursion, `minItems` above 1, external `$ref`, lookaround regex. Flatten nesting; prefer string enums.
3. **Call the provider's constrained-decoding parse** into the model. Check the stop reason before the content: truncated → retry with a higher output cap; refused → read the refusal, never retry blindly.
4. **Semantic validators on the model**: sums reconcile (gross minus deductions equals net), dates are ordered (statement start before end, pay months consecutive), identifiers pass a format check and exist in a lookup where one exists, and the salary credits in the statement match the slips' net pay within a tolerance you set. On failure, one retry that includes the validator message; after that, route the document to a review queue. The extracted record is a proposal until a human confirms it, and every retry and queue hand-off writes an event row (`building-agents`).
5. **Compare enum values case-insensitively.**
6. **Score it**: 50 documents with gold JSON; field-level exact or normalised match; per-field accuracy tracked over time. The bad field is usually one table column; fix the parser or the field description before touching the model.
7. **Long documents**: parse, split by section, extract per section with `section_path` carried through, merge with a deterministic reducer. One call never extracts 300 line items from 80 pages.
8. **Cache the schema**: the first call compiles a grammar that stays cached for 24 hours; keep the tool set constant between calls or the cache is lost.

Provider notes as of Oct 2026: on the Claude API the call is `client.messages.parse(output_format=Model)` with `output_config.format` underneath; `stop_reason` of `max_tokens` means truncated JSON and a `reasoning_extraction` refusal means a field asked for chain-of-thought, so ask for a one-sentence rationale instead. For provider-neutral code use Instructor's `from_provider(...)` with `max_retries=1`. Route bulk extraction to the cheap tier (Haiku 5.5 bills about 40 times less than Opus 5.5 on input) and keep the frontier tier for the judgement calls.

## Memory as files

Four vendors converged on the same shape in 2026: a directory of small Markdown files the agent reads at session start and edits as it works. It is auditable, portable across harnesses, and needs no service.

1. **Directory, not database**: `memory/user.md` (role, preferences), `memory/project.md` (current work, deadlines, decisions), `memory/feedback.md` (corrections, confirmed approaches), `memory/reference.md` (where things live). Cap each at about 200 lines; the agent consolidates when a file exceeds it.
2. **Session start**: read the directory listing, then only the files relevant to the task. **Session end**: update `project.md` with done and next; log decisions with absolute dates, never "next week".
3. **Reference material the agent must not change** sits read-only: a separate `kb/` path the memory handler rejects writes to, or a read-only mount where the runtime offers one.
4. **No secrets or raw personal data in memory**; the handler strips them. Every path is validated to stay under the memory root.
5. **Untrusted input cannot write durable memory without review.** When a session processes web pages, emails or tool output, memory writes go to a proposed file a human approves, or the store is read-only for that session. A writable store under untrusted input is a persistence channel for prompt injection.
6. **Periodic consolidation**: a scheduled job merges duplicates, removes stale entries and writes a new consolidated set; keep the old one for 30 days.
7. **Graph memory** earns its place only when questions are explicitly temporal or relational ("who owned this account before March"). Treat every memory vendor's benchmark as marketing.

### Claude Code and the Claude API

In Claude Code, auto memory plus a `CLAUDE.md` under 200 lines covers steps 1 and 2; run `/doctor prompt-audit` monthly to find stale or conflicting instructions. On the Claude API the memory tool (`memory_20250818`, GA) issues file operations under `/memories` against a handler you write, which is where steps 3 to 5 are enforced; pair it with compaction for long sessions.

## Output

- The pre-flight answers and the route, with the trigger that would flip it.
- For an index: the parsed corpus with page and heading metadata, the index, the frozen 50-query eval with recall@10 and precision@5, and the reranker decision with numbers.
- For extraction: the typed model with validators, the review-queue path, and the per-field accuracy report on 50 gold documents.
- For memory: the `memory/` directory, the read-only reference path, and the proposed-writes path for untrusted sessions.

What takes over: `llm-evals` for the eval set, the judge on generated answers and the regression gate; `data-analysis` when the question is a query over tables; `api-design` when the corpus or the extractor is exposed as an MCP server; `building-agents` for the event row and the confirm step around any write; `lending-domain` for the field lists and cross-checks of each Indian loan document.
