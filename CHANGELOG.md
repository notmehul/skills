# Changelog

Removals and merges are named here so nothing disappears silently. Format follows Keep a Changelog; dates are when the change was pushed.

## 2026-10-18

### Added

- Twelve skills for a business-use-case to ML and agents role, each distilled from a dated research brief (Oct 2026) and written to the portable-skill rules: `use-case-discovery`, `pilot-rollout`, `ai-governance`, `building-agents`, `llm-evals`, `applied-ml`, `data-analysis`, `knowledge-and-extraction`, `research-brief`, `conversation-design`, `lending-domain`, `study-design`.
- `verify`: an alias for `prove-it-works` under the name Claude Code's commit instructions look for.
- `api-design/references/mcp-server-2026.md`: the checklist for the stateless MCP spec of 2026-07-28.
- `writing-for-agents/SKILL-MECHANICS.md`: portable-skill rules, the description budget, the before-run rule for edits.
- Codex `agents/openai.yaml` and OpenCode `metadata.opencode/autoinvoke` on the three user-invoked skills, so "do not auto-invoke" holds in all three harnesses.

### Changed

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

### Removed

- Nothing retired. Every skill that predates this entry is still in the active set.
