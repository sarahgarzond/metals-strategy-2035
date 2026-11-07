# Aluminium and copper products: research notes (Stage 1)

Retrieved 2026-11-07. Draft prose is in sections/02_6_aluminium_copper.md. All numbers are logged in data/sources.csv (prefixes USGS_AL_, USGS_CU_, WB_AL_, WB_CU_, CT_).

## Access notes
- pubs.usgs.gov: WebFetch returned 403, but curl through the proxy worked. PDFs saved to data/raw/usgs/ with pdftotext output.
- World Bank Pink Sheet annual xlsx (updated 2026-01-06) downloaded via curl to data/raw/pinksheet_annual.xlsx.
- UN Comtrade public preview works only per reporter (reporterCode=all is rejected). 20 reporters, 6 HS codes, 2024, saved to data/raw/comtrade_al_cu_2024.csv. Several European reporters return value but no net weight (weight 0), so weights are used only where present. Totals over the 20 reporters are partial and not a world total.
- Not reachable: international-aluminium.org, copper.org (host not in allowed network list). WebSearch budget was exhausted, so no IEA, ICSG, European Aluminium, Wieland, KME, Aurubis, Constellium, Hydro facts were gathered.

## 1. Production
- World primary aluminium 74.0 Mt (2025e), 72.8 Mt (2024). China 45.0 Mt (about 61%, team estimate), India 4.2, Russia 3.9, Canada 3.3, UAE 2.7, Bahrain 1.6, Australia 1.5, Norway 1.3, Brazil 1.2. Capacity 79.7 Mt, utilisation about 93% (team estimate).
- Copper mine 23 Mt (Chile 5.3, DR Congo 3.2, Peru 2.7), refined 29.0 Mt of which China 14.0 Mt. Germany refines 0.61 Mt, Japan 1.4, Korea 0.61.

## 2. Trade (2024, UN Comtrade, reporter values)
- HS 7604 China exports 1,089 kt, USD 3.8bn. HS 7606 Germany exports 1,337 kt, USD 5.6bn, Korea 740 kt, US imports 922 kt, USD 3.6bn. HS 7607 China exports 1,556 kt, USD 5.7bn.
- HS 7409 exports: Germany 194 kt USD 2.4bn (about USD 12.3/kg), Japan 96 kt USD 1.3bn, China 124 kt USD 1.3bn. China imports 89 kt USD 1.1bn. HS 7408 Germany 405 kt USD 4.0bn. HS 7407 Germany 117 kt, Italy 110 kt.
- US policy: Section 232 aluminium tariff 25% (March 2025), 50% (June 2025). US semis imports 4.84 Mt (2024) to 4.40 Mt (2025e). US refined copper imports 0.90 to 1.70 Mt.

## 3. Consumption
US aluminium: transport 36%, packaging 24%, building 13%, electrical 9%. US copper: building 42%, electrical and electronic 23%, transport 18%. TODO(data): global and EU splits (IAI, European Aluminium, ICSG, Copper Alliance), host blocked.

## 4. Applications
Property logic: aluminium for density and conductivity (aerospace plate, automotive sheet, heat exchangers), copper for conductivity, CuNiSi for spring strength plus conductivity (connectors, lead frames), CuNi for seawater corrosion. Engineering knowledge, no number. TODO(data): CuNiSi volumes (HS 7409 does not separate alloys).

## 5. Market size
TODO(data): semifinished volume and value by product form. Searched UN Comtrade (partial reporters only), USGS (no semis totals). Trade value indicator only.

## 6. Prices (World Bank Pink Sheet, USD/t nominal)
| Year | Aluminium | Copper |
|---|---|---|
| 2000 | 1,549 | 1,813 |
| 2010 | 2,173 | 7,535 |
| 2020 | 1,704 | 6,174 |
| 2024 | 2,419 | 9,142 |
| 2025 | 2,632 | 9,947 |
CAGR 2000 to 2025: Al 2.1%, Cu 7.0% (team estimate). Cu/Al ratio 1.2 (2000) to 3.8 (2025) (team estimate). US ingot 180 c/lb 2025, COMEX 480 c/lb record.

## 7. Capacity and supply
Indonesia 500 kt North Kalimantan smelter (expected end 2025), San Ciprian Spain 228 kt restart (full mid 2026), South Carolina 229 kt smelter partial restart, Mississippi 650 kt recycled flat rolled mill (first coils June 2025), Minnesota billet plant +55 kt, two US sheet plants closed May and June 2025, China restarts in five provinces. Copper added to US critical minerals list 7 Nov 2025. TODO(data): European fabrication capacity, Chinese export tax policy.

## 8. Outlook 2035
TODO(data): IEA scenarios, IAI, ICSG. Team must download IEA Critical Minerals Data Explorer into data/raw/. Qualitative: tight smelter utilisation, electrification pulls copper and aluminium.

## Data chain table
| Material | Product form | Application | Industry | Geography | Market size | Growth |
|---|---|---|---|---|---|---|
| Aluminium | Sheet and plate 7606 | Body sheet, plate | Automotive, aerospace | DE, KR export, US import | DE exports USD 5.6bn | TODO(data) |
| Aluminium | Foil and profiles 7607, 7604 | Packaging, EV housings | Packaging, construction | China | CN foil exports USD 5.7bn | TODO(data) |
| Copper | Strip 7409, CuNiSi | Connectors, lead frames | Electronics, automotive | DE, JP, CN | DE exports USD 2.4bn | TODO(data) |
| Copper | Wire and bar 7408, 7407 | Cable, busbar | Energy, electrical | DE, IT | DE wire exports USD 4.0bn | TODO(data) |

## Interesting facts
1. March to June 2025: US Section 232 tariff on aluminium raised from 25% to 50%, US semis imports down to 4.4 Mt (USGS_AL_US_TARIFF_2025).
2. 2025: record COMEX copper average 4.80 USD/lb, US refined imports 1.7 Mt, yearend US stocks 450 kt (USGS_CU_COMEX_2025).
3. June 2025: 650 kt per year recycled aluminium flat rolled mill in Mississippi shipped first coils (operator TODO).
4. 2024: China exported 1,556 kt aluminium foil (CT_7607_X_CN_2024).
5. 7 November 2025: copper added to US Final 2025 List of Critical Minerals (USGS_CU_CRITICAL_2025).
