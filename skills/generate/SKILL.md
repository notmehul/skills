---
name: generate
description: >-
  Generate or edit raster images through Codex CLI's built-in imagegen skill
  (photos, illustrations, mockups, textures, sprites, UI stills, transparent
  cutouts). Use when the user says /generate, asks to generate images, make
  visuals, or edit an existing image with Codex imagegen. Do not use for
  SVG/HTML/CSS that should be written as code.
argument-hint: '<natural-language image request>'
---

# Generate Codex Image

`--full-auto` was removed in Codex CLI 0.147. Headless imagegen writes under `$CODEX_HOME/generated_images/` then copies into the workspace, so the drop-in is `--dangerously-bypass-approvals-and-sandbox` (alias `--yolo`). That is the old `--full-auto` behavior with an honest name. Do not call `codex exec --full-auto`.

## Generate

Run from the project directory. Done when stdout contains one `SAVED: <absolute path>` line per image, or when the command exits non-zero.

```bash
codex exec \
  --dangerously-bypass-approvals-and-sandbox \
  --skip-git-repo-check \
  -C "$(pwd)" \
  -- "$(cat <<EOF
Use the imagegen skill. Built-in image_gen tool path only. Do not use the CLI fallback.

If the user did not specify an output path, save under ./codex-images/<UTC-timestamp>-<n>.png.

For each saved image, print exactly one line:
SAVED: <absolute path>

User request:

$ARGUMENTS
EOF
)"
```

Show the command stdout verbatim. If the exit code is non-zero, show stderr and stop. Do not start another generate unless the user asks.

Express size, count, quality, transparency, and save paths in the user request. `imagegen` reads those from the prompt.

Keep anything that must be exact out of the prompt: a real product's UI, logos, and text longer than a short headline come out invented. Generate the scene or frame around them, then composite the real screenshot or logo in code, or pass it in through Edit's `--image`.

## Edit

First token is the input image path. The rest is the edit request.

```bash
codex exec \
  --dangerously-bypass-approvals-and-sandbox \
  --skip-git-repo-check \
  --image "<absolute-input-path>" \
  -C "$(pwd)" \
  -- "$(cat <<EOF
Use the imagegen skill. Built-in image_gen tool path only. Do not use the CLI fallback.
The image attached via --image is the edit target. Preserve unrelated parts unless the user request says otherwise.

If the user did not specify an output path, save under ./codex-images/<UTC-timestamp>-edit-<n>.png.

For each saved image, print exactly one line:
SAVED: <absolute path>

User edit request:

<edit instructions>
EOF
)"
```

## Safer scoped alternative

If the environment is already a trusted workspace and you want a sandbox instead of `--yolo`:

```bash
codex exec \
  --sandbox workspace-write \
  --add-dir "${CODEX_HOME:-$HOME/.codex}" \
  --approve-for-me \
  --skip-git-repo-check \
  -C "$(pwd)" \
  -- "<same instruction body as above>"
```

`--add-dir` is required so imagegen can write its default `$CODEX_HOME/generated_images/` path before copying into the project. If that still cannot call `image_gen`, fall back to `--dangerously-bypass-approvals-and-sandbox`.
