# Changelog

Removals and merges are named here so nothing disappears silently. Format follows Keep a Changelog; dates are when the change was pushed.

## 2026-10-18

### Added

- Twelve skills for a business-use-case to ML and agents role, each distilled from a dated research brief (Oct 2026) and written to the portable-skill rules: `use-case-discovery`, `pilot-rollout`, `ai-governance`, `building-agents`, `llm-evals`, `applied-ml`, `data-analysis`, `knowledge-and-extraction`, `research-brief`, `conversation-design`, `lending-domain`, `study-design`.
- `verify`: an alias for `prove-it-works` under the name Claude Code's commit instructions look for.
- `api-design/references/mcp-server-2026.md`: the checklist for the stateless MCP spec of 2026-07-28.
- `writing-for-agents/SKILL-MECHANICS.md`: portable-skill rules, the description budget, the before-run rule for edits.
- Codex `agents/openai.yaml` and OpenCode `metadata.opencode/autoinvoke` on the three user-invoked skills, so "do not auto-invoke" holds in all three harnesses.

- `ui-ux/references/polish.md` (from make-interfaces-feel-better, MIT), `public-page.md` and `redesign.md` (from taste-skill v2, MIT): component polish with exact values; the public-page rules (idea before style, the two-line headline arithmetic, type and colour numbers from a 247-site study, picture provenance and credits, the motion layer, a verify step, the dated tells); a redesign protocol and extraction-before-coding for image briefs.
- `design-taste-frontend` installed as a CLI-managed third-party skill (gitignored) for its direction library, open-collection picture search and real-browser inspector; `ui-ux` routes public pages to it and calls its inspector in the new "Verify before done" step with a product-UI allow profile.

### Changed

- `ui-ux`: a verify step; companion rows for the three references and the installed skill; internal conflicts settled (ease-out both ways and never ease-in; springs scoped to native apps with bounce 0 on the web; 44/40px targets with WCAG's 24px named as the floor; container width scoped to app shells; a 13px text floor; `scale(0.96)` press; stagger by list item versus by semantic group); a design-system detection paragraph; seven measurable items added to the public web pages checklist.
- `design-principles`: optical padding as the exception to symmetry; concentric nested radii; the shadow-as-border token; native form elements first; numbers in tabular figures and monospace for code and IDs only; font classes instead of named faces; icon stroke matched to text weight and `currentColor` states; ease-out both ways and no bounce; 13px floor.
- `frontend-design`: forked from the Anthropic copy and rewritten: the gradient-mesh, grain, dramatic-shadow and custom-cursor advice replaced with the study's strong-versus-weak numbers; named fonts replaced with classes and a stand-in table; idea from the subject before style.
- `pitching` replaces `pitch-builder`, `pitch-review` and `frame-control`: the three repeated the same Pitch Anything primer and Golden Rules. One skill, three references, the local additions kept, triggers narrowed so "how do I handle" no longer fires on technical questions.
- Descriptions trimmed to about 250 characters, trigger first, on `grilling`, `customer-research`, `elements-of-style`, `interrogate`, `frontend-design` (Codex caps the whole listing).
- `interrogate`: reviewer table under a Claude Code heading, a fallback for Codex and OpenCode.
- `ui-ux`: stack guidance generic again (the body had been customised to one React Native project), script paths relative to the skill folder, companions referenced as sibling folders.
- `generate`: the `--yolo` alias claim removed; Codex 0.159 has no such flag.
- `diagnosing-bugs`: reads `docs/architecture.md` and `docs/patterns.md`.
- `create-verification-skill`: the dead `/maintain-verification-skill` pointer replaced with the loop in prose.
- `tufte-viz`, `frontend-design`: the bundled `dataviz` and `frontend-design` plugin skills named as Claude Code's.
- `remotion-best-practices`: the provenance footer `AGENTS.md` had promised.
- `send-email-via-computer`: a personal address replaced with a placeholder.
- `README.md`: install paths, the Codex budget, the OpenCode double-discovery note, the `/skills` menu step for hiding synced twins, the `ui-ux-pro-max` ghost removed.
- `.gitignore`: `.venv/`.
- `.skill-lock.json`: the `ui-ux-pro-max` entry pointed at a folder that no longer exists; removed. Local scratch (`.venv`, `skills-backup-descriptions`, `skills-retired-2026-08-19`) moved to the Trash; none of it was tracked.
- `~/.claude/skills` cleaned: `.DS_Store` and a stale `.trash` copy of google-workspace to the Trash; the two Sanity skills that lived there as real folders moved under `skills/` (gitignored, third-party) with symlinks back, so every entry in `~/.claude/skills` is now a symlink into this repo, the app bundle, or claude.ai's `synced/`.

### Removed

- Nothing retired. Every skill that predates this entry is still in the active set.
