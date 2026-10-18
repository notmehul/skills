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
| **Codex** | nothing; it reads `$HOME/.agents/skills` and follows symlinks. The skill listing gets 2% of the context window by default, so with a library this size set `[skills] max_context_tokens = 10000` in `~/.codex/config.toml` or it shortens descriptions silently |
| **OpenCode** | nothing; it reads `~/.agents/skills`. It also reads `~/.claude/skills`, so with the symlinks below it sees each skill twice; on OpenCode 2.0.29 or later set `OPENCODE_DISABLE_CLAUDE_CODE_SKILLS=1` |
| **Claude Code** | reads `~/.claude/skills`, so symlink each skill in |

```sh
for d in ~/.agents/skills/*/; do
  ln -s "../../.agents/skills/$(basename "$d")" ~/.claude/skills/"$(basename "$d")"
done
```

Take the ones you want instead of all of them. They are independent folders, except where a skill names another by name in its text. One at a time: `npx skills add notmehul/skills -s <name>` or `gh skill install notmehul/skills` also work and record provenance.

New and edited descriptions stay at or under about 250 characters with the trigger first, because that is what the harness reads on every turn; the body loads only when the description matches. Older descriptions get trimmed as their skills are touched.

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
| `api-design` | Design or review an HTTP API or an MCP tool surface without breaking its consumers. |
| `prove-it-works` | Check the real artifact before saying done. |
| `verify` | The same, under the name Claude Code runs before each commit. |
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
| `pitching` | Build a pitch, review one, or handle the room, on the Pitch Anything frame. One skill, three branches. |
| `relationship-brief` | Brief yourself on one person before you talk to them. |
| `mia` | Market intelligence on an early-stage deal: one combined TAM, trends, competitors, founder claims checked, as an xlsx the analyst edits. |

**Business use cases to ML and agents**

Added Oct 2026 for a role that takes business use cases to models, agents and pilots. Each is distilled from a dated research brief; the examples use Indian home loans where a domain is needed.

| Skill | For |
| --- | --- |
| `use-case-discovery` | Shadow the operator, map and classify the workflow, score and gate candidates, write the one-page brief and eval spec. |
| `pilot-rollout` | Shadow, assisted, autonomous per action category, with gates, rollback triggers, a kill date and a handoff pack for a non-technical maintainer. |
| `ai-governance` | The system card, DPDP, an EU AI Act screen, vendor data terms, and the India finance-bot pre-flight. |
| `building-agents` | Runtime choice, proposal → confirm → execute, the event row, permissions, durability, when one agent is enough. |
| `llm-evals` | The afternoon eval loop, golden sets from traffic, judge calibration, agent trajectory checks, CI gates, red-teaming. |
| `applied-ml` | The prediction sentence, the baseline ladder, GBDT or tabular foundation model, split design, leakage, when to stop tuning. Forecasting, experiments and the stack as references. |
| `data-analysis` | The analytics guide file, a reliable text-to-SQL loop, assumptions logs, metric reconciliation, the decision table. |
| `knowledge-and-extraction` | Is a knowledge base the answer, which retrieval route, typed extraction from documents, memory as files. |
| `research-brief` | A dated, sourced brief with an UNVERIFIED discipline; literature review as a branch. |
| `conversation-design` | A chatbot or voice flow for high-intent Indian consumers in a regulated setting. |
| `lending-domain` | The Indian home-loan journey, its data, documents, economics, and what works in production. |
| `study-design` | A small, rigorous human-AI study: design checklist, preregistration, measurement, analysis, venue. |

## Skills that expect my machine

Some of these read local context that you will not have:

- `mehul-voice`, `relationship-brief`, `design-principles`, `frontend-design`, `git-release`, `grilling`, `pitching`, `tufte-viz` and `ui-ux` point at [Marshmallow](https://github.com/notmehul/marshmallow) under `~/.marshmallow/`. Without it, they degrade to the written guidance, which still works.
- The twelve business-to-ML skills cite research briefs under `research-2026-10/`, which is local and gitignored because the briefs quote named people and company figures. The skills themselves carry everything an agent needs.
- `generate` shells out to Codex CLI.
- `mia` is Claude Code only: it dispatches research subagents, and its file paths use `${CLAUDE_SKILL_DIR}`, which no other harness expands. It renders its workbook with Python and openpyxl, installed on first use by `scripts/setup.sh`.
- `ui-ux`, `skill-creator` and `mia` carry scripts and data files alongside `SKILL.md`; clone the whole folder, not just the markdown. `ui-ux` is a tracked, modified copy of its upstream (the provenance table has the source).

### Grok Bot / harness (synced from shared workflows)

| Skill | For |
| --- | --- |
| `assets-visual-taste` | Visual taste brief for covers and post graphics (Pinterest-derived). |
| `fill-biome-build-with-us-form` | Fill Biome's full-time Build With Us form; stop before submit. |
| `send-email-via-computer` | Send mail via browser Gmail only — never a mail API. |
| `studio-context` | Load the public-studio Notion brief before drafting or publishing. |

Two skills are missing from this repo on purpose. My `lead-finder` and `warm-path-finder` forks name real people and carry relationship data, so they stay on my machine.

## Forks of synced skills

Skills synced from a claude.ai account land in `~/.claude/skills/synced/` and appear as `anthropic-skills:<name>`. That copy is online and belongs to the account, so editing it locally is pointless: the next sync overwrites it. When one needs a local change:

1. Copy it into `skills/<same name>/`, record `metadata.forked-from` (skill id and `updatedAt`), and edit only the copy.
2. Symlink it into `~/.claude/skills/`. The local skill wins `/<name>`.
3. Hide the synced twin so the model is not choosing between two competing descriptions: open `/skills` in Claude Code, highlight the synced copy, press Space until it reads `off`, then Esc. That writes a `skillOverrides` entry to `.claude/settings.local.json` under whatever key Claude Code uses for the synced skill. (As of Oct 2026 the overrides had not been applied on this machine; the step is the fix.)
4. Upstream changes do not arrive on their own. Diff the synced copy against the fork by hand.

In this repo, `unslop` is such a fork.

## Installed from elsewhere

These are managed by the [`skills` CLI](https://github.com/vercel-labs/skills) or by an app bundle, so they are not tracked here:

```sh
npx skills add vercel-labs/skills -a claude-code                     # find-skills
npx skills add wheresryan22/anatomy -g -a claude-code -a codex -a cursor -a opencode   # anatomy: interactive isometric SVG figures (MIT)
# cua-driver: provided by CuaDriver.app (symlink into /Applications)
# sanity-best-practices, sanity-migration: Sanity's own skills, installed 29 Sep 2026 with the Sanity MCP; kept here so Claude Code's symlink is the only other copy
```

## Provenance and licence

Mine, under the MIT licence in [LICENSE](LICENSE): `blast-radius`, `cold-email`, `content-strategy`, `create-verification-skill`, `customer-research`, `diagnosing-bugs`, `git-release`, `grilling`, `generate`, `launch`, `mehul-voice`, `product-marketing`, `prove-it-works`, `verify`, `relationship-brief`, `ship-check`, `show-me-your-work`, `unslop`, `wizard`, `writing-for-agents`, and the twelve business-to-ML skills (`use-case-discovery`, `pilot-rollout`, `ai-governance`, `building-agents`, `llm-evals`, `applied-ml`, `data-analysis`, `knowledge-and-extraction`, `research-brief`, `conversation-design`, `lending-domain`, `study-design`), which distil public documentation, regulation and papers named in each skill's `metadata.source`; where a checklist shape was taken from another library it is credited there.

`mia` is mine too, but it lives in its own repo, [notmehul/mia](https://github.com/notmehul/mia), where it is a Claude Code plugin with tests and design docs. What is here is a copy of that plugin's `skills/mia/`, pinned in the footer of its `SKILL.md`. Change it there, not here.

The rest came from other people and keep their own terms. Where I changed one, the change is mine and the original is theirs:

| Skill | From | Licence |
| --- | --- | --- |
| `elements-of-style`, `pitching` (a merge of their `pitch-builder`, `pitch-review` and `frame-control`) | [alexanderSolod/skill-library](https://github.com/alexanderSolod/skill-library) | MIT |
| `ui-ux` | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill): their database, with the description rewritten to route into the rest of the design skills and a checklist added for public web pages | MIT |
| `resume-builder` | [dabydat/resume-builder-skill](https://github.com/dabydat/resume-builder-skill), rewritten for harnesses: content guidance only | MIT |
| `tufte-viz` | gist `aparente/e48c353755958621b3c0004593105a90` | as published |
| `remotion-best-practices` | [remotion-dev/skills](https://github.com/remotion-dev/skills), forked to add a beat sheet and a hook test | as published |
| `skill-creator` | Anthropic | as published |
| `api-design` | Sean Goedecke, [Everything I know about good API design](https://www.seangoedecke.com/good-api-design/): his rules in my wording, plus an MCP translation of each | ideas only, no text copied |
| `product-marketing`, `cold-email`, `content-strategy`, `launch`, `customer-research`, and parts of several others | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | MIT, see [NOTICE-marketingskills.md](NOTICE-marketingskills.md) |

If something here is yours and the attribution is wrong, open an issue and I will fix it.
