# Apparent consumption (production + imports − exports)

<!-- supersedes: nothing. linked from: chapter 4/6 triangulation. user request 2026-11-07. -->

## Method
Apparent consumption (AC) is calculated from Eurostat PRODCOM as:

AC = sold production quantity + imports quantity − exports quantity

(and the same formula in EUR where all three value series exist). This is a trade-balance identity for the reporting area. It is not end-use alloy demand and it is not stainless melt tonnage. Units follow PRODCOM (typically kg for these mill products). Source file: `data/clean/apparent_consumption_prodcom_2019-2024.csv` [AC_METHOD].

Germany trade legs are cross-checked against Comtrade World-partner net weight for the matching HS code in `data/clean/apparent_consumption_de_comtrade_crosscheck.csv`.

## Key results (latest complete year)

| Area | Year | Product (PRODCOM) | Sold prod. kg | Imports kg | Exports kg | Apparent consumption kg |
|---|---|---|---:|---:|---:|---:|
| EU27 | 2024 | Nickel flat 24452200 | 80,910,705 | 14,400,156 | 37,478,164 | 57,832,697 [AC_EU_NI_FLAT_2024] |
| Germany | 2024 | Nickel flat 24452200 | 30,561,000 | 17,901,184 | 18,087,152 | 30,375,032 [AC_DE_NI_FLAT_2024] |
| EU27 | 2024 | Nickel bar/rod/wire 24452100 | 2,500,000 | 5,577,729 | 2,697,382 | 5,380,347 [AC_EU_NI_BAR_2024] |
| EU27 | 2024 | Nickel tube 24452300 | 21,000,000 | 4,652,340 | 16,487,791 | 9,164,549 |
| EU27 | 2024 | Copper plate/sheet 24442330 | 1,963,235,208 | 47,911,734 | 304,736,537 | 1,706,410,405 |
| EU27 | 2024 | Aluminium plate/sheet 24422430 | 440,000,000 | 263,926,183 | 71,621,506 | 632,304,677 |

Germany nickel flat AC has been about 30 to 40 million kg since 2020, close to domestic sold production, because imports and exports nearly offset [AC_DE_NI_FLAT_2024].

## Triangulation rules for the report
1. **Vs Comtrade:** German HS 7506 export weight in 2024 was about 17.8 million kg (Comtrade), while PRODCOM DE export quantity for 24452200 was about 18.1 million kg. Directionally consistent; small gaps come from coverage, timing and product definition. Prefer PRODCOM for EU AC, Comtrade for partner corridors.
2. **Vs market reports:** Use paid market reports only to triangulate order of magnitude. Never as the sole source. Label any remaining gap as TODO(data) or team estimate with appendix assumptions.
3. **Vs supplier capacity:** Company melt or finishing capacity (Acerinox HPA, Outokumpu, ATI, etc. in `research/companies/`) is a supply ceiling, not AC. AC below named capacity is consistent; AC above a single mill’s capacity implies multi-supplier sourcing.
4. **Vs stainless production:** World and EU stainless melt (ISSF / association figures in metal notes) is a different universe (mostly Fe-Cr-Ni commodity flat). Specialty nickel alloy AC (tens of kt in the EU) is a thin layer on top of stainless melt (tens of Mt). Do not equate AC of 24452200 with stainless demand.

## Open gaps
- TODO(data): PRODCOM sold production missing for some DE years/products (flags in raw). No AC row without all three legs.
- TODO(data): No PRODCOM for cobalt, titanium, tungsten mill forms in the current clean extract; AC for those metals needs Comtrade plus national production, which is incomplete.
- Stainless melt series for the same years should be cited from the chromium/nickel notes when comparing scale.
