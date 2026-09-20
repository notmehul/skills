# Working in this repo

This folder is the one copy of my skills. Codex and OpenCode read it directly,
Claude Code reads it through symlinks in `~/.claude/skills/`, and it is a public
repo on GitHub at `notmehul/skills`. A change that sits uncommitted on the laptop
is a change the other machines and the other agents never see.

## Every change ends in a push

Whoever edits a skill finishes the job, in the same turn as the edit:

```sh
git -C ~/.agents status          # read this before staging
git -C ~/.agents add -A
git -C ~/.agents commit -m "<what changed and why>"
git -C ~/.agents push
```

Done when `git -C ~/.agents status` is clean and the push is confirmed. If the
push fails or you decide not to make one, say so in your reply rather than
leaving it silent.

## Read the diff before it goes public

Everything committed here is world-readable the moment it is pushed, and a push
cannot be taken back. Before staging, read the diff for:

- Real names, and anything about a specific person's relationships.
- Client, portfolio or deal details.
- Absolute paths under `/Users/`, which leak the account name and break for
  anyone else. Write `~/` instead.
- Credentials of any kind, including in a `.pyc` or other build artifact.

Anything private gets a `.gitignore` line, not a commit. `lead-finder` and
`warm-path-finder` are ignored for exactly this reason.

## A new skill needs three things

1. The folder at `skills/<name>/` with a `SKILL.md`, written to the bar in
   `skills/writing-for-agents/`.
2. A symlink so Claude Code sees it:
   `ln -s ../../.agents/skills/<name> ~/.claude/skills/<name>`.
3. A row in the right table in `README.md`, and a line in the provenance section
   when it came from someone else.

## Skills that live in another repo

`mia` is a copy of `skills/mia/` from `notmehul/mia`, and `remotion-best-practices`
is a fork of an upstream skill. Change those at the source and re-copy, rather
than editing the copy and letting the two drift. The footer of each `SKILL.md`
records where it came from and what was changed locally.

Skills under `~/.claude/skills/synced/` belong to the claude.ai account and are
overwritten on every sync. Fork them into this repo instead; `README.md` has the
procedure.
