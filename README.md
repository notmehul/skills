# skills

The agent skills I actually use, in one folder, shared across **Claude Code, Codex and OpenCode**.

A skill is a folder with a `SKILL.md` in it. The frontmatter says what the skill is and when to reach for it; the agent loads the body only when that description matches what you asked for. The format is the [Agent Skills open standard](https://agentskills.io), so the same folder works in every tool that reads it.

I keep one copy of each skill here rather than one per tool, because three drifting copies of the same instructions is worse than none.

## Install

```sh
git clone https://github.com/notmehul/skills.git ~/.agents
```

| Tool | What it needs |
| --- | --- |
| **Codex** | nothing; it reads `~/.agents/skills` and follows symlinks |
| **OpenCode** | nothing; it reads `~/.agents/skills` |
| **Claude Code** | reads `~/.claude/skills`, so symlink each skill in |

```sh
for d in ~/.agents/skills/*/; do
  ln -s "../../.agents/skills/$(basename "$d")" ~/.claude/skills/"$(basename "$d")"
done
```

Take the ones you want instead of all of them. They are independent folders, except where a skill names another by name in its text.

## The skills

**Writing**

| Skill | For |
| --- | --- |
| `unslop` | Cut the AI tells out of a draft. Runs on everything. |
| `elements-of-style` | Strunk and White, applied to a piece of prose. |
| `writing-for-agents` | Write a skill, an `AGENTS.md` or a `CLAUDE.md` that an agent follows the same way every run. |
| `git-release` | Commit messages, PR descriptions, changelog entries. |
| `resume-builder` | Write or tailor a CV. Content only, no layout. |
| `mehul-voice` | My own voice. Useful as a worked example of how to build one for yourself. |

**Building and shipping**

| Skill | For |
| --- | --- |
| `diagnosing-bugs` | Build the failing loop before theorising about the cause. |
| `blast-radius` | Find what a change breaks outside its own diff. |
| `prove-it-works` | Check the real artifact before saying done. |
| `create-verification-skill` | Generate a project-local skill that drives your app the way a user does. |
| `interrogate` | Adversarial multi-model review of a diff. |
| `grilling` | Interview me to a settled design, one round at a time. |
| `show-me-your-work` | A decision trail you can read the morning after an unattended run. |
| `ship-check` | Catch the mid-project pivot that is really an escape hatch. |
| `wizard` | Generate a bash wizard for the steps only a human can do. |
| `skill-creator` | Scaffold a skill and run evals on whether it triggers. |

**Design and media**

| Skill | For |
| --- | --- |
| `ui-ux` | Front door for any UI work: style direction, palette, type pairing, stack conventions. |
| `design-principles` | The restrained end: spacing scale, type ramp, dashboards. |
| `frontend-design` | The bolder end: work that reads as intentional, not templated. |
| `tufte-viz` | Charts, against Tufte's principles. |
| `generate` | Raster images through Codex CLI's imagegen. |
| `remotion-best-practices` | Remotion videos in React, with a beat sheet before any code. |

**Going to market**

| Skill | For |
| --- | --- |
| `product-marketing` | Write the positioning doc at `docs/positioning.md`. |
| `customer-research` | Interviews, surveys and public mining that can disconfirm the idea. |
| `content-strategy` | Research-led content built around an artifact people keep. |
| `cold-email` | One hook, one proof, one ask. |
| `launch` | The readiness gate, launch day, the week after. |
| `pitch-builder` | Build a pitch, on the Pitch Anything frame. |
| `pitch-review` | Audit one. |
| `frame-control` | Handle pushback in the room, after sorting a frame move from a real constraint. |
| `relationship-brief` | Brief yourself on one person before you talk to them. |
| `mi-os` | Turn a pitch or a market into testable claims and a sourced evidence pack. |

## Skills that expect my machine

Some of these read local context that you will not have:

- `mehul-voice`, `mi-os`, `relationship-brief`, `design-principles`, `frontend-design` and `frame-control` point at [Marshmallow](https://github.com/notmehul/marshmallow) under `~/.marshmallow/`. Without it, they degrade to the written guidance, which still works.
- `generate` shells out to Codex CLI.
- `ui-ux` and `skill-creator` carry scripts and data files alongside `SKILL.md`; clone the whole folder, not just the markdown.

Two skills are missing from this repo on purpose. My `lead-finder` and `warm-path-finder` forks name real people and carry relationship data, so they stay on my machine.

## Forks of synced skills

Skills synced from a claude.ai account land in `~/.claude/skills/synced/` and appear as `anthropic-skills:<name>`. That copy is online and belongs to the account, so editing it locally is pointless: the next sync overwrites it. When one needs a local change:

1. Copy it into `skills/<same name>/`, record `metadata.forked-from` (skill id and `updatedAt`), and edit only the copy.
2. Symlink it into `~/.claude/skills/`. The local skill wins `/<name>`.
3. Hide the synced twin with `"skillOverrides": {"anthropic-skills:<name>": "off"}` in `~/.claude/settings.json`, so the model is not choosing between two competing descriptions. (Tested 2026-09-19 on Claude Code v2.1.278.)
4. Upstream changes do not arrive on their own. Diff the synced copy against the fork by hand.

In this repo, `unslop` is such a fork.

## Installed from elsewhere

These are managed by the [`skills` CLI](https://github.com/vercel-labs/skills) or by an app bundle, so they are not tracked here:

```sh
npx skills add nextlevelbuilder/ui-ux-pro-max-skill -a claude-code   # ui-ux-pro-max
npx skills add vercel-labs/skills -a claude-code                     # find-skills
# cua-driver: provided by CuaDriver.app (symlink into /Applications)
```

## Provenance and licence

Mine, under the MIT licence in [LICENSE](LICENSE): `blast-radius`, `cold-email`, `content-strategy`, `create-verification-skill`, `customer-research`, `diagnosing-bugs`, `git-release`, `grilling`, `generate`, `launch`, `mehul-voice`, `mi-os`, `product-marketing`, `prove-it-works`, `relationship-brief`, `ship-check`, `show-me-your-work`, `unslop`, `wizard`, `writing-for-agents`.

The rest came from other people and keep their own terms. Where I changed one, the change is mine and the original is theirs:

| Skill | From | Licence |
| --- | --- | --- |
| `elements-of-style`, `pitch-builder`, `pitch-review`, `frame-control` | [alexanderSolod/skill-library](https://github.com/alexanderSolod/skill-library) | MIT |
| `ui-ux` | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill): their database, with the description rewritten to route into the rest of the design skills and a checklist added for public web pages | MIT |
| `resume-builder` | [dabydat/resume-builder-skill](https://github.com/dabydat/resume-builder-skill), rewritten for harnesses: content guidance only | MIT |
| `tufte-viz` | gist `aparente/e48c353755958621b3c0004593105a90` | as published |
| `remotion-best-practices` | [remotion-dev/skills](https://github.com/remotion-dev/skills), forked to add a beat sheet and a hook test | as published |
| `skill-creator` | Anthropic | as published |
| `product-marketing`, `cold-email`, `content-strategy`, `launch`, `customer-research`, and parts of several others | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | MIT, see [NOTICE-marketingskills.md](NOTICE-marketingskills.md) |

If something here is yours and the attribution is wrong, open an issue and I will fix it.
