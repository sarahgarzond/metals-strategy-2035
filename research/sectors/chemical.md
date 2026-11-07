# Research notes: Chemical process industry (report section 3.5)

Stage 1 research, retrieved 2026-11-07. Every figure maps to a data_id in data/sources.csv.
Access limits in this session: WebFetch failed for cefic.org, americanchemistry.com, globaldata.com and mysteel.net
(hosts not resolvable in the cloud session), so these figures come from WebSearch result summaries and are marked
"verify". The shared WebSearch budget was exhausted mid task, so several open points stay TODO(data).

## Data chain anchor
Material > Product form > Application > Industry > Geography > Market size > Growth

| Cell | Material | Form | Application | Region | 2025 EUR m | CAGR | 2035 EUR m | data_id |
|---|---|---|---|---|---|---|---|---|
| C1 | Alloy C-276, 59 (N06059), 31 (N08031), 625 | Plate, sheet, clad plate | Acid, chlorine, pharma reactors, columns, heat exchangers | EU, CN, US | 2,600 | 3.0% | 3,494 | MODEL_CHEM_CELLS |
| C2 | Ni alloys, super duplex (titanium alternative) | Plate, tube | HPAL, nickel sulphate, lithium refining | ID, CN, US, EU | 600 | 9.0% | 1,420 | MODEL_CHEM_CELLS |
| C3 | Zr 702, 705 | Plate, tube | Acetic acid, urea, sulfuric acid | CN, ME, US | 300 | 4.0% | 444 | MODEL_CHEM_CELLS |
| Sector total | All Client materials | All | All CPI | World | 9,000 | 2.5% | 11,520 | MODEL_CHEM_SECTOR |

All four lines are team estimates from model/model.py (low confidence). The sector total is a top down allocation of the
EUR 50.6bn addressable market (MODEL_TOTAL_2025). The remaining EUR 5.5bn of the sector total (team arithmetic, 9.0 minus
3.5) sits in specialty stainless (904L, 6Mo, super duplex), Ni 200/201, Alloy 400, 600, high alloyed welding consumables and
MRO volumes that are not yet broken out as separate cells. TODO(data): bottom up build by alloy from Eurostat PRODCOM
(24.45.30 nickel plates, sheets, strip) and UN Comtrade HS 7506, 7507, 8109 trade into chemical hubs.

## Q1 Market size and growth to 2035
Sector itself:
- World chemical sales 2024 about EUR 5.1 trillion, team arithmetic from Cefic (2004 EUR 1,406bn x 3.6) [CEFIC_WORLD_2024]. Low confidence, verify the stated value.
- Short term volume path: ACC January 2026 view 2.6% in 2025 [ACC_JAN_2026]. After the 2026 Gulf war and Strait of Hormuz closure, ACC mid year 2026 sees 0.5% in 2026 and 3.2% in 2027 [ACC_MIDYEAR_2026], Atradius 0.6% in 2026 [ATRADIUS_CHEM_2026].
- Long term growth 2025 to 2035: TODO(data): no primary long run forecast secured. Searched for UNEP Global Chemicals Outlook, OECD and ACC long range, budget ran out. Candidates: UNEP GCO II (sales projection to 2030), Cefic 2050 scenarios, ACC long term outlook.
High performance metal demand within it:
- Team estimate EUR 9.0bn in 2025, 2.5% p.a. to EUR 11.5bn in 2035 [MODEL_CHEM_SECTOR]. This makes CPI the largest sector by 2025 value in the model but one of the slowest growing.
- Triangulation: Haynes chemical processing product revenue USD 54.7m in the nine months to June 2024, down 20.7% y/y, about 12% of net revenue of USD 453.7m (team arithmetic) [HAYNES_10Q_2024]. Q3 FY2024 CPI volume +13.4% while average price -19.0%, showing price competition in CPI.
- Acerinox HPA (VDM plus Haynes) EBITDA EUR 135m in 2025 (+15%), despite weaker oil and gas and chemical processing demand [ACX_FY2025_HPA]. Management: CPI projects delayed [ACX_Q3_2025_CALL].
- Nickel first use: 9% of nickel goes into non ferrous alloys [NRCAN_NI_ENDUSE]. No CPI share of this, TODO(data) Nickel Institute or INSG.
- Paid reports (Hastelloy market, C-276 market) gave inconsistent numbers that differ by an order of magnitude. Not used.

Assessment: 2.5% p.a. looks plausible against weak 2025 to 2026 capex, but the model value of EUR 9.0bn is not
triangulated. If Haynes and VDM are representative, CPI is 10 to 20% of high performance nickel alloy mill revenue
(team assessment from one data point). Flag openly in prose.

## Q2 Drivers and risks
Drivers
1. Asian capacity build in acetic acid and derivatives: global acetic acid capacity 20.51 Mtpa (2023) to 29.09 Mtpa (2028), China 6.70 Mtpa and more than 90% of additions [GD_ACETIC_2028]. Asia adds 9.92 Mtpa in 2025 to 2030, largest single project in India [GD_ACETIC_2030]. Zr 702 is the standard for hot acetic acid (methanol carbonylation, Monsanto and Cativa type).
2. Middle East and Asian chlor alkali and PVC complexes: TA'ZIZ Ruwais PVC 500 kt/yr, caustic up to 796 kt/yr [NUCERA_TAZIZ]. nucera record new build chlor alkali order Dec 2025, plant completion end 2028 [NUCERA_MIDEAST_2025]. nucera Q2 FY2025/26 order intake EUR 316m, chlor alkali EUR 140m [NUCERA_Q2_2026].
3. Battery materials hydrometallurgy: Pomalaa HPAL, 120 kt/yr Ni in MHP, first two of five autoclaves January 2026, start Q3 2026 [VALE_POMALAA_2026].
4. Electrification and decarbonisation of base chemicals: BASF, SABIC and Linde e cracker demonstration, Ludwigshafen, April 2024, 6 MW, about 4 t/h [BASF_ECRACKER_2024], EUR 14.8m federal funding [TCE_ECRACKER_FUND].
5. PFAS regulation as a pull for metallic solutions: RAC opinion March 2026, SEAC draft 10 March 2026, final SEAC late 2026, no restriction in force before 2028 [ECHA_PFAS_2026]. Average European chemical plant has about 20,000 PFAS containing elements excluding piping, nickel alloys, Hastelloy and glass closest to fluoropolymer compatibility [CEFIC_PFAS_EQUIP_2026].
6. MRO and replacement in an ageing installed base (qualitative, TODO(data) on MRO share of CRA demand).
Risks
1. European capacity loss: 37 Mt closed since 2022, about 9% of capacity, Germany 8.8 Mt [CEFIC_CLOSURES]. EU output April 2026 16% below pre crisis [CEFIC_IRIS_2026_04]. EU share of world sales 13% versus China 46% [CEFIC_FF2025_SHARES].
2. Chinese capex downturn: FAI in raw chemical materials -7.9% Jan to Oct 2025 [NBS_FAI_CHEM_2025], -8.1% Jan to Aug 2026 [NBS_FAI_CHEM_2026]. Overcapacity in acetic acid (Mysteel, not fetched).
3. Gulf conflict 2026 and energy shock [ATRADIUS_CHEM_2026, ACC_MIDYEAR_2026].
4. Price competition: Haynes CPI average price -19% in Q3 FY2024 [HAYNES_10Q_2024].
5. Substitution by titanium, super duplex and non metallics (see Q8).
6. PFAS derogations could reduce the substitution upside (SEAC supports targeted derogations) [ECHA_PFAS_2026]. Industry funded Ricardo study: only about 10% of piping and 30% of seals replaceable [RICARDO_PFAS_REFINING].

## Q3 Emerging technologies and applications
- Electrically heated steam crackers (BASF Ludwigshafen) [BASF_ECRACKER_2024]. Direct resistive heating of tubes needs alloys with stable resistivity, creep and carburisation resistance. Tube alloy not disclosed, TODO(data). Team metallurgical view: centrifugally cast HP type and wrought Alloy 800H/HT or 617 type, and FeCrAl for heating elements in the radiant design.
- HPAL and nickel sulphate, cobalt sulphate and lithium hydroxide refining [VALE_POMALAA_2026].
- Membrane chlor alkali with nickel cathodes [INEOS_MEMBRANE_NI], now extending into alkaline water electrolysis (cross link section 3.3).
- PFAS free equipment design, metallic seals, lined to solid alloy shift [CEFIC_PFAS_EQUIP_2026].
- Urea high pressure section with new super duplex SAF 2906 [ALLEIMA_SAF2906] and bimetallic Zr 702 lined stripper tubes [ALLEIMA_STRIPPER].
- TODO(data): chemical recycling (pyrolysis), CO2 to methanol, green ammonia material specs not researched (budget).

## Q4 Materials required (alloy, grade, form, why)
| Application | Alloy and grade | Form | Why | Client fit |
|---|---|---|---|---|
| HCl, mixed acids, chlorinated organics, pharma API reactors | Alloy C-276 (N10276), C-22 (N06022), 59 (N06059), C-2000 | Plate, sheet, clad plate, tube, welding wire ERNiCrMo-4/-10/-13 | Mo and W resist reducing acids and pitting, low Fe avoids contamination | Core: Ni alloys plate, sheet, strip, wire |
| Sulfuric and phosphoric acid | Alloy 31 (N08031), Alloy 20, 904L, 6Mo stainless | Plate, sheet, tube | Cu and Mo for sulfuric acid, lower cost than NiCrMo | Core: Ni alloys and specialty stainless |
| Caustic soda evaporators, chlor alkali cathodes | Ni 200/201, Alloy 600 | Sheet, strip, expanded mesh, tube | Pure nickel is immune to caustic SCC [INEOS_MEMBRANE_NI] | Core: Ni strip |
| HF alkylation, wet chlorine, seawater cooled units | Alloy 400 | Plate, tube, bar | NiCu resists HF | Core |
| Hot acetic acid, formic acid, urea strippers | Zr 702, Zr 705 | Plate, tube, bimetallic tube liner | Zr immune to hot organic acids and urea carbamate [ALLEIMA_STRIPPER, GD_ACETIC_2028] | Core: zirconium |
| Urea HP section | Super duplex (Safurex, SAF 2906), 25Cr22Ni2Mo | Tube, pipe, plate | Passivation in carbamate without oxygen | Partial: specialty stainless |
| Crackers, reformers, e cracker | Alloy 800H/HT, 617, HP cast | Tube, plate, bar | Creep and carburisation | Partial: heat resistant Ni alloys |
| Repair and fabrication | Ni base and stainless filler | Wire, strip electrode | Matching or overalloyed weld metal | Core: welding consumables |
Alloy and UNS designations are standard metallurgical knowledge (team assessment).

## Q5 Geographic concentration
- China 46% of world chemical sales, EU27 13% [CEFIC_FF2025_SHARES]. US share TODO(data).
- New capacity: acetic acid more than 90% China to 2028 [GD_ACETIC_2028], India largest single project to 2030 [GD_ACETIC_2030]. Chlor alkali and PVC in the Gulf [NUCERA_TAZIZ, NUCERA_MIDEAST_2025]. HPAL in Indonesia (Sulawesi, Halmahera) [VALE_POMALAA_2026].
- Europe: shrinking capacity [CEFIC_CLOSURES], so demand shifts to MRO, conversion and specialty and pharma.
- Model regions for C1 EU, CN, US, C2 ID, CN, US, EU, C3 CN, ME, US [MODEL_CHEM_CELLS].

## Q6 Customers and competitors
Customers (named, from sources and team knowledge)
- Operators: BASF (Ludwigshafen, Zhanjiang), SABIC, INEOS (Daishan acetic acid JV with Zhejiang Petrochemical) [GD_ACETIC_2028], Shenghong, Guangdong Shengyuanda, TA'ZIZ (ADNOC and ADQ) [NUCERA_TAZIZ], AGC Vinythai, Huayou, Vale Indonesia, Ford (KNI) [VALE_POMALAA_2026], Harita and Lygend (Obi), Dow, Evonik, Covestro, Wanhua, Celanese, Eastman (team knowledge, no project data gathered).
- EPC, licensors, OEM: Linde Engineering (e cracker EPC) [BASF_ECRACKER_2024], thyssenkrupp nucera and Uhde, Stamicarbon [STAMI_SAFUREX], Casale, Saipem [ALLEIMA_STRIPPER], China ENFI (Obi HPAL process package, low confidence), Technip Energies, Topsoe, Asahi Kasei, INEOS Electrochemical [INEOS_MEMBRANE_NI].
- Equipment fabricators (team knowledge): De Dietrich Process Systems, Pfaudler (also glass lined substitute), Alfa Laval and Kelvion (heat exchangers), Sulzer (columns, pumps), KSB and Flowserve (pumps, valves), NobelClad and other explosion cladders.
Competitors (mills and distributors)
- Acerinox HPA: VDM Metals and Haynes [ACX_HAYNES, ACX_FY2025_HPA]. Haynes CPI 12% of revenue [HAYNES_10Q_2024].
- Special Metals (PCC), ATI (Zr, Hf, Nb plate, sheet, strip) [ATI_AR_2025], Alleima (Safurex, 2RE69, Zr bimetallic) [ALLEIMA_STRIPPER], Outokumpu (254 SMO, 904L), Nippon Yakin, Chinese mills (Baowu Special Metallurgy, Fushun Special Steel), Chinese Zr producers (State Nuclear Baoti) are team knowledge, TODO(data) on CPI shares.
- Distributors (team knowledge): thyssenkrupp Materials Services, Rolled Alloys, Sandmeyer Steel, NeoNickel.

## Q7 Competitor map (team assessment)
| Competitor | Applications | Forms | Strengths |
|---|---|---|---|
| VDM Metals (Acerinox) | NiCrMo acid service, Alloy 59, 31 | Plate, sheet, strip, bar, wire | Broad CPI grade list, German melt base, now combined with Haynes |
| Haynes (Acerinox) | C-276, C-22, C-2000, HYBRID BC1 | Sheet, plate, coil | Hastelloy brand, US service centres, but CPI only about 12% of sales [HAYNES_10Q_2024] |
| Special Metals (PCC) | 625, 600, 400, C-276 | Plate, bar, tube | Inconel and Monel brands, Berkshire Hathaway backing |
| ATI | Zr 702, 705 | Plate, sheet, strip | Integrated Zr sponge to mill, but 68% A&D focus [ATI_AR_2025] |
| Alleima | Urea, Zr bimetallic, super duplex | Tube, pipe | Licensor lock in with Stamicarbon [ALLEIMA_STRIPPER, STAMI_SAFUREX] |
| Outokumpu | 6Mo, 904L, duplex | Plate, coil | Scale, price |
| Chinese mills | C-276, 625, Zr | Plate, tube | Cost, proximity to more than 90% of acetic acid additions [GD_ACETIC_2028] |

## Q8 Gain or lose relevance
Gain
- PFAS restriction pushes lined equipment towards solid or clad NiCrMo [CEFIC_PFAS_EQUIP_2026, ECHA_PFAS_2026]. Magnitude uncertain, derogations likely.
- Zr in acetic acid and urea strippers as capacity grows in Asia [GD_ACETIC_2028, ALLEIMA_STRIPPER].
- Nickel in chlor alkali cathodes as Gulf PVC capacity grows [NUCERA_TAZIZ, INEOS_MEMBRANE_NI].
Lose
- Titanium clad steel dominates HPAL autoclaves [HPAL_TI_CLAD] (low confidence source), Ni alloys and super duplex only in ancillary piping, flash vessels and pumps.
- Super duplex replaces Ni and Zr in urea HP sections [ALLEIMA_SAF2906].
- Glass lined steel (Pfaudler, De Dietrich), graphite and SiC heat exchangers and fluoropolymer linings where PFAS derogations hold [RICARDO_PFAS_REFINING].
- Lean duplex and 6Mo replace NiCrMo at the low end, plus price competition [HAYNES_10Q_2024].

## Q9 Attractive value chain steps (team assessment)
1. Specification with licensors and EPCs (Stamicarbon, nucera, Linde, ENFI): earliest point where alloy and form are fixed.
2. Clad plate supply chain: thin NiCrMo and Zr sheet for explosion cladders.
3. Welding consumables and MRO kits for European and US installed base, which grows even when new capacity closes [CEFIC_CLOSURES].
4. Nickel strip and mesh for chlor alkali and electrolyser electrodes.
Less attractive: commodity C-276 plate for Chinese new builds (price competition).

## Spotlight facts
1. Vale Indonesia, Huayou and Ford, Pomalaa HPAL (PT Kolaka Nickel Indonesia), Sulawesi, first two of five autoclaves January 2026, start Q3 2026, 120 kt/yr Ni in MHP [VALE_POMALAA_2026]. Metal: titanium clad steel autoclaves, Ni alloy and super duplex in flash, piping and pumps (team view). Likely suppliers: explosion cladders, Chinese Ti and Ni alloy mills (TODO(data)).
2. BASF, SABIC and Linde, e cracker demonstration, Ludwigshafen, April 2024, 6 MW, 4 t/h [BASF_ECRACKER_2024]. Metal: high temperature Ni Cr Fe tube alloys and heating elements (alloy not disclosed). Suppliers TODO(data).
3. thyssenkrupp nucera, largest new build chlor alkali order, Middle East, December 2025, plant ready end 2028 [NUCERA_MIDEAST_2025]. TA'ZIZ Ruwais 500 kt/yr PVC [NUCERA_TAZIZ]. Metal: nickel cathode sheet and mesh, titanium anodes [INEOS_MEMBRANE_NI].
4. Alleima, SAF 2906 launch, 30 June 2025, urea HP section [ALLEIMA_SAF2906], bimetallic Zr 702 lined stripper tubes [ALLEIMA_STRIPPER].
5. INEOS and Zhejiang Petrochemical, Daishan acetic acid 1.0 Mtpa, start 2026 [GD_ACETIC_2028]. Metal: Zr 702 reactors and columns (standard, team view). Suppliers ATI, Chinese Zr producers (team view).

## Open data gaps
- TODO(data): long run (2035) global chemical growth forecast from a primary source.
- TODO(data): bottom up CPI demand by alloy (PRODCOM, Comtrade, Nickel Institute first use) to validate EUR 9.0bn.
- TODO(data): Acerinox HPA and VDM CPI share of sales.
- TODO(data): e cracker tube alloy and supplier.
- TODO(data): HPAL materials from primary engineering source (Nickel Institute, AMPP).
- TODO(data): nucera Middle East customer and capacity, TA'ZIZ FID status.
- TODO(data): MRO share of CRA demand.
- Verify Cefic, ACC, GlobalData values once the hosts are reachable.
