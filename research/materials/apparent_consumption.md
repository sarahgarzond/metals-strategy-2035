# Apparent consumption of nickel mill products (production + imports − exports)

<!-- supersedes: the 7 November 2026 version, whose EUR column was wrong. linked from: chapter 6.1 (Table 10) and appendix A3. reason: round 3 reviews (grader_tum, grader_industry, grader_client, factcheck) all flagged Table 10 values below the contained nickel value. -->

## Key findings
1. EU27 apparent consumption of nickel plate, sheet, strip and foil (PRODCOM 24452200) was 57.8 kt in 2024: sold production 80.9 kt, extra EU imports 14.4 kt and extra EU exports 37.5 kt [AC_EU_NI_FLAT_2024, data/clean/apparent_consumption_prodcom_2019-2024.csv].
2. The EUR column used in Table 10 (EUR 889 million in total, EUR 697 million for flat products) is not valid. It mixes production values that Eurostat rounds or estimates for confidentiality with trade values at full transaction prices. The implied unit values were EUR 12.0 per kg for flat products and EUR 4.5 per kg for tubes, below the value of the contained nickel alone (World Bank 2024 average USD 16,814 per t, about EUR 15.5 per kg at 1.08 USD per EUR) [NI_WB_AVG_2024, WB_PINKSHEET].
3. Diagnosis per product, EU27, 2024 (team calculation from the same file):

| PRODCOM code | Production kt | Production EUR/kg | Import kt, EUR/kg | Export kt, EUR/kg | Apparent consumption kt | Value range, EUR m (team estimate) |
|---|---:|---:|---|---|---:|---|
| 24452100 Bars, rods, profiles, wire | 2.5 (rounded estimate) | 40.0 | 5.6 at 25.4 | 2.7 at 33.4 | 5.4 (lower bound) | 137 to 180 |
| 24452200 Plate, sheet, strip, foil | 80.9 | 14.5 | 14.4 at 47.8 | 37.5 at 31.0 | 57.8 | 1,795 to 2,766 |
| 24452300 Tubes, pipes, fittings | 21.0 (rounded estimate) | 13.3 | 4.7 at 41.1 | 16.5 at 26.1 | 9.2 | 239 to 377 |

   Value range = apparent consumption in tonnes × the lower and upper of the import and export unit values. This values the market at the prices at which qualified product actually crosses the EU border, rather than at the confidential production value.
4. Sold production unit values of EUR 13 to 15 per kg are at or below the contained nickel value, so PRODCOM production value in these codes is not a usable price. Germany shows the same pattern: production EUR 8.8 per kg against imports EUR 29.0 and exports EUR 32.6 per kg [AC_DE_NI_FLAT_2024].
5. The bar figure is not credible as a market size. Production of 2.5 kt is a rounded Eurostat estimate, while Germany alone exported USD 638 million of HS 7505 in 2024, including intra EU trade [COMTRADE_7505_2019_2024]. The bar line must be shown as confidential, not as 5.4 kt.

## Recommended Table 10 for the report
* Show tonnes for flat products (57.8 kt) and tubes (9.2 kt) and mark bars as confidential.
* Show value as a range from trade unit values, labelled "team estimate": flat products about EUR 1.8 to 2.8 billion, tubes about EUR 0.24 to 0.38 billion.
* Add a unit value column and the contained nickel value (about EUR 15.5 per kg in 2024) so the reader sees the conversion premium. The export unit value of flat products, EUR 31 per kg, is about twice the contained nickel value, which matches German Comtrade export unit values of about USD 32,500 per t [NI_CT_DE_7506_2024_T].

## Spotlight facts
* In 2024 EU producers sold 80.9 kt of nickel plate, sheet, strip and foil, of which 37.5 kt left the EU at an average EUR 31.0 per kg, about twice the value of the nickel it contains (Eurostat PRODCOM DS-059358, World Bank Pink Sheet).
* In 2024 extra EU imports of nickel flat products were valued at EUR 47.8 per kg, the highest unit value of the three codes, which points to thin strip, foil and qualified alloy grades bought from the United States and Japan (PRODCOM 24452200).
* In 2024 the EU was a net exporter of nickel tubes (16.5 kt out, 4.7 kt in), which matches the strong German and Italian positions in HS 7507 in UN Comtrade.
* Outokumpu's planned high nickel capacity at Avesta, about 13 kt for about EUR 150 million announced in 2026, is about a quarter of EU apparent consumption of nickel flat products [CO_OUTOKUMPU_HINI_CAP_2026].

## Triangulation
| Number | Source 1 | Source 2 | Result |
|---|---|---|---|
| German flat export tonnes 2024 | PRODCOM DE exports 18.1 kt | Comtrade HS 7506 Germany exports 17.8 kt [COMTRADE_7506_2019_2024] | Consistent within 2 percent |
| Flat export unit value 2024 | PRODCOM EU exports EUR 31.0 per kg | Comtrade Germany HS 7506 USD 32.5 per kg (about EUR 30 per kg) | Consistent |
| Contained nickel value 2024 | World Bank Pink Sheet USD 16,814 per t [NI_WB_AVG_2024] | USGS MCS 2026 nickel price series [USGS_MCS2026_DATA] | Consistent order of magnitude |
| Scale of specialty layer | EU nickel flat apparent consumption 57.8 kt | Producer capacity: Outokumpu 13 kt project, ATI and Carpenter 10-K melt descriptions [CO_ATI_SALES_2025, CO_CRS_OPINC_2026] | Tens of kt, consistent |

## Source coverage
| Required source | Status | Evidence |
|---|---|---|
| Eurostat PRODCOM | used | data/clean/apparent_consumption_prodcom_2019-2024.csv, PRODCOM DS-059358 https://ec.europa.eu/eurostat/databrowser/view/DS-059358/ |
| UN Comtrade (tools/data/fetch.py comtrade) | used | data/clean/comtrade_7505_2019-2024.csv, data/clean/comtrade_7506_2019-2024.csv, data/clean/comtrade_7507_2019-2024.csv, https://comtradeplus.un.org/ |
| World Bank Commodity Data / Pink Sheet | used | data/clean/worldbank_pinksheet_monthly.csv, NI_WB_AVG_2024 |
| USGS Mineral Commodity Summaries 2026 | used | USGS_MCS2026_DATA, https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-nickel.pdf |
| IEA Global Critical Minerals Outlook 2026 | used | data/clean/iea_critical_minerals_demand_2026.csv (nickel demand outside energy technologies 2,906 kt in 2025) |
| Company annual reports, 10-K/20-F | used | Outokumpu annual report and capacity release CO_OUTOKUMPU_HINI_CAP_2026, ATI Form 10-K https://www.sec.gov/Archives/edgar/data/1018963/000162828026010140/ati-20251228.htm, Carpenter Form 10-K https://www.sec.gov/Archives/edgar/data/0000017843/000001784326000034/crs-20260630.htm, Aperam annual report 2025, Alleima annual report 2025 https://mb.cision.com/Main/21386/4324612/3995611.pdf |

## Rules for using these numbers
1. Apparent consumption is a trade balance identity for the EU. It is not end use alloy demand and not stainless melt.
2. PRODCOM EU27 trade is extra EU trade only. Intra EU flows (for example Germany to Austria and Italy) are inside the figure and do not appear as imports or exports.
3. PRODCOM 24452100 to 24452300 cover nickel and nickel alloys where nickel predominates by weight. Alloys with less than half nickel (for example many FeNi and some NiCr grades) are classified elsewhere.
4. Never add kg of different codes or stages, and never present production value from these codes as a price.

## Open gaps
TODO(data): Eurostat confidential production cells for 24452100 and 24452300 by member state. Ask Eurostat or use national statistics (Destatis GENESIS 42131) for Germany.
TODO(data): unit values by alloy grade are not public. The trade unit value range is a proxy and is labelled team estimate.
TODO(data): no PRODCOM codes isolate cobalt, titanium or tungsten mill products at the needed level, so apparent consumption for these metals needs Comtrade plus national production.
