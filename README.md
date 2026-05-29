# `~/.agents/skills` — canonical agent skills

Single source of truth for agent skills, shared across **Claude Code, Codex, and
OpenCode**. One copy per skill lives here; the tools find them as follows:

| Tool | How it reads this folder |
| --- | --- |
| **Codex** | reads `~/.agents/skills` natively (follows symlinks) — no config |
| **OpenCode** | reads `~/.agents/skills` natively — no config |
| **Claude Code** | only reads `~/.claude/skills`, so each skill is **symlinked** there: `~/.claude/skills/<name> → ../../.agents/skills/<name>` |

This matches the [Agent Skills open standard](https://agentskills.io); `.agents/skills`
is the convention all three converged on (the old per-tool dirs — `~/.codex/skills`,
`~/.config/opencode/skill` — are no longer read and were removed).

## Authored skills (tracked in this git repo)

`backend-developer`, `brainstorming`, `code-simplifier`, `design-principles`,
`frontend-design`, `product-builder`, `prompt-engineering`, `skill-creator`,
`software-architecture`, `subagent-driven-development`, `ui-designer`, `vc-market-sizing`.

Edit the `SKILL.md` here → all three tools pick it up. Keep wording **tool-neutral**
(say "you", not "Claude"; don't reference tool-specific features like TodoWrite) so a
skill stays portable across agents.

## Third-party skills (NOT tracked — see `.gitignore`)

Managed by the [`skills` CLI](https://github.com/vercel-labs/skills) or app bundles and
recorded in `.skill-lock.json`. Reproduce on a new machine with:

```sh
npx skills add nextlevelbuilder/ui-ux-pro-max-skill -a claude-code   # ui-ux-pro-max
npx skills add vercel-labs/skills -a claude-code                     # find-skills
npx skills add remotion-dev/skills -a claude-code                    # remotion-best-practices
# cua-driver: provided by CuaDriver.app (symlink into /Applications)
```

The `skills` CLI installs into `~/.agents/skills` and symlinks into each agent dir.

## Add a Claude symlink for a new skill

```sh
ln -s ../../.agents/skills/<name> ~/.claude/skills/<name>
```

(Codex and OpenCode need nothing — they read this folder directly.)
