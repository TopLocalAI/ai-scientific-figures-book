# Assets and sources / 素材与数据来源登记

中文说明：本表登记书中使用的全部第三方数据与图像，以及本书原创的生成图与模拟数据；第三方素材按其原许可使用，不受本书 CC BY 4.0 / MIT 覆盖。

Downloads were made on 2026-10-29. SHA-256 hashes are recorded in the provenance files named below. Third-party material stays under its provider's terms. The repository's CC BY 4.0 (text, figures, data) and MIT (code) licences cover only material the contributors hold rights in (see `LICENSE`). Figure ids such as `ch04-05` refer to `figures/chNN/chNN-NN-*` files, in both `-zh` and `-en` versions.

## 1. External datasets

| Dataset | Provider | URL | Licence (as stated by provider) | Used in | Copy in this repo | Required citation |
| --- | --- | --- | --- | --- | --- | --- |
| Daily values, site 05484500 Raccoon River at Van Meter, IA, 2016; parameters 99133 (nitrate + nitrite, mg/L as N) and 00060 (discharge) | U.S. Geological Survey, NWIS | `https://waterservices.usgs.gov/nwis/dv/?format=rdb&sites=05484500&parameterCd=99133,00060&startDT=2016-01-01&endDT=2016-12-31&statCd=00003` | U.S. federal government work, public domain (USGS data policy) | ch01-03, ch01-04, ch01-07 | `data/ch01/usgs-05484500-2016.rdb` (raw, unchanged); `data/ch01/ch01-raccoon-2016.csv` (parsed). Script: `scripts/ch01_fetch_usgs.py`. Record: `provenance/ch01/data-download.json` | U.S. Geological Survey, USGS water data for the Nation, NWIS site 05484500, https://doi.org/10.5066/F7P55KJN |
| palmerpenguins v0.1.0 `penguins.csv` | Allison Horst, Alison Hill, Kristen Gorman; data from Palmer Station LTER | https://raw.githubusercontent.com/allisonhorst/palmerpenguins/v0.1.0/inst/extdata/penguins.csv | CC0 1.0 | ch05-01, ch05-02, ch05-05, ch05-08 | `data/ch05/penguins.csv`. Script: `scripts/ch05_figures.py`. Record: `data/ch05/penguins-README.md` | Horst, Hill & Gorman (2020), https://doi.org/10.5281/zenodo.3960218; Gorman, Williams & Fraser (2014), PLoS ONE, https://doi.org/10.1371/journal.pone.0090081 |
| Mauna Loa monthly mean CO₂ (`co2_mm_mlo.csv`, file creation 2026-10-09) | NOAA Global Monitoring Laboratory; Scripps Institution of Oceanography | https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_mm_mlo.csv | U.S. government work, public domain. File header: data "made freely available to the public", with credit requested | ch04-05 (and the ch04-01, ch04-08 contact sheets); ch05-04, ch05-06, ch05-07 | Three identical copies (same SHA-256): `data/ch04/raw/co2_mm_mlo.csv`, `data/ch05/co2_mm_mlo.csv`, `data/ch05/noaa-co2-mm-mlo-2026-10-09.csv`. Scripts: `scripts/fetch_ch04_data.py`, `scripts/ch05_figures.py`. Records: `data/ch04/SOURCES.json`, `data/ch05/noaa-co2-README.md` | NOAA GML (X. Lan) and Scripps CO₂ Program (R. F. Keeling), as in the file header |
| Hawaii Ocean Time-series surface CO₂ system data (`HOT_surface_CO2.txt`) | HOT program, University of Hawaiʻi (J. E. Dore) | https://hahana.soest.hawaii.edu/hot/hotco2/HOT_surface_CO2.txt | **No licence stated.** The file header asks for a citation, which is not an open licence | ch04-05 (and the ch04-01, ch04-08 contact sheets) | `data/ch04/raw/HOT_surface_CO2.txt`. Script: `scripts/fetch_ch04_data.py`. Record: `data/ch04/SOURCES.json` | Dore, J. E., Lukas, R., Sadler, D. W., Church, M. J. & Karl, D. M. (2009). PNAS 106: 12235–12240 |
| World Ocean heat content, 0–700 m and 0–2000 m, pentadal (`pent_h22-w0-700m.dat`, `pent_h22-w0-2000m.dat`) | NOAA NCEI | https://www.ncei.noaa.gov/data/oceans/woa/DATA_ANALYSIS/3M_HEAT_CONTENT/DATA/basin/pentad/ | U.S. government work, public domain | ch04-03, ch04-06 (and the ch04-01, ch04-08 contact sheets) | `data/ch04/raw/pent_h22-w0-700m.dat`, `data/ch04/raw/pent_h22-w0-2000m.dat`. Script: `scripts/fetch_ch04_data.py`. Record: `data/ch04/SOURCES.json` | Levitus et al. (2012), and updates |
| Global Carbon Budget 2025 (`GlobalCarbonBudget_v2025.xlsx`, sheet "Global Carbon Budget") | Global Carbon Project | https://globalcarbonbudget.org/download/2341/ (data hub: https://globalcarbonbudget.org/data-hub/the-latest-gcb-data-2025/) | Fair Use Statement: data "freely available", and use is conditional on citation and acknowledgement. **No open licence stated; licence to confirm** | ch04-07 (and the ch04-01, ch04-08 contact sheets) | `data/ch04/raw/GlobalCarbonBudget_v2025.xlsx`. Script: `scripts/fetch_ch04_data.py`. Record: `data/ch04/SOURCES.json` | Friedlingstein et al. (2025), Global Carbon Budget 2025, Earth Syst. Sci. Data. The Fair Use Statement also requires an acknowledgement of the Global Carbon Project |
| BBBC022v1 Cell Painting: plate 20585, well A13 (mock/DMSO), sites 1–2, channels w1 (Hoechst 33342) and w5 (MitoTracker Deep Red); 696 × 520 px, 0.656 µm/px | Broad Bioimage Benchmark Collection (Anne Carpenter, Broad Institute) | https://bbbc.broadinstitute.org/BBBC022 (archives `BBBC022_v1_images_20585w1.zip`, `..._20585w5.zip`) | CC0 1.0 (confirmed on the dataset page) | ch08-01, ch08-02, ch08-03, ch08-04, ch08-08 (v1 and final) | Four TIFFs, `data/ch08/raw/IXMtest_A13_*.tif`; catalogue `data/ch08/ch08-case-catalog.csv`. Script: `scripts/ch08_fetch.py`. Record: `provenance/ch08/fetch-log.json` | Gustafsdottir et al. (2013), PLoS ONE; Ljosa, Sokolnicki & Carpenter (2012), Nat. Methods 9: 637, https://doi.org/10.1038/nmeth.2083 |
| BBBC022v1 image metadata (`BBBC022_v1_image.csv`) | Broad Bioimage Benchmark Collection | https://data.broadinstitute.org/bbbc/BBBC022/BBBC022_v1_image.csv | CC0 1.0 | Read by `scripts/ch08_fetch.py` to locate well A13 | `data/ch08/BBBC022_v1_image.csv` (full file, 37 MB) | As above |

## 2. External images

| Image | Author / rights holder | Provider and URL | Licence (as stated) | Used in | Copy in this repo | Modifications | Required citation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `Leaf_epidermis.jpg`: SEM of the *Nicotiana alata* upper leaf epidermis, Zeiss 962; 2048 × 2073 px, 8-bit grey | Louisa Howard, Dartmouth Electron Microscope Facility | Wikimedia Commons, https://commons.wikimedia.org/wiki/File:Leaf_epidermis.jpg (file: https://upload.wikimedia.org/wikipedia/commons/7/7c/Leaf_epidermis.jpg) | Public domain (Commons `PD-author`; facility statement) | ch08-05; ch08-07 (ai-enhancement, generative-risk); `figures/ch08/ch08-07-ai-upscaled-{1,2,3}.png` | `data/ch08/sourced/Leaf_epidermis.jpg` (unchanged); derived input `data/ch08/fig07-input-lowres.png` | ch08-05: cropped, with an inset and a scale bar taken from the instrument data bar. ch08-07: crop (640, 680, 1152, 1192), 4 × 4 area average to 128 × 128 px, then bicubic and generative upscaling (`provenance/ch08/codex-upscale.md`) | Louisa Howard, Dartmouth Electron Microscope Facility, via Wikimedia Commons (public domain) |
| `FluorescentCells.jpg`: bovine pulmonary artery endothelial cells (Molecular Probes demo slide; DAPI, tubulin, F-actin); 512 × 512 px RGB JPEG, no calibration | Not credited; NIH ImageJ sample image set | Wikimedia Commons, https://commons.wikimedia.org/wiki/File:FluorescentCells.jpg (file: https://upload.wikimedia.org/wikipedia/commons/0/09/FluorescentCells.jpg; origin http://rsb.info.nih.gov/ij/images/) | Public domain (Commons `PD-USGov`; "example image from the ImageJ package") | ch08-06 | `data/ch08/sourced/FluorescentCells.jpg` (unchanged) | Shown without a scale bar, with display annotations | NIH ImageJ sample image, via Wikimedia Commons (public domain) |
| `Leaf_epidermis_w_scale.jpg`, `Misc_pollen.jpg`, `Misc_pollen_colorized.jpg` | Dartmouth Electron Microscope Facility (derivative scale bar by Laitr Keiows) | Wikimedia Commons (URLs in `production/plans/ch08.md`) | Public domain | Named in the ch08 text only | Not redistributed; no figure | — | URL given in the text |

`provenance/ch08/sourced.md` lists both redistributed images with their SHA-256 hashes. Chapters 1, 6, 7 and 13 use no external images (`provenance/ch01/sourced.md`, `ch06/sourced.md`, `ch07/sourced.md`, `ch13/sourced.md`). The book reproduces no figure from any cited paper.

## 3. Generated and simulated material

**Generated images.** Codex's built-in image tool (`image_gen.imagegen`) made these files:

- the raster schematics, drafts and alternates (`*-alt1`, `*-alt2`) in `figures/ch01`–`ch12`;
- `figures/mechanism-codex.png`;
- the cover concepts in `figures/cover/`;
- `cases/ch07-insulin-glut4/images/`.

The tool reported no model name, version or seed, so we do not claim pixel-identical regeneration. Each chapter keeps its prompts, call records, hashes and visual reviews in `provenance/chNN/codex-images.md`, with `.json` records where present. The mechanism figure's prompt is in `provenance/mechanism-prompt.txt`, and the cover's is in `figures/cover/concepts/concepts.md`.

These outputs are original teaching material, released with the book under CC BY 4.0 to the extent such rights exist (see `LICENSE`). They show stipulated teaching scenarios, not research findings. For example, the R/K/P/I relationships in `mechanism-codex.png` are teaching assumptions, and the review checks the image against those assumptions, not against biology. The three `ch08-07-ai-upscaled-*.png` images are generative edits of the public-domain leaf crop above. They are deliberate counter-examples, not data.

**Data figures and TikZ.** Deterministic scripts in `scripts/` draw the Python figures from the data above. The TikZ figures (`figures/**/*.tex`) are original. `figures/workflow-*.tex` are MIT.

**Simulated data.** Every file below is labelled as simulated or original:

| File | Made by | Used in |
| --- | --- | --- |
| `data/paired-example.csv` (copies in `data/ch02/`, `data/ch05/`) | Built by hand: 8 fictional objects (`data/README.md`) | `figures/paired-comparison-*`, ch02-07, ch05-03 |
| `data/sim-perovskite-jv.csv`, `-jv-metrics.csv`, `-stability.csv`, `-stability-t80.csv` | `scripts/sim_perovskite.py` | ch09-05 to ch09-07; ch12; ch13 |
| `data/ch10/simulated/ch10-06-final-base-en.png` | `scripts/ch10_thumbnail_test.py` (flat placeholder art) | Fallback for ch10-07 |
| `data/ch11/ch11-object-counts.csv` | `scripts/ch11_diff_check.py` (counts objects in generated images) | ch11-05 |
| `data/ch12/poster-c0-text-{zh,en}.md` | Original text | ch12-06 |

**Screenshots.** `figures/workflow-ui-{zh,en}.png` and their copies `figures/ch01/ch01-08-guide-ui-{zh,en}.png` are browser screenshots of a local SciDraw AI development page. They were taken logged out and show no account details. They are not evidence of a public deployment. Product names and logos are not licensed as trademarks. The planned screenshots (`ch05-scivis-v*`, ch06-05 panel B, ch13-07) are not in the repository yet.
