# Cobalt alloys: raw research notes (Phase I, section 2.3)

Branch: worktree-agent-a4cf30a7bdf0059a6. Date of research: 2026-11-07. Raw files in data/raw/cobalt/.

## Access log (blocked hosts and alternatives)
- pubs.usgs.gov: reachable with curl (HTTP 200), PDF saved as data/raw/cobalt/usgs_mcs2026_cobalt.pdf. WebFetch got 403, so curl was used. The earlier medium confidence row is now high.
- Comtrade public preview: works per reporter with partnerCode=0 only. Reporter 0 (world) returns zero rows. HTTP 429 after bursts, so a 1.5 s pause and retries were needed. Reporters pulled: China, Germany, Belgium, Finland, Japan, USA, Canada, DR Congo, Norway, Australia, Korea, Netherlands, UK, Zambia (HS 8105) and China, Germany, USA, Japan, UK, France (HS 810520, 810590).
- World Bank Pink Sheet (CMO-Historical-Data-Monthly.xlsx, updated 3 Nov 2026) downloaded, but it contains no cobalt series (only nickel). Cobalt prices therefore come from USGS (LME cash annual averages). TODO(data): LME or Fastmarkets monthly cobalt history 2015 to 2026.
- www.cobaltinstitute.org, en.wikipedia.org, www.haynesintl.com: host not resolvable in this session. These need to be allowed in network settings.
- www.iea.org and reuters.com: 403 or not fetchable. WebSearch budget exhausted for this turn, so no IEA cobalt outlook figures could be gathered.

## 1 Production
World mine production 310 kt in 2025 (302 kt in 2024). DR Congo 230 kt (73%), Indonesia 44 kt (14%, up from 35 kt), Russia 7.7 kt, Madagascar 3.9 kt, Australia 3.7 kt, Philippines 3.7 kt, Canada 3.5 kt. Reserves 12 Mt, DR Congo 6.0 Mt. China is the leading refiner and consumer (USGS text, no number retrieved). [USGS_CO_MINE_2025, USGS_CO_DRC_2025, USGS_CO_IDN_2025, USGS_CO_RESERVES]
TODO(data): refined cobalt output by country (China share), Cobalt Institute 2025 market report, Glencore, CMOC, Umicore, Huayou, Jinchuan, Sherritt, Vale, Fort Saskatchewan, Kokkola (Finland), Harjavalta production figures.

## 2 Trade
HS 8105 covers mattes, intermediates, unwrought cobalt, powders, scrap and wrought articles. 2024 Comtrade values:
- China imports USD 3,213m, 640 kt gross weight, of which DR Congo USD 3,019m and 628 kt. Implied unit value about USD 5 per kg (team estimate, 3,212.9 / 640.2), which shows the flow is intermediate material, not metal.
- China exports USD 266m, 9.6 kt, mainly Netherlands USD 140m.
- USA exports USD 418m and imports USD 389m. UK exports USD 218m. Germany exports USD 148.5m and imports USD 130.0m. Japan exports USD 96m and imports USD 171m. Belgium USD 125m and 115m. Canada exports USD 255m. Norway exports USD 74m. Finland imports USD 6.6m.
- Wrought HS 810590 (best proxy for alloy semifinished cobalt products): USA exports USD 262.6m for 1,889 t (about USD 139/kg), UK USD 142.3m for 1,744 t, Germany USD 98.5m for 1,056 t (about USD 93/kg), China only USD 12.8m for 235 t. Chinese imports USD 67.1m for 650 t.
- DRC reports almost no HS 8105 exports (USD 6.3m), so DRC flow must be read from the Chinese mirror data. Hydroxide is HS 2822 and ores 2605, not pulled. TODO(data): HS 2822, 2605, 2833 and 8105.30 scrap, bilateral Germany partners.
Policy: DRC export ban Feb 2025, quotas 18,125 t rest of 2025 and 96.6 kt per year for 2026 and 2027 including 9.6 kt reserve. US imports rose to 14,000 t in 2025. [CT_8105_CN_IMP_2024, CT_8105_CN_IMP_DRC_2024, CT_8105_CN_EXP_2024, CT_8105_DE_2024, CT_8105_US_2024, CT_8105_UK_2024, CT_810590_DE_EXP_2024, CT_810590_US_EXP_2024, CT_810590_UK_EXP_2024, CT_810520_CN_EXP_2024, USGS_CO_QUOTA_2025, ARGUS_CO_QUOTA]

## 3 Consumption
Only US split found: superalloys 51% (mainly aircraft gas turbine engines), chemicals 25%, other metallic 15%, cemented carbides 9%. US consumption about 8,000 t (2025e), value USD 320m, net import reliance 79%, scrap 25% of consumption. USGS names the lithium ion battery as the leading global use and China as the leading consumer. [USGS_CO_US_USE_SUPERALLOY, USGS_CO_US_VALUE, USGS_CO_US_IMPREL, USGS_CO_US_SCRAP]
TODO(data): global split battery, superalloy, hard materials, magnets, catalysts, pigments (Cobalt Institute, CRU, Darton).

## 4 Applications
Supported by USGS substitutes text: jet engine superalloys (nickel base alloys or ceramics as substitutes), cemented carbides and diamond tools (cobalt binder), magnets (SmCo, AlNiCo, substitutes ferrites and NdFeB), prosthetics (CoCr, titanium substitute), catalysts. Property logic (hot hardness, wear and corrosion resistance, biocompatibility, magnetism at high temperature) is general metallurgy and needs a citation. TODO(data): Haynes International and Kennametal or Deloro Stellite product data sheets for Alloy 188, L605, Stellite 6, MP35N, FSX 414, Co-Cr-Mo ASTM F75 (searched: could not reach haynesintl.com).

## 5 Market size
No semifinished cobalt alloy market volume found. Available anchors: US consumption value USD 320m (2025e), trade value of wrought HS 810590 for four exporters 2024 about USD 516m (team estimate, sum of US, UK, Germany, China exports). TODO(data): global cobalt alloy semifinished volume and value, share of Client portfolio, 2015 to 2025 history.

## 6 Prices
LME cash cobalt, annual average USD/lb: 2021 23.17, 2022 28.83, 2023 15.48, 2024 11.84, 2025 15. US spot cathode: 2021 24.21, 2022 30.78, 2023 17.20, 2024 16.77, 2025 21. SMM forecast for intermediates end 2026: 28.8 USD/lb (range 24.5 to 33.0, low confidence). Drivers: DRC supply policy, Indonesian nickel byproduct supply, battery chemistry shift to LFP, Chinese stock policy. [USGS_CO_LME_PRICE, SMM_CO_PRICE_2026]
TODO(data): monthly 2026 price path, cobalt metal price versus alloy surcharge mechanics.

## 7 Capacity and supply
Concentration: DR Congo 73% of mine supply. Quota regime 96.6 kt per year 2026 and 2027 equals about 42% of 2025 DRC mine output of 230 kt (team estimate, 96.6 / 230), indicating a binding constraint if gross cobalt content is compared, and Argus describes it as about half of 2024 exports. US National Defense Stockpile solicitation for 7,480 t over 5 years cancelled in 2025. US import reliance 79%. [USGS_CO_DRC_2025, USGS_CO_QUOTA_2025, ARGUS_CO_QUOTA]
TODO(data): company expansions (Indonesian HPAL cobalt, Kokkola, ATI, Carpenter, Haynes capacity), Chinese refining capacity, recycling capacity.

## 8 Outlook to 2035
TODO(data): IEA Global Critical Minerals Outlook 2025 cobalt demand 2024 to 2035 under STEPS and APS (www.iea.org returned 403, search budget exhausted). Qualitative from USGS: battery cobalt content falling, LFP share large in China. Aerospace anchor from existing rows: Airbus 43,420 deliveries 2025 to 2044, Boeing 43,625 deliveries 2026 to 2045. [AIRBUS_GMF_2025, BOEING_CMO_2026]

## Mapping table
| Material | Product form | Application | Industry | Geography | Market size | Growth |
|---|---|---|---|---|---|---|
| Cobalt alloys (Co base superalloys, e.g. Alloy 188, L605) | Sheet, strip, bar, wire | Combustors, afterburner parts, turbine components | Aerospace | US, UK, Germany, France | US cobalt in superalloys about 51% of 8,000 t; value TODO(data) | TODO(data) |
| Cobalt alloys (Stellite type hardfacing) | Welding consumables, powder, bar | Wear and corrosion resistant surfaces, valves | Oil and gas, power, chemical | Global | TODO(data) | TODO(data) |
| CoCr and CoCrMo (F75, F1537, MP35N) | Bar, wire, castings, AM powder | Implants, stents, dental | Medical | US, EU | TODO(data) | TODO(data) |
| Cobalt in cemented carbide | Powder (binder) | Cutting, mining tools | Automotive and machinery | Global | US share 9% of consumption | TODO(data) |
| Wrought cobalt articles HS 810590 | Semifinished and articles | Mixed | Mixed | US USD 263m, UK USD 142m, DE USD 99m exports 2024 | about USD 516m (four exporters) | TODO(data) |

## Interesting facts (dated, named)
1. February 2025: DR Congo, which mined 230 kt or 73% of world cobalt, banned cobalt exports to end oversupply and low prices. In October 2025 quotas of 96.6 kt per year for 2026 and 2027 replaced the ban. Affected metal: cobalt hydroxide for Chinese refiners, downstream alloy makers pay through cobalt surcharges. [USGS_CO_QUOTA_2025]
2. 2025: US cobalt imports jumped to 14,000 t from 10,800 t in 2024 and industry stocks to 1,500 t as buyers hedged the ban, while the US government cancelled its 7,480 t five year National Defense Stockpile solicitation. Product: cobalt metal and alloy feed for aircraft engine superalloys. [USGS_CO_LME_PRICE, USGS_CO_US_IMPREL]
3. 2022 to 2024: LME cobalt fell from USD 28.83 per lb to USD 11.84 per lb, a 59% drop (team estimate), before recovering to USD 15 in 2025. [USGS_CO_LME_PRICE]
4. 2024: Chinese import unit value of HS 8105 was about USD 5 per kg, German exports of wrought cobalt articles about USD 93 per kg and US exports about USD 139 per kg. This is a roughly 19 to 28 fold value ladder from intermediate to semifinished (team estimate). [CT_8105_CN_IMP_2024, CT_810590_DE_EXP_2024, CT_810590_US_EXP_2024]
5. 2025: Indonesia lifted cobalt output to 44 kt from 35 kt as a byproduct of nickel laterite leaching, now 14% of world supply. [USGS_CO_IDN_2025]
