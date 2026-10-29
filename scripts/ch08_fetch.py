#!/usr/bin/env python3
"""Download chapter 8 raw assets (BBBC022 range extract + Commons JPEGs)."""
# SPDX-License-Identifier: MIT
import csv
import subprocess
import zipfile
from datetime import date
from pathlib import Path
from typing import List
from urllib.request import Request, urlopen

from ch08_utils import BBBC_FILES, BBBC_STATS, DATA, PROV, RAW, SOURCED, sha256, write_json

ROOT = Path(__file__).resolve().parents[1]

W1_ZIP = "https://data.broadinstitute.org/bbbc/BBBC022/BBBC022_v1_images_20585w1.zip"
W5_ZIP = "https://data.broadinstitute.org/bbbc/BBBC022/BBBC022_v1_images_20585w5.zip"
CSV_URL = "https://data.broadinstitute.org/bbbc/BBBC022/BBBC022_v1_image.csv"

SOURCED_URLS = {
    "FluorescentCells.jpg": "https://upload.wikimedia.org/wikipedia/commons/0/09/FluorescentCells.jpg",
    "Leaf_epidermis.jpg": "https://upload.wikimedia.org/wikipedia/commons/7/7c/Leaf_epidermis.jpg",
}


class HTTPRangeReader:
    """Read-only file-like object over HTTP Range requests."""

    def __init__(self, url: str, timeout: int = 60):
        self.url = url
        self.timeout = timeout
        self.pos = 0
        req = Request(url, method="HEAD")
        with urlopen(req, timeout=timeout) as resp:
            self.size = int(resp.headers["Content-Length"])

    def read(self, n: int = -1) -> bytes:
        if n == 0:
            return b""
        if n < 0:
            n = self.size - self.pos
        if self.pos >= self.size or n <= 0:
            return b""
        end = min(self.pos + n - 1, self.size - 1)
        req = Request(self.url, headers={"Range": f"bytes={self.pos}-{end}"})
        with urlopen(req, timeout=self.timeout) as resp:
            data = resp.read()
        self.pos += len(data)
        return data

    def seek(self, offset: int, whence: int = 0) -> int:
        if whence == 0:
            self.pos = offset
        elif whence == 1:
            self.pos += offset
        elif whence == 2:
            self.pos = self.size + offset
        else:
            raise ValueError(whence)
        self.pos = max(0, min(self.pos, self.size))
        return self.pos

    def tell(self) -> int:
        return self.pos

    def seekable(self) -> bool:
        return True

    def readable(self) -> bool:
        return True


def extract_zip_member(url: str, member_suffix: str, dest: Path) -> None:
    reader = HTTPRangeReader(url)
    with zipfile.ZipFile(reader) as zf:
        match = [n for n in zf.namelist() if n.endswith(member_suffix.split("/")[-1])]
        assert len(match) == 1, f"Expected one member for {member_suffix}, got {match}"
        dest.parent.mkdir(parents=True, exist_ok=True)
        with zf.open(match[0]) as src, dest.open("wb") as out:
            while True:
                chunk = src.read(1 << 20)
                if not chunk:
                    break
                out.write(chunk)


def curl_download(url: str, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ["curl", "-m", "60", "-sL", "-o", str(dest), url],
        check=True,
        timeout=90,
    )


def fetch_bbbc() -> List[dict]:
    RAW.mkdir(parents=True, exist_ok=True)
    records = []
    zip_for = {
        "hoechst_s1": W1_ZIP,
        "hoechst_s2": W1_ZIP,
        "mito_s1": W5_ZIP,
        "mito_s2": W5_ZIP,
    }
    for key, fname in BBBC_FILES.items():
        dest = RAW / fname
        need = True
        if dest.is_file():
            need = not sha256(dest).startswith(BBBC_STATS[key]["sha16"])
        if need:
            extract_zip_member(zip_for[key], fname, dest)
        records.append(
            {
                "file": str(dest.relative_to(ROOT)),
                "zip_url": zip_for[key],
                "member": fname,
                "downloaded": date.today().isoformat(),
                "sha256": sha256(dest),
                "license": "CC0 1.0 (BBBC022v1)",
            }
        )
    csv_path = DATA / "BBBC022_v1_image.csv"
    if not csv_path.is_file():
        curl_download(CSV_URL, csv_path)
    records.append(
        {
            "file": str(csv_path.relative_to(ROOT)),
            "url": CSV_URL,
            "downloaded": date.today().isoformat(),
            "sha256": sha256(csv_path),
            "license": "CC0 1.0",
        }
    )
    return records


def fetch_sourced() -> List[dict]:
    SOURCED.mkdir(parents=True, exist_ok=True)
    records = []
    for name, url in SOURCED_URLS.items():
        dest = SOURCED / name
        if not dest.is_file():
            curl_download(url, dest)
        records.append(
            {
                "file": str(dest.relative_to(ROOT)),
                "url": url,
                "downloaded": date.today().isoformat(),
                "sha256": sha256(dest),
            }
        )
    return records


def write_sourced_md(records: List[dict]) -> None:
    lines = [
        "# Chapter 8 sourced images",
        "",
        f"Verified on {date.today().isoformat()}.",
        "",
        "## S2 FluorescentCells.jpg",
        "- URL: https://commons.wikimedia.org/wiki/File:FluorescentCells.jpg",
        "- Author: NIH ImageJ sample set (Commons: public domain)",
        "- License: Public domain",
        "- Pixels: 512 × 512, 8-bit RGB JPEG",
        "- Calibration: **none** (JFIF density 1:1, no µm/pixel on Commons or ImageJ source page)",
        "",
        "## S3 Leaf_epidermis.jpg",
        "- URL: https://commons.wikimedia.org/wiki/File:Leaf_epidermis.jpg",
        "- Author: Louisa Howard, Dartmouth Electron Microscope Facility",
        "- License: Public domain (REMF catalog statement)",
        "- Pixels: 2048 × 2073, 8-bit grayscale JPEG",
        "- Calibration: instrument data bar bottom 25 px; 200 µm scale line measured by script",
        "",
        "## Downloads",
        "",
    ]
    for rec in records:
        lines.append(f"- `{rec['file']}` SHA-256 `{rec['sha256']}`")
    (PROV / "sourced.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_case_catalog() -> None:
    rows = []
    for key in ("hoechst_s1", "mito_s1", "hoechst_s2", "mito_s2"):
        path = RAW / BBBC_FILES[key]
        if not path.is_file():
            continue
        channel = "Hoechst 33342" if "hoechst" in key else "MitoTracker Deep Red"
        site = "1" if "s1" in key else "2"
        rows.append(
            {
                "filename": BBBC_FILES[key],
                "source": "BBBC022v1 plate 20585 well A13 mock",
                "site": site,
                "channel": channel,
                "size": "696x520",
                "bit_depth": "16-bit container 12-bit effective",
                "um_per_pixel": "0.656",
                "sha256": sha256(path),
                "license": "CC0 1.0",
                "status": "read-only original",
            }
        )
    out = DATA / "ch08-case-catalog.csv"
    if rows:
        with out.open("w", encoding="utf-8", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=list(rows[0].keys()))
            writer.writeheader()
            writer.writerows(rows)


def main() -> None:
    PROV.mkdir(parents=True, exist_ok=True)
    bbbc = fetch_bbbc()
    sourced = fetch_sourced()
    write_sourced_md(sourced)
    write_case_catalog()
    payload = {"bbbc": bbbc, "sourced": sourced}
    write_json(PROV / "fetch-log.json", payload)
    print("fetch complete")


if __name__ == "__main__":
    main()
