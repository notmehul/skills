---
name: verify
description: "Check the real artifact before declaring work done or committing it: run the feature, read the actual value, inspect the diff. Alias for prove-it-works, so the pre-commit convention picks it up."
license: MIT
metadata:
  version: "1"
  updated: "2026-10-18"
  harnesses: "claude-code codex opencode"
---

# Verify

This is `prove-it-works` under the name Claude Code's commit instructions look for. Read `../prove-it-works/SKILL.md` and apply it in full: check the real thing (run it, read the value, inspect the diff), script the check where you can, and treat delegated work's artifacts, never its summary, as the evidence. Done when you can point at the observation that proves the behaviour, or say plainly that you could not.
