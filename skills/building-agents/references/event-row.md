# The event row

One append-only table, written by the harness (hook or middleware), never by the model. Tool call, decision, approval, execution and result are separate rows linked by `run_id`, `proposal_id` and `case_id`. Dashboards and status tables are projections rebuilt from the log; the log is never updated in place.

## Schema

```
agent_events
  event_id        uuid, pk
  ts              timestamptz, server clock
  run_id          uuid            -- one agent run or session
  case_id         text            -- the business record this run serves (mandatory join key)
  parent_event_id uuid null       -- causal pointer
  actor           text            -- 'model:<name>', 'tool:<name>', 'human:<user_id>', 'system'
  kind            text            -- run_started | model_call | tool_call | tool_result |
                                  -- proposal | approval | rejection | execution_started |
                                  -- execution_result | execution_failed | policy_decision |
                                  -- fallback | budget_reached | handoff | compaction |
                                  -- run_finished | error
  tool            text null
  args            jsonb null      -- canonical, secrets redacted
  result          jsonb null      -- truncated, with a pointer to a blob when large
  risk_tier       text null
  proposal_id     uuid null
  idempotency_key text null
  decision_source text null       -- config | hook | user_permanent | user_temporary | user_reject | auto
  prompt_version  text null
  dataset_case_id text null       -- set when the run came from an eval
  tokens_in       int null
  tokens_out      int null
  cost_usd        numeric null
  trace_id        text null       -- OTel traceparent
  prev_hash       bytea null      -- optional SHA-256 chain for tamper evidence
```

## Rules

- The application role has no UPDATE or DELETE grant on the table.
- `case_id` is required on every tool call. Pass it as a header or in `_meta` on MCP calls so vendor-side logs can be joined later. A regulated-finance team reported that tool logs without the originating case id were fine for debugging and useless for audit (arXiv 2606.29142, as of Oct 2026).
- An `execution_*` row references a `proposal_id` whose latest decision is `approval`; enforce with a check constraint or a nightly query.
- A `fallback` row carries the reason and the model it fell back to.
- Redact credentials before the write. Large payloads go to object storage with a hash in the row. Store content pointers, not content, where traces hold personal data, so the table can outlive the trace retention window.
- Name columns after the OTel `gen_ai.*` conventions where one exists (`gen_ai.provider.name`, `gen_ai.request.model`, `gen_ai.usage.input_tokens`) so exports line up with any OTel backend. Those conventions are still marked Development as of Oct 2026 (semconv v1.42.0, Jun 2026); keep your own column names stable and map at export.

## Where the rows come from

Generic path: wrap every tool in a middleware that writes `tool_call` before and `tool_result` after; the proposal flow writes its own rows; the run loop writes `run_started`, `compaction`, `budget_reached` and `run_finished`.

| Runtime | Pause primitive for a proposal | Hook that writes the rows |
| :--- | :--- | :--- |
| Pydantic AI | Deferred tool | A capability with tool hooks wrapping every tool |
| OpenAI Agents SDK | `needs_approval` with `RunState` serialised to JSON | Run hooks; the `interruptions` list becomes `proposal` rows |
| LangGraph | `interrupt()` | Node wrappers; the node re-runs from the top on resume, so the code before the interrupt must be idempotent |
| Hosted harness | Server-side pause policy | Subscribe to the session event stream or webhooks and mirror rows, including budget and workflow-run events |

### Claude Code and the Claude Agent SDK

`PreToolUse` writes `tool_call` and `policy_decision` and can return `defer` to pause a headless run (the run exits with the pending tool payload and resumes by id). `PostToolUse` and `PostToolUseFailure` write `tool_result`. `PermissionRequest` writes `proposal` and can notify a reviewer. `SubagentStart`, `SubagentStop`, `PreCompact` and `PostCompact` write `handoff` and `compaction`. Interactive runs can gate through `canUseTool` instead of `defer`. Claude Code's own telemetry emits a `tool_decision` event with the same `decision_source` values as the column above.
