## 2.2 Nickel and nickel alloys

Nickel is the Client's largest material family, and its economics are set far upstream of the Client's plants by a mining and refining system that changed fundamentally between 2020 and 2025. This section follows the eight dimensions of the data foundation, starting with production and ending with the outlook to 2035, and it closes with the data chain table that links every product form to an application, an industry and a region.

### Production

Because Indonesia has taken over the market, world nickel supply is now a one country story. Global mine output reached an estimated 3.9 Mt of contained nickel in 2025, up 5% from 3.71 Mt in 2024, and Indonesia alone delivered about 2.6 Mt or two thirds of that total [USGS_NI_MINE_2025, USGS_NI_WORLD_2024]. The Philippines followed at 270 kt after a fall of about 24% [USGS_NI_PH_2025], Russia produced 200 kt [USGS_NI_RU_2025], and Canada and New Caledonia each reached 140 kt [USGS_NI_CA_2025, USGS_NI_NC_2025]. Australia is the clearest casualty of the price slump, since its output fell by about 54% to 45 kt when several mines went into care and maintenance [USGS_NI_AU_2025].

Mine output is only the first step, because the metal that reaches an alloy melt shop comes from refineries and intermediate plants. Indonesia held about 43% of global refining capacity in 2025 [UNCTAD_NI_REFINE_2026], with processing capacity above 2.7 Mt of contained nickel according to the Indonesian smelter forum [FINI_NI_CAP_2025]. The Class 1 metal that nickel alloys depend on comes mainly from Norilsk Nickel in Russia, which produced 199 kt in 2025 [NORNICKEL_NI_2025], and from Canadian, Norwegian, Finnish and Australian refineries. The reserve base supports this geography, since Indonesia holds 62 Mt of the more than 140 Mt of world reserves [USGS_NI_RES_2025].

### Trade

As a result of this concentration, trade flows run from Indonesia into China in the form of intermediates, while the established Western flows of refined metal and semifinished products remain small by comparison. China imported nickel mattes and intermediates worth USD 7.6bn in 2024, of which Indonesia supplied USD 6.2bn [CT_NI_7501_CN_M_2024]. Unwrought nickel (HS 7502) is a smaller market with exports of USD 11.4bn, led by China, Canada, Norway and Indonesia, and imports of USD 12.3bn led by China, the United States, Germany and Japan [CT_NI_7502_X_2024, CT_NI_7502_M_2024].

For the Client the semifinished headings matter more than the raw material flows. Exports of bars, rods and wire (HS 7505) reached USD 5.0bn in 2024, with the United States (USD 1.4bn) and Germany (USD 0.6bn) as the largest exporters [CT_NI_7505_X_2024]. Plates, sheet and strip (HS 7506) are a smaller market of USD 2.0bn in exports, where Germany leads with USD 0.58bn and 17.8 kt, ahead of the United States and Japan [CT_NI_7506_X_2024]. Tubes and fittings (HS 7507) add USD 1.7bn [CT_NI_7507_X_2024]. German strip and sheet moves mainly to Austria, Italy, China and the United States, and German bar and wire moves to the United Kingdom, the United States, Italy and France [CT_NI_7506_X_2024, CT_NI_7505_X_2024]. These figures are sums of reporting countries in the public preview endpoint and therefore understate full trade.

### Consumption

Since stainless steel absorbs most nickel, consumption data describe the stainless industry first and the alloy industry second. Stainless steel took about 66% of nickel use and batteries about 16%, while nickel base alloys held about 6%, plating 5% and alloy steels 3% [NICKEL_USE_SPLIT_2024]. Natural Resources Canada reports a different split with non ferrous alloys near 9%, so the alloy share lies between 6% and 9% depending on the definition, and the exact value remains a data gap that the team will close with the Nickel Institute tables (TODO(data): Nickel Institute end use table not retrievable because nickelinstitute.org is blocked).

Regional consumption follows stainless melting, which is concentrated in China, while alloy consumption follows aerospace, energy and chemical plants in the United States and Europe. The United States consumed about 120 kt of reported primary nickel in 2025 and covered about 60% of its apparent consumption from scrap, which shows how large the recycling loop is for alloys and stainless steel [USGS_NI_MINE_2025, USGS_NI_US_RECYC_2025]. Germany, the United States and the United Kingdom are the largest importers of nickel bar and wire, and these markets are therefore the natural reference for the Client's customer base [CT_NI_7505_M_2024].

### Applications

Because nickel gives alloys strength at high temperature and resistance to corrosion, the high value uses sit where both properties are needed together. Nickel base superalloys serve turbine discs and blades in jet engines and gas turbines, corrosion resistant alloys such as Alloy C-276 serve chemical processing and flue gas cleaning, and low expansion alloys such as FeNi36 serve precision instruments and electronics. Nickel and NiCr strip is also used in heating elements, in battery cell connectors and in sealing and fuel cell components.

The aerospace link is currently the strongest demand signal for the Client's alloys, because engine makers delivered 269 widebody engines in the first half of 2026 against 222 a year earlier, and Rolls Royce delivered 157 against 122, which tightens supply of nickel superalloys and premium quality titanium [ARGUS_ENGINES_H1_2026]. ATI plans a fifth vacuum induction melting furnace at Monroe, North Carolina, with 9 kt per year starting in the second half of 2027 [ARGUS_SUPERALLOY]. Market reports value the aerospace superalloy market at about USD 1.25bn in 2026, but this figure serves only as a triangulation point because the scope is unclear [GII_NI_SUPERALLOY_AERO_2026].

### Market size

As the next step, the size of the Client's relevant market has to be separated from the size of the nickel metal market. The contained value of 2025 mine output was about USD 59bn, calculated as 3.9 Mt at the average price of USD 15,162 per tonne (team estimate) [TE_NI_MINE_VALUE_2025]. At the semifinished level, the export value of bars, wire, strip, sheet and tubes in 2024 was about USD 8.65bn (team estimate), which is a lower bound because domestic sales are not captured [TE_NI_SEMIS_TRADE_2024]. Volume growth of mine supply was 5% in 2025, but price fell, so the value of metal shrank while semifinished markets depend more on alloy content and processing.

The EUR value of the nickel alloy and semifinished market is not yet derived from PRODCOM and the master model (TODO(data): Eurostat PRODCOM 2440 and 2441 nickel products value and volume for EU27 not yet pulled, and a USD to EUR conversion rate must be fixed in the model). The overall addressable market of EUR 50.6bn for the Client's portfolio is documented in the model architecture [MODEL_TOTAL_2025].

### Prices

Following from the supply shift, prices have fallen for three years and remain far below the historical peak. The annual LME average was USD 37,230 per tonne in 2007, USD 25,834 in 2022, USD 21,521 in 2023, USD 16,814 in 2024 and USD 15,162 in 2025 [WB_NI_2007, WB_NI_2022, WB_NI_2023, WB_NI_2024, WB_NI_2025]. In 2026 the monthly average rose to USD 17,154 for January to October, with a high of USD 18,806 in May and USD 15,436 in October, as Indonesian quota cuts supported the market [WB_NI_2026_YTD, ARGUS_NI_RKAB_2026].

The main price drivers are Indonesian ore policy, battery demand and the level of exchange inventories. Indonesia approved 379 Mwt of ore in 2025 and cut the initial 2026 quota to 260 to 270 Mwt before revising it towards 290 to 300 Mwt, with royalties of 11% to 19% [SPGLOBAL_RKAB_2026]. The International Nickel Study Group saw a primary surplus of 182 kt in 2024 and now expects a small surplus of 19 kt in 2026, with production of 3.87 Mt against usage of 3.85 Mt [USGS_NI_SURPLUS_2024, INSG_NI_2026]. For alloy producers the key point is that nickel surcharges pass metal price swings to customers, so the margin depends more on processing and mix than on the LME level.

### Capacity and supply

Since Indonesian supply is policy driven, supply risk for the Client is no longer about geology but about regulation and concentration. The Indonesian smelter forum expects processed output to fall by 3.5% to 4% in 2026 and mixed hydroxide precipitate capacity to exceed 900 kt of nickel by the end of 2027 [FINI_NI_CAP_2025]. Philippine permit restrictions in Palawan and Australian mine closures remove other sources of ore [USGS_NI_PH_2025, USGS_NI_AU_2025].

On the Western alloy side, capacity is being added in response to engine demand, as the ATI furnace at Monroe shows [ARGUS_SUPERALLOY]. Acerinox completed the acquisition of Haynes International in November 2024 and combined it with VDM Metals into a high performance alloys division, which makes it a direct competitor of the Client in Germany and the United States [ACX_HAYNES]. The Class 1 supply risk lies with Russia, because Norilsk Nickel is the largest single Class 1 producer and faces sanctions risk [NORNICKEL_NI_2025]. The United States has no primary refinery and a net import reliance of 41% including scrap [USGS_NI_MINE_2025].

### Outlook to 2035

Looking ahead, demand growth is expected from batteries, aerospace and energy, while supply growth is expected from Indonesia at lower rates than in 2020 to 2025. The IEA Stated Policies Scenario in the 2025 outlook reaches 5,689 kt of nickel demand by 2040, and the three largest refiners would hold 83% of refining by 2040, which would raise concentration further [IEA_NI_2040_STEPS]. The 2035 value is not yet available from the IEA Critical Minerals Data Explorer (TODO(data): team to download the explorer data to data/raw/ because iea.org blocks automated access).

Three technology shifts matter for the Client's portfolio over the next decade. Lower nickel and nickel free stainless and battery chemistries substitute for nickel in volume markets, titanium alloys substitute for nickel alloys in some corrosive uses [USGS_NI_MINE_2025], and additive manufacturing powders open new demand for nickel superalloys in engines. The alloy segment is likely to grow faster than the metal market because it follows aircraft and turbine output, and the Client should therefore plan on stable nickel supply but volatile prices (team estimate, to be quantified in the model).

### Data chain

The table links the product forms of the Client to the application, industry, geography, market size and growth. Market size values are trade based and in USD for 2024, and growth entries remain open where no source exists.

| Material | Product form | Application | Industry | Geography | Market size 2024 (export value) | Growth |
|---|---|---|---|---|---|---|
| Nickel and nickel alloys | Bar, rod and wire (HS 7505) | Turbine and engine components, fasteners, welding wire | Aerospace, energy | United States, Germany, France, United Kingdom | USD 4.98bn [CT_NI_7505_X_2024] | TODO(data): volume growth 2019 to 2024 from Comtrade time series |
| Nickel and nickel alloys | Plate, sheet and strip (HS 7506) | Heat exchangers, battery connectors, electronics | Chemical, electronics, automotive | Germany, United States, Japan, China | USD 1.95bn [CT_NI_7506_X_2024] | TODO(data) |
| Nickel and nickel alloys | Tube, pipe and fittings (HS 7507) | Process piping, downhole tubing | Oil and gas, chemical | United States, Germany, China | USD 1.72bn [CT_NI_7507_X_2024] | TODO(data) |
| Nickel and nickel alloys | Unwrought nickel (HS 7502) | Melt input for alloys and plating | All | China, Canada, Norway, Indonesia | USD 11.4bn [CT_NI_7502_X_2024] | Mine volume +5% in 2025 [USGS_NI_MINE_2025] |

### Interesting facts

On 6 February 2026 the USGS reported that Australian nickel mine output fell by about 54% in 2025, after several operators placed mines in care and maintenance owing to low prices [USGS_NI_AU_2025].

In 2025 the Philippines announced a 50 year ban on new mining permits in the province of Palawan, and its output fell by about 24% to 270 kt [USGS_NI_PH_2025].

In November 2024 Acerinox closed the Haynes International acquisition and merged it with VDM Metals into a high performance alloys division, which targets USD 71m of cost savings [ACX_HAYNES].

In the second half of 2027 ATI plans to start a fifth vacuum induction melting furnace in Monroe, North Carolina, adding 9 kt per year of superalloy melt capacity for jet engine customers [ARGUS_SUPERALLOY].

On 13 October 2026 the International Nickel Study Group moved its 2026 forecast from a 32 kt deficit to a 19 kt surplus, which shows how thin the balance has become [INSG_NI_2026].
