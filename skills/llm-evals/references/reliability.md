# Reliability: structured output, retries and fallbacks, personal data in traces

## Structured output

Generic rule: use the provider's constrained decoding for the final answer and strict schemas on tool arguments, parse into a typed model, then validate the content yourself. The shape is guaranteed; the content is not. Schema is shape, not truth: check in code that ids exist and amounts sit inside policy, and still treat the result as a proposal.

- Keep schemas flat: no recursion, no numeric or string-length constraints, `additionalProperties: false`, `minItems` of 0 or 1. The SDK moves unsupported constraints into field descriptions and validates them locally.
- Compare enum values case-insensitively. Mark everything `required` if field order matters.
- Keep chain-of-thought out of the schema; allow a short `rationale` string instead.

### Claude API, as of Oct 2026

- Final answer: `output_config.format = {type: "json_schema", schema}` (GA; the older `output_format` plus beta header is deprecated). Tool arguments: `strict: true`. In Python prefer `client.messages.parse(output_format=PydanticModel)` and read `response.parsed_output`.
- Forced `tool_choice` (`any` or a named tool) returns 400 on Opus 5.5, Sonnet 5.5 and Fable 5.1, and assistant prefill is gone on 4.6 and later. The old "force a tool call to get JSON" trick is over; use `output_config.format` or strict tools with `auto`.
- Handle `stop_reason == "refusal"` (billed, may be off-schema) and `stop_reason == "max_tokens"` (truncated JSON) explicitly; retry only the second, with a higher limit. A `reasoning_extraction` refusal means a field asked for chain-of-thought.
- The grammar compiles on first use and is cached 24 hours; changing the schema or the tool set between calls invalidates it along with the prompt cache.
- Limits per request: 20 strict tools, 24 optional parameters, 16 union-typed parameters. Native PDF input with citations is incompatible with `output_config.format`.

## Retry and fallback rules

- Classify first. 429, 5xx and timeouts → retry with exponential backoff and jitter, at most 3. 400 schema errors, auth errors and content refusals → no retry, route to a handler. `max_tokens` → one retry with a higher limit.
- The primary timeout is short enough to leave room for one fallback inside the user's latency budget.
- Fall back to a different provider only for the same capability class, and never silently downgrade a judged-quality path. Every fallback writes a `fallback` event row with the reason and the model.
- Cool a provider down after N consecutive failures. A 20-line dict does this for a solo builder; a proxy router does it when the routing table grows.
- The chain ends in a non-AI path: a cached answer, a rule result, or a queued item for a human. That last step is the proposal queue.

## Personal data in traces

- Content capture is off by default in every instrumentation (the OTel default, the Claude Code default, Codex `log_user_prompt=false`).
- Turn it on per field, not globally: mask by field name or path in the SDK export hook; whole-text scrubbing only where the structure is unknown.
- Fail closed: if the masker throws, drop the content and keep the metadata.
- Raw request and response bodies, when ever needed, go to a local directory with a 7-day lifecycle, never to the shared backend.
- Separate controls for what the trace store keeps and what the model provider sees; zero-data-retention eligibility differs per model and feature, so check it per model.
- Retention: traces 14 to 30 days with content; metrics and event rows indefinitely, with content pointers rather than content.
- Before a production transcript enters the golden set, run a personal-data evaluator and a human skim. For an Indian loan journey that means the applicant's name, PAN, account number and salary figures are masked before the case reaches the repo.
