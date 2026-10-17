---
name: api-design
description: "Design, change, or review an API contract: an HTTP API or an MCP server's tool surface. Use when adding or reshaping endpoints, tools, params, or response fields, when a diff touches a public contract, or on 'review this API/spec/tool schema'."
---

# API design

An API is a **contract** with consumers you cannot see or update. Every rule below protects that contract or makes it easy to adopt. A good API is boring: a consumer can guess how it works before reading the docs, so reach for the conventional shape (REST, JSON, plain nouns) over a clever one.

An **MCP tool surface** is an API whose consumer is an agent. Tool names, parameter schemas, and result shapes are the contract; agent prompts, configs, and other people's skills depend on them the way scripts depend on endpoints. Each rule says where MCP differs.

## The rules

1. **Never break userspace.** Adding a field, an optional param, or a new tool is safe; consumers ignore what they don't know. Removing, renaming, retyping, or moving one breaks them: `user.address` → `user.details.address` is a break, however much neater. Keep the awkward name (HTTP still spells it `referer`). Versioning is the last resort, because every version multiplies maintenance per endpoint and translation layers leak into core code. For MCP, a renamed tool or param silently breaks every prompt that named it; add the new one beside the old.
2. **Model the product's resources, not your internals.** The API mirrors the product's nouns. A storage quirk (comments as a linked list) or a background job (a `fetch_job` endpoint the consumer must poll) that leaks into the shape makes every consumer learn your implementation. When the resource model itself is awkward, the fix is in the product, and the API inherits it.
3. **Offer a long-lived API key.** Many consumers are not engineers (a PM with a script, a student, an ops person), and an OAuth dance loses them. Offer OAuth alongside, never as the only door. For MCP, remote servers take OAuth; also accept a key through an env var or header so local and scripted use works.
4. **Make retries safe.** A 4xx validation error means nothing happened; a 5xx or a timeout means the outcome is unknown. Write actions accept an optional **idempotency key**: the server records each key with its result and replays the result on a repeat instead of acting twice. A key/value store with expiry is enough, except where money moves and the key write must be atomic with the action. Reads and delete-by-ID are already idempotent. Keep the key optional so adoption stays easy. For MCP, agents retry relentlessly; a write tool's error says plainly whether the action happened.
5. **Rate limit every endpoint.** UI users act at click speed; API consumers act at code speed and will poll in a tight loop, bulk-import with no backoff, or turn a notification fan-out into a chat app. Tighter limits on expensive operations, `Retry-After` and remaining-quota headers on every response, and a per-consumer kill switch for incidents.
6. **Paginate any list that can grow, by cursor.** Offset pagination (`page=40`) makes the database count through every skipped row and slows with depth; a cursor (`WHERE id > :cursor ORDER BY id LIMIT n`) stays fast. Switching later is a breaking change, so choose cursor up front for anything unbounded. Every list response carries `next_cursor`, null on the last page. Offset is fine for a list that stays small.
7. **Make expensive fields opt-in.** A field that costs a join, a second service call, or a large payload is off by default and requested through `include=subscription` or an `includes` array. GraphQL generalises this at a high price (hard for non-engineers, hard to cache, fiddly to implement); reach for it only when `includes` clearly can't express the need. For MCP, result size is the agent's context window: return a compact default, and put verbose detail behind a param or a follow-up tool.
8. **Internal APIs relax rules 1 and 3, never 4.** With a few known consumers you can ship the fix to each one alongside a break, and require stronger auth. Retries and duplicates still cause incidents, so key operations keep idempotency.

## Designing

Before writing an endpoint or tool, write down its contract: the resource it acts on, the request and response shape, which fields are expensive, whether it writes, and whether its list can grow. Run the shape against every rule; a rule that doesn't apply gets one line saying why. Done when each rule is either reflected in the shape or marked not applicable.

## Reviewing

For a diff, a spec, or a tool schema:

1. Diff the contract, not the code. The contract is both sides of every endpoint and tool: what it accepts and what it returns, including how much it returns. List every added, removed, renamed, retyped, or moved field, param, endpoint, and tool, and every change in what a result contains, how it is shaped, or how much of it comes back. Read the old shape from `git show <base>:<path>` or the previous spec.
2. Check every contract change against rule 1. Then check every endpoint and tool, changed or not, against each of rules 2 through 8.
3. For a break, run `blast-radius` to find who depends on the old shape.

Rank each finding by its consequence for consumers:

- **Critical:** a break in a public contract, or a retry that duplicates or corrupts trusted state (a payment, an audit trail, a record other systems read).
- **Important:** a retry that only duplicates untrusted or reviewable state, a missing rate limit, a growing list with no cursor, or an expensive field on by default.
- **Minor:** the rest.

Each finding names the rule, the `file:line`, the consumer it hurts, and the fix. Done when every contract change from step 1 has a finding or is listed as cleared, and every endpoint and tool has been checked against every rule.

---

Distilled from Sean Goedecke, [Everything I know about good API design](https://www.seangoedecke.com/good-api-design/). The MCP translations are mine.
