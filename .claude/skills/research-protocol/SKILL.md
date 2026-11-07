---
name: research-protocol
description: The mandatory research method for every research agent. Structured databases first, then industry associations, then company level evidence, with market reports only to triangulate. Defines the note template that tools/research_audit.py checks. Use before any research task.
---
# Research protocol

Research is built in three layers, in this order. Market reports (Statista, Mordor, Grand View and similar) may only
confirm a number that a layer below already supports. They never carry an argument on their own.

## Layer 1: structured databases (pull the data yourself, never quote a summary of it)
Run the fetchers and cite the clean files. Each run logs itself in data/sources.csv.

| Database | What to take from it | Command |
|---|---|---|
| UN Comtrade | Exports and imports by HS code, country and partner, 2019 to latest year, value and kg | `python3 tools/data/fetch.py comtrade --hs <codes> --reporters <M49 codes>` |
| Eurostat PRODCOM | EU sold production, exports, imports by product code | `python3 tools/data/fetch.py prodcom --product <codes>` |
| Eurostat (other tables) | Industrial production indices, short term statistics | `python3 tools/data/fetch.py eurostat --dataset <code> --filters ...` |
| World Bank Pink Sheet | Monthly prices since 1960 (nickel, copper, aluminium, ...) | `python3 tools/data/fetch.py pinksheet` |
| USGS MCS 2026 | Mine and refinery production by country, reserves, U.S. consumption | `python3 tools/data/fetch.py usgs --commodity <name>` |
| OECD STAN | Output (P1), value added (B1G), employment by ISIC sector and country | `python3 tools/data/fetch.py stan --activity <C24,...> --countries ...` |
| OECD ICIO / TiVA | Inter industry relationships, trade in value added | data-explorer.oecd.org (SDMX) |
| UNIDO INDSTAT | Global manufacturing output by ISIC | Blocked for automated access: check data/raw/unido/ for team downloads, otherwise mark blocked and ask the team |
| IEA | Critical minerals demand and supply scenarios, EV, hydrogen, LNG, WEO | www.iea.org blocks scripts: first read the team downloads in data/raw/ (for example data/raw/WorldEnergyOutlook2025.pdf, use `pdftotext`) and data/raw/iea/, otherwise WebSearch the report pages |
| SEC EDGAR | 10-K, 20-F, 8-K, XBRL financials of listed companies | `python3 tools/data/fetch.py sec --ticker <T>` |
| WHO GHO | Health and ageing indicators | `python3 tools/data/fetch.py who --indicator <code>` |
| IRENA | Renewable capacity statistics | pxweb.irena.org API or IRENASTAT pages |

`python3 tools/data/fetch.py list` shows the HS and PRODCOM codes of the Client portfolio.

## Layer 2: industry associations and official outlooks (read the original document)
OICA, ACEA, ICAO, IATA, Airbus GMF, Boeing CMO, SIPRI, IEA, IRENA, GWEC, World Nuclear Association, IAEA PRIS, Cefic,
VCI, ACC, SEMI, WSTS, ZVEI, WHO, OECD Health, MedTech Europe, INSG, ICSG, Cobalt Institute, Nickel Institute,
WorldStainless, IMOA, ITIA, International Aluminium Institute. Always use the latest edition, open the original
(WebFetch works on any site) and note the page or table.

## Layer 3: company level evidence (the part that impresses industry readers)
Use data/companies.csv (61 competitors, customers, peers and suppliers) and research/companies/*.md (profiles written by
the company-researcher). From annual reports, 10-K, 20-F, investor presentations and earnings calls take: segment
revenue and margins, end market split, capacity and expansions (furnaces, presses, plants), order books, alloy and
product form statements, named customers, guidance, and quotes on shortages or substitution, always with page numbers.

## Rules
- Every figure states what it measures (mine or refined, contained metal or gross weight, value or volume, year, unit).
- Key numbers are triangulated: two independent sources, and the difference explained.
- Latest editions only (USGS MCS 2026, Airbus GMF 2026, Boeing CMO 2026, latest SEMI and IEA releases).
- Never invent. Missing data becomes `TODO(data): what was searched and where`.

## Note template (tools/research_audit.py checks it)
```
# <Unit name>
## Key findings            (5 to 10 numbered findings, each with numbers and sources)
## <Topic sections ...>     (the eight Phase I dimensions for metals, the nine questions for sectors)
## Company evidence        (what the companies in data/companies.csv report, with page references)
## Spotlight facts          (at least 3, numbered, each dated: who, what, where, when, metal, product form, suppliers)
## Triangulation            (table: | Number | Source 1 | Source 2 | Difference and choice |, at least 3 rows)
## Source coverage          (table: | Source | Status | Evidence |, one row per required source in data/source_matrix.json,
                             status used / not applicable / blocked, evidence = data/clean file, data_id or URL, or the reason)
## Open gaps                (TODO(data) items)
```
Run `python3 tools/research_audit.py research/<folder>/<note>.md` before you report back, and fix every FAIL.
