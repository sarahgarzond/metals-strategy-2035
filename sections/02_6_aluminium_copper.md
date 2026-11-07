## 2.6 Aluminium and copper products

Aluminium and copper are the two high volume base metals in the Client portfolio, and because both are traded in far larger tonnages than nickel or cobalt, the relevant question for strategy is which semifinished niches justify a premium over commodity supply. This section follows the data chain from material to product form, application, industry, geography, market size and growth, and it marks every gap openly.

### Production

Primary aluminium supply is dominated by China, which smelted an estimated 45.0 Mt in 2025 out of a world total of 74.0 Mt, a share of about 61% (team estimate) [USGS_AL_SMELT_2025_CN, USGS_AL_SMELT_2025_WORLD]. India followed with 4.2 Mt, Russia with 3.9 Mt and Canada with 3.3 Mt, so the three next largest producers together add up to only about a quarter of the Chinese volume [USGS_AL_SMELT_2025_IN, USGS_AL_SMELT_2025_RU, USGS_AL_SMELT_2025_CA]. World output grew from 72.8 Mt in 2024 to 74.0 Mt in 2025 [USGS_AL_SMELT_2024_WORLD], while yearend capacity reached 79.7 Mt, which implies a utilisation of about 93% (team estimate) [USGS_AL_CAP_2025_WORLD].

Copper is mined mainly in Chile, DR Congo and Peru, and the world mine total of about 23 Mt in 2025 [USGS_CU_MINE_2025] contrasts with a refined output of 29.0 Mt [USGS_CU_REF_2025_WORLD]. Because China refined an estimated 14.0 Mt, close to half of the world total (team estimate), although it mined only 1.8 Mt, the country depends on imported concentrate and scrap [USGS_CU_REF_2025_CN, USGS_CU_MINE_2025]. For the Client this means that European semifinished producers buy cathode and scrap on world markets, while the processing power of Chinese mills sets the global conversion cost.

### Trade

Since production concentrates in China while fabrication is spread over Europe, North America and East Asia, trade in semifinished products runs in several directions at once. The UN Comtrade extract for 2024 (20 reporting countries, see data/raw/comtrade_al_cu_2024.csv) shows that China exported 1,556 kt of aluminium foil (HS 7607) worth USD 5.7bn and 1,089 kt of bars and profiles (HS 7604) worth USD 3.8bn [CT_7607_X_CN_2024, CT_7604_X_CN_2024]. Germany exported 1,337 kt of aluminium sheet, plate and strip (HS 7606) worth USD 5.6bn, and Korea exported 740 kt [CT_7606_X_DE_2024, CT_7606_X_KR_2024]. The United States imported 922 kt of the same flat rolled products worth USD 3.6bn [CT_7606_M_US_2024].

Copper semifinished trade is smaller in tonnage but richer in value per kilogram. Germany exported 194 kt of copper plate, sheet and strip (HS 7409) worth USD 2.4bn, which equals about USD 12.3 per kg (team estimate), while Japan reached about USD 13.5 per kg on 96 kt and China about USD 10.5 per kg on 124 kt [CT_7409_X_DE_2024, CT_7409_X_JP_2024, CT_7409_X_CN_2024]. China was also the largest single importer of this product among the reporters pulled, with 89 kt worth USD 1.1bn, which points to a high end import niche next to a large domestic mill base [CT_7409_M_CN_2024]. German copper wire (HS 7408) exports reached 405 kt worth USD 4.0bn and bar and profile exports (HS 7407) 117 kt worth USD 1.0bn, with Italy next at 110 kt [CT_7408_X_DE_2024, CT_7407_X_DE_2024, CT_7407_X_IT_2024].

Trade policy now reshapes these corridors in a way that affects every German exporter of semifinished products. The United States imposed a 25% Section 232 tariff on aluminium and derivatives in March 2025 and doubled it to 50% for most countries by June, with the United Kingdom held at 25% [USGS_AL_US_TARIFF_2025]. US imports of crude and semi fabricated aluminium fell from 4.84 Mt in 2024 to an estimated 4.40 Mt in 2025 [USGS_AL_US_IMP_2025], and US refined copper imports rose to 1.7 Mt from 0.9 Mt as buyers built stocks ahead of expected copper tariffs [USGS_CU_US_REFIMP_2025]. These shifts matter for a German exporter because the transatlantic flat rolled and strip business now carries a tariff burden that must be passed on or absorbed.

### Consumption

Given that trade flows follow end use, the demand structure explains where fabricators earn their margin. In the United States, transportation took 36% of aluminium consumption in 2025, packaging 24% and building 13% [USGS_AL_US_USE_2025]. US copper use was led by building construction at 42%, followed by electrical and electronic products at 23% and transportation equipment at 18% [USGS_CU_US_USE_2025]. TODO(data): global and EU consumption splits by industry from International Aluminium Institute, European Aluminium and International Copper Study Group were searched but the hosts were not reachable in the cloud session, so only the US split is documented.

### Applications

Aluminium is chosen where low density and good thermal and electrical conductivity must be combined, which is why 2xxx and 7xxx plate and extrusions serve aerospace structures and 5xxx and 6xxx sheet serves automotive bodies, battery housings and heat exchangers. Copper is chosen for conductivity, and copper alloys add strength and corrosion resistance. CuNiSi strip and wire (for example alloys of the C70250 family) combine spring properties with conductivity for connectors and lead frames, and CuNi alloys resist seawater in marine and desalination heat exchangers. These property statements are engineering knowledge of the team, and no market volume for CuNiSi is available in public trade statistics. TODO(data): HS 7409 does not separate CuNiSi from other alloys, and producers such as Wieland, KME, Mueller and Olin were not yet checked for volume statements.

The USGS lists the main substitution paths between the two metals, and they define where the Client competes with its own products. Aluminium can replace copper in radiators, cooling tube and power cable, and copper can replace aluminium in electrical and heat exchange uses [USGS_AL_US_USE_2025, USGS_CU_US_USE_2025]. The price ratio between the two metals sets the incentive for such switching, and it widened from 1.2 in 2000 to 3.8 in 2025 (team estimate from [WB_CU_2000, WB_AL_2000, WB_CU_2025, WB_AL_2025]).

### Market size

Because a full volume and value series at semifinished level needs paid or association data, this version uses a trade value indicator. The reporter extract above shows flat rolled aluminium exports of USD 21.2bn from the 20 countries pulled in 2024, but this is a partial sum and not a world total, so it is not used in the model. TODO(data): semifinished market size by product form (strip, sheet and plate, bar, wire, tube, foil) for aluminium and copper, searched via UN Comtrade (all reporters need a keyed API), Eurostat PRODCOM and association statistics. The Client revenue of about EUR 400m in a EUR 50bn market must be split by material in the Excel model once this series is complete.

### Prices

Following the market size question, the price history shows a strong structural uptrend. According to the World Bank Pink Sheet, the annual average aluminium price rose from USD 1,549 per tonne in 2000 to USD 2,632 in 2025, and copper from USD 1,813 to USD 9,947 [WB_AL_2000, WB_AL_2025, WB_CU_2000, WB_CU_2025]. This equals about 2.1% p.a. for aluminium and 7.0% p.a. for copper (team estimate). Both metals gained about 8.8% between 2024 and 2025 (team estimate from [WB_AL_2024, WB_CU_2024]). The 2020 values were USD 1,704 and USD 6,174, so copper rose by about 61% in five years [WB_AL_2020, WB_CU_2020].

The US market shows an additional policy premium on top of this world price trend. The US average ingot price reached 180 cents per pound in 2025 against 129.5 in 2024 [USGS_AL_US_PRICE_2025], and the COMEX copper price averaged a record 480 cents per pound, against an LME average of 440, mainly because of tariff uncertainty [USGS_CU_COMEX_2025]. The drivers are energy cost for smelting, Chinese capacity limits, tariffs, ore grade decline and the energy transition demand for conductors.

### Capacity and supply

As prices rise, capacity responds only slowly and unevenly across the producing regions of the world. Chinese capacity is held at about 45 Mt and smelters in Guangxi, Guizhou, Qinghai, Sichuan and Yunnan resumed production or added potlines in 2025 [USGS_AL_CAP_2025_WORLD]. Outside China, a 500 kt smelter in North Kalimantan, Indonesia was expected to start by the end of 2025, and a 228 kt smelter in San Ciprian, Spain restarted with full output expected by mid 2026. In the United States, a 229 kt smelter in South Carolina plans a restart of more than 50 kt, and a 650 kt recycled flat rolled mill in Mississippi shipped its first coils in June 2025 [USGS_AL_RECYCLED_MILL_2025]. Two sheet facilities in Virginia and West Virginia closed in May and June 2025 [USGS_AL_US_TARIFF_2025].

For copper, concentrator shutdowns and lower ore grades reduced US mine output to 1.0 Mt in 2025 [USGS_CU_MINE_2025], and copper joined the US critical minerals list on 7 November 2025 [USGS_CU_CRITICAL_2025]. TODO(data): European fabrication capacity (Wieland, KME, Aurubis, Constellium, Speira, Hydro) and export policy items such as Chinese export tax changes were not retrieved.

### Outlook 2035

Looking ahead, supply and demand signals point in the same direction for both metals. Aluminium smelter utilisation near 93% leaves little spare capacity, so new demand from electrification and lightweight vehicles will need new smelters or recycling, which the Mississippi and Minnesota projects illustrate [USGS_AL_CAP_2025_WORLD, USGS_AL_RECYCLED_MILL_2025]. TODO(data): IEA scenario demand for copper and aluminium to 2035, IAI 2050 scenarios and ICSG forecasts were not retrievable because iea.org blocks automated downloads, so the team must download the IEA Critical Minerals Data Explorer into data/raw/.

### Data chain and spotlight facts

| Material | Product form | Application | Industry | Geography | Market size | Growth |
|---|---|---|---|---|---|---|
| Aluminium | Sheet and plate (HS 7606) | Body sheet, plate, heat exchangers | Automotive, aerospace | Germany, Korea exporters, US importer | Germany exports USD 5.6bn [CT_7606_X_DE_2024] | TODO(data) |
| Aluminium | Foil and profiles (HS 7607, 7604) | Packaging, building, EV housings | Packaging, construction, automotive | China exporter | China exports USD 5.7bn foil [CT_7607_X_CN_2024] | TODO(data) |
| Copper | Strip and sheet (HS 7409), CuNiSi | Connectors, lead frames, heat exchangers | Electronics, automotive, energy | Germany, Japan, China | Germany exports USD 2.4bn [CT_7409_X_DE_2024] | TODO(data) |
| Copper | Wire and bar (HS 7408, 7407) | Cable, busbar, contacts | Energy, electrical, data centres | Germany, Italy | Germany wire exports USD 4.0bn [CT_7408_X_DE_2024] | TODO(data) |

Interesting facts for the sector chapters:

1. In March 2025 the United States put a 25% Section 232 tariff on aluminium and derivatives and raised it to 50% by June 2025, which cut US imports of aluminium semis to 4.4 Mt and favours domestic rolling mills [USGS_AL_US_TARIFF_2025, USGS_AL_US_IMP_2025].
2. In 2025 the COMEX copper price averaged a record 4.80 USD per pound, and US refined copper imports nearly doubled to 1.7 Mt in anticipation of tariffs, which raised yearend US stocks to 450 kt [USGS_CU_COMEX_2025, USGS_CU_US_REFIMP_2025].
3. In June 2025 a 650 kt per year recycled aluminium flat rolled mill in Mississippi shipped its first coils, with the operator still to be confirmed (TODO(data): company name not given in USGS) [USGS_AL_RECYCLED_MILL_2025].
4. In 2024 China exported 1,556 kt of aluminium foil, the largest flow among the reporters pulled, which shows the scale of Chinese foil supply to world markets [CT_7607_X_CN_2024].
