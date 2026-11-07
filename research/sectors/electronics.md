# Research notes: 3.6 Electronics and electrical engineering

Scope: semiconductors (front end fabs, equipment, packaging), data centres (power distribution, cooling),
power electronics (SiC, GaN, 800 VDC), passive components (MLCC), displays (OLED masks), connectors and lead frames.
Retrieved 2026-11-07. Every figure carries its `data_id` from data/sources.csv.

## Method and access limits (read first)
1. WebFetch failed for wsts.org, semi.org, iea.org (403), haynesintl.com and metals-wire.net, because these hosts are outside
   the cloud session allow list. Figures from these publishers come from WebSearch summaries and secondary reposts, so their
   confidence is set to medium even where the publisher is primary. Verify in the original before the executive summary.
2. The shared web search budget ran out midway. Topics not researched are listed under Open data gaps.
3. UN Comtrade public preview worked (HS 740990, 741011). Raw JSON in data/raw/comtrade_electronics/.
4. Model figures (sector 6.5 EUR bn, cells E1 to E3) are team estimates from model/model.py and are not yet validated bottom up.

## Data chain mapping
| Material | Form | Application | Industry | Geography | Size 2025 | Growth | data_id |
|---|---|---|---|---|---|---|---|
| C-22, C-276, 316L VIM VAR | Strip (for welded tube), tube, bar | Fab gas delivery, wet benches, valves | Semiconductors | TW, US, KR, JP, DE | EUR 900m | 9.0% p.a. | MODEL_E1 |
| High conductivity Cu, CuNiSi | Strip, busbar | AI rack power, cold plates, connectors | Data centres, electrical | US, TW, CN | EUR 1,600m | 10.0% p.a. | MODEL_E2 |
| FeNi36, FeNi42 | Ultra thin strip, foil feedstock | OLED fine metal masks, lead frames | Displays, packaging | KR, CN, JP | EUR 400m | 8.0% p.a. | MODEL_E3 |
| Whole sector (Client type metals) | All | All | Electronics and electrical | World | EUR 6.5bn | 7.5% p.a. | MODEL_SEC_ELEC |

Model output: sector 13.4 EUR bn in 2035. E1 2,131 EUR m in 2035, score 4.45, tier A (second best cell of all 18).
E3 864 EUR m, score 4.05, tier A. E2 4,150 EUR m, score 3.55, tier B. E1 + E2 + E3 = 2.9 of 6.5 EUR bn, the remainder
(resistance and thermocouple wire, CuBe and other connector alloys, sputtering target feedstock, magnetic alloys) is not
yet modelled as cells. TODO(data): bottom up split of the remaining 3.6 EUR bn.

## Q1 Market size and growth to 2035
Sector level (the end market, value terms)
1. Semiconductor sales 2025: USD 795.6bn, up 26.2% [WSTS_SEMI_2025]. SIA: USD 791.7bn, up 25.6% [SIA_SEMI_2025]. WSTS used.
2. WSTS spring 2026: USD 1.51tn in 2026 (+89.9%), about USD 1.9tn in 2027 (+27%). Memory USD 230.0bn to 803.9bn
   2025 to 2026 [WSTS_FC_2026]. Q2 2026 update: H1 2026 USD 702bn, forecast largely confirmed.
3. McKinsey base case 2030: USD 2.3tn (range 1.7 to 2.6tn), growth mainly ASP and mix, unit shipments nearly flat [MCK_SEMI_2030].
   Implied 2025 to 2030 CAGR about 24% on WSTS 2025 (team calculation). Note: 2026 forecast already at USD 1.51tn, so
   the McKinsey 2030 base implies only about 11% p.a. from 2026 (team calculation: (2300/1510)^(1/4) − 1 ≈ 11.1%).
4. 2035: SEMI executives cite USD 2tn to 3tn [SEMI_2035_OUTLOOK]. Low confidence. TODO(data): no published 2035 forecast found.
5. Equipment billings 2025: USD 135.1bn, +15% [SEMI_EQUIP_2025]. Fab equipment spending 2026 USD 152bn (+24%), 2027
   USD 166bn [SEMI_WFF_2026]. 300mm fab equipment 2026 USD 149bn, USD 227bn by 2029 [SEMI_300MM_2026].
6. Physical volume driver (what matters for metal tonnage): installed 300mm capacity +7% in 2026 and about 7% p.a.
   2027 to 2029, total capacity +5% p.a. in 2026 and 2027 [SEMI_WFF_2026].
7. Data centres: electricity 415 TWh (2024) to 945 TWh (2030) [IEA_EAI_2025]. Hyperscaler capex USD 720bn to 745bn in 2026,
   from about USD 410bn in 2025 [HYPER_CAPEX_2026].
8. Copper in data centres: about 400 kt/yr on average over the next decade, peak 572 kt in 2028, more than 4.3 Mt in use by
   2035 [BNEF_DC_CU_2025]. Other analysts range from 330 kt to 1.1 Mt by 2030 (scope differences).
9. Power devices: SiC USD 11bn by 2031 at 20% CAGR [YOLE_SIC_2026], GaN USD 3.5bn by 2031 at 35% CAGR [YOLE_GAN_2026]. Market reports.
10. Copper alloys for connectors: USD 3.1bn (2025) to 5.5bn (2033) [GVR_CUALLOY_CONN]. Market report, low confidence, triangulation only.

High performance metal demand within the sector
1. Model: EUR 6.5bn in 2025 to EUR 13.4bn in 2035, 7.5% p.a. [MODEL_SEC_ELEC]. Team estimate.
2. Key interpretive point: chip value grows far faster than metal tonnage. Metal demand tracks wafer capacity (about 5 to 7% p.a.),
   rack power and kW installed, not chip revenue. The 7.5% model CAGR sits between the capacity growth and the copper demand
   trajectory, which is plausible but needs a bottom up check. TODO(data): metal intensity per wafer start (kg Ni alloy per
   1,000 wspm of new fab capacity) not found.

## Q2 Drivers and risks
Drivers
1. AI capex: hyperscaler capex about +77% in 2026 [HYPER_CAPEX_2026], memory boom [WSTS_FC_2026].
2. Fab build out across regions: Taiwan equipment spending +90% in 2025, Korea +26%, Japan +22% [SEMI_EQUIP_2025]. ESMC Dresden
   40,000 wspm, production 2027 [ESMC_DRESDEN_CAP, ESMC_TOPOUT_2026]. 146 new facilities or lines from 2026 [SEMI_WFF_2026].
3. Rack power density and liquid cooling: penetration of liquid cooling in AI chips about 33% (2025) to 53% (2026) [TF_LIQCOOL_2026].
4. 800 VDC power architecture (Kyber 2027) [NVDA_800VDC, NVDA_800VDC_CU45], SiC and GaN growth [YOLE_SIC_2026, YOLE_GAN_2026].
5. MLCC count per AI server, nickel powder demand [MLCC_NIPOWDER_2030, TOHO_NIPOWDER_2026].
6. Large format IT OLED (8.6 generation) [TREND_FMM].

Risks
1. Cyclicality: memory driven 2026 boom (+89.9%) creates a downside risk of a sharp correction. China equipment spend flat in 2025 (−0.5%).
2. Thrifting: 800 VDC cuts copper by up to 45% versus 415 VAC [NVDA_800VDC_CU45].
3. Value versus volume: McKinsey growth is ASP led, shipments nearly flat [MCK_SEMI_2030].
4. Copper supply deficit and price: shortfall about 6 Mt by 2035 [BNEF_DC_CU_2025], record LME 14,533 USD/t in 2026 [LME_CU_RECORD_2026],
   which raises incentive to substitute aluminium (team assessment, TODO(data): no source on aluminium busbar share).
5. Concentration: China, Taiwan, Korea took 79% of equipment billings [SEMI_EQUIP_2025], qualification is local.
6. Geopolitics and export controls (team assessment, no figure).

## Q3 Emerging technologies and applications
1. 800 VDC HVDC racks, solid state transformers (under study) [NVDA_800VDC_CU45].
2. Direct liquid cooling with copper cold plates, GB300 NVL72 fully liquid cooled, six small cold plates per compute tray,
   Rubin returns to one large plate per tray [TF_LIQCOOL_2026, TF_COLDPLATE_SUPPLIERS].
3. SiC and GaN power stages for 800 V EV and data centre PSUs [YOLE_SIC_2026, YOLE_GAN_2026].
4. 8.6 generation IT OLED with thinner Invar masks (20 um or less) [TREND_FMM, THELEC_FMM_20UM]. FMM sag with larger size [MT_FMM_2026].
5. High end MLCC with ultrafine nickel electrodes [TOHO_NIPOWDER_2026].
6. TODO(data): glass core substrates, backside power delivery, hybrid bonding, metal content not researched (budget exhausted).

## Q4 Materials required (alloy, grade, form, why)
| Application | Alloy and grade | Form | Why | data_id |
|---|---|---|---|---|
| Corrosive gas lines (HCl, Cl2, HBr, WF6) | Alloy C-22 (UNS N06022), C-276 | Strip for welded tube to ASTM B626, seamless tube, bar for valve bodies | C-22 corrosion 0.1 mpy versus 28.8 mpy for 316 in HCl vapour at 52 C | HAYNES_C22_HCL, CSI_C22_TUBE |
| Inert and bulk gas lines | 316L VIM VAR, electropolished | Tube, bar | Low inclusions and sulphur for electropolish, Ra 0.25 um | DOCKWEILER_2023, CSI_C22_TUBE |
| Wet benches, chemical delivery | C-22, C-276, fluoropolymer lined | Sheet, tube | Acid resistance | ICHOR_2025 (fluid delivery) |
| OLED fine metal mask | FeNi36 (Invar 36), low CTE, very low inclusion | Foil 20 um or thinner, rolled from precision strip | CTE match with glass during evaporation | THELEC_FMM_20UM, MT_FMM_2026 |
| Lead frames, glass sealing | FeNi42, CuFe2P, CuNiSi | Precision strip | CTE match to silicon, conductivity | MODEL_E3 (team) |
| Rack busbars, PDUs | Cu ETP, Cu OF | Flat bar, strip | Conductivity | NVDA_800VDC, SMM_JINTIAN_BUSBAR |
| Cold plates | Cu OF (C10200 type) | Strip, plate, skived fin | Thermal conductivity | TF_COLDPLATE_SUPPLIERS |
| Connectors | CuNiSi (C7025), CuNiSn, CuBe | Strip | Strength 45 to 60% IACS | GVR_CUALLOY_CONN |
| MLCC electrodes | Ni, ultrafine | Powder below 200 nm | Cost and co firing with BaTiO3 | MLCC_NIPOWDER_2030, TOHO_NIPOWDER_2026 |
Grades for lead frames and connectors are standard metallurgy knowledge (team assessment), no figure attached.

## Q5 Geographic concentration of demand
1. Equipment 2025: China USD 49.3bn, Taiwan 31.5bn, Korea 25.8bn, Japan 9.5bn. China, Taiwan, Korea = 79% [SEMI_EQUIP_2025].
2. Capacity growth 2026: Americas +109% and Europe and Mideast +199% in a SEMI capacity or spend metric (search summary
   ambiguous, TODO(data): verify metric) [SEMI_WFF_2026]. China largest installed capacity in 2026 and 2027.
3. Semiconductor sales: Asia Pacific USD 439.7bn (2025) to 823.9bn (2026) [WSTS_FC_2026].
4. Data centres: US adds up to 240 TWh (+130%) and China 175 TWh to 2030 [IEA_EAI_2025].
5. Copper alloy strip trade (HS 740990, 2024): exports 980 USD m, Germany 28.7%, Japan 26.4% [COMTRADE_740990_X_2024]. Imports
   1,104 USD m, China 16.1%, Singapore 10.0%, Mexico 9.6%, Malaysia 6.1%, Taiwan 5.6% [COMTRADE_740990_M_2024].
   Reading: Germany and Japan produce, Asian and Mexican assembly hubs consume.
6. Copper foil imports (HS 741011, 2024): China USD 1,210m of 3,657m reporter sum. Not logged as source row, mainly battery and PCB.
7. Displays: Korea and China (Samsung A6 Asan, BOE B16 Chengdu) [TREND_FMM]. FMM supply Japan about 90% [MT_FMM_2026].

## Q6 Customers and competitors (named)
Customers
1. Fab owners: TSMC (incl. ESMC Dresden JV with Bosch, Infineon, NXP) [ESMC_DRESDEN_CAP], Samsung, SK hynix, Micron, Intel (team list).
2. Gas and fluid subsystem makers (the real buyers of strip and tube): Ichor (USD 948m 2025) [ICHOR_2025], Ultra Clean Holdings (UCT),
   Swagelok, Fujikin (team list). Tube makers: Dockweiler (Neustadt-Glewe, EUR 164m 2023) [DOCKWEILER_2023], Valex, Cardinal UHP [CSI_C22_TUBE].
3. Data centre power: Vertiv, Eaton, Schneider Electric, Delta [NVDA_800VDC_CU45]. Cold plates: Cooler Master, AVC, Boyd, Auras, CoolIT [TF_COLDPLATE_SUPPLIERS].
4. FMM makers: DNP (dominant), Toppan (team list), Poongwon Precision, LG Innotek [ASIAE_POONGWON_2025]. Panel makers Samsung Display, BOE, LG Display [TREND_FMM].
5. MLCC: Murata, Samsung Electro-Mechanics, Taiyo Yuden (search summary, no row).
Competitors
1. Ni alloy mills: Haynes International and VDM Metals (both Acerinox) [ACX_HAYNES], Special Metals (PCC), Nippon Yakin Kogyo (team list).
2. Invar foil: Proterial [MT_FMM_2026], Zapp (Germany) [OLEDINFO_ZAPP], Hyundai BNG Steel (localising) [ASIAE_POONGWON_2025], Aperam Alloys Imphy (team list).
3. Copper strip and busbar: Ningbo Jintian (35,000 t chip busbar, 15,000 t rack busbar) [SMM_JINTIAN_BUSBAR], Wieland, Aurubis, KME, Diehl,
   Mitsubishi Materials, Furukawa, Kobe Steel, Poongsan, Boway, Materion (CuBe) (team list, no figures).
4. Nickel powder: Toho Titanium (JX Advanced Metals) [TOHO_NIPOWDER_2026], Shoei Chemical, JFE Mineral (team list).

## Q7 Competitor map
| Application | Form | Leading suppliers | Strength | Client position (team assessment) |
|---|---|---|---|---|
| Fab corrosive gas lines | C-22 strip and tube | Haynes and VDM (Acerinox), Special Metals | Alloy ownership, SEMI qualification | Credible with C-22 and C-276 strip, needs UHP surface and traceability |
| Bulk gas lines | 316L EP tube | Dockweiler, Valex, Swagelok supply chain | Cleanroom finishing | Feedstock supplier only |
| OLED masks | FeNi36 foil | Proterial, Zapp, Hyundai BNG | Proterial lock in with DNP | Precision strip feedstock, niche |
| Rack busbars | Cu flat bar | Jintian, Wieland, Aurubis | Scale and cost | Weak, commodity |
| Connectors | CuNiSi strip | Wieland, Mitsubishi Materials, Furukawa, Poongsan, Boway | Alloy IP, capacity | Medium |
| MLCC | Ni nano powder | Toho Titanium, Shoei, JFE Mineral | CVD and chemical routes | Low fit (AM powder is gas atomised, 15 to 45 um type) |

## Q8 Gain or loss of relevance
Gain
1. Ni alloys over 316L in corrosive gas service, as etch and deposition chemistries grow [HAYNES_C22_HCL, ICHOR_2025].
2. Copper in cold plates as liquid cooling penetration climbs [TF_LIQCOOL_2026].
3. FeNi36 thinner and wider foil for 8.6 generation OLED [TREND_FMM, THELEC_FMM_20UM].
Loss
1. Copper busbar mass per MW falls with 800 VDC (up to 45% less copper) [NVDA_800VDC_CU45].
2. Aluminium substitution in busbars at record copper prices (team assessment, TODO(data)).
3. FMM free OLED patterning (photolithographic routes such as JDI eLEAP or Visionox ViP) would remove Invar masks.
   TODO(data): adoption status not researched, search budget exhausted.
4. Ceramic and yttria coated parts inside process chambers rather than metal (team assessment, no figure).
5. Fluoropolymer lined systems in wet chemistry.

## Q9 Attractive value chain steps for the Client
1. Qualified UHP strip of C-22 and C-276 for welded tube and gas system components (cell E1, tier A, score 4.45).
2. Precision FeNi36 strip as foil feedstock and FeNi42 for lead frames (cell E3, tier A, 4.05), entry via Korean and Chinese
   localisation programmes [ASIAE_POONGWON_2025].
3. Selective copper alloy strip for connectors and cold plates (cell E2, tier B, 3.55), not busbar bulk.
4. European fab proximity: ESMC Dresden and Dockweiler as reference customers [ESMC_DRESDEN_CAP, DOCKWEILER_2023].

## Spotlight facts
1. NVIDIA, 800 VDC Kyber racks, 2027, copper busbar up to 200 kg per 1 MW rack at 54 VDC, up to 45% less copper versus 415 VAC.
   Partners Vertiv, Eaton, Schneider, Delta, Infineon, ST, TI, Navitas. Likely copper suppliers Jintian, Wieland, Aurubis (team assessment).
   [NVDA_800VDC, NVDA_800VDC_CU45, SMM_JINTIAN_BUSBAR]
2. ESMC (TSMC, Bosch, Infineon, NXP), Dresden, topped out 2026, production 2027, 40,000 300mm wspm. Gas and chemical delivery in
   316L EP and C-22 tube. Likely suppliers Dockweiler (tube), Ichor, UCT, Swagelok (subsystems), Acerinox mills (alloy).
   [ESMC_DRESDEN_CAP, ESMC_TOPOUT_2026, DOCKWEILER_2023, HAYNES_C22_HCL]
3. Samsung Display A6 Asan (2026) and BOE B16 Chengdu (2027), 8.6 generation IT OLED, FeNi36 foil 20 um or thinner for DNP masks,
   Proterial dominant, Zapp and Hyundai BNG alternatives. [TREND_FMM, THELEC_FMM_20UM, MT_FMM_2026, OLEDINFO_ZAPP]
4. Toho Titanium (JX Advanced Metals), Chigasaki, announced 10 Sep 2026, doubles ultrafine nickel powder for high end MLCC from 2027,
   customers Murata and Samsung Electro-Mechanics. [TOHO_NIPOWDER_2026]

## Open data gaps (TODO(data))
1. Metal intensity per wafer start or per MW of data centre (Ni alloy and Cu kg), searched SEMI, vendor notes, not found.
2. Bottom up split of the model sector value (6.5 EUR bn) beyond cells E1 to E3.
3. FMM free OLED adoption (eLEAP, ViP, photolithography), aluminium busbar substitution, TSMC capex and Arizona status, Wieland,
   Aurubis and KME electronics volumes: not searched, web search budget exhausted.
4. Primary verification of WSTS, SEMI, IEA figures (hosts blocked). Ask the team to download the SEMI and WSTS releases and the IEA
   Energy and AI dataset into data/raw/.
5. Published 2035 semiconductor or data centre forecasts (only executive remarks found).
6. Exact meaning of the SEMI regional growth figures (Americas +109%, Europe and Mideast +199%).

## Sources consulted (URLs, see data/sources.csv)
WSTS, SIA, McKinsey, SEMI (WWSEMS, World Fab Forecast, blog), IEA news release, Datacentres.com, The Northern Miner (BNEF), NVIDIA Technical
Blog, I-Connect007 (TrendForce), Tiger Brokers, Yole Group, Semiconductor Today, Grand View Research, SMM, UN Comtrade, 36Kr, MONOist,
Money Today, The Elec, Asia Economy, OLED-Info, Haynes International, CSI Designs, chemie.de, The Motley Fool, TrendForce, Focus Taiwan.
