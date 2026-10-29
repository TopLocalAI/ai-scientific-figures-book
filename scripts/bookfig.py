#!/usr/bin/env python3
"""Shared Matplotlib setup, save, and pre-save QC for book figures.

Latin and digits use TeX Gyre Heros; Chinese uses FandolHei. ``setup`` registers
both via fontconfig-style family fallback. Chinese PDFs go through PGF/XeLaTeX
because Fandol's CFF outlines are unreliable on Matplotlib's Type 42 path.
"""
# SPDX-License-Identifier: MIT
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FONT_FAMILY = ["TeX Gyre Heros", "FandolHei"]
# Intersection area above this fraction of the smaller text box is an overlap.
OVERLAP_FRAC = 0.15
# Float slop for the figure-edge test, in display pixels.
BOUNDS_EPS_PX = 0.5

_REGISTERED = False
_CMAP_CACHE: dict[str, set[int]] | None = None


class BookFigError(RuntimeError):
    """Raised when glyph, overlap, or bounds QC fails."""

    def __init__(self, stem: str, lang: str, issues: list[str]):
        self.stem = stem
        self.lang = lang
        self.issues = list(issues)
        body = "\n".join(f"- {item}" for item in self.issues)
        super().__init__(
            f"QC failed for {stem} [{lang}] ({len(self.issues)} issue(s)):\n{body}"
        )


def _kpsewhich(name: str) -> Path:
    try:
        found = subprocess.check_output(
            ["kpsewhich", name], text=True, timeout=30
        ).strip()
    except (subprocess.CalledProcessError, FileNotFoundError) as exc:
        raise RuntimeError(f"kpsewhich could not find {name}") from exc
    if not found:
        raise RuntimeError(f"kpsewhich returned nothing for {name}")
    return Path(found)


def _font_paths() -> dict[str, Path]:
    names = {
        "heros": "texgyreheros-regular.otf",
        "heros_bold": "texgyreheros-bold.otf",
        "heros_italic": "texgyreheros-italic.otf",
        "heros_bolditalic": "texgyreheros-bolditalic.otf",
        "fandol": "FandolHei-Regular.otf",
        "fandol_bold": "FandolHei-Bold.otf",
    }
    return {key: _kpsewhich(filename) for key, filename in names.items()}


def _cmap(path: Path) -> set[int]:
    from fontTools.ttLib import TTFont

    font = TTFont(path)
    try:
        codes: set[int] = set()
        for table in font["cmap"].tables:
            if table.isUnicode():
                codes.update(table.cmap)
        return codes
    finally:
        font.close()


def _cmaps() -> tuple[set[int], set[int]]:
    global _CMAP_CACHE
    if _CMAP_CACHE is None:
        paths = _font_paths()
        _CMAP_CACHE = {
            "heros": _cmap(paths["heros"]) | _cmap(paths["heros_bold"]),
            "fandol": _cmap(paths["fandol"]) | _cmap(paths["fandol_bold"]),
        }
    return _CMAP_CACHE["heros"], _CMAP_CACHE["fandol"]


def _preamble(paths: dict[str, Path]) -> str:
    heros = paths["heros"].parent.as_posix()
    fandol = paths["fandol"].parent.as_posix()
    heros_opts = ",".join(
        [
            f"Path={heros}/",
            "Extension=.otf",
            "UprightFont=texgyreheros-regular",
            "BoldFont=texgyreheros-bold",
            "ItalicFont=texgyreheros-italic",
            "BoldItalicFont=texgyreheros-bolditalic",
        ]
    )
    fandol_opts = ",".join(
        [
            f"Path={fandol}/",
            "Extension=.otf",
            "UprightFont=FandolHei-Regular",
            "BoldFont=FandolHei-Bold",
        ]
    )
    # Matplotlib's PGF backend rewrites every text run as
    # \setmainfont{TeX Gyre Heros} with no Path, which XeTeX cannot resolve.
    # Load the fonts by path first, then turn that command into a no-op.
    return "\n".join(
        [
            r"\usepackage{fontspec}",
            r"\usepackage{xeCJK}",
            rf"\setmainfont{{TeX Gyre Heros}}[{heros_opts}]",
            rf"\setsansfont{{TeX Gyre Heros}}[{heros_opts}]",
            rf"\setCJKmainfont{{FandolHei}}[{fandol_opts}]",
            rf"\setCJKsansfont{{FandolHei}}[{fandol_opts}]",
            r"\renewcommand{\setmainfont}[2][]{}",
        ]
    )


def setup(lang: str) -> None:
    """Apply the shared font, size, and line-width rcParams for ``zh`` or ``en``."""
    if lang not in {"zh", "en"}:
        raise ValueError(f"lang must be 'zh' or 'en', got {lang!r}")

    import matplotlib as mpl
    from matplotlib import font_manager

    global _REGISTERED
    paths = _font_paths()
    if not _REGISTERED:
        for path in paths.values():
            font_manager.fontManager.addfont(str(path))
        _REGISTERED = True

    mpl.rcParams.update(
        {
            "font.family": list(FONT_FAMILY),
            "font.size": 8,
            "axes.titlesize": 9,
            "axes.labelsize": 8,
            "xtick.labelsize": 8,
            "ytick.labelsize": 8,
            "legend.fontsize": 8,
            "figure.titlesize": 9,
            "axes.linewidth": 0.7,
            "lines.linewidth": 1.0,
            "patch.linewidth": 0.6,
            "xtick.major.width": 0.7,
            "ytick.major.width": 0.7,
            "xtick.major.size": 3.0,
            "ytick.major.size": 3.0,
            # ASCII hyphen is in both fonts. U+2212 lives only in Heros, and a
            # Fandol-locked run would draw it as a box. Keep the hyphen.
            "axes.unicode_minus": False,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
            "pgf.texsystem": "xelatex",
            "pgf.rcfonts": False,
            "pgf.preamble": _preamble(paths),
            "text.usetex": False,
        }
    )


def _strip_math(text: str) -> str:
    """Drop ``$...$`` spans. Mathtext is not drawn from Heros/Fandol."""
    out: list[str] = []
    i = 0
    n = len(text)
    while i < n:
        if text[i] == "\\" and i + 1 < n and text[i + 1] == "$":
            out.append("$")
            i += 2
            continue
        if text[i] == "$":
            j = i + 1
            while j < n:
                if text[j] == "\\" and j + 1 < n:
                    j += 2
                    continue
                if text[j] == "$":
                    break
                j += 1
            i = j + 1 if j < n else j
            continue
        out.append(text[i])
        i += 1
    return "".join(out)


def _normalize_allow(allow_overlap) -> list[tuple[str, str, str]]:
    if not allow_overlap:
        return []
    items: list[tuple[str, str, str]] = []
    for item in allow_overlap:
        if isinstance(item, str):
            parts = [part.strip() for part in item.split("||")]
            if len(parts) != 3 or not parts[0] or not parts[1] or not parts[2]:
                raise ValueError(
                    "allow_overlap strings must be 'text_a || text_b || reason' "
                    "with a non-empty reason"
                )
            items.append((parts[0], parts[1], parts[2]))
            continue
        if isinstance(item, (tuple, list)) and len(item) == 3:
            text_a, text_b, reason = (str(item[0]), str(item[1]), str(item[2]).strip())
            if not text_a or not text_b or not reason:
                raise ValueError(
                    "allow_overlap entries must include two text snippets and a reason"
                )
            items.append((text_a, text_b, reason))
            continue
        raise ValueError(
            "allow_overlap entries must be (text_a, text_b, reason) "
            "or 'text_a || text_b || reason'"
        )
    return items


def _allowed(text_a: str, text_b: str, items: list[tuple[str, str, str]]) -> str | None:
    for snippet_a, snippet_b, reason in items:
        if (snippet_a in text_a and snippet_b in text_b) or (
            snippet_a in text_b and snippet_b in text_a
        ):
            return reason
    return None


def _tick_artists(axes):
    """Tick labels and offset texts already attached to an axes.

    Do not call ``get_xticklabels`` / ``get_yticklabels``. Those refresh the
    locator and put 3D tick labels back in data coordinates after mplot3d has
    projected them, so later window extents are wrong.
    """
    found = []
    for name in ("xaxis", "yaxis", "zaxis"):
        axis = getattr(axes, name, None)
        if axis is None:
            continue
        for tick in (*getattr(axis, "majorTicks", ()), *getattr(axis, "minorTicks", ())):
            found.append(tick.label1)
            found.append(tick.label2)
        offset = getattr(axis, "offsetText", None)
        if offset is not None:
            found.append(offset)
    return found


def _hidden_tick(text) -> bool:
    """Tick labels on an axes with the axis turned off are not drawn."""
    axes = text.axes
    if axes is None or getattr(axes, "axison", True):
        return False
    return text in _tick_artists(axes)


def _iter_texts(fig):
    from matplotlib.text import Text

    for text in fig.findobj(Text):
        if not text.get_visible() or _hidden_tick(text):
            continue
        axes = text.axes
        if axes is not None and not axes.get_visible():
            continue
        raw = text.get_text()
        if raw is None or not str(raw).strip():
            continue
        yield text, str(raw)


def _text_extent(text, renderer):
    """Window extent of a text artist, including 3D labels after projection."""
    try:
        from mpl_toolkits.mplot3d import proj3d
        from mpl_toolkits.mplot3d.art3d import Text3D, _norm_text_angle
    except ImportError:  # pragma: no cover
        Text3D = ()
        proj3d = None
        _norm_text_angle = None
    if proj3d is not None and isinstance(text, Text3D) and text.axes is not None:
        import math

        import numpy as np
        from matplotlib import cbook

        position3d = np.array((text._x, text._y, text._z), dtype=float)
        direction = np.asarray(text._dir_vec, dtype=float)
        proj = proj3d._proj_trans_points(
            [position3d, position3d + direction], text.axes.M
        )
        dx = proj[0][1] - proj[0][0]
        dy = proj[1][1] - proj[1][0]
        angle = _norm_text_angle(math.degrees(math.atan2(dy, dx)))
        with cbook._setattr_cm(
            text, _x=float(proj[0][0]), _y=float(proj[1][0]), _rotation=angle
        ):
            return text.get_window_extent(renderer)
    return text.get_window_extent(renderer)


def collect_issues(fig, allow_overlap=None) -> list[str]:
    """Return glyph, overlap, and bounds problems for ``fig``."""
    from matplotlib.legend import Legend

    allow = _normalize_allow(allow_overlap)
    heros, fandol = _cmaps()
    issues: list[str] = []

    for _text, raw in _iter_texts(fig):
        missing = []
        for char in _strip_math(raw):
            if char.isspace():
                continue
            code = ord(char)
            if code not in heros and code not in fandol:
                missing.append(char)
        if missing:
            shown = " ".join(f"U+{ord(char):04X} {char!r}" for char in missing)
            issues.append(f"GLYPH {shown} in {raw!r}")

    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    width, height = fig.canvas.get_width_height()
    boxes: list[tuple[str, object]] = []
    for text, raw in _iter_texts(fig):
        bbox = _text_extent(text, renderer)
        boxes.append((raw, bbox))
        if (
            bbox.x0 < -BOUNDS_EPS_PX
            or bbox.y0 < -BOUNDS_EPS_PX
            or bbox.x1 > width + BOUNDS_EPS_PX
            or bbox.y1 > height + BOUNDS_EPS_PX
        ):
            issues.append(
                f"BOUNDS text {raw!r} "
                f"box=({bbox.x0:.1f},{bbox.y0:.1f})–({bbox.x1:.1f},{bbox.y1:.1f}) "
                f"figure={width:.1f}×{height:.1f}"
            )

    for legend in fig.findobj(Legend):
        if not legend.get_visible():
            continue
        bbox = legend.get_window_extent(renderer)
        if (
            bbox.x0 < -BOUNDS_EPS_PX
            or bbox.y0 < -BOUNDS_EPS_PX
            or bbox.x1 > width + BOUNDS_EPS_PX
            or bbox.y1 > height + BOUNDS_EPS_PX
        ):
            issues.append(
                f"BOUNDS legend "
                f"box=({bbox.x0:.1f},{bbox.y0:.1f})–({bbox.x1:.1f},{bbox.y1:.1f}) "
                f"figure={width:.1f}×{height:.1f}"
            )

    for i in range(len(boxes)):
        text_a, box_a = boxes[i]
        area_a = max(0.0, box_a.width * box_a.height)
        if area_a <= 0:
            continue
        for j in range(i + 1, len(boxes)):
            text_b, box_b = boxes[j]
            area_b = max(0.0, box_b.width * box_b.height)
            if area_b <= 0:
                continue
            x0 = max(box_a.x0, box_b.x0)
            y0 = max(box_a.y0, box_b.y0)
            x1 = min(box_a.x1, box_b.x1)
            y1 = min(box_a.y1, box_b.y1)
            if x1 <= x0 or y1 <= y0:
                continue
            inter = (x1 - x0) * (y1 - y0)
            smaller = min(area_a, area_b)
            if inter / smaller <= OVERLAP_FRAC:
                continue
            reason = _allowed(text_a, text_b, allow)
            if reason:
                continue
            issues.append(
                f"OVERLAP {text_a!r} ∩ {text_b!r} "
                f"inter={inter:.1f} ({100 * inter / smaller:.1f}% of smaller)"
            )
    return issues


def _output_stem(stem, lang: str) -> Path:
    path = Path(stem)
    if not path.is_absolute():
        path = ROOT / path
    return path.parent / f"{path.name}-{lang}"


def save(fig, stem, lang: str, allow_overlap=None, pad_inches: float = 0.12) -> Path:
    """QC ``fig``, then write ``{stem}-{lang}.pdf`` and a 300 dpi PNG.

    Chinese PDFs are PGF/XeLaTeX. English PDFs use Matplotlib's PDF backend.
    ``allow_overlap`` whitelists deliberate collisions. Each entry is
    ``(text_a, text_b, reason)`` or ``"text_a || text_b || reason"``.
    ``pad_inches`` is the tight-bbox padding. Rotated 3D labels need more
    than the default, because the PGF glyph extends past the Agg extent.
    """
    if lang not in {"zh", "en"}:
        raise ValueError(f"lang must be 'zh' or 'en', got {lang!r}")
    setup(lang)
    issues = collect_issues(fig, allow_overlap)
    if issues:
        raise BookFigError(str(stem), lang, issues)

    out = _output_stem(stem, lang)
    out.parent.mkdir(parents=True, exist_ok=True)
    pdf_path = out.with_suffix(".pdf")
    png_path = out.with_suffix(".png")
    common = {"facecolor": "white", "bbox_inches": "tight", "pad_inches": pad_inches}
    if lang == "zh":
        fig.savefig(pdf_path, backend="pgf", **common)
        subprocess.run(
            [
                "pdftocairo",
                "-png",
                "-r",
                "300",
                "-singlefile",
                str(pdf_path),
                str(png_path.with_suffix("")),
            ],
            check=True,
            timeout=120,
        )
    else:
        fig.savefig(pdf_path, **common)
        fig.savefig(png_path, dpi=300, **common)
    print(f"bookfig: saved {pdf_path.name} and {png_path.name}")
    return pdf_path


_PDFFONTS_TYPE = re.compile(
    r"(CID Type 0C \(OT\)|CID Type 0C|CID Type 0|TrueType \(OT\)|"
    r"TrueType|Type 3|Type 1C|Type 1|MMType 1)$"
)


def _parse_pdffonts(output: str) -> list[dict[str, str]]:
    """Parse ``pdffonts`` rows.

    Subset names such as ``TeXGyreHeros-Regular-Identity-H`` are wider than
    the name column, so the rest of that row is shifted. Read emb/sub/uni
    from the right, then the type phrase, instead of slicing header columns.
    """
    fonts = []
    for raw in output.splitlines():
        line = raw.rstrip()
        if not line.strip() or line.startswith("name ") or set(line.strip()) <= {"-"}:
            continue
        tail = re.search(r"\s(yes|no)\s+(yes|no)\s+(yes|no)\s+\d+\s+\d+\s*$", line)
        if tail is None:
            continue
        head = line[: tail.start()].rstrip()
        encoding = re.search(r"\s(\S+)\s*$", head)
        if encoding is None:
            continue
        head = head[: encoding.start()].rstrip()
        type_match = _PDFFONTS_TYPE.search(head)
        if type_match is None:
            continue
        fonts.append(
            {
                "name": head[: type_match.start()].strip(),
                "type": type_match.group(1),
                "emb": tail.group(1),
            }
        )
    return fonts


def check_directory(directory: Path) -> int:
    """Run pdffonts and scripts/check_overlap.py on every PDF in ``directory``."""
    directory = directory if directory.is_absolute() else ROOT / directory
    if not directory.is_dir():
        print(f"error: not a directory: {directory}", file=sys.stderr)
        return 1
    pdfs = sorted(directory.glob("*.pdf"))
    if not pdfs:
        print(f"error: no PDFs in {directory}", file=sys.stderr)
        return 1
    overlap_script = ROOT / "scripts" / "check_overlap.py"
    failures = 0
    for pdf in pdfs:
        print(f"== {pdf.relative_to(ROOT)} ==")
        try:
            proc = subprocess.run(
                ["pdffonts", str(pdf)],
                check=True,
                capture_output=True,
                text=True,
                timeout=30,
            )
        except subprocess.CalledProcessError as exc:
            failures += 1
            print(exc.stderr or exc.stdout or "pdffonts failed")
            continue
        fonts = _parse_pdffonts(proc.stdout)
        if not fonts:
            failures += 1
            print("FONT no embedded fonts")
        for font in fonts:
            bad_type = "Type 3" in font["type"]
            bad_emb = font["emb"] != "yes"
            if bad_type or bad_emb:
                failures += 1
                print(
                    f"FONT name={font['name']!r} type={font['type']!r} emb={font['emb']!r}"
                )
        if fonts and not any("Type 3" in font["type"] or font["emb"] != "yes" for font in fonts):
            print(f"FONT ok ({len(fonts)} embedded, no Type 3)")
        overlap = subprocess.run(
            [sys.executable, str(overlap_script), str(pdf)],
            capture_output=True,
            text=True,
            timeout=60,
        )
        sys.stdout.write(overlap.stdout)
        if overlap.stderr:
            sys.stderr.write(overlap.stderr)
        if overlap.returncode != 0:
            failures += 1
    if failures:
        print(f"\n{failures} check(s) failed.", file=sys.stderr)
        return 1
    print(f"\nOK: {len(pdfs)} PDF(s) passed pdffonts and overlap checks.")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Book figure fonts and QC.")
    sub = parser.add_subparsers(dest="command", required=True)
    check = sub.add_parser("check", help="pdffonts + check_overlap.py on a figure directory")
    check.add_argument("directory", type=Path, help="Directory of PDFs, e.g. figures/ch05")
    args = parser.parse_args(argv)
    if args.command == "check":
        return check_directory(args.directory)
    return 2


if __name__ == "__main__":
    sys.exit(main())
