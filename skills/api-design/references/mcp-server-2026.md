# Writing an MCP server against the 2026-07-28 spec

The 28 Jul 2026 revision made the protocol stateless and deprecated several 2025 habits. Read this when the API you are designing or reviewing is an MCP server. Deprecated features have a 12-month window, so the earliest removal is the first revision on or after 28 Jul 2027; build new servers to the new shape now.

## Checklist

- [ ] Targets spec `2026-07-28` over Streamable HTTP. Stateless: no `initialize` handshake, no `Mcp-Session-Id`. Every request carries the protocol version and client capabilities in `_meta`; `Mcp-Method` and `Mcp-Name` headers go on every POST.
- [ ] Implements `server/discover`. `tools/list` returns a deterministic order and carries `ttlMs` and `cacheScope`, so clients and prompt caches stay stable.
- [ ] State that must survive across calls is an explicit server-minted handle the client passes back as a tool argument.
- [ ] Uses none of Sampling, Roots or Logging (all deprecated). Logs go to stderr or OpenTelemetry; `traceparent` from `_meta` is propagated.
- [ ] Asks the human for input through MRTR: the tool returns `resultType: "input_required"` with `inputRequests`, and the client retries with `inputResponses`. No side channel. Long jobs use the tasks extension (`io.modelcontextprotocol/tasks`, polled with `tasks/get`).
- [ ] Auth: OAuth with `iss` validation (RFC 9207); Client ID Metadata Documents instead of Dynamic Client Registration; credentials keyed by issuer. Also accepts a key through an env var or header for local and scripted use (rule 3).
- [ ] Tool descriptions are written for the model and tested by an agent: distinct names, explicit parameters, one to five `input_examples` for any non-obvious schema, and a line on when not to use the tool.
- [ ] Every tool accepts and propagates a business `case_id`, and emits a `tool_call` and `tool_result` pair to the event store, so vendor-side logs can be joined to business records.
- [ ] Side-effecting tools are `propose_*` tools whose output is a proposal id, unless the action class has been explicitly classed as audit-tier after an eval showed it reliable and reversible (`building-agents` owns that procedure). Read-only tools run freely and still log.
- [ ] Result size respects the agent's context: compact default, verbose detail behind a param or a follow-up tool (rule 7). Past about ten tools, expect clients to defer-load and search them, so each description has to stand alone.
- [ ] Validated with the official SDK's conformance tests. Published to the registry under a verified namespace only if public; the registry API is still pre-GA as of Oct 2026.

## Review

Diff the tool surface the way the main skill's review step diffs an endpoint: every tool, parameter, result field and `resultType` added, removed, renamed or retyped. A renamed tool or parameter breaks every prompt and skill that named it; add the new one beside the old (rule 1). Run each write tool twice with the same arguments and the recovery a client would try after an ambiguous error, and count what got written (rule 4).

Source: MCP specification changelog for 2026-07-28 and the Anthropic "Writing effective tools" guidance (Sep 2025), as read on 17 Oct 2026.
