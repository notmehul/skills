# Checklists

Three lists for the branches that reach them: permissions before an unattended run, durability before a run that must survive restarts, and the browser agent when no API or MCP exists.

## Permission scoping for an unattended run

Distilled from Anthropic's auto-mode post (Mar 2026). Its classifier still missed 17% of over-eager actions, so the boundary is the sandbox and the allow list, never the classifier.

- [ ] The trust boundary is the current repo or project directory; anything outside is an exfiltration path unless configured.
- [ ] Broad allows are removed before the run: blanket shell, wildcard interpreters (`python *`, `node *`), package-manager run scripts.
- [ ] Allow rules name one command and its subcommand (`git status`, `jq`), never an interpreter or a shell.
- [ ] Read-only tools run free; in-repo edits run free because version control reviews them; everything else is gated.
- [ ] The gate judges the action and its arguments, never the agent's explanation.
- [ ] Tool output from the open web is untrusted. Readers of untrusted content get read-only tools; a separate privileged step acts on their structured summary.
- [ ] Denials return a reason to the agent. After 3 consecutive or 20 total denials the run stops and pages a human; a headless run terminates.
- [ ] Credentials never enter the sandbox or the model context; tools fetch them from a vault with a run-scoped token.
- [ ] Web fetch and search carry host allow lists; browser and computer use are high tier and approval gated.
- [ ] False positives (friction) and false negatives (misses) are measured separately on real runs, and the real over-eager examples grow into a regression set.

### Claude Code

Entering auto mode drops broad allow rules itself. Write the narrow rules as `Bash(git status:*)` or `Bash(jq:*)` in settings, or inside the skill's `allowed-tools` where the skill is Claude-only. The `tool_decision` telemetry event carries the source of every decision, which is what you audit for approval fatigue.

## Durable execution for an agent run

- [ ] Each model call and each tool call is its own step or activity; step results replay on resume instead of re-running.
- [ ] Downstream writes carry an idempotency key derived from `(run_id, step, canonical args)`.
- [ ] Human waits use the engine's wait primitive (DBOS `recv`, Temporal signal or update, LangGraph `interrupt`, Restate awakeable, Inngest `waitForEvent`) so the process can exit.
- [ ] Code before a wait is idempotent; LangGraph re-runs the node from the top on resume.
- [ ] Serialised state carries a version marker, so a deploy that changes agent definitions either loads old pending runs or fails loudly.
- [ ] Non-determinism (time, random, model calls) lives inside steps, never in workflow code.
- [ ] Retries have caps; exceeding the cap is a human-escalation event, never a loop.
- [ ] The resume path is tested by killing the process between approve and execute.

Engine choice as of Oct 2026 is an ops and licence question, since the main engines ship agent-SDK integrations: DBOS (MIT, a library on Postgres) first; Temporal (MIT) when you need signals across services, worker versioning or a team of operators; Hatchet (MIT, Postgres) if you want a dashboard out of the box. Restate (BSL) and Inngest (SSPL server) cost a licence review before anything else.

## Browser agent

Reach this only when the feasibility step found no API and no MCP server.

- [ ] Scoped to one site and one task, with an allowed-domain list set in the driver.
- [ ] A dedicated low-privilege login; never credentials to a money-moving account. Purchases, terms acceptance and cookie banners require confirmation.
- [ ] Page content is assumed to carry prompt injection: the goal lives in the system prompt and cannot be derived from the page; every action is logged; a screenshot is taken before and after each state-changing click.
- [ ] Discovered selectors and actions are cached so repeat runs are deterministic; the model is the fallback when the cached path breaks.
- [ ] A budget of steps and minutes per run; fail closed.
- [ ] Ten recorded tasks replayed weekly; expect the site to change.

Driver defaults as of Oct 2026: Browser Use (Python, MIT) for autonomous tasks in your own code; Stagehand only when the team is TypeScript (its standalone Python SDK was archived 1 Sep 2026; Python now goes through the API client).
