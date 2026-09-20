# Sheet dialect

The composer writes one markdown file per tab into `workspace/<slug>/sheet/`.
`scripts/render_sheet.py` turns those files into the workbook. The dialect is
ordinary markdown with a handful of conventions the renderer understands.
Anything outside these conventions renders as plain text, so the file stays
readable without the renderer.

## Files

- One file per tab. File names carry a two-digit prefix that sets tab order:
  `01-summary.md`, `02-market-size.md`, `03-trends.md`, `04-competitors.md`,
  `05-founder-claims.md`, `06-feature-matrix.md`, `07-public-sentiment.md`,
  `99-sources.md`.
- The tab name is the file's single H1. Keep it under 31 characters.

## Blocks

```markdown
# Market size
One-sentence subtitle: the first paragraph after the H1 renders muted under the title.

## Section title
> A muted note under a section. One line per blockquote line.

A plain paragraph renders as lead text, merged across the tab's width. Keep it to two sentences.

- A bullet renders as one merged row with a bullet.

| Header A | Header B | Header C |
|---|---|---|
| cell | cell | cell |
```

## Tables

- The header row and the `|---|` separator are required.
- Cells never contain a pipe character. Line breaks inside a cell are not supported; write a second row instead.
- Key-value block: a two-column table whose header cells are both empty renders as bold label plus wrapped value.

  ```markdown
  | | |
  |---|---|
  | Dominant tailwind | DPDP audit duties from 13 May 2027, dated and aimed at the beachhead. |
  ```

- Section row inside a table: the first cell in bold, every other cell empty. Renders as a bold row spanning the table.

  ```markdown
  | **Group 7: standalone memory APIs** | | | |
  ```

- Highlighted column: wrap the header cell in bold. Use it for the target company's column in a matrix.

  ```markdown
  | Feature | **Keel** | Recallio | Tessera |
  ```

- Matrix mode: put `<!-- matrix -->` on the line before a table. Columns after the first become narrow, headers rotate, glyph cells use a larger font. Use it for feature matrices with many solution columns.

## Cell content the renderer recognises

| Content | Renders as |
|---|---|
| `●●●`, `●●○`, `●○○`, `○○○` | Strength glyph, centred. Three characters exactly. |
| `▲ Tailwind`, `▼ Headwind` | Direction, green or red. |
| `✔ Verified`, `◐ Partly`, `✘ Contradicted`, `? Unverified` | Status, coloured by glyph. Also `Confirmed`, `Nuanced`, `Contradicted`, `Unverified`. |
| `[Mem0](https://...)` as the whole cell | Hyperlink on the cell text. |
| A number under a header containing `$M`, `$B`, `Raised` or `Points` | Right-aligned number. |
| A cell under a header of `#`, `Grp`, `Direction`, `Status`, `Horizon`, `Category`, `Tier`, `Confidence`, `Frequency`, `Severity` | Centred. |

Write numbers with units in the header rather than in every cell where a column is numeric (`Raised $M`), and with units in the cell where the column mixes text and numbers (`$3.34B`).

## Charts

A fenced block with the `chart` language renders as a native horizontal bar chart placed to the right of the tab's content at the row where the block appears. Data goes on a "chart data" sheet at the end of the workbook so the chart stays editable.

```chart
title: Market funnel 2026, $M
highlight: SOM pool: India (15%)
format: #,##0
TAM global | 7806
APAC (25%) | 1951
SAM: provenance buyers (25%) | 488
SOM pool: India (15%) | 73
```

- `title` is required. `highlight` is a label or a zero-based index and colours that bar teal. `format` is an Excel number format for the data labels; default `#,##0`.
- Two values per row make a stacked bar with two series. Name them with `series: Tailwinds, Headwinds` on its own line.
- Negative values are allowed and draw to the left; use `format: +0.0;-0.0` for signed points.
- One chart per section at most. A table with the same numbers next to a chart is fine when the table carries the basis text; otherwise pick one.

## Column widths

The renderer sizes columns from content. To override for a tab, put a directive after the H1:

```markdown
<!-- widths: 26, 60, 14, 12, 40 -->
```

## What the checker enforces

`scripts/check_sheet.py` runs before every render and writes `checks.md`. It fails the render on: a file without exactly one H1; typographic tells (em dash, en dash, curly quotes); any table cell over 350 characters; a glyph cell that is not one of the four patterns; a Founder claims row without a status; SAM above TAM, SOM above SAM, or TAM above $10 trillion in the Market size table; a chart block that does not parse. It warns on: a lead paragraph over 450 characters; a tab other than Summary with no link; a URL used in a tab that is missing from the Sources tab.
