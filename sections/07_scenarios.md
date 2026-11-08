# 7. Growth Scenarios to 2035

This chapter estimates alloy demand through 2035. The team used a calibrated tier 1 model for established applications and a separate tier 2 register for emerging applications [MODEL_AERO_MRO_G].

## 7.1 Growth Model and Scenario Assumptions

Tier 1 models demand as D = A × I × S. A represents industry activity, I represents alloy mass per unit, and S represents the share of units using a high-performance alloy. Each factor is a ratio of its 2035 value to its 2025 value. The index sets 2025 at 100. The model uses measured end uses, including the 11,499 t of cobalt used in aviation out of 20.0 kt used in superalloys in 2025. The IEA outlook for nickel outside energy technologies sets the broader limit for the estimates [AERO_CI_AVIATION_CO_2025, IEA_CM_CO_DEMAND_2025_2035].

Table 12: Tier 1 drivers and assumptions, low to high range

| Industry | Activity driver | Growth range to 2035 | Intensity, share | Key source |
|---|---|---|---|---|
| Aerospace | New engines and aftermarket | 2.0 to 5.0% and 3.0 to 4.2% a year | Share 0.90 to 1.03 | [AERO_AIRBUS_GMF2026_DELIVERIES] |
| Energy | Gas turbines, nuclear, other | Turbine output ratio 1.15 to 1.85 | ±1% a year | [CO_SIEMENSENERGY_CMD_2025] |
| Electronics | 300 mm fab capacity, components | Index 138 in 2031, then 0 to 6% | −1.5 to +1% a year | [SEMI_300MM_PATH] |
| Medical | Hip and knee procedures | 3.0 to 4.1% a year | CoCr share 0.90 to 1.02 | [MED_OECD_HIP_RATE_2023] |
| Chemical | Chemical activity | −1.0 to 2.5% a year | ±0.5% a year | [CEFIC_CAPUTIL_EU27_Q3_2026] |
| Oil and gas | Upstream investment, LNG | Ratio 0.80 to 1.12 and 1.15 to 1.51 | −1.5 to +1% a year | [OG_WEI2026_SSA_UPSTREAM_2026] |
| Automotive | Car sales, electric share | Electric share 40 to 62% in 2035 | Turbo alloy 0 to 2% a year | [IEA_GEVO_CN_CARS_2035] |

*Source: team assumptions, all parameters in Table A1.*

The team used a backtest to see how well past trends predicted recent outcomes. A trend fitted through 2019 underestimated gas power investment from 2020 to 2025. It had a mean absolute percentage error of 36.5 percent and a bias of minus 36.0 percent. The trend for EU vehicle output overestimated output by 23.0 percent [MODEL_AERO_MRO_G].

The model corrects half of each growth error, up to 1 percentage point per year. The remaining error widens the range in the Monte Carlo simulation. The team used 10,000 draws and seed 20261108 to estimate P10, P50, and P90, the 10th, 50th, and 90th percentiles.

## 7.2 Results by Industry, Product, and Region

Figure 3 and Table 13 show growth in turbines, engines, electronics, and implants. The automotive index stays near 98. Its two components move in different directions: combustion parts fall to 66 and electric vehicle parts rise to 192 [MODEL_AERO_MRO_G].

Figure 3: Energy technology and aerospace lead alloy demand to 2035, while automotive stays flat

*Source: team calculation, band P10 to P90, line P50 [MODEL_AERO_MRO_G].*

Table 13: Tier 1 alloy demand index 2035 by industry (2025 = 100)

| Industry | P10 | P50 | P90 | P50 growth a year |
|---|---|---|---|---|
| Energy | 126 | 156 | 193 | 4.5% |
| Aerospace | 137 | 147 | 158 | 3.9% |
| Electronics | 112 | 141 | 176 | 3.5% |
| Medical | 132 | 140 | 149 | 3.4% |
| Oil and gas | 93 | 115 | 143 | 1.4% |
| Chemical | 87 | 109 | 135 | 0.9% |
| Automotive | 81 | 98 | 119 | −0.2% |

*Source: team calculation [MODEL_AERO_MRO_G].*

The model projects stronger demand growth for precision FeNi and vacuum-melted bar than for flat products and tubes. The aerospace weight of 0.575 comes from measured data. The team estimated the other weights [MODEL_AERO_MRO_G].

Table 14: Product family index 2035 (2025 = 100) and main industry weights

| Product family | Main industry weights | P10 | P50 | P90 |
|---|---|---|---|---|
| Precision FeNi strip and foil | Electronics 0.60, electric vehicles 0.30 | 134 | 157 | 185 |
| Superalloy bar, billet, remelt stock | Aerospace 0.575, energy 0.30 | 131 | 143 | 158 |
| Nickel alloy bar, rod and wire | Chemical 0.25, oil and gas 0.25 | 115 | 128 | 142 |
| Plate, sheet, strip and foil | Chemical 0.30, energy 0.20 | 113 | 125 | 139 |
| Tubes and fittings | Oil and gas 0.35, chemical 0.25 | 111 | 125 | 141 |

*Source: team calculation, weighted industry indices [MODEL_AERO_MRO_G].*

The supply analysis estimates that IEA cobalt mine supply falls 30 percent short of 2035 demand. The gap reaches 36 percent if the Congo quota stays at its 2026 level. Superalloys require only 13 to 20 percent of the cobalt, so the shortfall is more likely to raise costs than to cap superalloy production. The estimated 21 percent refined nickel gap is an upper bound. Copper mines cover 62 percent of projected demand before scrap is counted [MODEL_AERO_MRO_G, AERO_USGS_CO_SUPER_SHARE].

Engine and turbine growth is concentrated in the United States and Western Europe. The United States accounts for a fifth of superalloy cobalt. China has 40 of the 81 reactors under construction, so much reactor tube demand is tied to China. Asia accounts for more than 80 percent of expected chemical industry growth [BASF_APAC_GROWTH_2035, AERO_USGS_CO_SUPER_SHARE, EE_NUC_WNA_UC].

Table 15 lists emerging opportunities, some drawn from the team's research workbook. The team adds an opportunity to tier 1 only after its stated condition is met [MODEL_AERO_MRO_G, TEAM_WORKBOOK_2035].

Table 15: Tier 2 register, not included in tier 1

| Opportunity, alloy and form | TRL | Evidence | Earliest volume | Signpost |
|---|---|---|---|---|
| Solid oxide cells, ferritic strip | 9 | Early signal | 2026 | Strip contract at Bloom Energy |
| Electrolysers, nickel strip and mesh | 8 to 9 | Early signal | 2026 | Nucera orders above EUR 356 m |
| Additive engine parts, superalloy powder | 7 to 9 | Early signal | 2027 | Part specification with volume |
| 800 VDC racks, less copper busbar | 6 to 7 | Early signal | 2027 | Eaton and Vertiv busbar launches |
| Small reactors, zirconium, Alloy 690 tube | 7 to 8 | Early signal | 2030 | Serial tube order after licence |
| Hydrogen turbines, castings and sheet | 5 to 7 | Speculative | 2030 | Order with hydrogen supply |
| Fusion magnets, Alloy C-276 tape foil | 4 to 6 | Speculative | 2030 | Magnet order for a pilot plant |
| sCO2 recuperators, nickel alloy plate | 5 to 6 | Speculative | 2032 | Pilot above 10 MW |

*Sources: team register, TRL and years are team estimates [CO_BLOOM_CAP_2026, NVDA_800VDC_ROWCUT, MODEL_AERO_MRO_G, TEAM_WORKBOOK_2035].*

Chapter 8 scores the measured opportunities in four growing industries and the emerging applications with dated milestones.
