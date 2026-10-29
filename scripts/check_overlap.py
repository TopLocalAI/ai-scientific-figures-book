#!/usr/bin/env python3
"""Detect overlapping words and margin violations in PDF text (pdftotext -bbox-layout)."""
# SPDX-License-Identifier: MIT
from __future__ import annotations

import argparse
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path

OVERLAP_FRAC = 0.10
MARGIN_PT = 5.0


@dataclass(frozen=True)
class WordBox:
    page: int
    line_id: int
    text: str
    xmin: float
    ymin: float
    xmax: float
    ymax: float

    def area(self) -> float:
        return max(0.0, self.xmax - self.xmin) * max(0.0, self.ymax - self.ymin)


@dataclass(frozen=True)
class PageInfo:
    number: int
    width: float
    height: float


def _float_attr(el: ET.Element, name: str) -> float:
    return float(el.attrib[name])


def parse_bbox_layout(xml_text: str, page_filter: set[int] | None) -> tuple[list[PageInfo], list[WordBox]]:
    root = ET.fromstring(xml_text)
    pages: list[PageInfo] = []
    words: list[WordBox] = []
    for page_idx, page_el in enumerate(root.findall(".//page"), start=1):
        if page_filter is not None and page_idx not in page_filter:
            continue
        width = _float_attr(page_el, "width")
        height = _float_attr(page_el, "height")
        pages.append(PageInfo(page_idx, width, height))
        line_id = 0
        for flow in page_el.findall("flow"):
            for block in flow.findall("block"):
                for line in block.findall("line"):
                    line_id += 1
                    for word in line.findall("word"):
                        words.append(
                            WordBox(
                                page=page_idx,
                                line_id=line_id,
                                text="".join(word.itertext()).strip(),
                                xmin=_float_attr(word, "xMin"),
                                ymin=_float_attr(word, "yMin"),
                                xmax=_float_attr(word, "xMax"),
                                ymax=_float_attr(word, "yMax"),
                            )
                        )
    return pages, words


def intersection_area(a: WordBox, b: WordBox) -> float:
    x1 = max(a.xmin, b.xmin)
    x2 = min(a.xmax, b.xmax)
    y1 = max(a.ymin, b.ymin)
    y2 = min(a.ymax, b.ymax)
    if x2 <= x1 or y2 <= y1:
        return 0.0
    return (x2 - x1) * (y2 - y1)


def run_pdftotext(pdf: Path) -> str:
    proc = subprocess.run(
        ["pdftotext", "-bbox-layout", str(pdf), "-"],
        check=True,
        capture_output=True,
        text=True,
    )
    return proc.stdout


def parse_page_range(spec: str | None, num_pages: int) -> set[int] | None:
    if not spec:
        return None
    pages: set[int] = set()
    for part in spec.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            lo, hi = part.split("-", 1)
            pages.update(range(int(lo), int(hi) + 1))
        else:
            pages.add(int(part))
    bad = [p for p in pages if p < 1 or p > num_pages]
    if bad:
        raise SystemExit(f"page out of range 1–{num_pages}: {bad}")
    return pages


def main() -> int:
    parser = argparse.ArgumentParser(description="Check PDF for overlapping text and margin violations.")
    parser.add_argument("pdf", type=Path, help="PDF file to check")
    parser.add_argument(
        "--pages",
        metavar="RANGE",
        help="Optional page list, e.g. 1,3-5 (1-based)",
    )
    args = parser.parse_args()
    if not args.pdf.is_file():
        print(f"error: not a file: {args.pdf}", file=sys.stderr)
        return 1

    raw = run_pdftotext(args.pdf)
    # pdftotext wraps HTML; strip to <doc> for XML parser
    doc_match = re.search(r"<doc>.*</doc>", raw, re.DOTALL)
    if not doc_match:
        print("error: pdftotext output missing <doc>", file=sys.stderr)
        return 1
    wrapped = f"<?xml version='1.0'?>{doc_match.group(0)}"
    all_pages_count = wrapped.count("<page ")
    page_filter = parse_page_range(args.pages, all_pages_count)
    page_infos, word_boxes = parse_bbox_layout(wrapped, page_filter)
    page_by_num = {p.number: p for p in page_infos}

    issues = 0

    by_page: dict[int, list[WordBox]] = {}
    for w in word_boxes:
        by_page.setdefault(w.page, []).append(w)

    for page_num, boxes in sorted(by_page.items()):
        pinfo = page_by_num[page_num]
        for w in boxes:
            if not w.text:
                continue
            too_left = w.xmin < MARGIN_PT
            too_top = w.ymin < MARGIN_PT
            too_right = w.xmax > pinfo.width - MARGIN_PT
            too_bottom = w.ymax > pinfo.height - MARGIN_PT
            if too_left or too_top or too_right or too_bottom:
                issues += 1
                print(
                    f"MARGIN page {page_num}: {w.text!r} "
                    f"box=({w.xmin:.1f},{w.ymin:.1f})–({w.xmax:.1f},{w.ymax:.1f}) "
                    f"page=({pinfo.width:.1f}×{pinfo.height:.1f})"
                )

        n = len(boxes)
        for i in range(n):
            for j in range(i + 1, n):
                a, b = boxes[i], boxes[j]
                if a.line_id == b.line_id:
                    continue
                inter = intersection_area(a, b)
                if inter <= 0:
                    continue
                smaller = min(a.area(), b.area())
                if smaller <= 0:
                    continue
                if inter / smaller > OVERLAP_FRAC:
                    issues += 1
                    print(
                        f"OVERLAP page {page_num}: {a.text!r} ∩ {b.text!r} "
                        f"inter={inter:.1f} ({100 * inter / smaller:.1f}% of smaller) "
                        f"a=({a.xmin:.1f},{a.ymin:.1f})–({a.xmax:.1f},{a.ymax:.1f}) "
                        f"b=({b.xmin:.1f},{b.ymin:.1f})–({b.xmax:.1f},{b.ymax:.1f})"
                    )

    if issues:
        print(f"\n{issues} issue(s) found.", file=sys.stderr)
        return 1
    print("OK: no overlapping text or margin violations detected.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
