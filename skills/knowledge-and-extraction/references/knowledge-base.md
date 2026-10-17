# Building the knowledge base, and choosing the parser

Reach this only when the pre-flight said no five times and the routing rule landed on an index.

## Build checklist

1. **Parse** with Docling to Markdown plus HTML tables plus JSON; keep page numbers and headings in metadata. Run the VLM pipeline only on pages Docling flags as scanned or low-text. Spot-check 10 pages per document type for table integrity before anything else: a bank statement whose columns shifted will poison every step below.
2. **Chunk** structure-aware: never split a table, or a heading from its first paragraph; target 500 to 1,000 tokens; store `doc_id, section_path, page_start, page_end`. No contextual prefixes by default.
3. **Index** BM25 and dense in the same store; fuse with RRF; return the top 30 to a reranker; keep the top 5 to 8.
4. **Rerank** locally with Qwen3-Reranker, or hosted with Cohere Rerank 4. Measure with and without: after parsing, the reranker is the largest single quality lever.
5. **Eval before tuning**: 50 real queries with labelled relevant chunks; report recall@10 and precision@5; add RAGAS-style faithfulness on 20 generated answers. Freeze as a regression suite. Any change to parser, chunker, embedder or reranker re-runs it. Recall@10 on about 50 labelled queries is the single highest-leverage number; circulating rules of thumb (precision@5 of 0.7 or better for a narrow base, recall@20 of 0.8 or better for a broad one) are conventions, not standards.
6. **Only then** try contextual retrieval or late chunking, and keep them only if recall@10 improves on your set. A Feb 2026 evaluation found contextualised chunks help in-corpus retrieval and hurt in-document retrieval, so the default is plain structure-aware chunks.
7. **Answer with citations** (chunk ids to page numbers); refuse when the top reranker score falls below a threshold set from the eval set.
8. **Freshness job**: re-parse changed documents only; version the index; log what changed.

Store defaults as of Oct 2026: LanceDB 0.40.0 (7 Oct 2026) embedded, with hybrid FTS plus vector and built-in rerankers, when nothing else exists; pgvector when the data already lives in Postgres (enable iterative scans, or filtered HNSW queries return too few rows). turbopuffer for many small per-tenant namespaces; Qdrant (Apache 2.0) for heavy filtered search at scale; sqlite-vec is still pre-v1 and fine only for per-user stores under about 100K vectors.

Reranker licences, read from the model cards as of Oct 2026: Qwen3-Reranker 0.6B, 4B and 8B are Apache 2.0 (confirmed on the 8B card) and the strongest open option; BGE reranker v2-m3 is Apache 2.0 and the safe small fallback; Jina reranker v3 weights are reported CC-BY-NC (secondary), so not for commercial self-hosting; zerank-2 is reported non-commercial or proprietary (secondary). Round-ups contradict each other on licences; the model card is the only source that counts. Cohere Rerank 4 (Dec 2025) is the hosted default at roughly $2 per 1,000 searches (secondary; re-check before quoting).

## Parser selection

```
born-digital PDF, Office, HTML; local; free           → Docling (default)
scanned, forms, handwriting, photos                   → Docling VLM pipeline first; if it fails,
                                                        Mistral OCR 4.1 (API) or dots.ocr 1.5 /
                                                        PaddleOCR-VL (self-host)
field-level citations and confidence; regulated       → Reducto
already on LlamaIndex, need pinned behaviour          → LlamaParse `agentic`, pin `version=`
Chandra 2                                             → only inside its licence carve-out; never assume
```

Always benchmark 20 of your own pages per candidate: vendor benchmarks use papers and reports, not photographed salary slips. Always keep tables as HTML, not Markdown pipes, when they have merged cells.

Model and licence notes, as of Oct 2026 (re-check prices before quoting):

| Parser | Version and date | Licence or price | Note |
| :--- | :--- | :--- | :--- |
| Docling | 2.140.0, 16 Oct 2026 | MIT | PDF, Office, HTML, EPUB, email, XBRL, images, audio and video; chart to table; VLM pipeline with granite-docling (258M); HybridChunker; an MCP server. The lean local default. |
| Mistral OCR 4.1 | GA 31 Aug 2026; `mistral-ocr-latest` points to it; 4.0 retired 30 Sep 2026 | OCR 3 was $2 per 1,000 pages, half price via batch; the exact 4.1 price is UNVERIFIED | Paragraph-level bounding boxes and block-level confidence scores. Whether it closed the gap to open VLM-OCR models on benchmarks is UNVERIFIED. |
| dots.ocr 1.5 | 2026 | MIT | 83.9 on olmOCR-bench (vendor-run table). |
| PaddleOCR-VL 1.6 | 2026 | Apache 2.0 (secondary) | Leads OmniDocBench v1.6 at 96.34 (secondary); like every VLM-OCR model it drops sharply on photographed pages (91.9 clean versus 72.2 photos, secondary). |
| Chandra 2 | Mar 2026 | Code Apache 2.0; weights modified OpenRAIL-M: free for research, personal use and companies under $2M funding or revenue, commercial licence otherwise | 85.8 on olmOCR-bench (vendor-run). |
| Reducto | per-product list pricing from 1 Sep 2026 | $10 per 1,000 pages Parse (preview), $20 Extract or Split, $40 Deep Extract or Deep Split, $7.50 Classify | Field-level citations and confidence; the regulated-volume choice. |
| LlamaParse | tiers `fast`, `cost_effective`, `agentic`, `agentic_plus`; dated versions such as `version="2026-01-08"` | Credits; Parse and Extract differ and secondary numbers conflict, read the pricing page | Keep only for documents Docling fails on, pinned. |

Treat the vendors' comparative benchmarks (Unstructured ranking itself above Reducto and LlamaParse, Reducto claiming the opposite) as marketing. Visual retrieval (ColPali-style) costs about 1,000 vectors per page and generalises less than claimed; use text retrieval for born-digital pages and visual retrieval only for the visually dense subset, if at all.
