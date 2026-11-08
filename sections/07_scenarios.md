# 7. Growth Scenarios to 2035

The final link asks how large alloy demand could become by 2035, answered by a calibrated tier 1 model and a separate tier 2 register, both team estimates [MODEL_T1_RESULTS_2035].

## 7.1 Growth Model and Scenario Assumptions

Tier 1 writes demand as D = A × I × S, the activity driver times alloy mass per unit times the share of units using a high performance alloy, each as a ratio of 2035 to 2025 and indexed to 2025 = 100. It is calibrated to measured end use, as 11,499 t of the 20.0 kt of superalloy cobalt went to aviation in 2025, and the IEA nickel path outside energy technologies sets the envelope [AERO_CI_AVIATION_CO_2025, IEA_CM_NI_OTHER_2025_2035].

Table 12: Tier 1 drivers and assumptions, low to high range

| Industry | Activity driver | Growth range to 2035 | Intensity, share | Key source |
|---|---|---|---|---|
| Aerospace | New engines and aftermarket | 2.0 to 5.0% and 3.0 to 4.2% a year | Share 0.90 to 1.03 | [AERO_AIRBUS_GSF2026_SERVICES_2045] |
| Energy | Gas turbines, nuclear, other | Turbine output ratio 1.15 to 1.85 | ±1% a year | [CO_SIEMENSENERGY_CMD_2025] |
| Electronics | 300 mm fab capacity, components | Index 138 in 2031, then 0 to 6% | −1.5 to +1% a year | [SEMI_300MM_PATH] |
| Medical | Hip and knee procedures | 3.0 to 4.1% a year | CoCr share 0.90 to 1.02 | [MED_OECD_HK_COUNT_2023] |
| Chemical | Chemical activity | −1.0 to 2.5% a year | ±0.5% a year | [CEFIC_CAPUTIL_EU27_Q3_2026] |
| Oil and gas | Upstream investment, LNG | Ratio 0.80 to 1.12 and 1.15 to 1.51 | −1.5 to +1% a year | [OG_WEI2026_UPSTREAM_OG_2026] |
| Automotive | Car sales, electric share | Electric share 40 to 62% in 2035 | Turbo alloy 0 to 2% a year | [IEA_GEVO_EV_SHARE_2035] |

*Source: team assumptions, all parameters in Table A1.*

A backtest shows that past trends erred in both directions, because fitted to 2019 the trend underestimated gas power investment for 2020 to 2025 with a mean absolute percentage error of 36.5 percent and a bias of minus 36.0 percent, but overstated EU vehicle output by 23.0 percent [MODEL_BT_WEI_GASPWR, MODEL_BT_EUROSTAT_C29_EU27_2020]. Half of each growth error is corrected, capped at 1 percentage point a year, and the rest widens the ranges of a Monte Carlo simulation with 10,000 draws and seed 20261108, yielding the percentiles P10, P50 and P90.

## 7.2 Results by Industry, Product, and Region

The results place growth in turbines, engines, electronics and implants, as Figure 3 and Table 13 show, while automotive stays near 98 because combustion parts fall to 66 and electric vehicle parts rise to 192 [MODEL_T1_RESULTS_2035].

Figure 3: Energy technology and aerospace lead alloy demand to 2035, while automotive stays flat

![Figure 3](fig/fig3_scenarios.svg)

*Source: team calculation, band P10 to P90, line P50 [MODEL_T1_RESULTS_2035].*

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

*Source: team calculation [MODEL_T1_RESULTS_2035].*

Weighted into product families, the model favours precision FeNi and vacuum melted bar over flat products and tubes, although only the aerospace weight of 0.575 is measured and the others are team assumptions [MODEL_FAM_RESULTS_2035].

Table 14: Product family index 2035 (2025 = 100) and main industry weights

| Product family | Main industry weights | P10 | P50 | P90 |
|---|---|---|---|---|
| Precision FeNi strip and foil | Electronics 0.60, electric vehicles 0.30 | 134 | 157 | 185 |
| Superalloy bar, billet, remelt stock | Aerospace 0.575, energy 0.30 | 131 | 143 | 158 |
| Nickel alloy bar, rod and wire | Chemical 0.25, oil and gas 0.25 | 115 | 128 | 142 |
| Plate, sheet, strip and foil | Chemical 0.30, energy 0.20 | 113 | 125 | 139 |
| Tubes and fittings | Oil and gas 0.35, chemical 0.25 | 111 | 125 | 141 |

*Source: team calculation, weighted industry indices [MODEL_FAM_RESULTS_2035].*

In the supply overlay, IEA cobalt mine supply falls 30 percent short of 2035 demand, 36 percent if the Congo quota stays at its 2026 level, yet superalloys need only 13 to 20 percent of it, so cobalt is a cost risk rather than a volume ceiling, while the refined nickel gap of 21 percent is an upper bound and copper mines cover 62 percent of demand before scrap [MODEL_SUPPLY_OVERLAY_2035, CO_USGS_QUOTA_2026].

Regionally, engine and turbine growth sits in the United States, a fifth of superalloy cobalt, and Western Europe, while reactor tube demand follows the 40 of 81 reactors under construction in China and Asia takes more than 80 percent of chemical growth [AERO_USGS_CO_SUPER_SHARE, EE_NUC_WNA_UC, BASF_APAC_GROWTH_2035].

Beyond these measured markets, Table 15 registers emerging options, partly from the team research workbook, which enter tier 1 only once their signpost occurs [MODEL_TIER2_REGISTER_2026, TEAM_WORKBOOK_2035].

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

*Sources: team register, TRL and years are team estimates [MODEL_TIER2_REGISTER_2026, TEAM_WORKBOOK_2035, CO_BLOOM_CAP_2026, NVDA_800VDC_ROWCUT].*

Measured growth in four industries and these dated options define the opportunity space that chapter 8 scores.
