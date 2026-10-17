# Literature review

The academic branch of `research-brief`: related work for a paper, a reading list, "what does the literature say". The source hierarchy, the conflict rule and the four graders from `SKILL.md` apply unchanged; a paper is a primary source and a blog summary of it is not. Insufficient literature context was CHI's most frequent assisted desk-reject reason in 2025 and 2026, so this branch is where a solo researcher's paper lives or dies.

## Steps

1. **Define** the question, the inclusion criteria and a stopping rule in writing. For human-AI interaction work the defaults are years 2023 to 2026 and the venues CHI, CSCW (PACM HCI), UIST, FAccT, HCOMP, IUI and the NeurIPS and ICLR human-AI workshops, plus the Nature family and Science Advances for behavioural results. Done when a stranger could tell from the criteria whether a given paper is in or out.
2. **Seed** with 3 to 5 anchor papers the question cannot be written without, and snowball in both directions: what they cite, and who cites them. Done when a snowball step turns up no new paper that passes the criteria.
3. **Search programmatically** so the set is reproducible (see "Programmatic search"). Record the query strings and the date. Done when the queries sit in the repository.
4. **Verify every candidate before it enters the bib** with the five checks below. Done when every entry in the `.bib` has passed all five and the ones that failed are in a discard list with the reason.
5. **Store in a reference manager** and export the bib from it. Hand-typed entries are where errors enter. Done when the `.bib` is generated, never edited by hand.
6. **Write the review as an argument.** Group by mechanism (what increases reliance, what reduces it, what the after-effects are), state the field's disagreements as disagreements (explanations help versus hurt; a two-step paradigm reduces versus increases over-reliance), and end on the gap the study fills. A list of papers in date order is a reading log. Done when each paragraph makes a claim and its citations support that claim.
7. **Disclose agent assistance** in search and summarisation wherever any text came from it. CHI's LLM policy requires it, and undisclosed use is a desk reject.

## Tools

Graph and snowball: Connected Papers or ResearchRabbit, both built on Semantic Scholar data. Citation context, supporting versus contrasting: Scite. Deep agentic search with short summaries that push you to the source: Undermind. Structured extraction into comparison tables: Elicit, exploratory rather than systematic. Quick orientation: Consensus. All of these are paid or freemium as of Oct 2026; Semantic Scholar and OpenAlex are free.

Reference manager: Zotero, free and local, with the Better BibTeX plugin for stable citation keys and clean `.bib` export. AI plugins for Zotero exist; none were verified for this skill.

## Programmatic search

- **Semantic Scholar Academic Graph API**: paper search, batch lookup, citations and references. Useful fields: `externalIds` (DOI, arXiv), `openAccessPdf`, `citationCount`, `tldr`. An API key raises rate limits; the exact limits are `UNVERIFIED` (the docs page rate-limited the fetch).
- **OpenAlex**: the works endpoint filters by DOI, title, year and venue. A free tier plus paid plans with API keys exist; the specifics are `UNVERIFIED`.

Keep the scripts and their output in the paper's repository, beside the stimuli and the analysis code.

## The five checks before a citation enters the bib

This is the step that stops hallucinated references. Run it on every entry, including the ones you are sure about.

1. Resolve the DOI (`https://doi.org/<doi>`) or the arXiv id, and confirm title, author list, year and venue match the entry character for character.
2. If an agent produced the citation, require a URL and re-fetch the abstract yourself. Discard anything that does not resolve in Semantic Scholar, OpenAlex or Crossref.
3. Check retraction and erratum status (Crossref `update-to` metadata, Retraction Watch). Corrigenda land on recent papers too; a 2025 scoping review in this field picked one up in June 2026.
4. Read at least the abstract and the results section before citing a finding. A number you have only seen in a secondary summary is not yet yours to cite.
5. Record the sentence you will cite the paper for, in a notes field, so the claim-to-source link survives drafting.

## Output

Back to `research-brief`: the `.bib`, the discard list with reasons, the query log, and the review written as an argument that ends on the gap. `study-design` takes the gap when it becomes a study; `unslop` and `mehul-voice` take the prose.
