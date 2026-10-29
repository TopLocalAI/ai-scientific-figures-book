# Chapter 1 data: USGS site 05484500 (2016)

| File | Description |
|---|---|
| `usgs-05484500-2016.rdb` | Raw NWIS daily-value download (unchanged) |
| `ch01-raccoon-2016.csv` | Parsed daily means for plotting |

## CSV fields

| Field | Meaning | Units / codes |
|---|---|---|
| `date` | Calendar day | `YYYY-MM-DD` |
| `nitrate_mgL_as_N` | Nitrate plus nitrite, in situ daily mean | mg/L as N; empty = missing |
| `nitrate_qual` | Quality code | `A` = approved |
| `discharge_cfs` | Daily mean discharge | ft³/s |
| `discharge_qual` | Quality code | `A` approved; `A:e` approved estimate (ice-affected) |

Missing nitrate days (rows kept, value blank): 2016-09-18, 2016-09-19, 2016-12-14.

Conversion used in figures: 1 ft³/s = 0.028316846592 m³/s.

## Source and license

- URL: `https://waterservices.usgs.gov/nwis/dv/?format=rdb&sites=05484500&parameterCd=99133,00060&startDT=2016-01-01&endDT=2016-12-31&statCd=00003`
- Downloaded: 2026-10-29 (see `provenance/ch01/data-download.json` for SHA-256).
- U.S. Geological Survey, National Water Information System, site 05484500, Raccoon River at Van Meter, Iowa.
- License: U.S. Federal Government work / public domain (USGS data policy).
- Citation: U.S. Geological Survey, USGS water data for the Nation, https://doi.org/10.5066/F7P55KJN .
