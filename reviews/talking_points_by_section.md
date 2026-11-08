<!-- supersedes: nothing (new writing brief). linked from: user request for talking points per section with data and resources for a better writing model. user instruction: "this is terrible writing horrible. please give me the results from the research and in a separee file the talking points i should include on each section with specific data and resources so a better writing model can later write the paper" -->

# Talking points by section (writing brief)

Companion to `reviews/research_results.md`. For each TOC heading: **claim to make**, **numbers to use**, **sources / files**, **caveats**, **spotlights**. Not finished prose.

Citation markers: `[DATA_ID]` → (Author, Year). Log any new number in `data/sources.csv` before the final draft cites it.

---

## 1. Introduction

**Talking points**
- Central question is metal-first: production, availability, trade and industrial uses → opportunities in high-performance materials to 2035.
- Audience is the client board and alloy industry experts (TUM project study).
- Report sequence: metal markets → industry needs → trade → scenarios → recommendations.
- VDM Metals catalogue is an **application benchmark**, not proof of Münvest capability.

**Data / resources**
- `data/toc.json`, `CLAUDE.md` central question
- Client naming: industry chapters say “the company”; elsewhere follow draft names
- Acerinox owns VDM and Haynes → count HPA once

**Do not**
- Invent TAM / EUR 50.6 bn unless labelled team estimate and methodology allows
- Open with buzzwords or “exciting growth stories”

---

## 2. Report Objective and Scope

**Talking points**
- Objective: how selected metals shape opportunities for the company through 2035.
- Scope metals: Ni, Co, Cr, Mo, Ti, W + Zr, Cu, Al, Mn (and “additional” only if evidence exists).
- Scope industries: automotive, oil and gas, energy/environment, aerospace, chemical, electronics, medical.
- Deliverables: ≤30 pages body + references/appendices; later deck and Metals Atlas.

**Data / resources**
- `data/toc.json`
- `data/companies.csv` for competitor / customer universe
- Phase III criteria list in `model/model.py` (attractiveness, growth, fit, …) for forward pointer only

---

## 3. Analytical Framework and Methodology

**Talking points**
1. Four dimensions **as designed**: Supply / Trade / Demand / Outlook.
2. Chapter map: 4 = Supply, 6 = Trade, 5 = Demand, 7 = Outlook, 8 integrates.
3. Metal-first sequence (not industry-first).
4. Data chain: Material → Product form → Application → Industry → Geography → Market size → Growth.
5. Apparent consumption identity: AC = sold production + imports − exports [AC_METHOD].
6. PRODCOM 24452200 mixes pure Ni and Ni alloy → **upper bound**, not qualified demand.
7. Assessment criteria chapter 8 uses (name them; weights live in model.py).
8. Optional one short table: dimensions ↔ data chain (only allowed refinement → log in `reviews/framework_changes.md`).

**Data / resources**
- Team framework text in Google Doc / imported chapter 3
- `research/materials/apparent_consumption.md`
- `data/clean/apparent_consumption_prodcom_2019-2024.csv`
- ICIO / UNIDO / STAN as **supporting** industry structure, not alloy tonnes: `data/clean/icio_*`, `unido_*`, `oecd_stan_*`

**Numbers to cite**
- AC_METHOD; AC_EU_NI_FLAT_2024 (57.8 M kg); AC_DE_NI_FLAT_2024 (30.4 M kg); AC_EU_NI_BAR_2024 (5.4 M kg)
- Optional ICIO: ICIO_2022_WORLD_C24B_TO_C27 (~220 bn USD), C24B_TO_C29 (~109 bn)

---

## 4. Metal Markets: Production & Form

### Shared spine for every metal subsection
1. Commercial forms (what mills sell: plate, strip, bar, wire, tube, powder…).
2. Production stages (mine → intermediate → primary → mill product). Keep stages separate.
3. Producer structure (countries / firms; concentration).
4. Availability and prices (USGS + Pink Sheet where relevant).
5. Link to chapter 5 applications and chapter 6 HS codes.
6. Close with implication for the company (form + qualification, not generic “grow”).

**Master resources for all metals**
- Notes: `research/materials/<metal>.md` + `<metal>_trade.md` + `<metal>.sources.csv`
- USGS MCS: `data/clean/usgs_*` / `data/raw/`
- Pink Sheet: World Bank via fetch
- PRODCOM AC where built: `apparent_consumption_prodcom_2019-2024.csv`
- Comtrade: `comtrade_<hs>_*.csv`

---

### 4.1 Nickel

**Talking points**
- Mine supply concentrated in Indonesia (2.31 Mt 2024 → 2.60 Mt est. 2025; ~62–67% of world).
- Primary surplus 116 kt (2024) / 299 kt (2025); forecast surplus shrinks 2026–27 but stays positive.
- NPI / Class 1 distinction: Class 1 ≥99.80% Ni for melting feedstock of specialty alloys.
- Stainless melt world 64.2 Mt (2025); stainless takes ~70% of primary Ni use → specialty is the minority residual.
- EU nickel flat AC 57.8 M kg (2024); DE 30.4 M kg; EU net exporter of flat.
- EU bar/rod/wire AC 5.4 M kg; EU net importer.
- Acerinox HPA: 83 kt melt / 47 kt finish / EUR 1,683 m sales (2025) = competitor capacity, **not** EU AC.
- Outokumpu stainless deliveries 1,751 kt; Avesta high-Ni add ~13 kt early 2028.
- ATI ~70 M lb Ni use (~32 kt contained) 2025.

**Must-cite IDs**
NI_USGS_MINE_W_2024/2025, NI_USGS_MINE_ID_*, NI_INSG_PROD/USE/BAL_2025, NI_INSG_BAL_2026, NI_LME_SPEC, NI_WS_MELT_2025, AC_EU_NI_FLAT_2024, AC_DE_NI_FLAT_2024, AC_EU_NI_BAR_2024, NI_ACX_HPA_2025, CO_OUTOKUMPU_DELIVERIES_2025, CO_OUTOKUMPU_HINI_CAP_2026, NI_ATI_NI_LB_2025

**Files**
`research/materials/nickel.md`, `nickel_trade.md`, `apparent_consumption.md`, `data/clean/usgs_mcs2026_nickel.csv`

**Caveats**
- Never equate flat AC with “alloy demand for Münvest”.
- Never say HPA melt “covers” EU AC.

---

### 4.2 Cobalt

**Talking points**
- Mine / refined split; DRC mine dominance; China refining.
- Battery vs superalloy / hardmetal share (use Cobalt Institute / USGS; label shares carefully).
- Aerospace and medical CoCr as high-value residual, not volume story.
- Price volatility → inventory and contract implications for alloy makers.

**Resources**
`research/materials/cobalt.md`, `cobalt_trade.md`, `cobalt.sources.csv`
`data/raw/aerospace/cobalt_institute_cmr2025.pdf`, `usgs_mcs2026_cobalt.pdf`
Comtrade HS 8105: `comtrade_8105_*`

**TODO if missing**
Mill-form AC for Co not built → `TODO(data)` or stay qualitative.

---

### 4.3 Chromium

**Talking points**
- Ferrochrome / stainless linkage; South Africa / Kazakhstan / Turkey structure as in USGS.
- Stainless melt China 40.9 Mt / EU 5.7 Mt / world 64.2 Mt (2025) [CR_SS_MELT_2025_*].
- Specialty duplex / Ni-Cr alloys are thin relative to stainless melt.

**Resources**
`research/materials/chromium.md`, `chromium_trade.md`, `chromium.sources.csv`

---

### 4.4 Molybdenum

**Talking points**
- By-product copper mines vs primary; Chile / China / USA structure.
- Role in stainless (316/317), duplex, Ni alloys, tool steels.
- Forms: FeMo, Mo oxide, mill Mo products.

**Resources**
`research/materials/molybdenum.md`, `molybdenum_trade.md`, `molybdenum.sources.csv`

---

### 4.5 Titanium

**Talking points**
- Sponge → melt → mill products; aerospace qualification lag.
- USGS MCS titanium; sponge country concentration.
- Mill product trade HS 8108 (see Comtrade files).
- Airbus / Boeing fleet growth drives mill Ti demand (link 5.4).

**Resources**
`research/materials/titanium.md`, `titanium_trade.md`
`data/raw/aerospace/usgs_mcs2026_titanium.pdf`
`comtrade_8108_*`

---

### 4.6 Tungsten

**Talking points**
- China dominance in mine and intermediate; EU dependence.
- China HS 8101 2023: export USD 268.3 M / 5.27 M kg vs import USD 56.3 M / 0.08 M kg [COMTRADE_8101].
- Cemented carbide vs alloy / heavy metal applications.

**Resources**
`research/materials/tungsten.md`, `tungsten_trade.md`
`data/clean/prodcom_tungsten_ds059358.csv`, `comtrade_8101_*`

---

### 4.7 Other Selected Metals

#### 4.7.1 Zirconium
- Nuclear / chemical / medical; sponge and mill forms.
- `research/materials/zirconium.md`, `zirconium_trade.md`, `prodcom_zirconium_codes.csv`, Comtrade 8109.

#### 4.7.2 Copper
- Scale dwarfs specialty Ni: EU Cu plate AC 2024 ≈ 1.71 bn kg.
- Electrification / busbar / connector; link electronics and energy.
- `copper.md`, `copper_trade.md`; PRODCOM 24442330 / 24442200.

#### 4.7.3 Aluminium
- Aerospace plate / automotive body; EU Al plate AC ≈ 632 M kg 2024.
- `aluminium.md`, `aluminium_trade.md`; PRODCOM 24422430.

#### 4.7.4 Manganese
- Steel / stainless / battery Mn; keep stages clear.
- `manganese.md`, `manganese_trade.md`.

#### 4.7.5 Additional Metals
- Only if research note has sourced facts; otherwise drop or one sentence “out of scope for AC”.

---

## 5. Industry Needs

**Shared rules for every 5.x**
- Numbered table + italic Sources line.
- Close with **“What the company should do:”** (concrete forms, industries, regions, qualification path).
- ≥3 spotlight facts: who / what / where / when / metal / form / likely suppliers.
- Link metals from chapter 4; do not re-litigate mine statistics.

---

### 5.1 Automotive

**Talking points**
- Historical production / EV share from OICA, ACEA, IEA GEO (files under `data/raw/iea/`).
- Alloy pockets: turbo, exhaust, sensors, connectors, battery interconnect (Cu/Ni), glow-plug decline.
- ICIO metal→auto: C24B→C29 world ~USD 109 bn 2022 (structure, not alloy tonnes).
- Company action: specify forms (strip, wire, foil) and platforms, not “EV opportunity”.

**Resources**
`research/sectors/automotive.md`, `automotive.sources.csv`
Eurostat STS: `data/raw/eurostat_sts_inpr_a_C29.json`
ICIO clean files

---

### 5.2 Oil and Gas

**Talking points**
- Upstream / midstream spend ~USD 570 bn 2025 (**not** 670).
- Corrosion-resistant alloys: CRA tubing, clad plate, weld overlay, flanges.
- LNG / CCS / H2 pipelines as incremental CRA demand (fund with IEA trackers; team downloads in `data/raw/`).
- Company action: OCTG / cladding / welding consumables by basin and project list.

**Resources**
`research/sectors/oil_gas.md`, `oil_gas.sources.csv`
Company notes: Tenaris, Vallourec, Baker Hughes, etc. if in `research/companies/`

**Hard fix from round 1**
Never cite USD 670 bn.

---

### 5.3 Energy and Environmental Technology

**Talking points**
- Power, renewables, electrolysers, fuel cells, environmental equipment.
- Materials: Ni-based for SOEC / interconnects; specialty stainless; Cu for conductors.
- Only count **funded / FID** projects when sizing near-term demand.
- Company action: stack OEMs, EPC, and replacement cycles.

**Resources**
`research/sectors/energy_environment.md`, `energy_environment.sources.csv`
IRENA / IEA (WebSearch + manual PDFs in `data/raw/iea/`)

---

### 5.4 Aerospace

**Talking points**
- Airbus GMF: fleet 23,310 (2025) → 45,550 (2045); 42,060 new deliveries over horizon.
- Team interpolate ~32,600 aircraft in service in 2035 (label **team estimate**).
- Engine: Safran LEAP 1,802 engines (+28%) in 2025; GE Aerospace commercial engines +25% in **first 9 months of 2026** (not FY).
- Cobalt Institute: aviation Co consumption 11,499 t; keep logged **72%** commercial share (not 73% DRC mine share).
- ATI aerospace/defense ~68% of sales (company report year in note).
- Forms: disc billet, ring, plate, sheet, fastener wire, powder for AM.
- Company action: OEM / Tier-1 qualification timeline; forge vs mill product entry.

**Resources**
`research/sectors/aerospace.md`, `aerospace.sources.csv`
`data/raw/aerospace/airbus_gmf_2026_presentation.pdf`, `airbus_gsf_2026_presentation.pdf`
Companies: `airbus.md`, `safran.md`, `rolls-royce.md`, `mtu.md`, `ati.md`

**Hard fixes from round 1**
- GE period = 9M 2026.
- Do not invent “USD 217 bn off-wing” (removed).

---

### 5.5 Chemical Processing

**Talking points**
- CAPEX replacement and corrosion failures drive alloy plate, tube, clad, weld wire.
- Alloys: Ni-Cr-Mo (e.g. C-276), Zr where required, duplex/superduplex.
- Geography: DE / Benelux / US Gulf / China chemical parks.
- Company action: MRO distributors + EPC specs; thickness and weld consumables.

**Resources**
`research/sectors/chemical.md`, `chemical.sources.csv`
Cefic / company filings in company research folder

---

### 5.6 Electronics and Electrical Engineering

**Talking points**
- Expansion alloys, soft magnetics, resistance alloys, Cu strip/busbar.
- Spotlight example pattern: NVIDIA 800 VDC rack architecture reduces Cu busbar mass vs 54 VDC (use only if sourced in electronics note).
- ICIO C24B→C27 world ~USD 220 bn 2022.
- Company action: strip gauges, plating partners, design-in with connector / magnet OEMs.

**Resources**
`research/sectors/electronics.md`, `electronics.sources.csv`
SEMI / company notes (Infineon, etc. if present)

---

### 5.7 Medical Technology

**Talking points**
- Implantables: CoCr, Ti, Zr; instruments and tubing.
- Demography / procedure volumes: WHO / OECD hip-knee files in `data/clean/`.
- Geography: DE, CH, AT MedTech clusters; US FDA pathway as barrier.
- Spotlight: J&J ortho spin or similar **only** with filing citation.
- Company action: ISO 13485 / implant grade melt; distributor vs OEM dual path.

**Resources**
`research/sectors/medical.md`, `medical.sources.csv`
`data/clean/oecd_health_hip_knee_procedures.csv`
`data/clean/who_*.csv`
`data/raw/medical/medtech_europe_ff2025.pdf`, `wpp2024_summary.pdf`

---

## 6. Global Market Dynamics and Trade

**Talking points**
1. Product classification: HS chapters used (75 Ni, 81 specialty, 72 stainless, 74 Cu, 76 Al, 83 welding, 84 engines as demand proxy).
2. Why reporters: DE (mill hub), US/JP/KR (aero/auto), CN (volume + W), ID (Ni mine/NPI), FR/IN (aero / growth demand), IT/UK.
3. DE HS 7506 World 2024: USD 578 M / 17.8 M kg; partners AT, IT, CN, US, FR, ES.
4. PRODCOM ↔ Comtrade check on DE Ni flat exports (~1.8% gap).
5. China tungsten corridor (8101) as concentration risk.
6. Bilateral files for sourcing dependence (who supplies whom).
7. Link AC: EU net exporter flat Ni / net importer bar Ni → different commercial posture by form.
8. Trade does **not** equal qualified alloy demand.

**Must-cite**
COMTRADE_PORTFOLIO_WORLD_2019_2024, COMTRADE_BILATERAL_PRIORITY_2022_2024, COMTRADE_7506, COMTRADE_8101, AC_* as needed

**Files**
`research/materials/trade_chapter_6.md`
`data/clean/comtrade_portfolio_world_2019-2024.csv`
`data/clean/comtrade_bilateral_priority_2022-2024.csv`
Per-HS CSVs

---

## 7. Market Scenarios to 2035

*(Canonical after [writer](8c43a4f3-a5b7-4e9f-a258-2f485a5ef524) round-1 apply; supersedes earlier strategist auto upside +1% / index 110. Prose in `sections/07_scenarios.md` is draft only; copy rules and table numbers, not the style.)*

### 7.1 Market Model and Scenario Assumptions
**Talking points**
- Demand indexed to 100 in 2025; 2035 index = 100 × (1 + annual rate)^10. Three cases: downside / base / upside. No probabilities.
- Prices and FX held constant → indices are **volume** sensitivities only.
- **Never** multiply indices by EU flat AC 57.8 M kg or bar AC 5,380,347 kg. Qualified share unknown until shipment map.
- Flat AC = ceiling of mixed PRODCOM 24452200, not qualified alloy demand [AC_EU_NI_FLAT_2024].
- Bar AC = net import identity, not an aerospace order book [AC_EU_NI_BAR_2024].
- No company-weighted total until 2025 shipment shares exist.
- Automotive upside = **+0.5%/yr** (hybrid path; not a flat zero) [TE_AUTO_UPSIDE_2035]. Aerospace downside = **+1%/yr** (hottest static parts can substitute; disc stays). Growth in that downside stops only if missed approval + wider substitution arrive together.
- New engine hardware vs shop visits = **two lines**. Hardware read on HS 7505 / HS 7502, not flat balance.
- Fix 16 rejected: no scenario-fan figure.

### 7.2 Results by Industry, Product, and Region
**Live indices (2025=100 → 2035)** — must reproduce exactly:

| Industry | Downside | Base | Upside | Rates d/b/u |
| --- | ---: | ---: | ---: | --- |
| Automotive | 82 | 90 | **105** | -2% / -1% / **+0.5%** |
| Oil and gas | 90 | 105 | 116 | -1% / +0.5% / +1.5% |
| Energy, committed programmes | 100 | 134 | 179 | 0% / +3% / +6% |
| Aerospace and IGT | 110 | 134 | 155 | +1% / +3% / +4.5% |
| Chemicals | 95 | 116 | 134 | -0.5% / +1.5% / +3% |
| Electronics and electrical | 100 | 128 | 155 | 0% / +2.5% / +4.5% |
| Medical implant alloys | 105 | 122 | 141 | +0.5% / +2% / +3.5% |

**Table 12 drivers (cite these IDs, not raw industry CAGRs)**
- Auto: cars without plug 58.2 M → 42.9 M team path; ACEA_CAR_REG_2025, IEA_GEVO_EV_SHARE_2025/2035
- O&G: ~USD 570 bn upstream 2025; 2026 print USD 546 bn; CPS ~USD 65 bn/yr above STEPS; **never** USD 670 bn. OG_WEO2025_*, OG_WEI2026_*
- Energy: committed H2 4.3 Mt/yr by 2030 FID+; pipeline 27 Mt not orders. EE_H2_*
- Aero: fleet path ~3.4%/yr team interp 23,310 (2025) → ~32,600 (2035) → 45,550 (2045); LEAP 1,802 (+28%) is **not** the alloy rate. AERO_AIRBUS_GMF2026_*, AERO_LEAP_2025
- Chemicals: rates on named grade replacement, not on 57.8 M kg; NI_ACX_HPA_2025 (47 kt finish)
- Electronics: WSTS USD 795.6 bn (+26.2%) 2025 is chip spike, not alloy rate. WSTS_WORLD_2025
- Medical: OECD hip/knee path ~3.36%/yr 2013–2023; alloy rate below device market; Carpenter medical ex-surcharge USD 224 m. MED_OECD_HK_COUNT_2023, MED_CRS_MED_EXSUR_2026

**Shop-visit evidence (aero subsection)**
CO_GE_CES_2025 (26.6% margin, services 75% of CES), CO_SAFRAN_PROP_2025, CO_MTU_REV_2025, AERO_AIRBUS_GSF2026_SERVICES_2045, AERO_CI_AVIATION_CO_2025 (11,499 t Co = Co indicator, not Ni tonne scale)

**Do not**
- Add a scenario fan chart that only repeats Table 11
- Turn any index into capacity tonnes in chapter 7 or 8

**Resources**
`sections/07_scenarios.md` (facts only), Appendix A2 for unrounded indices, `reviews/research_results.md` §I

---

## 8. Strategic Recommendations

*(Canonical after [writer](8c43a4f3-a5b7-4e9f-a258-2f485a5ef524); see `reviews/round_1/applied.md`. Source: `sections/08_recommendations.md`.)*

### 8.1 Priority Products, Industries, Regions, and Customers
**Plant rule (open with this)**
- Capacity follows the **trade result**, not a growth story. Named grade + named form + buyer who can repeat.
- **Bar / rod / wire**: EU net import; AC 5,380,347 kg (band ~5.1–5.6 M kg). **No bar capacity vote** until UK supply footnote + HS 7502 are in the text [AC_EU_NI_BAR_2024].
- **Flat**: EU net export of mixed code; 57.8 M kg = ceiling only. Pursue plate/strip only where named grade is imported or displaces a named supplier [AC_EU_NI_FLAT_2024].
- Aerospace wrought offer: billet (via named forger, e.g. Aubert & Duval), approved sheet, repair wire → HS 7505 / 7502. Alloy plate → HS 750620 (DE 2024 World export ~15.0 M kg / USD 500 M; not-alloyed 750610 ~2.8 M kg) [COMTRADE_750610_750620_2019_2024].
- Expansion alloys / Crofer 22 / Aluchrom / Konstantan → HS ch. 72/74. Nickel 201 electrolyser strip → unalloyed HS 7506.
- Acerinox HPA = VDM + Haynes **once**: 83 kt melt / 47 kt finish / EUR 1,683 m (2025) [NI_ACX_HPA_2025]. Haynes = aero + IGT book; VDM = weaker chemical / O&G book [CO_HAYN_SYN_2026].
- Special Metals / PCC Hereford = outside EU27 → UK billet/bar absent from EU AC [CO_PCC_REV_2025]. Cast blades stay Howmet/PCC.

**Verbs**
- **Qualify**: aero billet / approved sheet / repair wire; chemical plate + weld on named grade; electrical strip/wire only if company already melts grade and account is named.
- **Keep / harvest**: O&G only on company’s own sour-service approval; profitable auto engine/exhaust (turbo, valve, plug, exhaust).
- **Hold as option**: electrolysers, powders, medical implant bar (until financed programme / implant maker / own regulatory path).
- **Stop**: undifferentiated stainless; China implant tenders; unfunded H2 / powder programmes.

**Named buyers**
1. Aero/IGT: GE Aerospace, Safran, Rolls-Royce, MTU, Pratt & Whitney (EU + NA); Siemens Energy (sold out to FY2028) [CO_SIEMENSENERGY_CMD_2025]
2. Chemical: Alloy C-276 / 625 / 59 plate + matching weld via fabricators
3. Electrical: magnetic / expansion / resistance strip to component makers (not sized on Ni flat AC)

**Table 13**: score eight criteria in **words** for three pursue columns + keep/do-not-fund. **No composite score** (no 2025 shipment shares).
**Table 14 stop/harvest**: glow plugs; undifferentiated stainless; China implants; unfunded H2 (tk nucera green H2 orders EUR 26 m of EUR 348 m FY2025) [CO_TKNUCERA_ORDERS_2025]; powders/GRX-810; Cu/Al plate until three-leg AC logged.

### 8.2 Recommended Actions and Implementation Roadmap
**Two clocks (Table 15)**
| Window | Decision now | Kill rule |
| --- | --- | --- |
| Months 0–3 | Set bar book vs EU net import; take glow plugs off growth list; contribution per bottleneck hour | Any bar capacity add before UK + HS 7502 footnotes |
| Months 3–12 | **≤5 live accounts**; **EUR 200,000 per account** sample cap until quantity agreed (team planning) [TE_PLAN_ACCOUNTS, TE_PLAN_SAMPLE] | Second sample with no annual quantity; disc / sour OCTG forced onto short clock |
| Months 12–24 | Finishing capital only after repeat order **and** contribution under ch.7 downside clears company hurdle | Capital without repeat+downside; powder/electrolyser without financed programme |

**Also**
- Hurdle rate = company’s own (do not invent).
- Pricing: conversion + monthly alloy adjustment (Ni/Mo/Cr/Co/W/Nb) + extras; stainless surcharge stays on stainless invoices.
- Melt routes distinct: VIM+VAR rotating; VIM+ESR corrosion plate; AOD for Crofer / 5–12% Ni grades.
- Appendix A4 / month 0–3 map still needed: 2025 revenue by row, UK supply, HS 7502, shipment weights.

**Resources**
`sections/08_recommendations.md`, `reviews/research_results.md` §I, company notes for GE/Safran/RR/MTU/ATI/Carpenter/Acerinox/Outokumpu/Siemens Energy/tk nucera

---

## 9. Conclusion

**Talking points**
- Restate answer to central question in 4–6 sentences using the four dimensions.
- One sentence each: Supply (ID/Ni surplus + specialty residual), Trade (DE corridors + form-specific AC), Demand (aero / CRA / medical pockets), Outlook (scenario ranges).
- Close on company priorities (forms × industries × regions) without new numbers.
- No new citations that were not in earlier chapters.

---

## References

Auto-generated from `data/sources.csv` + in-text markers. APA 7. Author string must match (e.g. “U.S. Geological Survey, 2026a”).

---

## Appendices

### A1 Definitions and evidence
- Class 1 Ni, AC identity, PRODCOM code definitions, HS list, HPA vs stainless.

### A2 Reproducible scenario calculations
- Model assumptions, formulas, Excel / `model.py` outputs.

### A3 Interpretation of existing sector estimates
- How paid reports were triangulated; what was rejected.

### A4 Information needed before investment
- Plant nameplate by alloy family; customer tonnes and margins; Co/Ti/W mill AC; IEA CME file once downloaded. HS 750610/750620 World split is available in `data/clean/`.

---

## Writing model checklist (give this to the next model)

1. Read `reviews/research_results.md` for numbers.
2. Follow this file section by section; do not invent claims.
3. Enforce house style: no dashes as punctuation, no semicolons, no banned words (`.claude/skills/house-style/`), every sentence ≥12 words.
4. Every number → `[DATA_ID]` logged in `data/sources.csv`.
5. Label team estimates; use `TODO(data): …` when a leg is missing.
6. Industry chapters: table + Sources line + “What the company should do:”.
7. Never split VDM and Haynes; never treat VDM catalogue as Münvest capability.
8. After draft: run house-style lint + fact-check against this pack and `reviews/round_1/fact_check.md`.
