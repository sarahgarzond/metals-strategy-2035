# Research notes: 3.3 Environmental and energy technology

Scope: hydrogen and electrolysers, fuel cells (SOFC/SOEC), nuclear (large LWR, SMR, Gen IV, fusion), wind, solar,
industrial gas turbines (IGT), flue gas desulphurisation (FGD), waste to energy (WtE), geothermal, CCS.
Retrieved 2026-11-07. Every figure carries its data_id from data/sources.csv. Confidence in brackets.

Method caveat: the web search budget for the session ran out during research, and direct fetches of gwec.net,
sec.gov, world-nuclear-news.org and utilitydive.com failed (hosts outside the cloud session allow list). Several
primary figures were therefore taken from search summaries of the primary page and are flagged medium confidence
with "verify" in sources.csv.

## Q1 Market size and growth to 2035

Sector (macro investment context)
- Global energy investment USD 3.3 trillion in 2025, clean energy USD 2.2 trillion, grids about USD 400bn per year,
  solar PV about USD 450bn [IEA_WEI_2025] (high). Nuclear investment more than USD 70bn in 2025 [IEA_WEI_NUC_2025] (medium, secondary).
- Electricity demand rises about 40% by 2035 (CPS and STEPS) and nuclear capacity rises by at least one third,
  potentially 70%, from 420 GWe in 2024 [IEA_WEO_2025_NUC] (medium).
- Renewables: about 4,600 GW added 2025 to 2030, solar about 80%, China nearly 60% [IEA_REN_2025] (medium).
- Wind: 165 GW installed in 2025 (+40%), 1,299 GW cumulative, offshore 9.3 GW, 969 GW expected 2026 to 2030 [GWEC_GWR_2026] (medium).
- Hydrogen: installed water electrolysis about 2 GW in 2024 [IEA_H2_2025], 4.2 Mt/yr low emission H2 from operating or FID
  projects by 2030 vs announced 37 Mt/yr [IEA_H2_2030_FID] (high). Electrolyser manufacturing capacity 58 GW/yr end 2025
  but output under 5 GW, utilisation about 9% [ARGUS_ELY_2026] (medium, secondary on IEA GHR 2026).
- Gas turbines: GE Vernova 116 GW backlog plus slots at Q2 2026 (53 firm), output 20 GW/yr Q3 2026 rising to 30 GW/yr
  target in 2030 [GEV_2Q26]. Siemens Energy firm backlog 69 GW, about 25% data centres [SE_Q3FY26]. Global Q2 2026
  orders 38 GW record, US about half, Mitsubishi large frame backlog 35 GW [TM_GT_ORDERS_Q2] (low).
- CCS: about 50 Mt/yr operating in Q1 2025, pipeline about 430 Mt/yr by 2030, 80% of it in North America and Europe [IEA_CCUS_2025] (high).

High performance metal demand within the sector
- Model value: EUR 8.5bn in 2025, 6.5% p.a., EUR 16.0bn in 2035 [MODEL_SEC_ENERGY] (team estimate, low).
  This is a top down allocation in model.py, not yet validated bottom up.
- Bottom up cross check from model cells: N1 nuclear EUR 1.7bn (7%), N2 hydrogen EUR 0.25bn (18%), N3 WtE/FGD overlay
  EUR 0.9bn (4%), W1 desalination and scrubbers EUR 1.0bn (4.5%) = EUR 3.85bn. Gap about EUR 4.65bn assumed to be IGT
  superalloy sheet and bar, copper and aluminium for wind, solar and grid, and other. TODO(data): IGT superalloy wrought
  demand (t) and copper semis share in wind/solar; searched IEA, GWEC, Haynes literature without a tonnage figure.
- TODO(data): nickel intensity of alkaline electrolysers. Secondary sources disagree by more than two orders of magnitude
  (about 1 t/MW attributed to IEA vs 0.3 to 0.5 kg/kW). Do not use until IEA Critical Minerals Data Explorer is downloaded to data/raw/.
- TODO(data): nuclear grade zirconium tonnage per GW (UxC report paid, not used).

## Q2 Drivers and risks

Drivers
1. Electricity demand growth and AI data centres pull gas turbines and firm low carbon power [IEA_WEO_2025_NUC, GEV_2Q26, SE_Q3FY26].
2. Nuclear policy: Sizewell C FID 22 July 2025, GBP 38bn [SZC_FID_2025], US partnership with Westinghouse at least
   USD 80bn, about eight AP1000 (FT) [WEC_US_80BN], Darlington BWRX-300 four units [OPG_DARLINGTON], 70 GW under construction [IEA_NUC_2025].
3. Hydrogen and CCS policy in EU, Middle East and US [IEA_H2_2030_FID, IEA_CCUS_2025, NEOM_H2, EQUINOR_NL_2025].
4. Coal plant pollution control retrofits in India: 22 GW FGD installed, 102 GW in advanced stage (Jan 2025) [PRAYAS_FGD_2025].

Risks
1. Hydrogen overbuild and cancellations: 2030 potential cut from 49 to 37 Mt/yr, factory utilisation about 9%, Chinese
   systems at USD 500 to 1,100/kW vs USD 1,900 to 2,500/kW elsewhere [IEA_H2_2030_FID, ARGUS_ELY_2026].
2. Nuclear construction delays and cost overruns (IEA; Sizewell C cost nearly double the earlier EDF estimate, secondary).
3. Indian SO2 norms relaxed again in 2025 for most plants, so FGD retrofit demand is uncertain [PRAYAS_FGD_2025 notes].
4. Gas turbine slot reservations (63 GW at GE Vernova) may not all convert to firm orders [GEV_2Q26].
5. US solar forecast cut almost 40% by IEA [IEA_REN_2025 notes].

## Q3 Emerging technologies and applications
- SOEC and SOFC: ferritic Cr interconnects (Crofer 22 APU up to 900 C, developed by ThyssenKrupp VDM with FZ Juelich) [CROFER_TK_2003].
  Bloom Energy targets 2 GW/yr by end 2026, Brookfield up to USD 5bn for AI data centre deployment [BLOOM_2GW].
  Bloom's interconnect alloy is not public (TODO(data)).
- Large alkaline electrolysers: NEOM more than 2 GW thyssenkrupp nucera 20 MW modules, 600 t/d H2, commissioning 2027 [NEOM_H2].
- SMR and Gen IV: BWRX-300 at Darlington [OPG_DARLINGTON], Kairos KP-FHR with 316H stainless structure and FLiBe salt [KAIROS_316H].
  Some SMR concepts use non zirconium cladding (UxC listing, low).
- Fusion: ITER first wall needs up to 270 t CuCrZr-IG, divertor heat sink also CuCrZr-IG plate, pipe, forging [ITER_CUCRZR], Luvata supplies ITER grade [LUVATA_FUSION].
- Enhanced geothermal: Fervo Cape Station 100 MW Phase I, first power 24 Sep 2026, casing temperatures 400 F to 460 F [FERVO_CAPE_2026].
- CCS transport and storage hubs: Northern Lights 1.5 Mt/yr, Phase 2 at least 5 Mt/yr by 2H 2028 [EQUINOR_NL_2025].

## Q4 Materials required (alloy, grade, form, why)
| Application | Alloy / grade | Form | Why | Source |
|---|---|---|---|---|
| PWR steam generator tubes | Alloy 690, Alloy 800 | Tube (from bar/hollow) | PWSCC resistance, eddy current cleanliness | ALLEIMA_TM2026 |
| Fuel cladding, grids, channels | Zircaloy 2/4, ZrNb | Tube, strip | Low neutron absorption | UXC_ZIRC |
| Gen IV salt reactor structure | 316H | Plate | Qualified creep data in ASME code | KAIROS_316H |
| IGT combustor, transition duct | HASTELLOY X, HAYNES 282 | Sheet, plate | Oxidation and creep, fabricability | HAYNES_IGT |
| Alkaline electrolyser | Nickel (Ni 200/201 type), nickel coated steel | Strip, expanded mesh, sheet | Alkaline corrosion resistance, catalytic electrodes | IRENA_H2_2020 |
| SOEC/SOFC interconnect | Crofer 22 APU / 22 H type ferritic Cr steel | Thin strip | CTE match, conductive oxide at 600 to 900 C | CROFER_TK_2003 |
| PEM electrolyser (substitute) | Titanium, PGM | Sheet, porous transport layer | Acidic, high potential | IRENA_H2_2020 |
| FGD absorber inlet/outlet ducts, stacks | C-276, Alloy 59, 6Mo (AL-6XN) | Plate, sheet, wallpaper | Acid chloride condensate | NI_FGD |
| WtE waterwalls, superheaters | Alloy 625 overlay, 686 type filler | Weld wire, strip | Chloride molten salt corrosion | KAWAHARA_2007, SMC_686_WTE |
| Fusion first wall and divertor heat sink | CuCrZr-IG | Plate, pipe, forging | Conductivity plus strength at temperature | ITER_CUCRZR |
| CCS wells | 25Cr, Alloy 825 (team assessment, not confirmed for Northern Lights) | OCTG, clad | Wet CO2 corrosion | EQUINOR_NL_2025 notes |

## Q5 Geographic concentration
- China: 65% of installed or FID electrolyser capacity and nearly 60% of manufacturing capacity [IEA_H2_2025, IEA_H2_2030_FID],
  over 120 of 165 GW of wind [GWEC_GWR_2026], nearly 60% of new renewables to 2030 [IEA_REN_2025], large share of nuclear construction (secondary).
- North America and Europe: about 80% of 2030 CCS capture capacity [IEA_CCUS_2025], US about half of Q2 2026 gas turbine orders [TM_GT_ORDERS_Q2],
  nuclear new build (US, UK, Canada) [WEC_US_80BN, SZC_FID_2025, OPG_DARLINGTON].
- Middle East: NEOM hydrogen [NEOM_H2], gas turbine orders at Siemens Energy (secondary).
- India: FGD retrofits and wind (6.3 GW 2025) [PRAYAS_FGD_2025, GWEC_GWR_2026].

## Q6 Customers and competitors
Customers (OEMs, EPCs, Tier 1s): GE Vernova, Siemens Energy, Mitsubishi Power (IGT); Westinghouse, EDF/Framatome, GE Hitachi, Doosan Enerbility,
NuScale, Rolls-Royce SMR, Kairos Power (nuclear); thyssenkrupp nucera, ACWA Power, Air Products, Bloom Energy (H2/fuel cells);
Equinor, Shell, TotalEnergies (CCS); Fervo, Vallourec, Turboden (geothermal); Fusion for Energy, Ansaldo Nucleare (fusion).
Competitors: VDM Metals and Haynes (Acerinox HPA) [ACX_HAYNES], Special Metals [SMC_686_WTE], Alleima [ALLEIMA_TM2026],
ATI, Western Zirconium, Framatome, Westinghouse Specialty Metals, Chepetsky [UXC_ZIRC], Luvata [LUVATA_FUSION],
Integrated Global Services (thermal spray substitute) [IGS_HVTS]. Chinese electrolyser supply chain [ARGUS_ELY_2026].

## Q7 Competitor map
| Competitor | Application | Form | Strength |
|---|---|---|---|
| Acerinox HPA (VDM Metals, Haynes) | IGT combustors, SOFC interconnects, FGD | Sheet, plate, thin strip, wire | Grade ownership (HASTELLOY X, 282, Crofer, Alloy 59) |
| Special Metals | WtE overlay, IGT, nuclear | Bar, wire, filler | INCO-WELD filler range |
| Alleima | Steam generator tubes, fuel tubes | Tube | 400+ steam generators, +60% capacity 2026 |
| ATI, Western Zirconium, Framatome, Chepetsky | Zirconium cladding and sponge | Sponge, tube, strip | Integrated sponge to tube |
| Luvata | Fusion and magnets | CuCrZr, OF copper | ITER grade qualification |
| Chinese electrolyser chain | Alkaline stacks | Nickel components | Cost 50% or more below Western systems |

## Q8 Gain or lose relevance
Gain: alkaline (nickel) holds cost lead, SOEC/SOFC creates thin ferritic strip niche, SMR and Gen IV require qualified
Ni alloys and 316H, IGT boom pulls combustor sheet, CuCrZr for fusion.
Lose: PEM shifts electrolyser value to titanium and PGM [IRENA_H2_2020], HVTS thermal spray displaces Alloy 625 overlay in some WtE boilers [IGS_HVTS],
glass block and titanium clad stack linings undercut C-276 [NI_FGD], 6Mo substitutes C-276 in milder FGD zones [NI_FGD],
coal phase out in EU and US shrinks FGD, non zirconium SMR cladding [UXC_ZIRC].

## Q9 Attractive value chain steps
1. Qualified nuclear strip, bar and wire (Alloy 690 and 800 bar, Zr strip) where qualification is the entry barrier (cell N1).
2. Precision thin strip for SOEC/SOFC interconnects and nickel strip and mesh for alkaline stacks (cell N2), selling coated or slit to stack makers.
3. IGT combustor sheet and repair welding consumables, with MRO pull through as fleets run harder (TODO(data) on IGT MRO alloy volume).
4. Weld overlay wire and strip for WtE and FGD, defend position (cell N3).
Less attractive: commodity copper and aluminium for wind and solar (Chinese scale, low differentiation).

## Spotlight facts
1. Alleima, Tube Mill 2026, Sandviken (Sweden), inaugurated 2 June 2026, SEK 330m, +60% steam generator tube capacity,
   Alloy 690 (Sanicro 69) and Alloy 800 (Sanicro 30) tube, attendees Doosan Enerbility, NuScale, Rolls-Royce SMR, Westinghouse [ALLEIMA_TM2026].
2. NEOM Green Hydrogen Company (ACWA Power, Air Products, NEOM), Oxagon (Saudi Arabia), more than 2 GW alkaline modules
   from thyssenkrupp nucera, 600 t/d H2, commissioning 2027, nickel electrodes in sheet and mesh form, nickel semis suppliers undisclosed [NEOM_H2].
3. Fervo Energy, Cape Station, Beaver County (Utah), first power 24 Sep 2026, 100 MW Phase I, 7 inch casing at 400 F rising to 8 5/8 inch at 460 F,
   supply partners Vallourec, Turboden, ABB, casing grades undisclosed [FERVO_CAPE_2026].
4. GE Vernova, 116 GW gas backlog plus slots (Q2 2026), output to 30 GW/yr by 2030, combustor sheet in HASTELLOY X and HAYNES 282 type alloys,
   likely sheet suppliers Haynes (Acerinox) and other Ni alloy mills (team assessment) [GEV_2Q26, HAYNES_IGT].
5. Fusion for Energy, ITER (Cadarache, France), up to 270 t CuCrZr-IG for 215 first wall panels, plate and forging, Luvata qualified supplier [ITER_CUCRZR, LUVATA_FUSION].

## Open data gaps
- Bottom up validation of EUR 8.5bn and 6.5% p.a. (TODO(data)).
- Nickel tonnes per GW alkaline electrolyser (TODO(data), needs IEA Critical Minerals Data Explorer in data/raw/).
- IGT wrought superalloy tonnage and MRO share (TODO(data)).
- Zirconium tonnes per GW and SMR cladding choices (TODO(data), UxC paid).
- Bloom Energy interconnect alloy and supplier (TODO(data)).
- CRA grades in Northern Lights and Fervo wells (TODO(data)).
- Primary verification of GWEC, GE Vernova, Siemens Energy and IEA figures taken from search summaries.
