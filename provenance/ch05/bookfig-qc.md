# Chapter 5 bookfig QC

`scripts/bookfig.py` is the shared Matplotlib saver. `setup(lang)` registers TeX Gyre Heros and FandolHei and sets `font.family` to `['TeX Gyre Heros', 'FandolHei']`. `save` runs glyph, overlap (15% of the smaller box), and bounds checks before writing. Chinese PDFs go through PGF/XeLaTeX; the PNG is rasterized from that PDF at 300 dpi. English PDFs use the PDF backend. No `allow_overlap` entries were needed.

The first save, with figure content still unchanged, failed all 22 calls and wrote nothing. It reported missing glyphs ✕ U+2715, ✓ U+2713, ₂ U+2082, and ⁻ U+207B; n labels sitting on species names (`n = 151` ∩ `Adelie`); and subplot titles crossing (`C 全部记录 + 均值 ± SD` ∩ `D 云雨图`). Full log: `/tmp/ch05-qc-first.txt`.

After the layout fixes, one process saved all 22 stems (`RERUN_DONE failures=0`). `python scripts/bookfig.py check figures/ch05` then printed `OK: 22 PDF(s) passed pdffonts and overlap checks.` Fonts are CID Type 0C, embedded, not Type 3. Pedagogical errors kept on the bad panels: truncated 3D bars, twin axes without axis titles, and the jet colormap.

`pdffonts` rows whose subset names are wider than the name column are parsed from the right (emb/sub/uni) so a long Identity-H name is not reported as unembedded.
