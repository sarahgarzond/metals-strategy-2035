# Research notes: Oil and gas including LNG (report section 3.2)

Status: Stage 1 research, retrieved 2026-11-07. All figures map to rows in data/sources.csv (data_id in brackets).
Access limits in this session: iea.org returned 403, most trade press and company hosts (gtt.fr, alleima.com, butting.com,
offshore-technology.com, steelorbis.com, igu.org, rivieramm.com) did not resolve, and the shared WebSearch budget ran out
mid task. Many figures therefore come from search result summaries of primary pages and are logged with confidence
medium. They must be verified against the primary PDF before the executive summary uses them.

## Data chain position
Material > Product form > Application > Industry (Oil and gas) > Geography > Market size > Growth
Model cells (model/model.py): O1 LNG (Alloy 625, 825, Invar 36, 9% Ni, plate, clad, strip, US QA KR CN, EUR 1.3bn, 4.5% p.a.)
and O2 sour and deepwater (Alloy 825, 625, 718, clad pipe, OCTG, bar, ME BR NO, EUR 2.2bn, 2.0% p.a.) [MODEL_OG_CELLS].
Sector total EUR 8.0bn 2025, 2.0% p.a., EUR 9.75bn 2035 [MODEL_OG_2025]. All three are team estimates.

## Q1 Market size and growth to 2035
Sector spend (driver indicators):
| Indicator | Value | Year | data_id |
|---|---|---|---|
| Upstream oil and gas investment | just under USD 570bn, down about 4% | 2025 | IEA_WEI2025_UPSTREAM |
| Upstream oil investment | below USD 500bn, third annual fall | 2026 | IEA_WEI2026_UPOIL |
| Total gas investment | USD 330bn, decade high, upstream gas plus 8% | 2026 | IEA_WEI2026_GAS |
| Offshore energy capex | above USD 300bn | 2026 | RYSTAD_OFFSHORE_2026 |
| LNG export capacity additions | 345 bcm/yr (about 250 Mtpa) | 2025 to 2030 | IEA_LNG_TRACKER |
| LNG FIDs | 68.4 Mtpa (IGU) vs 84 Mtpa (LNG Prime) | 2025 | IGU_LNG_FID_2025, LNGPRIME_FID_2025 |
| LNG demand | 422 Mtpa to 650 to 710 Mtpa | 2025 to 2040 | SHELL_LNG_OUTLOOK_2026 |
| Stainless OCTG world exports HS 730424 | USD 2.48bn, 266 kt | 2024 | COMTRADE_730424_2024 |
| Clad pipe market (market report) | about USD 3.9bn | 2023 | CLADPIPE_MR_2023 (triangulation only) |

High performance metal demand in the sector: EUR 8.0bn in 2025 and about EUR 9.75bn in 2035 at 2.0% p.a. [MODEL_OG_2025].
Assessment: the 2.0% average hides a split. LNG and gas grow faster (Shell implies about 3% p.a. LNG demand growth
2025 to 2040: (680/422)^(1/15) minus 1 = 3.2% at the midpoint, team calculation), while upstream oil spend falls three
years in a row. The model O1 cell at 4.5% and O2 at 2.0% are consistent with this direction. The residual EUR 4.5bn
(refining, valves, pumps, general MRO) is not evidenced yet: TODO(data): searched for a refinery and downstream
nickel alloy demand figure, none found, IEA WEO refinery capacity outlook needed from a manual download.

Implied team check of the Shell growth: (650/422)^(1/15) = 2.9% p.a., (710/422)^(1/15) = 3.5% p.a.

## Q2 Drivers and risks
Drivers
1. LNG wave: 345 bcm/yr capacity 2025 to 2030 [IEA_LNG_TRACKER], record FIDs in 2025, US above 90% of FIDs (IEA via
   press). Each train needs cryogenic piping, 9% Ni tanks, Ni base welding consumables, and the carriers need Invar or 304L membranes.
2. Shipping: GTT booked 37 LNG carrier orders in 2025, order book 261 LNG carriers at year end [GTT_FY2025], CEO sees
   about 150 carriers needed for 2025 FIDs [LNGPRIME_FID_2025].
3. Sour and acid gas in the Gulf: Hail and Ghasha EPC awards about USD 17bn [ADNOC_HAILGHASHA_EPC], SeAH and Inox Tech
   200,000 t of line pipe and clad pipe including 14,000 t clad [SEAH_ADNOC_2023].
4. Brazilian pre salt (high CO2, H2S): Alloy 625 lined pipe for Buzios [CLADTEK_BUZIOS10, BUTTING_BRAZIL_MLP, VALLOUREC_BUZIOS].
5. Decline mitigation: about 40% of upstream spend slows declines at existing fields [IEA_WEI2025_UPSTREAM], ageing
   fields produce more water and CO2, which raises corrosion severity.
6. CCS wells need CRA once free water is present [AADE_CCS_CRA].

Risks
1. Falling upstream oil capex [IEA_WEI2026_UPOIL], US shale spend down 7%.
2. Geopolitics: March 2026 strikes on Ras Laffan affected about 17% of Qatari LNG export capacity, repair three to five
   years, Hormuz transits minimal, force majeure extended monthly [RASLAFFAN_DAMAGE_2026]. North Field East first train
   reported slipping to H1 2027 [QATAR_NFE_2026]. Two way effect: delays Qatari demand for metals, but raises security of
   supply investment elsewhere (US, Africa, Asia regas).
3. Substitution by high Mn steel, TCP, clad instead of solid (Q8).
4. Nickel price volatility (see DEN_NI_PRICE_2026, section 2.2) feeds directly into CRA quotes.
5. Shipyard and FPSO capacity bottlenecks 2026 to 2027 [RYSTAD_OFFSHORE_2026].

## Q3 Emerging technologies and applications
1. Ultra large LNG carriers, 271,000 m3 with NO96 Super+ at Hudong-Zhonghua [GTT_FY2025]. More Invar per vessel (team assessment).
2. Mechanically lined pipe (MLP) instead of metallurgically clad or solid CRA for reeled installation in Brazil
   [BUTTING_BRAZIL_MLP, CLADTEK_BUZIOS10]. Liner is a thin CRA tube made from strip or plate.
3. CCS injection wells and CO2 pipelines: 25Cr super duplex and Ni alloys in the wet zone [AADE_CCS_CRA].
   TODO(data): Northern Lights tubing specification, searched, not found (Stainless Steel World lead unverified).
4. Hydrogen service qualification of overlay pipe (market report mention only, CLADPIPE_MR_2023 notes, low).
5. Thermoplastic composite pipe for jumpers [STROHM_WHIPTAIL_2024] (substitute).
6. Subsea tiebacks and subsea tree awards peaking 2028 [RYSTAD_OFFSHORE_2026], which means umbilicals and 718 bar.

## Q4 Materials required
| Application | Alloy and grade | Product form | Why | Client fit |
|---|---|---|---|---|
| LNG carrier membrane (GTT NO96) | Invar FeNi36 (Aperam Invar M93) | Cold rolled strip 0.7 mm, 500 to 536 mm strakes | Near zero thermal expansion at minus 163 C | Strip, FeNi36 in portfolio (electronics) |
| LNG carrier membrane (GTT Mark III) | 304L | Corrugated sheet | Cheaper membrane | Commodity, low fit |
| Onshore LNG tanks | 9% Ni steel | Plate | Toughness at minus 196 C | Plate is steel mill product, low fit, but Ni base filler metal is high fit |
| Welding of 9% Ni and CRA girth welds | Ni base fillers (ERNiCrMo-3 / Alloy 625 type) | Wire, strip | Matching strength and toughness at cryogenic temperature | Welding consumables in portfolio |
| Sour gas and pre salt flowlines and risers | Alloy 625, Alloy 825 | Liner strip and plate for MLP and clad plate | H2S, CO2, chlorides | High fit |
| Sour well completions | Alloy 825, G3, 028 type, 718 | Seamless tube, bar | ISO 15156 sour service limits | Tubes made by integrated Japanese mills, bar is a fit |
| Subsea valves, hangers, bolts | Alloy 718, 725 | Bar, forging stock | High strength plus sour resistance | Bar is a fit |
| Umbilicals | Super duplex SAF 2507 | Seamless tube | Hydraulic control lines | Alleima dominated |
| CCS wells | 25Cr super duplex, Ni alloys | Tube | Wet CO2 corrosion | Medium |
Note: ISO 15156, API 6A 718 and the filler designations are standard industry knowledge, no source row needed for
non numeric facts, but the team should add a citation for ISO 15156 in the final round. TODO(data): 9% Ni steel tank
plate tonnage per 160,000 m3 tank, not searched because of budget.

PREN values: 13Cr about 13, 22Cr about 36, 25Cr about 42 [AADE_CCS_CRA].

## Q5 Geographic concentration of demand
1. United States: above 90% of 2025 LNG FIDs (IEA via press), 62 Mtpa of 84 Mtpa per LNG Prime [LNGPRIME_FID_2025].
2. Qatar: NFE 32 Mtpa plus NFS 16 Mtpa, target 142 Mtpa [QATAR_NFE_2026], disrupted [RASLAFFAN_DAMAGE_2026].
3. UAE and Saudi Arabia: sour gas, Middle East record 20% of upstream spend in 2025 [IEA_WEI2025_UPSTREAM].
4. Brazil: pre salt MLP [BUTTING_BRAZIL_MLP, CLADTEK_BUZIOS10].
5. Korea and China shipyards for Invar demand [APERAM_IMPHY_2025, GTT_FY2025].
6. Southeast Asia gas: Kutei North Hub Indonesia [ALLEIMA_KUTEI_2026].
7. Supply side of OCTG: Japan 57% of HS 730424 exports [COMTRADE_730424_2024].

## Q6 Customers and competitors
Customers (named in evidence): Petrobras, Allseas, TechnipFMC, Subsea 7, Saipem, ADNOC, NPCC, Tecnimont, QatarEnergy,
GTT (licensor that specifies Invar), Hanwha Ocean, HD Hyundai Samho, Hudong-Zhonghua, ExxonMobil Guyana. Pipe makers as
direct customers for liner material: Butting, Cladtek, Inox Tech (SeAH), Vallourec.
Further LNG EPCs (Bechtel, Technip Energies, Chiyoda, McDermott, KBR) are named from team knowledge, no award detail logged.

Competitors: Aperam Alloys Imphy (Invar M93, doubling capacity [APERAM_IMPHY_2025]), VDM Metals within Acerinox HPA
together with Haynes [ACX_HAYNES], Special Metals (PCC), ATI, Alleima (umbilical and OCTG tubes [ALLEIMA_KUTEI_2026]),
Nippon Steel and JFE (Japan 57% of stainless OCTG exports [COMTRADE_730424_2024]), Tenaris, Vallourec, POSCO (9% Ni
and HMS [POSCO_HMS]). Welding consumables: voestalpine Böhler Welding, ESAB, Lincoln Electric (team knowledge, not logged).
Distributors: TODO(data): no distributor evidence retrieved (Corrotherm and Rolled Alloys are candidates from search hits).

## Q7 Competitor map
| Competitor | Application | Form | Strength |
|---|---|---|---|
| Aperam Imphy | LNG membranes NO96 | Invar strip strakes | Incumbent, doubled capacity 2025, GTT reference |
| VDM Metals plus Haynes (Acerinox) | Clad, OCTG feedstock, 718 bar, Invar | Plate, strip, bar, wire | Full Ni alloy range, German peer of the Client, scale after Haynes deal |
| Special Metals (PCC) | Subsea bolts, 718 and 725 bar, OCTG | Bar, tube | US qualification base |
| Nippon Steel, JFE | Sour well OCTG | Seamless tube | Japan 57% of HS 730424 exports |
| Alleima | Umbilicals, OCTG | Seamless tube | SAF 2507 reference, SEK 995m order |
| Butting, Cladtek, Inox Tech, Vallourec | Lined and clad pipe | MLP, clad pipe | Customers for liner strip, also competitors to clad plate |
| POSCO | Onshore LNG tanks | 9% Ni plate, HMS plate | Substitution threat |
Strength descriptions without a data_id are team assessments.

## Q8 Where high performance metals gain or lose relevance
Gain: sour gas and pre salt (Hail and Ghasha, Buzios), CCS wet zones, LNG membranes (Invar), Ni base welding
consumables, older fields with more water and CO2.
Lose: high Mn steel claims about 30% cheaper material than 9% Ni steel [POSCO_HMS], TCP replaces steel jumpers (70 in
Stabroek) [STROHM_WHIPTAIL_2024], clad and lined pipe replaces solid CRA (market report says overlay at 40 to 60% of
solid CRA installed cost, low confidence), 304L Mark III membranes compete with Invar NO96. Titanium stress joints and
composite risers are niche (team knowledge, not quantified). TODO(data): share of LNG carrier orders by GTT technology
(NO96 vs Mark III) not retrieved.
Net effect: mass of solid Ni alloy per project falls, but thin liner strip, clad plate and consumables gain.

## Q9 Attractive value chain steps for the Client
1. Ni alloy liner strip and plate (625, 825) sold to MLP and clad pipe makers (Butting, Cladtek, Inox Tech). Strip is a
   core Client form. Medium competition.
2. Ni base welding consumables for CRA girth welds, overlay and 9% Ni tanks. Recurring, project linked, high margin
   (team assessment).
3. Second source Invar FeNi36 strip for membranes with GTT qualification. Aperam is the incumbent, qualification is
   the barrier (team assessment).
4. 718 and 725 bar for subsea equipment (Tier 1 TechnipFMC, SLB OneSubsea, Baker Hughes are candidates, team knowledge).
Less attractive: seamless OCTG (Japan integrated mills), 9% Ni plate (steel mills), umbilical tube (Alleima).

## Spotlights
1. Petrobras Buzios 10, Brazil: Allseas awarded Cladtek 120 km of Inconel 625 mechanically lined pipe, Petrobras
   largest MLP scope to date [CLADTEK_BUZIOS10]. Metal Alloy 625, form liner tube from strip or plate. Likely liner
   suppliers: VDM, Special Metals, Client (team assessment). TODO(data): award date.
2. Aperam Imphy, France, March 2025: new line doubles Invar M93 capacity for GTT NO96, strakes up to 50 m, 536 mm wide,
   under 1 mm, for Korean and Chinese yards [APERAM_IMPHY_2025, GTT_NO96_SPEC].
3. ADNOC Hail and Ghasha, UAE: USD 17bn EPC (Saipem, NPCC, Tecnimont), SeAH and Inox Tech 200,000 t pipe incl. 14,000
   t clad from H1 2024 [ADNOC_HAILGHASHA_EPC, SEAH_ADNOC_2023]. Liner alloy not disclosed (likely 625 or 825, team assessment).
4. Kutei North Hub, Indonesia, June 2026: Alleima SEK 995m SAF 2507 umbilical tubing, deliveries 2026 to 2030 [ALLEIMA_KUTEI_2026].

## Open data gaps
1. Residual EUR 4.5bn downstream and MRO demand inside the sector total, no evidence.
2. Nickel alloy consumption by end use (Nickel Institute), not found.
3. Award dates and liner tonnage for Cladtek Buzios 10.
4. 9% Ni plate and Ni filler mass per LNG tank and per train.
5. GTT technology split NO96 vs Mark III in the order book, Invar tonnes per vessel.
6. Northern Lights and other CCS well material specifications.
7. Distributor landscape for oil and gas Ni alloys.
8. IEA WEO 2025 oil and gas demand 2035 by scenario (search budget exhausted).
