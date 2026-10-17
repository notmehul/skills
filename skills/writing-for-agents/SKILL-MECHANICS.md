# Skill mechanics

The skill-specific branch of [`writing-for-agents`](SKILL.md): what changes when the document is a skill (frontmatter, the invocation choice, and router skills). Everything else about writing it is the universal reference in `SKILL.md`.

## Invocation

Two choices, trading the two loads:

- A **model-invoked** skill keeps a `description`, so the agent can fire it autonomously, and other skills can reach it. You can still type its name: model-invocation always _includes_ user reach; a description only ever adds agent discovery, never removes the human's. The description is the skill's top-level context pointer, forced to stay loaded at all times: permanent context load in exchange for discoverability. A model-invoked skill whose content is all reference is also one home for shared reference: another skill can invoke it, so reference needed by several skills lives in one place. Mechanics: omit `disable-model-invocation`, and write a model-facing description carrying the trigger branches (the pointer-writing rules in `SKILL.md` apply in full).
- A **user-invoked** skill strips the description from the agent's reach: only the human typing its name can invoke it, and no other skill can. Zero context load, but it spends cognitive load: you are the index that must remember it exists. Mechanics: set `disable-model-invocation: true`; the `description` becomes human-facing: a one-line summary, trigger lists stripped.

Pick model-invocation only when the agent must reach the skill on its own, or another skill must. If it only ever fires by hand, make it user-invoked and pay no context load.

Shared reference that two user-invoked skills both need can live in neither: with no descriptions, neither can fire the other. Push it to a plain file outside the skill system: external reference any skill can point at.

## Splitting by invocation

The invocation cut of splitting (the sequence cut lives in `SKILL.md`): split off a model-invoked skill when you have a distinct leading word that should trigger it on its own (a trigger word you actually use in your prompts), or another skill must reach it. You pay context load for the new always-loaded description, so that independent reach has to be worth it.

## Router skills

When user-invoked skills multiply past what you can remember, that piled-up cognitive load is cured by a **router skill**: one user-invoked skill that names the others and when to reach for each, so the human has one skill to remember instead of many. It can only hint, never fire them: user-invoked skills have no description, so nothing but the human can reach them.

## Portable skills

This library is read by Claude Code, Codex and OpenCode, so a skill's body uses nothing only one harness understands. The six fields the Agent Skills spec defines are `name`, `description`, `license`, `compatibility`, `metadata` (string to string) and `allowed-tools`. Claude-only keys (`disable-model-invocation`, `argument-hint`, `when_to_use`) are ignored elsewhere; Codex reads `agents/openai.yaml` (`policy.allow_implicit_invocation: false`) and OpenCode reads `metadata: {opencode/autoinvoke: "false"}` for the same intent, so a user-invoked skill sets all three. In the body: paths relative to the skill folder (never `${CLAUDE_SKILL_DIR}` or `/Users/...`), no `$ARGUMENTS`, no `!`-prefixed shell, no MCP tool names, and harness-specific commands under a heading that names the harness with a generic path first. Record `metadata.updated` (ISO date) and `metadata.source` for anything mined from elsewhere.

## The description budget

Codex gives the whole skill listing 2% of the context window (8,000 characters when the window is unknown; `skills.max_context_tokens` raises it to at most 10,000 tokens) and shortens or drops descriptions silently past that, so each description stays at or under 250 characters with the trigger clause first. Claude Code truncates each description at 1,536 characters instead. Either way the description names the branches that should trigger it and never summarises the workflow: an agent that reads a summary follows the summary and skips the body. Test a description with 20 phrasings, half of them near-misses that should not fire.

## Editing a skill

Run the scenario once without the change in a fresh context (a subagent where the harness has one), keep that transcript, then edit. The before-run is the evidence that the edit was needed and the baseline the after-run is judged against.
