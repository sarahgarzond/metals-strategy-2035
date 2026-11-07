# Aerospace and defence (civil, defence, space): research notes

Section 3.4. Stage 1 research, 2026-11-07. Every figure maps to a data_id in data/sources.csv.
Data chain: Material > Product form > Application > Industry (Aerospace) > Geography > Market size > Growth.

Session limits: the WebSearch budget for the turn ran out before all planned searches were done, and
airbus.com, oliverwyman.com and argusmedia.com could not be fetched (host not allowed). Several figures therefore rest on
secondary coverage of primary releases and are flagged with confidence medium or low.

## 1. Market size and growth to 2035

### Sector activity (demand drivers)
| Metric | Value | data_id | Note |
|---|---|---|---|
| Airbus deliveries 2025 | 793 (766 in 2024) | AIRBUS_DELIV_2025 | 607 A320 family, 57 A350, 36 A330, 93 A220 |
| Airbus backlog end 2025 | 8,754 aircraft | AIRBUS_BACKLOG_2025 | cite as AIRBUS_DELIV_2025 |
| Airbus 2026 guidance | about 870 | AIRBUS_TARGET_2026 | A320 rate 70 to 75 per month by end 2027, held back by Pratt & Whitney engines |
| Boeing deliveries 2025 | 600 | BOEING_DELIV_2025 | 737 rate 42 to 47 per month, 787 rate 8 to 10 |
| Airbus GMF 2025 to 2044 | 43,420 new aircraft | AIRBUS_GMF_2025 | 34,250 single aisle, 9,170 widebody |
| Boeing CMO 2026 to 2045 | 43,625 new aircraft | BOEING_CMO_2026, BOEING_CMO_MIX_2026 | 33,545 single aisle, 7,715 widebody |
| Boeing services 2026 to 2045 | USD 4.9 trn cumulative | BOEING_SMO_2026 | |
| Commercial MRO 2026 | USD 139.6bn, 3.3% p.a. to 2036 | OW_MRO_2026 | fleet 30,046 to 41,135 (3.2% p.a.) |
| CFM LEAP deliveries 2025 | 1,802 (+28%) | GE_LEAP_2025 | +15% in 2026 per one secondary source |
| GE priority supplier material input 2025 | more than +40% vs 2024 | GE_SUPPLY_INPUT_2025 | direct proxy for mill and forge throughput |
| World military expenditure 2025 | USD 2,887bn, +2.9% real | SIPRI_MILEX_2025 | Europe USD 864bn (+14%), US USD 954bn, China USD 336bn |
| NATO target 2035 | 5% GDP, at least 3.5% core | NATO_HAGUE_2025 | previous benchmark 2% |
| Space economy | USD 630bn (2023) to USD 1.8 trn (2035), about 9% p.a. | WEF_SPACE_2035 | mostly services, hardware share small |
| SpaceX Falcon 9 launches 2025 | 165 (134 in 2024) | SPACEX_LAUNCH_2025 | global count 324 to 329 depending on tracker |

### High performance metal demand within the sector
| Metric | Value | data_id |
|---|---|---|
| Aerospace and defence demand for Client addressable metals 2025 | EUR 7.5bn (team estimate) | MODEL_AERO_2025 |
| CAGR 2025 to 2035 | 7.0% p.a. (team estimate) | MODEL_AERO_2025 |
| 2035 | EUR 14.8bn = 7.5 x 1.07^10 (team estimate) | MODEL_AERO_2025 |
| Share of Client addressable market | 14.8% of EUR 50.6bn | MODEL_TOTAL_2025 |
| Model cell A1 Ni superalloys 718, 625, 282 bar, billet, wire | EUR 3.8bn, 7.5% p.a. | MODEL_AERO_2025 |
| Model cell A2 Ni and Co superalloy AM powder | EUR 350m, 15% p.a. | MODEL_AERO_2025 |
| Model cell A3 Ni alloys for defence and space, sheet and bar | EUR 700m, 9% p.a. | MODEL_AERO_2025 |

Scope: excludes titanium, which the Client does not produce. Includes Ni and Co alloys, specialty stainless, aluminium and
copper products, AM powders and welding consumables sold into aerospace OEM, MRO, defence and space.

Triangulation of the EUR 7.5bn (order of magnitude check, not a bottom up proof):
- ATI FY2025 sales USD 4.6bn, A&D 68% (call), so about USD 3.1bn A&D (team estimate) [ATI_FY2025].
- Carpenter FY2026 sales USD 3,124m, A&D about 65% (secondary, unverified), so about USD 2.0bn (team estimate) [CRS_FY2026].
- Two US mills alone therefore sell about USD 5bn into A&D, before PCC (Special Metals, not disclosed by Berkshire),
  Acerinox HPA (Haynes, VDM), Aubert & Duval, Proterial, Chinese mills and aluminium and copper suppliers. EUR 7.5bn looks
  conservative rather than aggressive. TODO(data): EUR/USD rate row for conversions, PCC and Chinese mill A&D revenue.

Growth cross checks for 7.0% p.a.: Airbus 2026 target +9.7% vs 2025 (team calculation 870/793), LEAP +28% in 2025,
ATI jet engine sales +21% [ATI_FY2025], Carpenter A&D +15% [CRS_FY2026], Howmet Engine Products +16% with commercial engine
spares +44% [HWM_ENGINE_2025], MRO only 3.3% p.a. [OW_MRO_2026]. The near term rate is clearly above 7%, the long run
(fleet 3.2% p.a., MRO 3.3% p.a.) below it, so 7% averages a ramp up phase to about 2029 and a normal phase after.
TODO(data): kg of superalloy per LEAP, GTF, Trent engine (buy weight versus fly weight) for a volume build.

## 2. Drivers and risks
Drivers: record backlog (8,754 Airbus), narrowbody rate ramp (A320 70 to 75 per month, 737 to 47), next generation engine
content per engine rising (ATI management comment in ATI_FY2025), spares boom from GTF and LEAP durability problems
(HWM_ENGINE_2025), European rearmament (+14% in 2025, NATO 3.5% core by 2035), launch cadence (SpaceX 165).
Risks: engine OEM supply bottlenecks (Pratt & Whitney commitments limit A320 ramp), quality escapes (GTF powder metal),
substitution by CMC in the hot section, composite airframes, US tariffs (Airbus guidance includes current tariffs),
cyclical shocks (2020 style), long qualification cycles (often 2 to 5 years, team knowledge, TODO(data) source),
nickel and cobalt price and supply risk (see 2.2, 2.3), capacity build by incumbents (ATI 9 kt VIM, Carpenter 9,000 t).

## 3. Emerging technologies and applications
- Powder metallurgy discs and AM: LEAP fuel nozzle tips, 100,000 shipped from Auburn by 2021, 20 parts to 1, about 25% lighter [GE_AM_NOZZLE].
- CMC hot section: LEAP 18 CMC shrouds, GE9X liners and nozzles [ACERS_CMC_LEAP], density one third of Ni alloys, 2,400 F [GE_CMC_PROPS].
- Space propulsion: copper alloy GRCop-42 (CuCrNb) powder for regeneratively cooled chambers, KBM 2023, Sandvik Osprey [GRCOP_KBM_2023].
  In house superalloys at SpaceX (SX500) [SPACEX_SX500], low confidence.
- Aluminium lithium plate and extrusions (Constellium Airware, Issoire and Ravenswood) [CSTM_EMBRAER_2025].
- Not sourced this round: open rotor (CFM RISE), hydrogen (Airbus ZEROe), hybrid electric, hypersonics. TODO(data).

## 4. Materials required (alloy, grade, form, why)
| Application | Alloy | Form | Why |
|---|---|---|---|
| Discs, shafts, casings, fasteners | Alloy 718, 718Plus, Waspaloy, 720Li, PM grades | VIM/VAR billet, bar, ring rolled forgings, wire for fasteners | strength and fatigue to about 650 to 700 C |
| Combustors, ducts, exhaust | Alloy 625, Hastelloy X, HAYNES 230, 282 | sheet, strip, wire | oxidation resistance, weldability |
| Seals, honeycomb, bellows, springs | Alloy 718, X750, Co alloys | thin strip, foil, wire | elasticity at temperature |
| Hot section repair, MRO | 625, 718, Co based filler | welding wire, rod, powder | spares and repair boom |
| AM parts (nozzles, brackets, space) | 718, 625, CoCr, GRCop-42, CuCrZr | gas atomised powder | part consolidation |
| Airframe | 7xxx, 2xxx, Al-Li alloys, PH stainless (15-5PH, 17-4PH) | plate, sheet, extrusions, bar | strength to weight |
| Rocket chambers | Cu alloys (GRCop-42, CuCrZr), 718 | powder, bar, strip | thermal conductivity |
| Electrical and harness | high conductivity Cu, CuNi | wire, strip | conductivity |
Material notes are team metallurgical knowledge, sources for content per engine still TODO(data).

## 5. Geographic concentration of demand
Final assembly and engine OEM hubs: US (GE Aerospace Evendale and Lafayette, Pratt & Whitney East Hartford, Boeing Seattle and
Charleston), France (Airbus Toulouse, Safran), UK (Rolls-Royce Derby), Germany (Airbus Hamburg, MTU Aero Engines Munich,
Rolls-Royce Dahlewitz), China (COMAC Shanghai). Fleet demand shifts east: Asia-Pacific 46% of new passenger aircraft demand
to 2044 [AIRBUS_GSF_APAC]. Defence spend: US 33% of world, Europe fastest at +14% [SIPRI_MILEX_2025].
Metal buying, however, stays concentrated in the US and Western Europe, where the forgers and casters sit (Howmet, PCC, Aubert & Duval, Otto Fuchs, Leistritz).
TODO(data): regional split of aerospace metal demand, UN Comtrade HS 7505/7506/7507 into US, FR, UK, DE.

## 6. Customers and competitors
Customers. Airframers: Airbus, Boeing, COMAC, Embraer, Dassault. Engines: GE Aerospace, Safran, CFM, Pratt & Whitney (RTX),
Rolls-Royce, MTU Aero Engines. Tier 1 and forgers: Howmet, PCC (Wyman Gordon), Aubert & Duval, Otto Fuchs, Leistritz, GKN Aerospace.
Space: SpaceX, ArianeGroup, Blue Origin, Rocket Lab, Isar Aerospace. MRO: Lufthansa Technik, MTU Maintenance.
Competitors. Mills: PCC Special Metals, ATI, Carpenter, Haynes and VDM (Acerinox HPA), Aubert & Duval, voestalpine Böhler,
Proterial, Daido, Chinese mills. Al: Constellium, Arconic, Kaiser, Novelis. Powder: Carpenter Additive, Sandvik Osprey, Höganäs,
Oerlikon, KBM. Strip and wire specialists: Ulbrich, Fort Wayne Metals, Alleima. Distributors: Reliance (AMI Metals),
thyssenkrupp Materials Services aerospace, TW Metals. Names from team knowledge where no data_id is given, verify in round 2.

## 7. Competitor map (see section table)
- PCC Special Metals: Inconel trademark family, billet and bar, integrated with forging and casting. Strength vertical integration.
- ATI: Monroe NC fifth VIM furnace, 9 kt/yr from H2 2027 [ARGUS_SUPERALLOY], jet engine sales +21% [ATI_FY2025]. Billet, bar, sheet, powder.
- Carpenter: Athens AL brownfield, about USD 400m, +9,000 t melt, early FY2028 [CRS_ATHENS]. Bar, billet, wire, powder.
- Acerinox HPA (Haynes, VDM): HPA EBITDA EUR 135m +15% [ACX_HPA_2025], Haynes sheet for combustors, VDM strip and wire.
- Aubert & Duval: owned by Airbus, Safran, Tikehau Ace (EV EUR 95m, 2022) [AD_ACQ_2022], closed die forgings, powders.
- Howmet: castings, fasteners, engine products +16% [HWM_ENGINE_2025]. Customer rather than competitor for mills.
- Constellium: Airware Al-Li plate [CSTM_EMBRAER_2025].

## 8. Gain or loss of relevance
Gain: hotter and more numerous engines, spares, AM powder, space copper alloys, defence engines.
Loss: CMC replacing Ni alloy in shrouds, liners, nozzles [ACERS_CMC_LEAP, GE_CMC_PROPS], composites and titanium replacing
aluminium in airframes (787 50% composites, 20% aluminium, 15% titanium, 10% steel) [B787_MATERIALS].
Net view (team assessment): Ni alloys keep rotating parts (discs, shafts) where CMC is not used, CMC takes static hot parts,
aluminium loses airframe share in widebodies but holds it in narrowbodies until a new single aisle programme.

## 9. Attractive value chain steps for the Client
1. Thin strip, sheet and wire in 718, 625, 282 and X750 for casings, seals, springs and fasteners (fits Client forms).
2. Welding wire and repair powders for MRO (spares +44% at Howmet).
3. AM powders in Ni, Co and Cu alloys (cell A2 at 15% p.a.), including GRCop type copper powder for space.
4. Defence and space niche sheet and bar (cell A3, 9% p.a.).
Less attractive: large diameter rotating grade billet (incumbents adding capacity, heavy VIM/VAR capex, long qualification),
commodity aluminium plate (scale players).

## Spotlight facts
1. ATI, Monroe NC, fifth VIM furnace, 9 kt/yr, H2 2027, Ni superalloy remelt stock for billet and bar, customers engine OEMs [ARGUS_SUPERALLOY]. Carpenter Athens AL, +9,000 t, early FY2028 [CRS_ATHENS].
2. Pratt & Whitney GTF (PW1100G-JM): July 2023 powder metal condition, HPT stage 1 and 2 discs, engines built mid 2015 to mid 2021 [GTF_PM_2023]. About 3,000 engines in scope and 637 aircraft parked April 2024 (secondary, in notes). Supplier of the powder not identified, TODO(data).
3. GE Aerospace Auburn AL, LEAP fuel nozzle tips by laser powder bed fusion, 100,000 shipped by August 2021, 19 per engine [GE_AM_NOZZLE]. At 1,802 LEAP in 2025 that is about 34,000 tips per year (team estimate = 1,802 x 19). Alloy reported as CoCr in GE patents, not confirmed for LEAP.
4. GRCop-42 CuCrNb powder for rocket chambers, KBM Advanced Materials (Ohio, 2023), Sandvik Osprey, printers Velo3D, Nikon SLM [GRCOP_KBM_2023].
5. Airbus, Safran and Tikehau Ace buy Aubert & Duval (France, February 2022, EV EUR 95m) to secure superalloy and forging supply [AD_ACQ_2022].

## Open data gaps
- TODO(data): superalloy kg per engine and buy to fly ratio (searched superalloy tonnage, only paid reports found).
- TODO(data): regional split of aerospace metal demand (Comtrade query not run).
- TODO(data): aerospace share of Acerinox HPA and VDM sales.
- TODO(data): EUR/USD conversion row.
- TODO(data): confirm LEAP nozzle alloy, GTF powder supplier, Aubert & Duval deal closing.
- TODO(data): verify SIPRI figures in SIPRI fact sheet, Airbus GSF 46% in Airbus PDF.
- TODO(data): Rafale and European fighter engine rates, COMAC C919 deliveries (search budget exhausted).
