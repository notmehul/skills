#!/usr/bin/env bash
# Create .venv with openpyxl next to the plugin root, using uv when present.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"
cd "$ROOT"
if [ -x .venv/bin/python ] && .venv/bin/python -c "import openpyxl" 2>/dev/null; then
  echo ".venv ready"
  exit 0
fi
if command -v uv >/dev/null 2>&1; then
  uv venv -q .venv
  uv pip install -q --python .venv/bin/python openpyxl
else
  python3 -m venv .venv
  .venv/bin/pip install -q openpyxl
fi
echo ".venv ready: use .venv/bin/python for render_sheet.py"
