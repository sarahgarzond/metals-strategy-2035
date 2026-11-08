<!-- supersedes: nothing (new evidence pack). linked from: user request to replace terrible section prose with research results + talking points for a better writing model. user instruction: "this is terrible writing horrible. please give me the results from the research and in a separee file the talking points i should include on each section with specific data and resources so a better writing model can later write the paper" -->

# Research results (facts only)

Status: 2026-11-07. Sources live in `data/sources.csv` (~1,000 rows). Full notes in `research/materials/`, `research/sectors/`, `research/companies/` (61 profiles). Clean extracts in `data/clean/`.

**Do not treat this file as report prose.** It is the evidence pack for a later writing model.

---

## Method rules (must not be broken)

| Rule | Detail |
|---|---|
| Stages stay separate | Mine ≠ primary ≠ mill product ≠ stainless melt |
| Apparent consumption | AC = sold production + imports − exports [AC_METHOD] |
| AC caveat | PRODCOM 24452200 mixes pure nickel and nickel alloy. Use as **upper bound**, not “qualified alloy demand” |
| VDM / Haynes | One Acerinox High Performance Alloys (HPA) group. Never two competitors |
| VDM catalogue | Application **benchmark** only. Not Münvest qualifications or order book |
| Market reports | Triangulate only. Never sole source for a number |
| Missing legs | No AC figure if any of sold / import / export is missing |

---

## A. Scale ladder (nickel system)

| Stage | Figure | Year | data_id / file |
|---|---|---|---|
| World mine (contained Ni) | 3.71 Mt → est. 3.90 Mt | 2024 / 2025 | NI_USGS_MINE_W_2024, NI_USGS_MINE_W_2025 |
| Indonesia mine | 2.31 Mt → est. 2.60 Mt (~62–67%) | 2024 / 2025 | NI_USGS_MINE_ID_2024, NI_USGS_MINE_ID_2025 |
| Indonesia reserves | 62 Mt of >140 Mt world | 2025 | NI_USGS_RES_ID_2025 |
| World primary production | 3.589 Mt / 3.875 Mt | 2024 / 2025 | NI_INSG_PROD_2025 |
| World primary use | 3.473 Mt / 3.577 Mt | 2024 / 2025 | NI_INSG_USE_2025 |
| Primary surplus | 116 kt / 299 kt | 2024 / 2025 | NI_INSG_BAL_2025 |
| Surplus forecast | 19 kt (2026), 70 kt (2027) | INSG Oct 2026 | NI_INSG_BAL_2026 |
| CN+ID NPI share | ~half of primary (older vintage) | 2025–26 | NI_INSG_NPI_2025 |
| Class 1 definition | ≥99.80% Ni, LME shapes | — | NI_LME_SPEC |
| World stainless melt | 64.157 Mt | 2025 | NI_WS_MELT_2025 / CR_SS_MELT_2025_WORLD |
| China stainless melt | 40.868 Mt | 2025 | CR_SS_MELT_2025_CHN |
| EU stainless melt | 5.659 Mt | 2025 | CR_SS_MELT_2025_EU |
| Stainless share of primary Ni use | “just under 70%” (INSG qualitative) | — | nickel research note |

**Scale check:** EU stainless melt ≈ 5.7 Mt vs EU nickel flat AC ≈ 0.058 Mt. Specialty mill AC is kt-scale; stainless is Mt-scale.

Clean USGS nickel: `data/clean/usgs_mcs2026_nickel.csv`

---

## B. Apparent consumption (PRODCOM)

File: `data/clean/apparent_consumption_prodcom_2019-2024.csv`  
Cross-check DE: `data/clean/apparent_consumption_de_comtrade_crosscheck.csv`  
Note: `research/materials/apparent_consumption.md`

### Nickel flat — PRODCOM 24452200 (kg)

| Area | Year | Sold | Imports | Exports | **AC** | data_id |
|---|---|---:|---:|---:|---:|---|
| EU27 | 2024 | 80,910,705 | 14,400,156 | 37,478,164 | **57,832,697** | AC_EU_NI_FLAT_2024 |
| DE | 2024 | 30,561,000 | 17,901,184 | 18,087,152 | **30,375,032** | AC_DE_NI_FLAT_2024 |
| EU27 | 2023 | 71,394,665 | (see file) | (see file) | 53,191,380 | same file |

Reading: EU is **net exporter** of this flat code. DE imports ≈ exports → AC ≈ domestic sold production.

### Nickel bar / rod / wire — PRODCOM 24452100 (kg)

| Area | Year | Sold | Imports | Exports | **AC** | data_id |
|---|---|---:|---:|---:|---:|---|
| EU27 | 2024 | 2,500,000 | 5,577,729 | 2,697,382 | **5,380,347** | AC_EU_NI_BAR_2024 |

Reading: EU is **net importer**. Sold production cell is Eurostat `:R` (rounding base 500,000 kg) → AC band roughly 5.1–5.6 M kg.

### Nickel tube — PRODCOM 24452300 (kg)

| Area | Year | Sold | AC |
|---|---|---:|---:|
| EU27 | 2024 | 21,000,000 | 9,164,549 |
| DE | 2022 | 26,619,000 | 12,086,159 |

(Log a data_id before citing tube AC in final prose.)

### Other forms with AC (same file)

| Product | Code | EU27 2024 AC (kg) |
|---|---|---:|
| Copper plate/sheet | 24442330 | 1,706,410,405 |
| Aluminium plate/sheet | 24422430 | 632,304,677 |
| Copper wire | 24442200 | 779,482,080 |

---

## C. Trade (Comtrade)

Portfolio World partner 2019–2024: `data/clean/comtrade_portfolio_world_2019-2024.csv` [COMTRADE_PORTFOLIO_WORLD_2019_2024]  
Reporters: DE, US, CN, JP, KR, UK, IT, ID, FR (code 251), IN (code 699)  
Bilateral priority 2022–2024: `data/clean/comtrade_bilateral_priority_2022-2024.csv` [COMTRADE_BILATERAL_PRIORITY_2022_2024]

### Germany HS 7506 → World

| Year | Value USD | Net weight kg | data_id |
|---|---:|---:|---|
| 2024 | 577,777,531 | 17,775,010 | COMTRADE_7506 |
| 2023 | ~580 M | 14.2 M | COMTRADE_7506 |

PRODCOM DE export 24452200 2024: 18,087,152 kg ≈ Comtrade (gap ~1.8%).

### Top German HS 7506 export partners 2024

| Partner | USD m | kg m |
|---|---:|---:|
| Austria | 90.7 | 4.04 |
| Italy | 70.1 | 1.98 |
| China | 61.1 | 1.83 |
| USA | 55.3 | 1.54 |
| France | 53.4 | 1.29 |
| Spain | 44.8 | 1.84 |

### China HS 8101 (tungsten) 2023

Export USD 268.3 M / 5.27 M kg; import USD 56.3 M / 0.08 M kg. Partners: JP, KR, US. [COMTRADE_8101]

### Priority HS for corridors

7502, 7505, 7506, 7507, 8101, 8105, 8108, 8109, 7219, 7409, 7410, 7606, 8311, 8411  
Per-HS: `data/clean/comtrade_<hs>_2019-2024.csv` and `comtrade_<hs>_bilateral_2022-2024.csv`

---

## D. Competitor / supplier capacity (not AC)

| Fact | Value | data_id |
|---|---|---|
| Acerinox HPA melt 2025 | 83 kt alloy | NI_ACX_HPA_2025 |
| Acerinox HPA finish 2025 | 47 kt | NI_ACX_HPA_2025 |
| Acerinox HPA sales 2025 | EUR 1,683 m | NI_ACX_HPA_2025 |
| Outokumpu stainless deliveries 2025 | 1,751 kt | CO_OUTOKUMPU_DELIVERIES_2025 |
| Outokumpu Avesta high-Ni add | ~13 kt (remelt early 2028) | CO_OUTOKUMPU_HINI_CAP_2026 |
| ATI Ni use 2025 | ~70 M lb (~32 kt contained) | NI_ATI_NI_LB_2025 |

**Do not** say EU flat AC “sits under” 83 kt melt as if Acerinox covers Europe. Finished 47 kt is worldwide, all forms. Output ≠ nameplate.

Profiles: `research/companies/acerinox.md`, `outokumpu.md`, `ati.md`, `haynes.md`, `special-metals.md`, …

---

## E. ICIO / UNIDO / STAN

| Dataset | File | Use |
|---|---|---|
| OECD ICIO metal→demand | `data/clean/icio_2019_2022_metal_use_by_industry.csv` | C24A/C24B → demand industries |
| ICIO output/VA | `data/clean/icio_2019_2022_output_va_focus.csv` | Focus countries |
| World C24B→C27 2022 | ~USD 220 bn | ICIO_2022_WORLD_C24B_TO_C27 |
| World C24B→C29 2022 | ~USD 109 bn | ICIO_2022_WORLD_C24B_TO_C29 |
| UNIDO INDSTAT | `data/clean/unido_indstat_rev4_focus_1991-2023.csv` | 132 countries |
| OECD STAN | `data/clean/oecd_stan_P1.csv`, `oecd_stan_B1G.csv` | Sector output (not alloy t) |

---

## F. Sector headlines

| Sector | Keep these facts | Full note |
|---|---|---|
| Aerospace | Fleet 23,310 (2025) → 45,550 (2045); 42,060 deliveries; ~32,600 in 2035 = **team** interpolate; LEAP 1,802 (+28%) 2025; GE +25% = 9M **2026**; aviation Co 11,499 t; ATI aero/def ~68% | `research/sectors/aerospace.md` |
| Automotive | EV share; turbo/exhaust/sensor alloys; glow plugs decline | `research/sectors/automotive.md` |
| Oil & gas | Spend ~USD 570 bn 2025; **no** USD 670 bn; CP ~USD 65 bn/yr above STEPS | `research/sectors/oil_gas.md` |
| Energy / H2 | Electrolyser / SOEC / interconnect; funded projects only | `research/sectors/energy_environment.md` |
| Chemical | Replacement CAPEX; corrosion plate + weld wire | `research/sectors/chemical.md` |
| Electronics | Expansion / soft magnetic / resistance strip | `research/sectors/electronics.md` |
| Medical | Implant CoCr / Zr; DE/CH/AT; J&J ortho spin | `research/sectors/medical.md` |

---

## G. Coverage and gaps

**Present:** 10 metal notes + trade + AC; 7 sectors; 61 companies; Comtrade 27 HS; bilateral 14 HS; PRODCOM AC; USGS; Pink Sheet; ICIO; UNIDO; STAN.

**Open:** HS 750610/750620 split; Acerinox nameplate by plant; Co/Ti/W mill AC; IEA CME raw file; customer tonnes/margins (A4).

---

## H. How to use with the talking-points file

1. Numbers → this file + `data/sources.csv`
2. Argument per chapter → `reviews/talking_points_by_section.md`
3. Spotlights / caveats → `research/**/*.md`
4. Logic fixes from graders → `reviews/round_1/fixes.md`
5. Discard current `sections/*.md` prose quality; replace from these packs

---

## I. Scenario indices and plant rules (writer lock after round 1, 2026-11-07)

Canonical after [writer](8c43a4f3-a5b7-4e9f-a258-2f485a5ef524) applied fixes 1–15 (`reviews/round_1/applied.md`). Supersedes earlier [strategist](44b96c75-4373-4577-9854-d926424cff05) caps where they differ. Draft prose: `sections/07_scenarios.md`, `sections/08_recommendations.md`. Prefer this pack + talking points over that prose style.

### Index formula
2035 index = 100 × (1 + annual rate)^10. Prices/FX constant. **Do not** multiply by AC tonnes.

### 2035 indices (2025 = 100) — live Table in `sections/07_scenarios.md`

| Industry | Down | Base | Up | Rates |
| --- | ---: | ---: | ---: | --- |
| Automotive | 82 | 90 | **105** | -2 / -1 / **+0.5** % |
| Oil and gas | 90 | 105 | 116 | -1 / +0.5 / +1.5 % |
| Energy, committed programmes | 100 | 134 | 179 | 0 / +3 / +6 % |
| Aerospace and IGT | 110 | 134 | 155 | +1 / +3 / +4.5 % |
| Chemicals | 95 | 116 | 134 | -0.5 / +1.5 / +3 % |
| Electronics and electrical | 100 | 128 | 155 | 0 / +2.5 / +4.5 % |
| Medical implant alloys | 105 | 122 | 141 | +0.5 / +2 / +3.5 % |

Unrounded values → Appendix A2. Auto upside ID: TE_AUTO_UPSIDE_2035.

### Hard commercial rules
| Rule | Detail |
| --- | --- |
| Flat AC | 57.8 M kg = mixed-code **ceiling** only [AC_EU_NI_FLAT_2024] |
| Bar AC | Net import; no capacity vote until UK + HS 7502 footnotes [AC_EU_NI_BAR_2024] |
| Aero forms | Billet / approved sheet / repair wire on HS 7505 + 7502 |
| Alloy plate | HS 750620 once split exists |
| Ch. 72/74 book | Expansion, Crofer 22, Aluchrom, Konstantan, soft magnetic |
| Ni 201 strip | Unalloyed HS 7506 |
| HPA once | 83 kt melt / **47 kt finish** worldwide all forms / EUR 1,683 m [NI_ACX_HPA_2025]. Not a European capacity ceiling |
| Sample gates | **≤5 accounts**; **EUR 200,000 per account** sample cap (team planning) [TE_PLAN_ACCOUNTS, TE_PLAN_SAMPLE]; company hurdle rate |
| Stop list | Glow plugs as growth; undifferentiated stainless; China implants; unfunded H2; powders; Cu/Al plate without three-leg AC |
| Fix 16 | **Rejected**: no flat-vs-bar chart / scenario fan (would repeat tables) |
| Withheld | Outokumpu 5.5–12% Ni range (not in logged row); Acerinox melt footnote verbatim (not in logged row → A4) |
| Aviation Co | Keep logged **72%** commercial share (not 73% = DRC mine share) |

### Extra IDs introduced in ch.7–8
TE_AUTO_UPSIDE_2035; TE_PLAN_ACCOUNTS; TE_PLAN_SAMPLE; WSTS_WORLD_2025; OG_WEI2026_*; EE_H2_*; MED_OECD_HK_COUNT_2023; MED_CRS_MED_EXSUR_2026; CO_GE_CES_2025; CO_SAFRAN_PROP_2025; CO_MTU_REV_2025; CO_HAYN_SYN_2026; CO_SIEMENSENERGY_CMD_2025; CO_PCC_REV_2025; CO_ATI_*; CO_CRS_*; CO_TKNUCERA_ORDERS_2025; AERO_AIRBUS_GSF2026_SERVICES_2045; AERO_CI_AVIATION_CO_2025
