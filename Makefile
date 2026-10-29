LATEXMK ?= latexmk
LATEXFLAGS = -xelatex -interaction=nonstopmode -halt-on-error -file-line-error -synctex=1 -latexoption=-no-shell-escape

.PHONY: all zh en figures check clean
all: zh en

zh:
	mkdir -p build/zh pdf
	$(LATEXMK) $(LATEXFLAGS) -outdir=build/zh main.tex
	cp build/zh/main.pdf pdf/ai-scientific-figures-zh.pdf

en:
	mkdir -p build/en pdf
	$(LATEXMK) $(LATEXFLAGS) -outdir=build/en main-en.tex
	cp build/en/main-en.pdf pdf/ai-scientific-figures-en.pdf

figures:
	python3 scripts/plot_paired.py

check:
	python3 scripts/check_book.py

clean:
	$(LATEXMK) -C -outdir=build/zh main.tex
	$(LATEXMK) -C -outdir=build/en main-en.tex
