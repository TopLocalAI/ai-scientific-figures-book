#!/usr/bin/env python3
"""Check figure provenance, pairing, and bilingual source completeness."""
# SPDX-License-Identifier: MIT
import csv
import hashlib
import json
import re
from pathlib import Path
from statistics import mean

ROOT = Path(__file__).resolve().parents[1]
with (ROOT / "data/paired-example.csv").open(encoding="utf-8", newline="") as stream:
    rows = list(csv.DictReader(stream))
assert len(rows) == 8
assert len({row["sample_id"] for row in rows}) == 8
assert [row["sample_id"] for row in rows] == [f"SIM{i:02}" for i in range(1, 9)]
pairs = [(float(r["before"]), float(r["after"])) for r in rows]
assert pairs[3] == (18.0, 17.0)
assert sum(b > a for a, b in pairs) == 7
record = json.loads((ROOT / "provenance/paired-data-check.json").read_text())
assert record["before_mean"] == mean(a for a, _ in pairs)
assert record["after_mean"] == mean(b for _, b in pairs)
assert record["objects"] == len(rows)
assert record["measurements"] == 2 * len(rows)

image_record = json.loads((ROOT / "provenance/mechanism-review.json").read_text())
assert hashlib.sha256((ROOT / image_record["asset"]).read_bytes()).hexdigest() == image_record["sha256"]
assert (ROOT / image_record["prompt"]).is_file()

# Every Chinese chapter has an English counterpart with the same sections and labels.
zh_chapters = sorted((ROOT / "chapters/zh").glob("[01][0-9]-*.tex"))
assert len(zh_chapters) == 14, [p.name for p in zh_chapters]  # preface + 13 chapters
for zh_path in zh_chapters:
    en_path = ROOT / "chapters/en" / zh_path.name
    assert en_path.is_file(), en_path.name
    zh_text, en_text = zh_path.read_text(), en_path.read_text()
    sections = lambda s: len(re.findall(r"\\section\*?\{", s))
    labels = lambda s: sorted(re.findall(r"\\label\{([^}]+)\}", s))
    assert sections(zh_text) == sections(en_text), zh_path.name
    assert labels(zh_text) == labels(en_text), zh_path.name
for lang in ("zh", "en"):
    for asset in (
        f"figures/paired-comparison-{lang}.pdf",
        f"figures/paired-comparison-{lang}.png",
        f"figures/workflow-ui-{lang}.png",
        f"figures/workflow-{lang}.tex",
        f"chapters/{lang}/00-preface.tex",
        f"chapters/{lang}/appendices.tex",
    ):
        assert (ROOT / asset).is_file(), asset
for entry in ("main.tex", "main-en.tex"):
    for source in re.findall(r"\\input\{([^}]+)\}", (ROOT / entry).read_text()):
        assert (ROOT / f"{source}.tex").is_file(), source
print("PASS: 13 bilingual chapters with matching sections and labels, source files, original image hash, and simulated-data invariants")
