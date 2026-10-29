# Chapter 3 figure provenance (Cursor agent)

## Reuse FIG ch03-05a

| Source | Target | Status |
|--------|--------|--------|
| `figures/ch03/ch03-03c-cand-branch.png` | overlay in `ch03-05a-v1-issues-*.tex` | **Source missing** — not copied; TikZ overlay written, awaits codex PNG |

## Codex-image (not produced in this task)

- ch03-02a/b/c sketches, ch03-03a/b/c candidates, ch03-05b, ch03-06-final-base — see `ch03-codex.md` parallel task.

## TikZ standalone (this task)

- ch03-01, ch03-04, ch03-07: complete `.tex` zh/en
- ch03-02, ch03-03, ch03-05a, ch03-06: composite `.tex` zh/en (compile when PNG bases exist)

## FIG ch03-04 area percentages

Candidate PNGs were not present at build time. Wireframe proxy percentages are computed inside the TikZ figure; re-run `scripts/ch03_figures.py` after candidates exist to record PNG-based measurements in `data-check.json`.
