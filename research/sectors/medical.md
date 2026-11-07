# Research notes: Medical technology (report section 3.7)

Status: Stage 1 research, 2026-11-07. Author: sector analyst (medical).
Every figure carries its data_id from data/sources.csv. "Team estimate" marks own calculations.
Access limits in this session: medtecheurope.org, sec.gov, orthoworld.com, pmc.ncbi.nlm.nih.gov, fwmetals.com,
zapp.com and businesswire.com did not resolve from the cloud session, so several primary figures were taken from
search result summaries and are flagged confidence medium. The web search budget ran out before the Oxinium,
Integer, dental AM and nitinol market checks, which are listed as open gaps at the end.

## Data chain position
Material (CoCr, MP35N, 316LVM, Ni for NiTi, Zr2.5Nb, CoCr and 316L AM powder) > Product form (bar, fine wire,
thin strip, tube hollows, powder) > Application (hip and knee, trauma, spine, TAVR frames, stents, leads,
PFA catheters, dental frameworks, instruments) > Industry (Medical technology) > Geography (US, EU, then
China and Japan) > Market size > Growth.

## Q1 Market size and growth to 2035

Sector (end device level)
| Metric | Value | data_id | Note |
|---|---|---|---|
| European medtech market 2024 (excl. IVD) | EUR 170bn | MTE_EU_MEDTECH_2024 | MedTech Europe on Fitch data |
| Europe share of world market | 26.4% | MTE_EU_SHARE_2024 | US is largest |
| Implied world market 2024 | about EUR 644bn | TEAM_WORLD_MEDTECH_2024 | team estimate 170 / 0.264 |
| Orthopedic device sales 2025 | USD 64.9bn, +4.9% | OW_ORTHO_2025 | second page says 64.6bn, +4.3% |
| Orthopedic forecast 2029 | above USD 78bn | OW_ORTHO_2029 | implied about 4.7% p.a. |
| Joint replacement / trauma | USD 23.9bn / 9.6bn | OW_JOINT_TRAUMA | low confidence, year to verify |
| Ortho CAGR to 2035 (paid) | 4.34% p.a. | MKT_ORTHO_TH_2035 | triangulation only |
| Paid PFA market 2025 | USD 2.3bn, 18.4% p.a. 2026 to 2035 | MKT_PFA_2025 | triangulation only |

High performance metal demand within it (Client addressable)
| Metric | Value | data_id |
|---|---|---|
| Medical technology demand for Client materials 2025 | EUR 2.0bn | MODEL_MED_2025 |
| Growth | 6.0% p.a., 2035 about EUR 3.6bn | MODEL_MED_2025 |
| Cell M1 (CoCr, MP35N type, 316LVM bar and fine wire) | EUR 1,100m, 6.5% p.a., 2035 about EUR 2,065m | MODEL_M1_2025 |

Cross checks on the EUR 2.0bn: Carpenter Technology medical end use USD 351.2m in FY2025, 12% of sales
(CRS_MED_FY2025), ATI medical USD 139.4m in 2025, down from 224.9m (ATI_MED_2025). Add private wire and
strip makers (Fort Wayne Metals, Zapp, Alleima medical, Ulbrich, Elgiloy, Heraeus) whose revenues are not
published. The EUR 2.0bn is therefore plausible but not proven bottom up. TODO(data): revenues of Fort Wayne
Metals, Zapp and Alleima medical segment, and a tonnage for medical CoCr (Cobalt Institute report 2025 gives
total cobalt demand 276 kt, CI_CO_DEMAND_2025, but no medical split in the excerpts).
Paid report spread: one report puts "medical implants CoCr alloys" at USD 5.8bn in 2025 (MKT_COCR_MED_2025),
which clearly includes component or implant value. Not used.

Why the metal layer grows faster than the device layer (6.0 to 6.5% vs about 4.5 to 5% ortho): procedure growth
plus structural heart and electrophysiology growing in double digits (EW_TAVR_Q4_2025, BSX_FARAPULSE_2024,
MDT_FY26), offset by substitution of CoCr heads by ceramics and of wrought parts by printed titanium.

## Q2 Drivers and risks

Drivers
1. Ageing. WHO: 1.1bn people aged 60+ in 2023, about 2.1bn by 2050 (WHO_60PLUS_2050).
2. Joint volumes. US Medicare primary THA +176% and TKA +139% from 2019 to 2040, baseline 262,369 THA and
   480,958 TKA (SHICHMAN_THA_TKA_2040). Revision THA +42%, revision TKA +149% by 2040 (SHICHMAN_REV_2040).
   Medicare only, so not a national total.
3. Structural heart and EP. Edwards TAVR Q4 2025 USD 1.16bn, +12% (EW_TAVR_Q4_2025). Farapulse above USD 1bn
   in its first year 2024 (BSX_FARAPULSE_2024). Medtronic FY26 revenue USD 36.4bn, cardiac ablation +78%,
   PFA +145% (MDT_FY26).
4. OEM growth: Stryker USD 25.1bn, +11.2% (SYK_2025). Zimmer Biomet USD 8.23bn, +7.2%, knees USD 3.32bn,
   hips USD 2.09bn (ZBH_2025).

Risks
1. Cobalt regulation. EU MDR Annex I 10.4.1: CMR 1A/1B substances above 0.1% w/w need a specific justification
   (EU_MDR_CMR). Cobalt is Carc. 1B and Repr. 1B, ANSM applies this from 1 Oct 2021, not an SVHC so not banned
   (OBELIS_COBALT_CMR). Every CoCr and MP35N device in the EU carries this justification burden, which favours
   titanium, ceramics and oxidised zirconium on new designs.
2. Price pressure. China national VBP 2021 cut hip and knee prices by about 82% on average (CN_VBP_JOINTS_2021).
3. Trade. US Section 232 investigation on medical devices opened 2 Sept 2025, still open per one secondary source
   (US_S232_MED_2025). A German supplier selling semis into US implant plants may face duties or local content
   pressure.
4. Destocking volatility. Carpenter medical sales fell 6% in FY2025 on OEM inventory management
   (CRS_MED_FY2025). ATI medical fell from USD 224.9m to 139.4m as capacity moved to aerospace (ATI_MED_2025).
   This is also an opening: a supplier that keeps medical capacity is valued.
5. Qualification length. Changing a material or supplier in a Class III device requires a regulatory change,
   so share moves slowly in both directions (team assessment, no figure).

## Q3 Emerging technologies and applications
1. Pulsed field ablation catheters (Farapulse, Affera Sphere-9, Abbott). Metals: nitinol wire and tube for
   self expanding baskets, platinum iridium electrodes (team assessment from device design, not confirmed per
   product). Fast growth (MDT_FY26, MKT_PFA_2025).
2. Transcatheter valves. Balloon expandable SAPIEN 3 on MP35N CoCr frame (FDA_SAPIEN3_MP35N), self expanding
   Medtronic Evolut on nitinol. A secondary summary says Edwards mitral and tricuspid systems grew 56% to
   USD 551m in 2025, not logged and not used in prose until verified (TODO(data)).
3. Additive manufacturing. Stryker Cork AM site 156,000 sq ft, opened Aug 2022, more than 300,000 Tritanium
   devices implanted (SYK_CORK_AM). Printed porous titanium replaces wrought and cast parts in spine and
   acetabular cups. CoCr powder is used for dental frameworks and some knee components (team assessment,
   TODO(data): dental CoCr AM volume).
4. Robotic surgery and powered instruments raise demand for precipitation hardening stainless and fine
   stainless wire and cable (team assessment, no figure).
5. Neuromodulation and leadless pacing need MP35N and drawn filled tube (DFT) fine wire, Pt alloy cores
   (team assessment, Fort Wayne Metals is the known DFT supplier, no figure).

## Q4 Materials required (alloy, grade, form, why)
| Application | Alloy and standard | Form | Why |
|---|---|---|---|
| Femoral heads, knee femoral components, tibial trays | CoCrMo (ASTM F75 cast, ASTM F1537 / ISO 5832-12 wrought) | Bar, forging stock, investment casting | Wear resistance against polyethylene, fatigue strength |
| Hip stems, trauma plates and nails | Ti6Al4V ELI (F136), 316LVM (F138, ISO 5832-1), CoCrMo | Bar, plate, wire | Modulus (Ti), cost and formability (316LVM) |
| Oxidised zirconium heads and femoral knees | Zr2.5Nb (ASTM F2384) | Bar | Ceramic surface on metal core, used by Smith+Nephew OXINIUM |
| Coronary stents, TAVR frames | L605 (F90), MP35N (F562), PtCr | Seamless tube hollow, fine bar | Radiopacity, strength at thin struts |
| Self expanding frames, PFA baskets, guidewires | NiTi (F2063) | Wire, tube, strip, sheet | Superelasticity |
| Pacing and neuro leads | MP35N, DFT MP35N/Ag or Pt cores | Fine and ultrafine wire | Fatigue life, conductivity |
| Surgical instruments | 1.4021, 1.4542 (17-4PH), 1.4441 | Bar, strip | Hardness, sterilisation resistance |
| Dental frameworks | CoCr (ISO 22674) | Discs, powder | Strength and cost against gold |
| Printed implants | Ti6Al4V powder, CoCr powder | Powder | Porous ingrowth structures |

Client fit: CoCr alloys, MP35N type CoNi alloys, specialty stainless (316LVM, instrument grades), Zr (Zr2.5Nb
feasible if Client melts Nb bearing Zr, TODO(data): confirm Client Zr grades), AM powders (CoCr, 316L) and
fine wire and strip forms. Gaps: no titanium, no nitinol melting, no precious metals. Nickel is a NiTi
ingredient but the Client is not a NiTi producer.

## Q5 Geographic concentration of demand
1. United States is the largest market, Europe second at 26.4% of world (MTE_EU_SHARE_2024).
2. At Zimmer Biomet 55% of knee and hip sales are in the US (TEAM_ZBH_US_SHARE).
3. Manufacturing hubs (team assessment from company sites): Warsaw Indiana (Zimmer Biomet, DePuy, Medtronic
   spine), Memphis, Minneapolis (Medtronic, Boston Scientific, Abbott), Irvine (Edwards), Cork, Galway and
   Limerick in Ireland (Stryker, Boston Scientific, Medtronic), Tuttlingen in Germany (instruments, Aesculap),
   Switzerland (Straumann, Mathys, Johnson and Johnson MedTech sites), and growing Costa Rica and Malaysia
   (Alleima Penang medical wire, ALLEIMA_PENANG_2025).
4. China is large but price capped by VBP (CN_VBP_JOINTS_2021) and served increasingly by domestic suppliers.
TODO(data): UN Comtrade HS 902131 (artificial joints) and HS 902190 trade flows by country, not yet pulled.

## Q6 Customers and competitors
Customers (OEMs): Stryker, Zimmer Biomet, Johnson and Johnson MedTech (DePuy Synthes), Smith+Nephew, Medtronic,
Abbott, Boston Scientific, Edwards Lifesciences, B. Braun (Aesculap), Straumann, Dentsply Sirona, Enovis,
Globus Medical. Tier 1 contract manufacturers: Integer, Viant, Tecomet, Orchid Orthopedic Solutions,
Resonetics, Cirtec (team assessment, no revenue figures retrieved, TODO(data)).

Competitors (mills, wire and strip makers):
| Competitor | Focus | Evidence |
|---|---|---|
| Carpenter Technology (US) | CoCr (BioDur), Ti, stainless bar | Medical USD 351.2m FY2025 (CRS_MED_FY2025) |
| ATI (US) | Ti, Zr, Nb, NiTi | Medical USD 139.4m 2025, falling (ATI_MED_2025) |
| Fort Wayne Metals (US, Ireland) | Fine wire, NiTi melt, MP35N, DFT | Second VAR, up to 1m lb/yr NiTi (FWM_NITINOL_VAR) |
| Resonetics (US) | NiTi tube, components | Bought SAES medical nitinol USD 900m (RESONETICS_SAES_2023) |
| Montagu owned ex JM MDC | Pt alloys, NiTi components | USD 700m deal 2024 (JM_MDC_2024) |
| Alleima (SE) | Medical fine wire, stainless | Penang plant, deliveries 2026 (ALLEIMA_PENANG_2025) |
| Zapp (DE) | CoCr, MP35N type, stainless wire, strip, bar | Product pages, no figures |
| Heraeus (DE, US) | Precious metal medical components | Product pages, no figures |
| Ulbrich, Elgiloy Specialty Metals (US) | Thin strip, CoCrNi strip and wire | Team knowledge, no figures |
| VDM Metals (Acerinox) | Ni alloys, limited medical | ACX_HAYNES context |
| CeramTec (DE) | Ceramic heads (substitute) | NJR_HEADS_2016 |

## Q7 Competitor map
See table in Q6 plus mapping in the section. Pattern: US mills hold the bar and billet layer for CoCr and Ti,
US and Irish wire specialists hold fine wire and NiTi, private equity platforms (Resonetics, Montagu) consolidate
components. European independents (Zapp, Alleima, Heraeus) hold precision wire and strip. ATI pulling back from
medical is the clearest share opportunity (ATI_MED_2025).

## Q8 Where high performance metals gain or lose relevance
Lose: CoCr femoral heads lose to ceramics (NJR 2016: ceramic 40%, metal 60%, CeramTec reports ceramic overtook
metal later, NJR_HEADS_2016, manufacturer claim). Printed porous Ti replaces some CoCr and Ti wrought parts
(SYK_CORK_AM). EU CMR rules push new designs away from cobalt (EU_MDR_CMR, OBELIS_COBALT_CMR). Polymers (PEEK)
compete in spine cages (team assessment).
Gain: MP35N and L605 in balloon expandable valves and stents (FDA_SAPIEN3_MP35N, EW_TAVR_Q4_2025), NiTi in PFA
and self expanding frames (FWM_NITINOL_VAR, MDT_FY26), revisions with CoCr knee components (SHICHMAN_REV_2040),
CoCr powder in dental AM.

## Q9 Attractive value chain steps
1. Certified remelted (VIM, VAR, ESR) CoCr and MP35N type bar and fine wire with ISO 13485 traceability, the
   M1 cell (MODEL_M1_2025). Highest value per kg in the Client portfolio and sticky qualification.
2. Thin strip and fine wire in MP35N, L605 and 316LVM for leads, stents and instrument springs.
3. Tube hollows for stent and valve frame tubing, sold to tube drawers (Resonetics, Fort Wayne Metals,
   Minitubes), partnership rather than own tube drawing.
4. CoCr and 316L AM powder for dental and orthopaedic printers.
Less attractive: commodity 316L instrument bar (price competition), NiTi (needs melt capability and Ti supply,
incumbents consolidating), China joint market (VBP prices).

## Spotlight facts
1. Edwards Lifesciences SAPIEN 3 (Irvine, California, FDA approval 2015): balloon expandable frame of MP35N
   cobalt chromium (FDA_SAPIEN3_MP35N), laser cut from seamless tube made from fine bar. TAVR sales USD 1.16bn
   in Q4 2025 alone (EW_TAVR_Q4_2025). Likely upstream suppliers of MP35N bar and tube: Fort Wayne Metals,
   Carpenter, Zapp (team assessment, not confirmed by Edwards).
2. Fort Wayne Metals (Fort Wayne, Indiana, early 2025): second VAR furnace raises nitinol melt to up to 1m lb
   (about 450 t) per year, sold as bar, strip, sheet and wire (FWM_NITINOL_VAR). Demand from PFA catheters
   (Boston Scientific, Medtronic) and self expanding valves.
3. Stryker AMagine site (Anngrove, Cork, Ireland, Aug 2022): 156,000 sq ft printing site for porous titanium
   Tritanium implants, more than 300,000 devices implanted (SYK_CORK_AM). Powder is Ti6Al4V, so this is a
   substitution threat for wrought CoCr and Ti bar.
4. Consolidation: Resonetics paid USD 900m for SAES medical nitinol (Oct 2023, RESONETICS_SAES_2023), Montagu
   paid USD 700m for Johnson Matthey Medical Device Components (2024, JM_MDC_2024).
5. ATI medical sales fell from USD 224.9m (2024) to 139.4m (2025) as capacity moved to aerospace (ATI_MED_2025).

## Open data gaps
TODO(data): medical cobalt and CoCr tonnage (Cobalt Institute end use split, searched Cobalt Market Report 2025 excerpts).
TODO(data): NJR 2025 head material split (searched NJR annual report 2025, only HQIP announcement found).
TODO(data): Smith+Nephew OXINIUM volumes and Zr2.5Nb supplier (search budget exhausted).
TODO(data): Integer, Viant, Tecomet revenues (search budget exhausted).
TODO(data): nitinol market size (search budget exhausted, paid reports only).
TODO(data): dental CoCr AM volumes (search budget exhausted).
TODO(data): UN Comtrade HS 902131 and 902190 by country.
TODO(data): Edwards full year 2025 TAVR and total sales (conflicting secondary figures, verify in 10-K).
TODO(data): verify Shichman author list and DOI, MedTech Europe PDF, Carpenter 10-K figures in source documents.
