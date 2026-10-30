# Use AI to Make Better Scientific Figures

**From Research Ideas to Paper Figures** · An open bilingual book by TopLocalAI

[简体中文](README.zh-CN.md)

**Version 1.0.0, 2026-10-30.** The book is complete: preface, 13 chapters, appendices A–G and cover. The English edition has 421 pages, the Chinese edition 442 pages (170 × 240 mm).

## Download

- **[English PDF](https://github.com/TopLocalAI/ai-scientific-figures-book/releases/latest/download/ai-scientific-figures-en.pdf)**
- **[中文 PDF](https://github.com/TopLocalAI/ai-scientific-figures-book/releases/latest/download/ai-scientific-figures-zh.pdf)**

These links always point to the latest release; each PDF is about 78 MB. Earlier versions: [all releases](https://github.com/TopLocalAI/ai-scientific-figures-book/releases).

## What the book is about

The book is for graduate students, postdocs and other researchers who make figures for papers, talks and posters. It shows how to decide what a figure has to say, turn research content into a brief, work with AI on layouts, data plots, images and schematics, check the scientific content of every output, and deliver figures whose data, prompts and revisions can be traced. Worked cases come from biomedicine, materials and energy, engineering, earth and environmental science, and data science.

## Contents

1. Building Your AI Workflow for Scientific Figures
2. Turning Research Content into a Figure Brief
3. Working Out Layout and Sketches with AI
4. A Visual Language for the Whole Paper
5. Visualizing Data with AI Assistance
6. Method and Workflow Diagrams
7. Mechanism and Structure Schematics
8. Presenting Experimental Images Honestly
9. Assembling Panels into a Paper Figure
10. Graphical Abstracts: One Image for One Contribution
11. From "Make It Nicer" to Executable Revisions
12. From Paper Figures to Talks and Posters
13. Checking, Exporting and Delivering Traceable Figures

Appendices A–G: figure brief templates, a prompt and revision-instruction rewrite table, a figure legend checklist, a pre-submission delivery checklist, a glossary, case studies and asset sources, and a dimension and font-size reference.

## Practice with SciDraw AI

[SciDraw AI](https://sci-draw.com) is the practice platform used throughout the book; every tool mentioned in the PDF is a clickable link.
The [figure workflow guide](https://sci-draw.com/figure-workflow) lets you pick a figure type and follow a 3–4 step route of tools.

## Read and build

The source is LaTeX: `main-en.tex` (English) and `main.tex` (Chinese), with chapters in `chapters/en/` and `chapters/zh/`. Build with TeX Live (XeLaTeX, latexmk, Chinese support, Fandol fonts); no proprietary fonts or shell escape are needed.

    make check           # manuscript and example integrity
    make                 # both PDFs
    make en              # English only
    make zh              # Chinese only

PDFs are written to `pdf/` and intermediate files to `build/`; both are ignored by git. On Ubuntu, CI installs texlive-xetex, texlive-lang-chinese, texlive-latex-extra, texlive-fonts-recommended, tex-gyre, fonts-texgyre, fonts-lmodern and latexmk. The GitHub Actions workflow "Build bilingual PDFs" can be started from the Actions tab (Run workflow) and uploads both PDFs as an artifact.

The saved figures are enough to build the book. To regenerate figures:

    python3 -m venv .venv
    . .venv/bin/activate
    python3 -m pip install -r requirements.txt
    make figures         # regenerates the paired-data example
    make

`requirements.txt` covers the paired-data example; the per-chapter scripts (`scripts/chNN_*.py`) also use numpy, Pillow, pandas, SciPy, colorspacious and openpyxl.

## Examples, data and provenance

Figures combine image-generation-model base images with LaTeX/TikZ labels, matplotlib plots from public or clearly labelled simulated data, TikZ diagrams, and openly licensed images. Cases include USGS river nitrate, insulin–GLUT4 signalling, a Li-ion battery, a perovskite solar cell multi-panel figure built from simulated data, a wildfire graphical abstract and BBBC022 microscopy images.

The tool, prompt and revisions behind each generated figure are recorded in [provenance/](provenance/README.md); third-party sources and licences are listed in [ASSETS.md](ASSETS.md); datasets are described in [data/README.md](data/README.md). HOT and Global Carbon Budget raw data are not redistributed; `scripts/fetch_ch04_data.py` downloads them. No API credentials are required to read or build the book.

## Contribute, licence and citation

Please read [CONTRIBUTING.md](CONTRIBUTING.md). Keep the Chinese and English editions aligned in meaning, preserve provenance, and keep simulated data and teaching assumptions clearly separate from research evidence.

Text, figures and original data: [CC BY 4.0](LICENSES/CC-BY-4.0.txt). Code: [MIT](LICENSES/MIT.txt). Third-party materials stay under their own terms ([ASSETS.md](ASSETS.md)). [LICENSE](LICENSE) defines the exact scope, including AI-generated assets and trademarks.

Citation metadata is in [CITATION.cff](CITATION.cff).
