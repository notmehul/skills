"""Parser for the sheet dialect (see references/sheet-dialect.md).

A tab file is ordinary markdown. This module turns it into a small tree the
renderer and the checker both consume. It has no dependencies beyond the
standard library.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

GLYPHS = {"●●●", "●●○", "●○○", "○○○"}
GLYPH_RE = re.compile(r"^[●○]{3}$")
DIRECTION_RE = re.compile(r"^(▲|▼)\s*(.*)$")
STATUS_RE = re.compile(r"^(✔|◐|✘|\?)(\s|$)")
STATUS_WORDS = {
    "verified": "✔", "confirmed": "✔", "live": "✔",
    "partly": "◐", "partial": "◐", "partially confirmed": "◐", "nuanced": "◐", "unverified": "?",
    "contradicted": "✘",
}
LINK_RE = re.compile(r"^\[([^\]]+)\]\((\S+?)\)$")
INLINE_LINK_RE = re.compile(r"\[([^\]]+)\]\((\S+?)\)")
BOLD_RE = re.compile(r"^\*\*(.+)\*\*$")
WIDTHS_RE = re.compile(r"<!--\s*widths:\s*([\d.,\s]+)-->")
MATRIX_RE = re.compile(r"<!--\s*matrix\s*-->")
TELLS = "—–“”‘’"


@dataclass
class Table:
    headers: list[str]
    rows: list  # list[list[str]] or ("section", text)
    kv: bool = False
    matrix: bool = False
    highlight_cols: set = field(default_factory=set)  # zero-based column indexes
    line: int = 0

    @property
    def ncols(self) -> int:
        return len(self.headers)

    def data_rows(self):
        for r in self.rows:
            if isinstance(r, list):
                yield r


@dataclass
class Chart:
    title: str
    rows: list  # [(label, [values])]
    series: list[str] = field(default_factory=list)
    highlight: int | None = None
    fmt: str = "#,##0"
    line: int = 0


@dataclass
class Tab:
    title: str
    name: str = ""
    subtitle: str = ""
    widths: list[float] | None = None
    blocks: list = field(default_factory=list)  # (kind, payload)
    path: Path | None = None


def _split_row(line: str) -> list[str]:
    inner = line.strip()
    if inner.startswith("|"):
        inner = inner[1:]
    if inner.endswith("|"):
        inner = inner[:-1]
    return [c.strip() for c in inner.split("|")]


def _is_separator(line: str) -> bool:
    s = line.strip()
    return s.startswith("|") and set(s.replace("|", "").replace("-", "").replace(":", "").strip()) == set()


def _parse_table(lines: list[str], start: int, matrix: bool) -> tuple[Table, int]:
    headers_raw = _split_row(lines[start])
    i = start + 1
    if i >= len(lines) or not _is_separator(lines[i]):
        raise ValueError(f"line {start + 1}: table header must be followed by a |---| separator row")
    i += 1
    headers: list[str] = []
    highlight: set[int] = set()
    for j, h in enumerate(headers_raw):
        m = BOLD_RE.match(h)
        if m:
            highlight.add(j)
            headers.append(m.group(1))
        else:
            headers.append(h)
    kv = len(headers) == 2 and all(h == "" for h in headers)
    rows: list = []
    while i < len(lines) and lines[i].strip().startswith("|"):
        cells = _split_row(lines[i])
        if len(cells) < len(headers):
            cells = cells + [""] * (len(headers) - len(cells))
        elif len(cells) > len(headers):
            raise ValueError(f"line {i + 1}: row has {len(cells)} cells, header has {len(headers)}")
        m = BOLD_RE.match(cells[0])
        if m and all(c == "" for c in cells[1:]):
            rows.append(("section", m.group(1)))
        else:
            rows.append(cells)
        i += 1
    return Table(headers=headers, rows=rows, kv=kv, matrix=matrix, highlight_cols=highlight, line=start + 1), i


def _parse_chart(lines: list[str], start: int) -> tuple[Chart, int]:
    i = start + 1
    title, series, highlight, fmt = "", [], None, "#,##0"
    rows: list = []
    while i < len(lines) and not lines[i].strip().startswith("```"):
        raw = lines[i].strip()
        i += 1
        if not raw:
            continue
        key, _, val = raw.partition(":")
        k = key.strip().lower()
        if "|" not in raw and k in ("title", "series", "highlight", "format"):
            v = val.strip()
            if k == "title":
                title = v
            elif k == "series":
                series = [s.strip() for s in v.split(",") if s.strip()]
            elif k == "highlight":
                highlight = v
            elif k == "format":
                fmt = v.strip('"')
            continue
        parts = [p.strip() for p in raw.split("|")]
        label, vals = parts[0], parts[1:]
        try:
            nums = [float(v.replace(",", "")) for v in vals]
        except ValueError as exc:
            raise ValueError(f"line {i}: chart value is not a number: {vals}") from exc
        if not nums:
            raise ValueError(f"line {i}: chart row needs at least one value")
        rows.append((label, nums))
    if i >= len(lines):
        raise ValueError(f"line {start + 1}: chart block is not closed")
    if not title:
        raise ValueError(f"line {start + 1}: chart block needs a title")
    if not rows:
        raise ValueError(f"line {start + 1}: chart block has no data rows")
    hl: int | None = None
    if highlight is not None:
        if highlight.isdigit():
            hl = int(highlight)
        else:
            labels = [r[0] for r in rows]
            if highlight not in labels:
                raise ValueError(f"line {start + 1}: chart highlight '{highlight}' is not a row label")
            hl = labels.index(highlight)
        if hl >= len(rows):
            raise ValueError(f"line {start + 1}: chart highlight index {hl} is out of range")
    nser = len(rows[0][1])
    if any(len(r[1]) != nser for r in rows):
        raise ValueError(f"line {start + 1}: chart rows have different numbers of values")
    return Chart(title=title, rows=rows, series=series, highlight=hl, fmt=fmt, line=start + 1), i + 1


def parse_tab(text: str, path: Path | None = None) -> Tab:
    lines = text.splitlines()
    tab: Tab | None = None
    blocks: list = []
    i = 0
    pending_matrix = False
    seen_h1 = 0
    para: list[str] = []

    def flush_para():
        nonlocal para
        if para:
            txt = " ".join(p.strip() for p in para).strip()
            if tab is not None and not tab.subtitle and not blocks and txt:
                tab.subtitle = txt
            elif txt:
                blocks.append(("para", txt))
            para = []

    while i < len(lines):
        raw = lines[i]
        s = raw.strip()
        if s.startswith("# ") and not s.startswith("## "):
            flush_para()
            seen_h1 += 1
            if seen_h1 > 1:
                raise ValueError(f"line {i + 1}: a tab file has exactly one H1")
            tab = Tab(title=s[2:].strip(), path=path)
            i += 1
            continue
        if tab is None and s:
            raise ValueError(f"line {i + 1}: the file must start with an H1 tab title")
        m = WIDTHS_RE.search(s)
        if m and tab is not None:
            tab.widths = [float(x) for x in m.group(1).replace(" ", "").split(",") if x]
            i += 1
            continue
        if MATRIX_RE.search(s):
            pending_matrix = True
            i += 1
            continue
        if s.startswith("```chart"):
            flush_para()
            chart, i = _parse_chart(lines, i)
            blocks.append(("chart", chart))
            continue
        if s.startswith("```"):
            raise ValueError(f"line {i + 1}: only ```chart fences are supported")
        if s.startswith("## "):
            flush_para()
            blocks.append(("section", s[3:].strip()))
            i += 1
            continue
        if s.startswith("### "):
            flush_para()
            blocks.append(("section", s[4:].strip()))
            i += 1
            continue
        if s.startswith(">"):
            flush_para()
            blocks.append(("note", s.lstrip("> ").strip()))
            i += 1
            continue
        if s.startswith("- ") or s.startswith("* "):
            flush_para()
            blocks.append(("bullet", s[2:].strip()))
            i += 1
            continue
        if s.startswith("|"):
            flush_para()
            table, i = _parse_table(lines, i, pending_matrix)
            pending_matrix = False
            blocks.append(("table", table))
            continue
        if not s:
            flush_para()
            i += 1
            continue
        para.append(s)
        i += 1
    flush_para()
    if tab is None:
        raise ValueError("file has no H1 tab title")
    tab.blocks = blocks
    tab.name = tab_name_from_path(path) if path else tab.title
    return tab


def tab_name_from_path(path: Path) -> str:
    """'02-market-size.md' -> 'Market size'. The H1 stays the displayed title."""
    stem = re.sub(r"^\d+[-_ ]*", "", Path(path).stem)
    words = stem.replace("-", " ").replace("_", " ").strip()
    return (words[:1].upper() + words[1:]) if words else Path(path).stem


def load_sheet(sheet_dir: Path) -> list[Tab]:
    tabs = []
    for p in sorted(Path(sheet_dir).glob("*.md")):
        tabs.append(parse_tab(p.read_text(encoding="utf-8"), p))
    return tabs


def cell_kind(text: str, header: str) -> str:
    """Classify a cell for rendering: glyph, direction, status, link, num, center, text."""
    h = header.strip().lower()
    if GLYPH_RE.match(text):
        return "glyph"
    if DIRECTION_RE.match(text):
        return "direction"
    if STATUS_RE.match(text) or text.strip().lower() in STATUS_WORDS:
        return "status"
    if LINK_RE.match(text):
        return "link"
    if any(k in h for k in ("$m", "$b", "raised", "points")):
        return "num"
    if h in {"#", "grp", "direction", "status", "horizon", "category", "tier", "confidence", "conf.", "frequency", "severity", "year", "founded", "stage"}:
        return "center"
    return "text"


def parse_money(text: str) -> float | None:
    """'$7.8B' -> 7.8e9; '$488M' -> 4.88e8; '$0.2-2.9M' -> 2.9e6 (upper bound); plain numbers pass through."""
    t = text.strip().replace(",", "").replace("~", "").replace("approx.", "").strip()
    m = re.search(r"\$?\s*([\d.]+)(?:\s*-\s*([\d.]+))?\s*([KMBT])?\b", t, re.I)
    if not m:
        return None
    val = float(m.group(2) or m.group(1))
    mult = {"k": 1e3, "m": 1e6, "b": 1e9, "t": 1e12}.get((m.group(3) or "").lower(), 1.0)
    return val * mult
