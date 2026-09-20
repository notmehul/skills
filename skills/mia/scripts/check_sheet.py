"""Deterministic checks on a sheet directory. Writes checks.md next to it.

Run: python3 check_sheet.py workspace/<slug>   (expects workspace/<slug>/sheet/*.md)
Exit code 1 when any check fails; warnings do not change the exit code.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from sheet_md import (  # noqa: E402
    GLYPH_RE, INLINE_LINK_RE, STATUS_RE, STATUS_WORDS, TELLS, Tab, load_sheet, parse_money, parse_tab,
)

CELL_MAX = 350
PARA_MAX = 450
TAM_CEILING = 10e12


def _iter_cells(tab: Tab):
    for kind, payload in tab.blocks:
        if kind == "table":
            for r in payload.data_rows():
                for j, c in enumerate(r):
                    yield payload, j, c


def check_tabs(tabs: list[Tab]) -> tuple[list[str], list[str]]:
    fails: list[str] = []
    warns: list[str] = []
    if not tabs:
        fails.append("no tab files found in sheet/")
        return fails, warns
    if not tabs[0].name.lower().startswith("summary"):
        warns.append(f"first tab is '{tabs[0].name}', expected Summary first (name the file 01-summary.md)")

    urls_used: dict[str, str] = {}
    source_urls: set[str] = set()
    for tab in tabs:
        name = tab.name
        text_blobs = [tab.subtitle]
        for kind, payload in tab.blocks:
            if kind in ("para", "note", "bullet", "section"):
                text_blobs.append(payload)
                if kind == "para" and len(payload) > PARA_MAX:
                    warns.append(f"{name}: lead paragraph over {PARA_MAX} characters ({len(payload)}): '{payload[:60]}...'")
            elif kind == "table":
                for r in payload.rows:
                    if isinstance(r, tuple):
                        text_blobs.append(r[1])
                    else:
                        text_blobs.extend(r)
                for _, j, c in [(payload, j, c) for r in payload.data_rows() for j, c in enumerate(r)]:
                    if len(c) > CELL_MAX:
                        fails.append(f"{name}: table cell over {CELL_MAX} characters ({len(c)}): '{c[:60]}...'")
                    if ("●" in c or "○" in c) and not GLYPH_RE.match(c) and not re.search(r"[●○]{3}\s*[●○]{3}", c):
                        if len(c) <= 4:
                            fails.append(f"{name}: glyph cell '{c}' is not one of ●●● ●●○ ●○○ ○○○")
            elif kind == "chart":
                text_blobs.append(payload.title)
        for blob in text_blobs:
            bad = [ch for ch in TELLS if ch in blob]
            if bad:
                fails.append(f"{name}: typographic tell {bad} in '{blob[:70]}...'. Use a comma, a period, a hyphen or straight quotes.")
            for m in INLINE_LINK_RE.finditer(blob):
                urls_used.setdefault(m.group(2), name)
        # per-tab link presence
        has_link = any(INLINE_LINK_RE.search(b) for b in text_blobs)
        if not has_link and not name.lower().startswith(("summary", "sources")):
            warns.append(f"{name}: no source link on this tab")

        lname = name.lower()
        if lname.startswith("sources"):
            for blob in text_blobs:
                for m in INLINE_LINK_RE.finditer(blob):
                    source_urls.add(m.group(2))
                for m in re.finditer(r"https?://\S+", blob):
                    source_urls.add(m.group(0).rstrip(").,"))
        if lname.startswith("founder claims"):
            for kind, payload in tab.blocks:
                if kind != "table" or payload.kv:
                    continue
                headers = [h.lower() for h in payload.headers]
                if "status" not in headers:
                    continue
                si = headers.index("status")
                for r in payload.data_rows():
                    c = r[si].strip()
                    if not (STATUS_RE.match(c) or c.lower() in STATUS_WORDS):
                        fails.append(f"{name}: claims row '{r[min(1, len(r)-1)][:50]}' has no status glyph (✔ ◐ ✘ ?)")
        if lname.startswith("market size"):
            fails.extend(_check_sizing(tab))

    # URLs used on tabs but missing from Sources
    if source_urls:
        for url, where in urls_used.items():
            if url not in source_urls:
                warns.append(f"{where}: link {url} is not listed on the Sources tab")
    elif urls_used:
        warns.append("no Sources tab found; every link used on a tab should also appear there")
    return fails, warns


def _check_sizing(tab: Tab) -> list[str]:
    fails: list[str] = []
    vals: dict[str, float] = {}
    for kind, payload in tab.blocks:
        if kind != "table" or payload.kv:
            continue
        for r in payload.data_rows():
            key = r[0].strip().upper()
            if key in ("TAM", "SAM", "SOM") and key not in vals:
                for c in r[1:]:
                    v = parse_money(c)
                    if v is not None and ("$" in c or v > 1000):
                        vals[key] = v
                        break
    tam, sam, som = vals.get("TAM"), vals.get("SAM"), vals.get("SOM")
    if tam is not None and tam > TAM_CEILING:
        fails.append(f"Market size: TAM ${tam:,.0f} is above $10T; the market definition is too broad")
    if tam is not None and sam is not None and sam > tam:
        fails.append(f"Market size: SAM ${sam:,.0f} is above TAM ${tam:,.0f}")
    if sam is not None and som is not None and som > sam:
        fails.append(f"Market size: SOM ${som:,.0f} is above SAM ${sam:,.0f}")
    return fails


def run(workspace: Path) -> int:
    sheet_dir = workspace / "sheet"
    fails: list[str] = []
    warns: list[str] = []
    tabs: list[Tab] = []
    for p in sorted(sheet_dir.glob("*.md")):
        try:
            tabs.append(parse_tab(p.read_text(encoding="utf-8"), p))
        except ValueError as exc:
            fails.append(f"{p.name}: {exc}")
    f2, w2 = check_tabs(tabs)
    fails += f2
    warns += w2
    lines = ["# Checks", ""]
    lines.append(f"Result: {'FAIL' if fails else 'PASS'}. {len(fails)} fail, {len(warns)} warn.")
    lines.append("")
    if fails:
        lines.append("## Fix before delivering")
        lines += [f"- {f}" for f in fails]
        lines.append("")
    if warns:
        lines.append("## Worth a look")
        lines += [f"- {w}" for w in warns]
        lines.append("")
    (workspace / "checks.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    return 1 if fails else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: check_sheet.py workspace/<slug>")
        sys.exit(2)
    sys.exit(run(Path(sys.argv[1])))
