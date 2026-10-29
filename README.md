# Use AI to Make Better Scientific Figures

**From Research Ideas to Paper Figures** · An open bilingual book by TopLocalAI

[简体中文](README.zh-CN.md) · [English PDF](pdf/ai-scientific-figures-en.pdf) · [中文 PDF](pdf/ai-scientific-figures-zh.pdf)

Learn to define a figure's purpose, work with AI, inspect its scientific content, and deliver traceable results. **SciDraw AI** is the common practical platform. AI assistance is discussed throughout the book.

**Status: v0.1.0 working draft, 2026-10-29.** Both editions contain the preface, Chapters 1 and 2, a thirteen-chapter roadmap, exercises, and references. Chapters 3–13 are planned, not completed.

## Read and build

The editable source is LaTeX: main.tex is Chinese; main-en.tex is English. Chapters live in chapters/zh/ and chapters/en/. Shared figures, data, and provenance keep the editions aligned.

Use TeX Live with XeLaTeX, latexmk, Chinese language support, Fandol fonts, and the usual LaTeX extra packages. No proprietary system fonts or shell escape are required.

    make check
    make                 # both PDFs
    make zh              # Chinese only
    make en              # English only

PDFs are copied to pdf/; intermediate files stay in ignored build/. The committed PDFs are reading copies of this draft. On Ubuntu, the CI uses texlive-xetex, texlive-lang-chinese, texlive-latex-extra, texlive-fonts-recommended, tex-gyre, fonts-lmodern, and latexmk.

To regenerate the numerical examples:

    python3 -m venv .venv
    . .venv/bin/activate
    python3 -m pip install -r requirements.txt
    make figures
    make

## What is inside

- **Chapter 1 — Build your AI scientific-figure workflow:** identify the question, choose a route, preserve data and source materials.
- **Chapter 2 — Turn research content into a drawing brief:** define objects, relationships, evidence, constraints, and review criteria.
- **Roadmap:** composition, visual language, data plots, methods, mechanisms, experimental images, panels and legends, graphical abstracts, revision, presentations, and delivery.

## Examples and provenance

The paired dataset contains eight fictional objects and sixteen observations. Codex wrote a deterministic plotting script that preserves all values. The mechanism figure is an actual output of Codex's built-in image generator, accompanied by its executed prompt and review. These are teaching examples, not real research findings and not SciDraw AI generation results.

Interface screenshots show the local development guide. Its route /figure-workflow is a development reference, not a claim that the feature is publicly deployed.

See [ASSETS.md](ASSETS.md), [data/README.md](data/README.md), and [provenance/README.md](provenance/README.md). No API credentials are required to read or build the book.

## Contribute and reuse

Please read [CONTRIBUTING.md](CONTRIBUTING.md). Keep the Chinese and English learning objectives aligned, preserve source provenance, and clearly distinguish teaching assumptions from research evidence.

Manuscript, original teaching data, and figures: [CC BY 4.0](LICENSES/CC-BY-4.0.txt). Scripts and reusable typesetting infrastructure: [MIT](LICENSES/MIT.txt). [LICENSE](LICENSE) defines the scope, including AI assets and trademarks.

Citation metadata is available in [CITATION.cff](CITATION.cff).
