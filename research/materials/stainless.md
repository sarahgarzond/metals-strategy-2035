# Specialty stainless steels (duplex, superduplex, superaustenitic, high Mo) - research notes

Stage 1, 2026-11-07. Scope note: no source found that isolates specialty grades. Hard data exist for total stainless (World Stainless Association) and for HS 7218 to 7223 (UN Comtrade), which mix commodity 304/430 with specialty grades. All specialty share figures are TODO(data) or labelled proxy.

## Access notes
- Blocked or unresolvable in the cloud session: worldstainless.org, imoa.info, outokumpu.com, en.wikipedia.org (DNS), pubs.usgs.gov (403). WebSearch budget was exhausted mid task, so IMOA, Nickel Institute, company reports (Outokumpu, Acerinox, Aperam, Sandvik, Tubacex, Haynes/ACX) were not reached.
- Worked: UN Comtrade public preview, World Bank Pink Sheet xlsx (thedocs.worldbank.org).
- Raw: data/raw/comtrade_stainless_HS7218_7223_2024.json (15 reporters x X/M), data/raw/comtrade_DE_7219_M_partners.json, data/raw/pinksheet_annual.xlsx.

## 1 Production
- World melt shop 64.2 Mt in 2025 (WSA_SS_MELT_2025), 62.6 Mt in 2024 (WSA_SS_MELT_2024). China 39.4 Mt in 2024 (WSA_SS_CN_2024), above 40.8 Mt or 64% in 2025. Europe 6.1 Mt (WSA_SS_EU_2024).
- Specialty grades are a small share. TODO(data): duplex and superaustenitic tonnage by producer (searched: duplex market volume Mt, only USD market reports found). Indonesia is now an integrated 300 series exporter (see trade).
- Major producers (qualitative, no log row yet): Outokumpu (Tornio, Avesta, Krefeld), Acerinox/VDM, Aperam, Sandvik, Tubacex, Industeel, Nippon Yakin, Aperam, Chinese TISCO and Baosteel. TODO(data) capacity by plant from annual reports.

## 2 Trade (HS 7218 to 7223, 2024, USD m, from CT_* rows)
| Reporter | 7219 exports | 7219 imports | 7222 exports | 7222 imports |
|---|---|---|---|---|
| China | 5048 (3586 kt) | 2113 | 377 | 389 |
| Indonesia | 5789 (3240 kt) | 327 | 1 | 89 |
| Belgium | 3314 | 257 | 54 | 71 |
| Finland | 2654 | 162 | 3 | 38 |
| Italy | 2262 | 2763 | 1142 | 403 |
| Germany | 1063 | 3787 (1305 kt) | 962 | 971 |
| India | 556 | 1855 | 1070 (380 kt) | 130 |
Sum of 15 reporters exports: 7219 USD 29.1bn, 7220 4.2bn, 7222 6.0bn. Indonesia also exported 7218 semifinished worth USD 2.4bn.
Derived unit values (team estimate = value / net weight): China 7219 about 1.4 USD/kg, Indonesia 1.8, Finland 2.8, Belgium 2.8, Germany bars 7222 about 5.5, India bars 2.8. Higher unit values of Nordic and German flows hint at richer mix, not proof.
Germany imports 7219 mainly from Finland 1141, Belgium 630, Italy 561, France 516, Sweden 295 (USD m).
Caveat: several rows have netWgt 0 (missing), so weights are partial.

## 3 Consumption
TODO(data): split of stainless by end use and region (searched: ISSF end use; hosts blocked). Qualitative: chemical and petrochemical, oil and gas (subsea, umbilicals), desalination, pulp and paper, flue gas cleaning, construction and storage tanks, food processing.

## 4 Applications and why
Duplex: roughly double the yield strength of 304/316 and good chloride stress corrosion resistance, enabling thinner walls. Superduplex and superaustenitic (6Mo, e.g. 254SMO class, Alloy 31): seawater, scrubbers, bleach plants, FGD. Specific PREN and strength figures TODO(data) (IMOA blocked).

## 5 Market size
- Proxy: total stainless 64.2 Mt (2025). Value not logged.
- Duplex market value triangulation only: USD 2.96bn (MR_DUPLEX_HTF_2024) and 5.9bn (MR_DUPLEX_KEN_2024) for 2024, scope differs by factor 2. Do not use in exec summary.
- TODO(data): specialty stainless share of 64.2 Mt and EUR value at semifinished level. Model owner should use a team estimate with explicit assumption.

## 6 Prices
Nickel annual average, nominal USD/t (World Bank): 2005 14744, 2010 21809, 2015 11863, 2020 13787, 2021 18465, 2022 25834, 2024 16814, 2025 15162. 2025 is 41% below the 2022 peak (team estimate). Mo and Cr prices TODO(data): not in Pink Sheet, IMOA and Fastmarkets not reached. Existing rows: ARGUS_NI_RKAB_2026 (quota cut), DEN_NI_PRICE_2026 (17494 USD/t Jan to Aug 2026). Surcharge systems (alloy surcharge) pass raw material cost through to buyers, TODO(data) source.

## 7 Capacity and supply
Indonesia export growth and Chinese 64% share create overcapacity in 300 series. Indonesia 2026 RKAB cut to 250 to 270 Mwt (ARGUS_NI_RKAB_2026). EU safeguard and anti dumping measures: TODO(data) not verified. Specialty capacity expansions: TODO(data).

## 8 Outlook 2035
TODO(data): IEA/other quantitative scenario for stainless. Qualitative drivers: LNG and hydrogen infrastructure, desalination, FGD, offshore wind and CCS pipelines favour duplex. Risk: Chinese and Indonesian push into duplex lean grades.

## Chain table
| Material | Product form | Application | Industry | Geography | Market size | Growth |
|---|---|---|---|---|---|---|
| Stainless total | Flat 7219/7220 | General | All | China 64% of melt | 64.2 Mt | 2.1% in 2025 (WSA headline) |
| Duplex 2205/2304 | Plate, strip, tube | Tanks, pressure vessels | Chemical, desalination | Europe, Asia | TODO(data) | TODO(data) |
| Superduplex 2507 | Bar, tube, plate | Subsea, umbilicals | Oil and gas | North Sea, Brazil, US Gulf | TODO(data) | TODO(data) |
| 6Mo superaustenitic | Plate, tube | Scrubbers, bleach plants | Energy, paper | Europe, Asia | TODO(data) | TODO(data) |
| Stainless bars | 7222 | Fasteners, shafts | Machinery | Germany, Italy, India | 6.0bn USD exports (15 reporters) | TODO(data) |

## Interesting facts (all logged)
1. 2024: Indonesia exported USD 5.8bn of flat stainless (HS 7219), more than China at 5.0bn (CT_7219_ID_X_2024, CT_7219_CN_X_2024), reversing the old import dependence.
2. 2024: Germany imported USD 1.14bn of flat stainless from Finland alone, mostly Tornio (Outokumpu) and equal to 30% of its 7219 imports (CT_7219_DE_M_FI_2024, team estimate share).
3. 2022 to 2025: nickel fell from 25.8k to 15.2k USD/t (WB_NI_2022, WB_NI_2025), cutting alloy surcharges for stainless buyers.
4. 2026: Indonesia cut its ore quota to 250 to 270 Mwt from about 379 Mwt (ARGUS_NI_RKAB_2026), lifting LME nickel above 18.9k in January.
