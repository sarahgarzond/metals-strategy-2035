# Fact check round 6

Scope: sections 02, 06, 07, 08, 09, Table 2 (T2_* rows), report/report.html references. Title page exempt. fetch.py not run. About 60 numeric claims checked (well above 15 percent), against data/clean/model_*.csv, comtrade_portfolio_world, comtrade_hs6_alloy_*, research/model/outlook_results.md and data/sources.csv.

Counts: ok 52 | inconsistent 2 | unsourced or weakly sourced 4 | outdated 0 | wrong 0. All cited IDs in sections/*.md map to a row in data/sources.csv (0 missing). All cited rows have author, intext_author, pub_date, ref_type, title and url or doi.

## Ranked findings

| Rank | Location | Claim | Status | Evidence | Fix |
|---|---|---|---|---|---|
| 1 | report.html References | International Energy Agency (2025c) and (2025d) are the same item: "World energy outlook 2025", same URL | inconsistent | Two reference entries, identical title and URL, differing only in date detail (2025d adds "November") | Merge to one sources.csv row, or give the second a distinct title (for example the Extended dataset it supports) |
| 2 | report.html References | Eurostat (2024) and Eurostat (2026c) both "Sold production, exports and imports", same URL, different years | inconsistent | Different pub_date for the same PRODCOM database page. Letters a, b, c are used across years, which is APA wrong when years differ only by retrieval | Either merge, or title the second row with the dataset code as is already done for DS-059358. Check that the APA year equals the data vintage |
| 3 | Table 2, T2_NI_FIRSTUSE_2024 (66, 16, 6 percent) | Nickel use shares | unsourced | Notes: Nickel Institute page returned 403, "values as printed in the draft", never read from the source | Re-read the page by hand or from the Nickel Institute fact sheet, or flag as team draft value. Same status as other rows below |
| 4 | Table 2, T2_MO_ENDUSE_2025 (17, 14), T2_CU_ENDUSE_2024 (26, 23, 17) | IMOA and ICSG shares | unsourced | Notes say "Not re-read in this run" | Open the IMOA annual review and ICSG factbook and confirm the shares and the stated year |
| 5 | Table 2, T2_AL_ENDUSE_2020 (25, 23, 12) | Aluminium shares, 2020 demand | outdated / weak | CRU for IAI dated Jan 2022, shares "approximate, not located line by line", 2020 is a post Covid base year | Locate the figures in the PDF or replace with the IAI or Aluminium Insider 2024 split. State the year in the table |
| 6 | Table 2, T2_TI_US_AERO_2025 (>50 percent aerospace) | Titanium share | inconsistent | Row note says "U.S. only", yet the table sits in a world market chapter | Label the cell "US" or find a world share (for example Roskill or USGS world sponge end use) |
| 7 | 6.1 text vs Table 10 Sources line | Text says "ten major reporters" for 64.5, 30.6, 41.3 and 18.0 kt. Table 10 sources and appendix A2.4 say "eight reporters" for 80.3 kt, 38.2 kt, 15.3 kt | inconsistent | hs6 summary: 10 reporters give 64.54 kt (750512), 30.57 (750522), 41.34 (750620), 18.0 (750712). The 8 reporter set gives 80.3 kt (bar plus wire), 38.21, 15.27. Bar plus wire for ten reporters is 95.1 kt. Both are correct for their own set, but a reader sees two bar and wire totals | State once "ten reporters" vs "the eight reporters of the four digit files" in 6.1 and in the Table 10 note, and add 95.1 kt (ten) next to 80.3 kt (eight) or use one set |
| 8 | Ch 7.2 Supply paragraph (12 percent) | "superalloys need only 12 percent" of cobalt mine supply | ok with note | model_supply_overlay: 26.4 kt is 12 percent of base supply, 13 percent in the Congo quota case. MODEL_SUPPLY_OVERLAY_2035 source row says 26.3 kt (P50) and 12 and 18 percent | Align sources.csv notes (26.3 vs 26.4 kt and 18 percent applies to the CMOC case, 13 percent to the quota held case) |
| 9 | 6.4 tariff text | Section 232 at 50 percent, copper 50 percent from 1 Aug 2025, general duty 2 to 3 percent, 15 percent joint statement, 10 percent surcharge for 150 days, Section 301 EU rate 10 percent from 24 July 2026 | ok | Matches rows US_232_COPPER_2025, USITC_HTS_75_2026 (2.5 to 3 for 7505 and 7506, 2 to 3 for 7507), US_EU_JOINT_STATEMENT_2025, US_EO14389_2026, US_PROC11012_2026, USTR_301_2026_EU. Surcharge started 24 Feb 2026, so its 150 days ended about 23 July, consistent with the 301 start. Rows state chapter 99 and exemption lists are unchecked, and the text says so. Section 232 goods are exempt from 301 per the USTR row, but the text does not say it | Add one clause that Section 232 goods are exempt from the 301 duty, and reflect that the "up to 10 percent" statement is a ceiling |
| 10 | 6.4 CBAM, CRMA | CBAM definitive 1 Jan 2026, covers FeCr and FeNi, not chapter 75. CRMA lists nickel, cobalt, tungsten | ok | EU_CBAM_2026 and W_EU_CRMA_2024 rows. CBAM source is an EY alert, not EUR-Lex | Prefer the Commission page or Regulation (EU) 2023/956 as primary |

## Checked and ok (no action)

| Location | Claim | Status | Evidence |
|---|---|---|---|
| Table 10 and 14 | Bar family 131 kt (102 to 169) in 2025 and 153 kt (116 to 200) in 2035, flat 282 and 326, tubes 45 and 50, superalloy 193 and 248 | ok | model_family_tonnes.csv P10/P50/P90 round to these |
| Table 10 and 14 | EUR bn: superalloy 4.9 to 9.1 and 6.3 to 11.7, bar 3.3 to 4.4 and 3.9 to 5.1, flat 8.7 to 13.5 and 10.1 to 15.6, tubes 1.2 to 1.8 and 1.3 to 2.1 | ok | model_family_value.csv central low to high |
| Table 14 | Index P50 129, 116, 116, 112, 129 | ok | tier1 product_family rows |
| Table 13 | All index values (P10, P50, P90, no haircut) and cobalt bases 11.5 to 15.4 and 8.5 to 11.0 kt | ok | model_tier1_results.csv nickel and cobalt rows. Automotive 102 vs 108 without haircut, oil and gas 98 vs 105 correct |
| 7.2 | Combustion index 69, EV parts 200 | ok | tier1 sub index rows |
| Table 15 | Congo mine gap 54 percent, Indonesian cut 21 to 55 percent, aerospace index 114, tier changes (3.70, 3.45, Monitor, Harvest), tungsten no change | ok | model_shock_tiers.csv, model_supply_overlay.csv. Appendix says 114 (96 to 133) |
| 7.2 supply | Cobalt mine gap 30 percent, 36 percent quota held | ok | 30.1 and 36.0 percent |
| 7.1 | Haircut mean 0.982 of 0.894, 0.983, 1.068, IEA 0.951, aerospace median 0.96, other 0.94, deliveries 2,103 and 2,181, ratio 1.25 to 1.76 | ok | outlook_results.md lines 7, 38 to 41, 206 to 207, 279 |
| Table 17 | All seven scores recomputed with weights 15/20/15/10/10/10/10/10: 3.85, 3.85, 3.70, 3.60, 3.45, 3.15, 3.00 | ok | arithmetic and model_scores.csv. Priorities and criteria values match. Order of rows is by score, with Alloy 690 (3.15) after CoCr (3.45) |
| 8.1 | Growth 3.6 percent (gas turbine), 3.7 (new engines), 4.2 (fab, 4.15), pool EUR 4.0 bn and 0.11 bn, miss by 0.05, combined programme under 3 of 4 weightings | ok | model_scoring_inputs.csv, model_scores.csv equal weight and barrier variants |
| Table 11 | Top exporters, mirror lines, Germany net trade +79, +414, +105, −736 | ok | comtrade_portfolio_world 2024 |
| 6.2 and Figure 2 | Germany USD 0.968 bn to 1.418 bn, +47 percent | ok | 967.9 and 1,418.1 USD m, +46.5 percent |
| 6.3 | UK turbojets USD 39.8 bn, US 26.4 kt at USD 44.2 per kg, Germany 10.4 kt at 34.4 | ok | portfolio file and hs6 main reporters |
| 6.1 | Alloy shares 97, 85, 87 percent | ok | hs6 share file, eight reporters |
| Ch 2 and Ch 9 | 193 to 248 kt, EUR 6.3 to 11.7 bn, indices 141, 136, 132, 102, 3.85, three of four weightings | ok | Identical to ch 6 to 8 and model files, no cross chapter drift found |
| report.html References | No duplicate author year keys, no unlettered multiple entries, no in text author mismatch found for the (Author, Year) forms matched | ok | Scripted check. The seven Comtrade entries share one URL but differ in bracketed query, acceptable under APA |

## Residual checks
- Not independently re-fetched from original websites (fetch.py not run, network sources unverified): T2 shares, USTR exemption lists, IEA gap figures, Airbus and Boeing outlook values. Values were compared to the clean files and research notes only.
- 8.2 Table 18 company figures (Alleima fourth VAR, ATI Monroe 9 kt, Avesta EUR 11,500 per annual tonne, Aperam Imphy doubled) were not traced in this round.
- Ch 8 states the Alloy 718 pool "up to EUR 4.0 bn", the model range is 2.81 to 5.22. Add the range, since 4.0 is the P50 central value.
