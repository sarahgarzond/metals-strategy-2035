# Research notes: Automotive (report section 3.1)

Stage 1 research, retrieved 2026-11-07. Every figure carries its data_id in data/sources.csv.
Access limits in this session: oica.net, acea.auto, iea.org (403 and blob storage), reports.voestalpine.com,
tatasteelnederland.com and afia.pt could not be fetched, so many figures come from WebSearch summaries of the primary
release and are logged at medium confidence with "verify" in the notes. The shared WebSearch budget ran out during
this stage, so several follow-ups are open (see section 11).

## 0 Data chain position
Material > Product form > Application > Industry (Automotive) > Geography > Market size > Growth.
Model anchor: automotive addressable market EUR 6.0bn in 2025, 1.5% p.a., EUR 6.96bn in 2035 (MODEL_AUTO_2025,
MODEL_AUTO_2035, team estimate from model.py SECTORS). This is 11.9% of the EUR 50.6bn portfolio market (MODEL_TOTAL_2025).

| Model cell | Material | Form | Application | Regions | 2025 EUR m | CAGR | 2035 EUR m | Score / tier |
|---|---|---|---|---|---|---|---|---|
| V1 | Ni 201 strip, Cu busbar, Ni plated strip | Strip | EV battery tabs, power electronics, motors | CN, EU | 1,400 | 8.0% | 3,022 | 2.75 / C |
| V2 | Alloy 600, 601, heat resistant strip | Strip, wire | Exhaust sensors, glow and spark plugs, gaskets | EU, CN | 900 | -3.0% | 664 | 2.35 / C |
| Remainder | Stainless exhaust, aluminium, other copper | Strip, sheet, tube | Exhaust, thermal, body, wiring | All | 3,700 | about -1.2% (implied) | 3,280 | not scored |

Source: MODEL_AUTO_V1, MODEL_AUTO_V2, MODEL_AUTO_REST. Scores with model weights (V1 [4,4,3,1,3,2,1,2], V2 [3,1,4,3,1,2,3,2]).
Observation for the model owner: sector CAGR 1.5% with V1 at 8% implies the unscored remainder shrinks about 1.2% p.a.
This is plausible (ICE stainless exhaust erosion) but is not yet documented by a source. TODO(data): split the remainder
into stainless exhaust (EN 1.4509, 1.4512), aluminium strip and copper wire with PRODCOM or Comtrade data.

## 1 Market size and growth to 2035
Vehicle market (volume):
- World motor vehicle production 96.4 million in 2025, up 3.9% from 92.7 million (OICA_PROD_2025).
- Asia Pacific 59.2 million, more than 61% of the world (OICA_APAC_PROD_2025). China 34.53 million, NEV production
  above 16.6 million (+29%) (OICA_CN_PROD_2025). Americas 18.74 million, down 2.1% (OICA_AM_PROD_2025). India 6.49 million
  (OICA_IN_PROD_2025). United States 10.24 million and Japan about 8.41 million (MND_US_JP_PROD_2025, secondhand, low).
- TODO(data): Europe and Germany production 2025 (OICA or VDA). Not retrieved.
- TODO(data): global light vehicle production forecast 2035. S&P Global Mobility extension forecast is paywalled.
  Searched spglobal.com, found only that the base forecast runs current year plus seven and that Asia Pacific provides
  84% of expected sales volume growth (2025 presentation, not logged because it refers to sales).

Electrification (drives the material mix):
- Electric car sales above 20 million in 2025, +20%, one quarter of new car sales (IEA_GEVO_SALES_2025).
- Shares 2025: China almost 55% (IEA_GEVO_CN_SHARE_2025), EU just under 27% incl. PHEV (IEA_GEVO_EU_SHARE_2025),
  United States around 10% (IEA_GEVO_US_SHARE_2025). Chinese carmakers delivered 60% of global EV sales (IEA_GEVO_CN_OEM_2025).
- Forecast 2026: 23 million, 28% (IEA_GEVO_FCST_2026).
- 2030: around 40% of LDV and two/three wheeler sales in STEPS, previous edition (IEA_GEVO25_2030).
- 2035: around 50% in exploratory scenarios, scenario label unconfirmed, one article says 60% (IEA_GEVO_2035_SHARE, low).
- EU 2025 registrations about 10.8 million (ACEA_EU_REG_2025): BEV 17.4% (ACEA_BEV_2025), HEV 34.5% (ACEA_HEV_2025),
  PHEV 9.4% (ACEA_PHEV_2025), petrol 26.6% (ACEA_PETROL_2025), diesel 8.9% (ACEA_DIESEL_2025).

High performance metal demand in automotive: team model EUR 6.0bn to 6.96bn (1.5% p.a.). Volume growth of vehicles
(about 1% p.a. implied by OICA trend, not a forecast) and a shift of value from ICE heat resistant parts (V2, -3%) to
battery and power strip (V1, +8%). Triangulation: copper strip market (all industries) USD 5.8bn to 9.2bn in 2024 and 6%
to 8% CAGR (MR_CU_STRIP_2024, market report, low, triangulation only). TODO(data): a primary triangulation of nickel alloy
and copper alloy strip used in vehicles (Nickel Institute end use, ICSG end use).

## 2 Drivers and risks
Drivers
1. Electrification raises copper per car: ICE 23 kg, HEV 40 kg, PHEV 60 kg, BEV 83 kg (ICA_CU_VEHICLE_2017, 2017 IDTechEx
   study). Cross check about 25 kg vs just under 70 kg (KI_CU_VEHICLE).
2. Large format cylindrical cells (46xx) need nickel plated steel can strip and nickel or nickel plated tab strip
   (CSIRO_CELLCANS, TATA_HILUMIN, BMW_GEN6_CELLS).
3. 800 V platforms (BMW Neue Klasse, BMW_GEN6_CELLS notes) move demand to high conductivity copper busbars and
   CuNiSi connector strip that keeps contact force at higher temperature (AURUBIS_CONNECTOR).
4. EU Automotive Package (16 Dec 2025) cuts the 2035 target to 90% and lets PHEV and range extenders register after
   2035 (EC_AUTO_PKG_2025), which slows the erosion of exhaust, sensor and glow plug demand (V2).
Risks
1. LFP above half of EV batteries (IEA_GEVO_LFP_2025): less nickel in cathodes (not a Client form) and more prismatic
   aluminium cans and blade cells, which cuts the share of nickel plated steel cans.
2. 48 V and zonal architectures cut harness copper (MOTOR1_CYBERTRUCK_48V). Reported saving of about 45 kg per Cybertruck
   is unverified, TODO(data).
3. Chinese dominance: Chinese carmakers 60% of EV sales (IEA_GEVO_CN_OEM_2025) and China 34.53 million units, with domestic
   strip suppliers (Jiangsu Jiutian, Zhongshan Sanmei per MR_NIPS_PLAYERS).
4. Europe weak: S&P cut European LV production by 82,000 units in 2026 and 176,000 in 2027 (search summary, not logged,
   TODO(data) verify before use). Q1 2026 EV sales reported down 8% globally (IEA_GEVO_FCST_2026 notes).
5. Price pressure and low entry barriers in commodity strip (model scores competitive intensity 1 and entry barriers 1 for V1).

## 3 Emerging technologies and applications
- 46xx cylindrical cells (BMW Gen6 4695 and 46120, Tesla 4680): deep drawn and wall ironed nickel plated steel cans
  (CSIRO_CELLCANS). Pre-plated strip that removes post plating (WAELZHOLZ_NI_STRIP).
- 800 V traction and SiC power modules: copper busbars, Cu ETP and OF copper, CuNiSi and CuCrZr strip.
- 48 V zonal low voltage networks (Cybertruck): less copper wire, more small connectors.
- Fuel cell vehicles and trucks: bipolar plates in titanium (Toyota) or coated stainless (Hyundai) (IDTECHEX_BPP).
  Coated stainless strip (316L, 1.4404 type, or ferritic) is the Client entry path, linked to model cell N2 in energy.
- Sodium ion cells (aluminium current collector on both electrodes) would remove copper foil. Qualitative, no figure.
- Additive manufacturing for tooling inserts and spare parts (maraging and hot work powders), relevant to the Client AM
  powders. TODO(data): automotive share of metal AM.

## 4 Materials required (alloy, grade, form, why)
| Application | Alloy / grade | Form | Why |
|---|---|---|---|
| Cylindrical cell cans | Low carbon steel, Ni plated and diffusion annealed (HILUMIN type) | Strip 0.2 to 0.5 mm (thickness range is a team estimate from teardown reports, not logged) | Deep drawing, corrosion resistance to electrolyte, low contact resistance |
| Cell tabs, busbars in modules | Ni 201 / Ni 200, Ni plated copper, Cu ETP | Thin strip | Weldability (laser, ultrasonic), conductivity |
| HV connectors and terminals | CuNiSi (C19005, C70250 type), CuSn | Precision strip | Strength with conductivity, stress relaxation at 150 °C class |
| Busbars, motor hairpins | Cu ETP, Cu OF | Flat bar, rectangular wire | Conductivity, formability |
| Glow plug tubes, sensor caps, manifolds | Alloy 601, Alloy 600 | Strip, wire, tube | Oxidation resistance above 1,000 °C (VDM_ALLOY601_DS) |
| Exhaust gaskets, turbo seals | Alloy 718, X750 type | Strip | Spring properties at heat. Single less authoritative source for turbo seals, flag |
| Exhaust lines | Ferritic stainless 1.4509, 1.4512 | Strip, tube | Thermal fatigue, cost (team classification, TODO(data) volumes) |
| Fuel cell bipolar plates | 316L, coated stainless, titanium grade 1 | Thin foil strip 0.1 mm class | Corrosion in PEM environment, conductivity with coating |
| Prismatic cell cans, battery trays | Aluminium 3003, 5xxx, 6xxx | Strip, extrusions | Weight, LFP prismatic format |

## 5 Geographic concentration
China 34.53 of 96.4 million vehicles (36%) and almost 55% EV share. Asia Pacific above 61%. Americas 18.74 million.
Europe: TODO(data) production figure. Client relevant hubs: Germany (OEM and Tier 1 headquarters), Hungary (BMW Debrecen,
CATL Debrecen, EVE plant), Poland and Czechia (Tier 1 and cells), China (Ni plated strip, connectors), US (Tesla Austin).

## 6 Customers and competitors (named)
Customers: OEMs BMW, Volkswagen, Mercedes Benz, Stellantis, Toyota, Hyundai, Tesla, BYD. Cell makers CATL, EVE Energy
(BMW_GEN6_CELLS), LG Energy Solution, Panasonic, Samsung SDI. Tier 1 Bosch, Denso, Niterra (spark plugs, glow plugs,
sensors, about 80% of revenue automotive, NITERRA_AUTO_SHARE low), Aumovio (former Continental automotive), ZF, Forvia,
Valeo, Mahle, Eberspächer, Tenneco, TE Connectivity, Aptiv, Yazaki, Sumitomo Electric.
Competitors: nickel alloys VDM Metals (Acerinox HPA with Haynes, ACX_HAYNES), Special Metals, Aperam, Nippon Yakin.
Ni plated strip: Tata Steel Nederland HILUMIN, Toyo Kohan, Waelzholz, Jiangsu Jiutian, Zhongshan Sanmei. Copper alloy strip:
Wieland, Aurubis (Stolberg, Pori, Buffalo retained), KME (bought Zutphen and slitting centres, EUR 280m turnover, 2022,
AURUBIS_KME_FRP), Mitsubishi Materials, Proterial, Materion, NGK Insulators, Lebronze Alloys, AMPCO Metal (GNW_CU_CONNECTOR).
Specialty steels and AM: voestalpine High Performance Metals, 20% of divisional revenue automotive (VOEST_HPM_AUTO_2026).
Distributors: thyssenkrupp Materials Services, Jacquet, TW Metals (TW Metals lists Alloy 601 bar and wire, search result only).

## 7 Competitor map
| Application | Form | Main competitors | Strength |
|---|---|---|---|
| Cell cans | Ni plated steel strip | Tata Steel, Toyo Kohan, Waelzholz, Jiangsu Jiutian | Scale plating lines, OEM qualification, steel base cost |
| Tabs and module busbars | Ni and Cu strip | Chinese strip mills, Wieland, Aurubis, KME | Price, proximity to Chinese and Hungarian cell plants |
| HV connectors | CuNiSi strip | Wieland, Aurubis, KME, Mitsubishi Materials, Proterial, Materion | Alloy portfolio, Tier 1 approvals with TE, Aptiv |
| Glow plug, sensor, gasket | Alloy 600 and 601 strip and wire | VDM Metals, Special Metals, Nippon Yakin | Melting and VIM base, long approvals |
| Bipolar plates | Coated stainless or Ti foil | Stainless mills and coaters (TODO(data) names) | Thin gauge rolling and coating |
| Tooling and AM | Tool steel, AM powder | voestalpine HPM | Tool steel integration |

## 8 Where high performance metals gain or lose
Gain: Ni plated and Ni strip in cylindrical cells, CuNiSi strip in 800 V connectors, coated stainless foil in fuel cells.
Lose: ICE heat resistant parts (V2, -3% p.a.), diesel at 8.9% of EU registrations (ACEA_DIESEL_2025), ceramic silicon
nitride glow plugs (qualitative), aluminium cans with LFP prismatic cells (IEA_GEVO_LFP_2025), copper harness with 48 V,
titanium vs stainless in bipolar plates (Toyota titanium, IDTECHEX_BPP).

## 9 Attractive value chain steps
Model scores both automotive cells tier C. Recommended roles: (a) precision thin strip with slitting and plating service for
European Tier 1 connector and battery module makers, (b) Alloy 601 strip and wire as cash niche with price discipline,
(c) coated stainless foil for bipolar plates as an option linked to hydrogen cell N2, (d) avoid the commodity can strip volume
race against Tata Steel and Toyo Kohan. Closed loop scrap return with Tier 1 stamping plants is a qualitative opportunity.

## 10 Spotlight facts
S1 BMW Neue Klasse iX3, Debrecen (Hungary), series production late October 2025, first of five Gen6 battery plants
(BMW_DEBRECEN_SOP). Gen6 46 mm round cells, 4695 and 46120, from CATL and EVE Energy, up to 120 GWh at six plants
(BMW_GEN6_CELLS). Metal: nickel plated steel can strip, Ni or Ni plated copper tab strip, copper busbars at 800 V.
Likely suppliers: Tata Steel HILUMIN, Toyo Kohan, Waelzholz (can strip, not confirmed by BMW). Can material undisclosed.
S2 European Commission Automotive Package, Brussels, 16 December 2025: 90% CO2 target for 2035 and PHEV and range
extenders allowed after 2035 (EC_AUTO_PKG_2025). Metal: Alloy 601 and 600 strip and wire for glow plug tubes, sensor caps,
manifolds (VDM_ALLOY601_DS). Customers: Bosch, Niterra, Denso. Likely suppliers: VDM Metals, Special Metals, Nippon Yakin.
S3 Tesla Cybertruck, Gigafactory Texas, 2023: 48 V low voltage architecture (MOTOR1_CYBERTRUCK_48V). Metal: copper wire and
CuNiSi or CuSn connector strip, less copper per vehicle. Likely harness and connector suppliers: Yazaki, Sumitomo Electric,
Aptiv, TE Connectivity, strip from Wieland, Aurubis, Mitsubishi Materials. Copper saving figure unverified, TODO(data).
S4 Toyota vs Hyundai fuel cells: Toyota uses titanium bipolar plates, Hyundai steel plates (IDTECHEX_BPP). Metal: titanium
grade 1 or coated 316L foil. Shows where titanium substitutes the Client's stainless.

## 11 Open data gaps (TODO(data))
1. OICA, ACEA and IEA figures pulled from search summaries because the hosts were blocked. Verify against the primary tables.
2. Europe and Germany vehicle production 2025.
3. Light vehicle production forecast 2035 (S&P Global Mobility, paywalled, or IEA GEVO 2026 outlook chapter).
4. IEA GEVO 2026 2035 EV share, scenario label (team to download GEVO 2026 into data/raw/).
5. Primary triangulation of automotive nickel alloy and copper alloy strip demand (Nickel Institute, ICSG end use).
6. Split of the EUR 3.7bn model remainder (stainless exhaust, aluminium, copper wire).
7. Cybertruck copper saving per vehicle (press reports 45 kg, unverified).
8. Niterra revenue split from the integrated report. VDM Metals and Acerinox HPA automotive share.
9. Capacity of Ni plated strip lines (Tata, Toyo Kohan, Chinese producers).
10. Bipolar plate foil suppliers and coating firms.
