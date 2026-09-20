---
name: git-release
description: "Write a commit message, pull-request description, CHANGELOG entry, or README. Use when committing, opening a PR, cutting a release, or refreshing a project README."
---

# Git & Release Writing

Produce the prose around shipping code: commits, PRs, changelogs, READMEs. Match
the repo's existing conventions first; the defaults below apply when none exist.

## Commit Messages

- **Conventional Commits**: `type(scope): summary` — types `feat, fix, docs,
  refactor, perf, test, chore, build, ci`. Imperative mood, ~72-char subject,
  lowercase summary, no trailing period.
- Body (when non-trivial): *why*, not *what* the diff already shows. Wrap ~72.
- One logical change per commit. Don't bundle unrelated edits.
- Reference issues (`Closes #123`) when relevant.
- If the change was AI-assisted and the repo uses trailers, add the co-author
  trailer the project expects (e.g. `Co-Authored-By: ...`). Follow the repo's
  CLAUDE.md if it specifies one.

## Pull-Request Descriptions

Lead with subject matter, not ceremony (Mehul dislikes vague/performative
framing). Structure:
- **What & why** — one tight paragraph: the problem and the approach.
- **Changes** — bulleted, grouped by area; call out anything reviewers should
  scrutinize.
- **Testing** — what you ran and what it proved (or honestly, what's untested).
- **Risk / rollback** — migrations, breaking changes, how to revert.
- Keep it scannable. No filler.

## Changelogs

- **Keep a Changelog** format + **SemVer**. Group under Added / Changed /
  Deprecated / Removed / Fixed / Security.
- Write for *users*, not committers — describe behavior change and impact, link
  PRs/issues. Maintain an `## [Unreleased]` section.

## OSS README (for MIT/public projects)

Structure for a builder audience: one-line what-it-is → the problem in plain
terms → quickstart (install + minimal example) → how it works (a diagram/flow if
it clarifies) → constraints/philosophy → license. For Marshmallow specifically,
mirror his launch voice: plain, anti-hype, local-first, inspectable, "not another
AI memory MCP slop fest." Pair with `mehul-voice` for narrative sections.

## Anti-Patterns

- Vague subjects ("update code", "fixes"), bundled unrelated changes.
- PR descriptions that restate the diff instead of the reasoning.
- Changelog entries written for committers, not users.
- Marketing-speak in a builder-facing README.

## Ask When

- The repo has an established commit/PR/changelog convention that differs from
  the above — follow the repo, not this default.
