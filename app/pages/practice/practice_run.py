#import modules
import pandas as pd
import streamlit as st

#create title name
st.title('Exchange List')

#create dataframe
data = [
  {
    "id": "gdax",
    "name": "Coinbase Exchange",
    "year_established": 2012,
    "country": "United States",
    "description": "",
    "url": "https://www.coinbase.com",
    "image": "https://assets.coingecko.com/markets/images/23/small/Coinbase_Coin_Primary.png?1621471875",
    "has_trading_incentive": "false",
    "trust_score": 10,
    "trust_score_rank": 1,
    "trade_volume_24h_btc": 42746.17659100889,
    "trade_volume_24h_btc_normalized": 42746.17659100889
  },
  {
    "id": "kucoin",
    "name": "KuCoin",
    "year_established": 2014,
    "country": "Seychelles",
    "description": "",
    "url": "https://www.kucoin.com/",
    "image": "https://assets.coingecko.com/markets/images/61/small/kucoin.png?1640584259",
    "has_trading_incentive": "false",
    "trust_score": 10,
    "trust_score_rank": 2,
    "trade_volume_24h_btc": 18980.045863731793,
    "trade_volume_24h_btc_normalized": 18980.045863731793
  },
  {
    "id": "bybit_spot",
    "name": "Bybit",
    "year_established": 2018,
    "country": "null",
    "description": "Bybit is a cryptocurrency exchange that offers a professional platform featuring an ultra-fast matching engine, excellent customer service and multilingual community support for crypto traders of all levels. Established in March 2018, Bybit currently serves more than 10 million users and institutions offering access to over 100 assets and contracts across Spot, Futures and Options, launchpad projects, earn products, an NFT Marketplace and more. Bybit is a proud partner of Formula One racing team, Oracle Red Bull Racing, esports teams NAVI, Astralis, Alliance, Virtus.pro, Made in Brazil (MIBR), City Esports, and Oracle Red Bull Racing Esports, and association football (soccer) teams Borussia Dortmund and Avispa Fukuoka.",
    "url": "https://www.bybit.com",
    "image": "https://assets.coingecko.com/markets/images/698/small/bybit_spot.png?1629971794",
    "has_trading_incentive": "false",
    "trust_score": 10,
    "trust_score_rank": 3,
    "trade_volume_24h_btc": 13632.802846075683,
    "trade_volume_24h_btc_normalized": 13632.802846075683
  },
  {
    "id": "huobi",
    "name": "Huobi Global",
    "year_established": 2013,
    "country": "Seychelles",
    "description": "",
    "url": "https://www.huobi.com",
    "image": "https://assets.coingecko.com/markets/images/25/small/Huobi.?1655200466",
    "has_trading_incentive": "false",
    "trust_score": 10,
    "trust_score_rank": 4,
    "trade_volume_24h_btc": 11441.29535515161,
    "trade_volume_24h_btc_normalized": 11441.29535515161
  },
  {
    "id": "kraken",
    "name": "Kraken",
    "year_established": 2011,
    "country": "United States",
    "description": "",
    "url": "https://r.kraken.com/c/2223866/687155/10583",
    "image": "https://assets.coingecko.com/markets/images/29/small/kraken.jpg?1584251255",
    "has_trading_incentive": "false",
    "trust_score": 10,
    "trust_score_rank": 5,
    "trade_volume_24h_btc": 17522.950540069505,
    "trade_volume_24h_btc_normalized": 11183.842336408168
  },
  {
    "id": "crypto_com",
    "name": "Crypto.com Exchange",
    "year_established": 2019,
    "country": "Cayman Islands",
    "description": "Crypto.com Exchange is the best place to trade crypto, with deep liquidity, low fees and best execution prices, users can trade major cryptocurrencies like Bitcoin, Ethereum, and many more and receive great CRO-powered rewards",
    "url": "https://crypto.com/exchange",
    "image": "https://assets.coingecko.com/markets/images/589/small/Crypto.jpg?1629861084",
    "has_trading_incentive": "false",
    "trust_score": 10,
    "trust_score_rank": 6,
    "trade_volume_24h_btc": 10510.512054908993,
    "trade_volume_24h_btc_normalized": 10510.512054908993
  },
  {
    "id": "binance_us",
    "name": "Binance US",
    "year_established": 2019,
    "country": "United States",
    "description": "",
    "url": "https://www.binance.us/",
    "image": "https://assets.coingecko.com/markets/images/469/small/Binance.png?1568875842",
    "has_trading_incentive": "false",
    "trust_score": 10,
    "trust_score_rank": 7,
    "trade_volume_24h_btc": 5736.988665997307,
    "trade_volume_24h_btc_normalized": 5414.981910101876
  },
  {
    "id": "bitfinex",
    "name": "Bitfinex",
    "year_established": 2014,
    "country": "British Virgin Islands",
    "description": "",
    "url": "https://www.bitfinex.com",
    "image": "https://assets.coingecko.com/markets/images/4/small/BItfinex.png?1615895883",
    "has_trading_incentive": "false",
    "trust_score": 10,
    "trust_score_rank": 8,
    "trade_volume_24h_btc": 3582.1408454988023,
    "trade_volume_24h_btc_normalized": 3026.3143406866575
  },
  {
    "id": "gemini",
    "name": "Gemini",
    "year_established": 2014,
    "country": "United States",
    "description": "",
    "url": "https://gemini.sjv.io/bZ49k",
    "image": "https://assets.coingecko.com/markets/images/50/small/gemini.png?1605704107",
    "has_trading_incentive": "false",
    "trust_score": 10,
    "trust_score_rank": 9,
    "trade_volume_24h_btc": 1249.8761631673185,
    "trade_volume_24h_btc_normalized": 1249.8761631673185
  },
  {
    "id": "binance",
    "name": "Binance",
    "year_established": 2017,
    "country": "Cayman Islands",
    "description": "",
    "url": "https://www.binance.com/",
    "image": "https://assets.coingecko.com/markets/images/52/small/binance.jpg?1519353250",
    "has_trading_incentive": "false",
    "trust_score": 9,
    "trust_score_rank": 10,
    "trade_volume_24h_btc": 379630.333871581,
    "trade_volume_24h_btc_normalized": 171991.31533723217
  },
  {
    "id": "bitget",
    "name": "Bitget",
    "year_established": 2018,
    "country": "Singapore",
    "description": "",
    "url": "https://www.bitget.com/",
    "image": "https://assets.coingecko.com/markets/images/540/small/Bitget_new_logo_2.png?1630049618",
    "has_trading_incentive": "false",
    "trust_score": 9,
    "trust_score_rank": 11,
    "trade_volume_24h_btc": 20334.76471915918,
    "trade_volume_24h_btc_normalized": 16739.83223225486
  },
  {
    "id": "gate",
    "name": "Gate.io",
    "year_established": "null",
    "country": "Hong Kong",
    "description": "Gate was established in 2013, and it is the top 10 exchanges in the world in terms of authentic trading volume. It is also the first choice of over 8 million registered customers, covering 130+ countries worldwide, as we are providing the most comprehensive digital asset solutions.",
    "url": "https://gate.io/",
    "image": "https://assets.coingecko.com/markets/images/60/small/gate_io_logo1.jpg?1654596784",
    "has_trading_incentive": "false",
    "trust_score": 9,
    "trust_score_rank": 12,
    "trade_volume_24h_btc": 30230.846985258475,
    "trade_volume_24h_btc_normalized": 15868.682441707564
  },
  {
    "id": "okex",
    "name": "OKX",
    "year_established": 2013,
    "country": "Belize",
    "description": "",
    "url": "https://www.okx.com",
    "image": "https://assets.coingecko.com/markets/images/96/small/WeChat_Image_20220117220452.png?1642428377",
    "has_trading_incentive": "false",
    "trust_score": 9,
    "trust_score_rank": 13,
    "trade_volume_24h_btc": 30756.983520207083,
    "trade_volume_24h_btc_normalized": 14996.950921389644
  },
  {
    "id": "poloniex",
    "name": "Poloniex",
    "year_established": 2014,
    "country": "Seychelles",
    "description": "Poloniex was founded in January 2014 as a global cryptocurrency exchange. It provides spot trading, futures trading, staking, and various services to users in nearly 100 countries and regions with various languages available.\r\n\r\nIn 2022, Poloniex launched a brand new trading system to provide global retail and professional users with higher speed, as well as better stability and usability.",
    "url": "https://poloniex.com/",
    "image": "https://assets.coingecko.com/markets/images/37/small/poloniex.png?1663310089",
    "has_trading_incentive": "false",
    "trust_score": 9,
    "trust_score_rank": 14,
    "trade_volume_24h_btc": 2169.679714164355,
    "trade_volume_24h_btc_normalized": 2169.679714164355
  },
  {
    "id": "bitmex_spot",
    "name": "BitMEX",
    "year_established": "null",
    "country": "null",
    "description": "",
    "url": "https://www.bitmex.com/spot/",
    "image": "https://assets.coingecko.com/markets/images/866/small/bitmex.jpeg?1652794708",
    "has_trading_incentive": "false",
    "trust_score": 9,
    "trust_score_rank": 15,
    "trade_volume_24h_btc": 32.03364071135725,
    "trade_volume_24h_btc_normalized": 32.03364071135725
  },
  {
    "id": "digifinex",
    "name": "DigiFinex",
    "year_established": 2018,
    "country": "Seychelles",
    "description": "",
    "url": "https://www.digifinex.com/",
    "image": "https://assets.coingecko.com/markets/images/225/small/DF_logo.png?1594264355",
    "has_trading_incentive": "false",
    "trust_score": 8,
    "trust_score_rank": 16,
    "trade_volume_24h_btc": 37073.1766554192,
    "trade_volume_24h_btc_normalized": 26290.6053934035
  },
  {
    "id": "mxc",
    "name": "MEXC Global",
    "year_established": 2018,
    "country": "null",
    "description": "Established in April 2018, MEXC Global is one of the world’s leading digital-asset trading platforms. The core team comes from world-class enterprises and financial companies with rich experience in blockchain and financial industries.",
    "url": "https://www.mexc.com/",
    "image": "https://assets.coingecko.com/markets/images/409/small/WeChat_Image_20210622160936.png?1624349423",
    "has_trading_incentive": "false",
    "trust_score": 8,
    "trust_score_rank": 17,
    "trade_volume_24h_btc": 35919.762121113505,
    "trade_volume_24h_btc_normalized": 24943.446941390663
  },
  {
    "id": "whitebit",
    "name": "WhiteBIT",
    "year_established": 2018,
    "country": "Estonia",
    "description": "",
    "url": "https://whitebit.com",
    "image": "https://assets.coingecko.com/markets/images/418/small/whitebit_final.png?1667923522",
    "has_trading_incentive": "false",
    "trust_score": 8,
    "trust_score_rank": 18,
    "trade_volume_24h_btc": 21701.320080659734,
    "trade_volume_24h_btc_normalized": 21701.320080659734
  },
  {
    "id": "bkex",
    "name": "BKEX",
    "year_established": 2018,
    "country": "British Virgin Islands",
    "description": "",
    "url": "https://www.bkex.com/",
    "image": "https://assets.coingecko.com/markets/images/293/small/New_BKEX_logo.png?1646724631",
    "has_trading_incentive": "false",
    "trust_score": 8,
    "trust_score_rank": 19,
    "trade_volume_24h_btc": 27346.715244272546,
    "trade_volume_24h_btc_normalized": 15810.582772054142
  },
  {
    "id": "bingx",
    "name": "BingX",
    "year_established": "null",
    "country": "null",
    "description": "Founded in 2018, BingX is a crypto social trading exchange that offers spot, derivatives and copy trading services to more than 100 countries worldwide.\r\n\r\nBingX prides itself as the people's exchange by unlocking the fast-growing cryptocurrency market for everyone, connecting users with experts traders and a platform to invest in a simple, engaging and transparent way.",
    "url": "https://bingx.com/",
    "image": "https://assets.coingecko.com/markets/images/812/small/YtFwQwJr_400x400.jpg?1646056092",
    "has_trading_incentive": "false",
    "trust_score": 8,
    "trust_score_rank": 20,
    "trade_volume_24h_btc": 14685.198181792597,
    "trade_volume_24h_btc_normalized": 14685.198181792597
  },
  {
    "id": "bitmart",
    "name": "BitMart",
    "year_established": 2017,
    "country": "Cayman Islands",
    "description": "",
    "url": "https://www.bitmart.com/en",
    "image": "https://assets.coingecko.com/markets/images/239/small/Bitmart.png?1628066397",
    "has_trading_incentive": "false",
    "trust_score": 8,
    "trust_score_rank": 21,
    "trade_volume_24h_btc": 10070.774727806476,
    "trade_volume_24h_btc_normalized": 10070.774727806476
  },
  {
    "id": "btcex",
    "name": "BTCEX",
    "year_established": 2021,
    "country": "Canada",
    "description": "BTCEX is a highly extensible digital asset trading platform, which provides spot, spot leverage, futures, perpetual contracts, and USDT-settled options. In addition, it also supports multi-product portfolio margin models to improve the utilization of user funds.",
    "url": "https://www.btcex.com",
    "image": "https://assets.coingecko.com/markets/images/753/small/C8tiQdwL_400x400.jpg?1641348961",
    "has_trading_incentive": "false",
    "trust_score": 8,
    "trust_score_rank": 22,
    "trade_volume_24h_btc": 8166.90317859294,
    "trade_volume_24h_btc_normalized": 8166.90317859294
  },
  {
    "id": "phemex",
    "name": "Phemex",
    "year_established": 2019,
    "country": "Singapore",
    "description": "Launched in 2019, Phemex is a Singapore-based cryptocurrency and derivatives trading platform led by former Morgan Stanley executives. Serving around 5 million active users in over 200 countries, Phemex supports 150+ trading pairs with up to 100x leverage.\r\n\r\n-  Fee Structure: 0.1% for both maker and taker\r\n-  Contract Fee Structure: 0.01% for maker and 0.06% for taker\r\n-  Up to $100 Welcome Bonus for new users\r\n-  Earn up to 8.5% APY interest income on crypto assets\r\n-  Free academy with 450+ carefully curated articles about crypto & trading\r\n-  Security: Hierarchical Deterministic Cold Wallet System with 2-level human scrutiny offline signatures.",
    "url": "https://phemex.com/",
    "image": "https://assets.coingecko.com/markets/images/564/small/Phemex_logo_4.png?1641357471",
    "has_trading_incentive": "false",
    "trust_score": 8,
    "trust_score_rank": 23,
    "trade_volume_24h_btc": 7937.33040313981,
    "trade_volume_24h_btc_normalized": 7937.33040313981
  },
  {
    "id": "bithumb",
    "name": "Bithumb",
    "year_established": 2014,
    "country": "South Korea",
    "description": "",
    "url": "https://www.bithumb.com/",
    "image": "https://assets.coingecko.com/markets/images/6/small/bithumb_BI.png?1573104549",
    "has_trading_incentive": "false",
    "trust_score": 8,
    "trust_score_rank": 24,
    "trade_volume_24h_btc": 10883.92246058568,
    "trade_volume_24h_btc_normalized": 7332.2828324407965
  },
  {
    "id": "hotbit",
    "name": "Hotbit",
    "year_established": 2018,
    "country": "Estonia",
    "description": "Founded in 2018 and holding Estonian MTR licence, American MSB licence, an Australian AUSTRAC licence and a Canadian MSB licence，HotBit cryptocurrency exchange is known as a cryptocurrency trading platofrm that continues to develop and integrate various forms of businesses such as spot trading, financial derivatives, cryptocurrency investment and DAPP into one platform. Currently, Hotbit’s businesses covers more than 210 countries and areas. Based on its globalized and unified strategies, HotBit continues to focus on world's emerging markets such as Russia, Turkey and southeastern Asia markets, and was ranked one of the top 3 most welcomed exchanges by Russian media in 2019.",
    "url": "https://www.hotbit.io/",
    "image": "https://assets.coingecko.com/markets/images/201/small/hotbit.jpg?1531043195",
    "has_trading_incentive": "false",
    "trust_score": 8,
    "trust_score_rank": 25,
    "trade_volume_24h_btc": 4218.428608280305,
    "trade_volume_24h_btc_normalized": 4218.428608280305
  },
  {
    "id": "btcturk",
    "name": "BtcTurk PRO",
    "year_established": 2013,
    "country": "Turkey",
    "description": "",
    "url": "https://pro.btcturk.com/",
    "image": "https://assets.coingecko.com/markets/images/223/small/BTCTurk-exchange.jpg?1536726120",
    "has_trading_incentive": "false",
    "trust_score": 8,
    "trust_score_rank": 26,
    "trade_volume_24h_btc": 3553.148313031001,
    "trade_volume_24h_btc_normalized": 2816.3430000595627
  },
  {
    "id": "exmo",
    "name": "EXMO",
    "year_established": 2013,
    "country": "United Kingdom",
    "description": "",
    "url": "https://exmo.com/",
    "image": "https://assets.coingecko.com/markets/images/59/small/exmo_logo_blue.png?1662098170",
    "has_trading_incentive": "false",
    "trust_score": 8,
    "trust_score_rank": 27,
    "trade_volume_24h_btc": 2694.706503803466,
    "trade_volume_24h_btc_normalized": 2694.706503803466
  },
  {
    "id": "bitmax",
    "name": "AscendEX (BitMax)",
    "year_established": 2018,
    "country": "Singapore",
    "description": "AscendEX (formerly BitMax) is a leading global digital asset financial platform founded by a group of Wall Street quantitative trading veterans in 2018, building on core value of “Efficiency, Resilience and Transparency.” \r\n \r\nDriven by its continuous innovative product development and early-mover advantage in strategic alignment with the leading projects from DeFi ecosystem, AscendEX offers trading services across over 200 trading pairs across cash, margin, and futures products, in particular margin trading of over 50 tokens in cross-asset collateral mode and futures trading in both cross-asset and isolated margin modes.",
    "url": "https://ascendex.com/en/global-digital-asset-platform",
    "image": "https://assets.coingecko.com/markets/images/277/small/%E5%8E%9F%E8%89%B2.png?1650557355",
    "has_trading_incentive": "false",
    "trust_score": 8,
    "trust_score_rank": 28,
    "trade_volume_24h_btc": 5380.877617008565,
    "trade_volume_24h_btc_normalized": 2142.714114194671
  },
  {
    "id": "latoken",
    "name": "LATOKEN",
    "year_established": 2017,
    "country": "Cayman Islands",
    "description": "",
    "url": "https://latoken.com/",
    "image": "https://assets.coingecko.com/markets/images/124/small/LA_token.png?1605773251",
    "has_trading_incentive": "false",
    "trust_score": 8,
    "trust_score_rank": 29,
    "trade_volume_24h_btc": 2992.330563210205,
    "trade_volume_24h_btc_normalized": 2086.5038839182266
  },
  {
    "id": "dextrade",
    "name": "Dex-Trade",
    "year_established": 2019,
    "country": "Belize",
    "description": "Dex-Trade is a centralized cryptocurrency exchange founded in 2017 and registered in Belize. This is a modern space for safe and comfortable trading with minimal commissions.\r\n\r\nDex-Trade is a universal exchange for both beginners and professional traders. The minimum spread and high liquidity in order books allow you to trade efficiently with orders of any volume.\r\nAlong with global opportunities, the exchange also provides a demo trading mode for risk-free testing of your trading strategies. Our dedicated support team is online 24/7 to assist you with any questions.\r\n\r\nYou can learn more about Dex-Trade on the website.\r\nhttps://dex-trade.com/info/about\r\n\r\nIf you are looking for listing and promotion options with Dex-Trade please visit our listing page and a personal manager will help you to utilize our proven tools and intelligent market-making system to engage with the vast exchange community in the best possible way. https://dex-trade.com/listing",
    "url": "https://dex-trade.com/",
    "image": "https://assets.coingecko.com/markets/images/380/small/Dex-Trade_logo_new.png?1599629803",
    "has_trading_incentive": "false",
    "trust_score": 7,
    "trust_score_rank": 30,
    "trade_volume_24h_btc": 4978.606867934489,
    "trade_volume_24h_btc_normalized": 1893.0125220373045
  },
  {
    "id": "coinex",
    "name": "CoinEx",
    "year_established": 2017,
    "country": "United Kingdom",
    "description": "",
    "url": "https://www.coinex.com/",
    "image": "https://assets.coingecko.com/markets/images/135/small/coinex.jpg?1527737297",
    "has_trading_incentive": "false",
    "trust_score": 8,
    "trust_score_rank": 31,
    "trade_volume_24h_btc": 1641.6205243603436,
    "trade_volume_24h_btc_normalized": 1641.6205243603436
  },
  {
    "id": "bitkub",
    "name": "Bitkub",
    "year_established": 2018,
    "country": "Thailand",
    "description": "",
    "url": "https://www.bitkub.com",
    "image": "https://assets.coingecko.com/markets/images/249/small/bitkub.png?1537180687",
    "has_trading_incentive": "false",
    "trust_score": 8,
    "trust_score_rank": 32,
    "trade_volume_24h_btc": 1434.8376106543997,
    "trade_volume_24h_btc_normalized": 1434.8376106543997
  },
  {
    "id": "coinstore",
    "name": "Coinstore",
    "year_established": 2020,
    "country": "Singapore",
    "description": "Coinstore was founded in 2020. There are 180 employees worldwide distributed mainly in Asia, Europe, and the Middle East, serving more than 1,500,000 registered users in 175 countries. Coinstore provides global users with fast and smooth cryptocurrency trading services, derivatives business, OTC services, and NFT services. Coinstore Labs provides project owners with integrated solutions of “technology development, compliance counseling, integrated marketing, community operations, investment incubation” and much more.\r\n\r\nCoinstore supports 102 spot pairs and 34 futures pairs. All features are available on Coinstore’s mobile app for iOS and Android, and on desktop.",
    "url": "https://www.coinstore.com/#/",
    "image": "https://assets.coingecko.com/markets/images/747/small/coinstore.jpeg?1639530357",
    "has_trading_incentive": "false",
    "trust_score": 8,
    "trust_score_rank": 33,
    "trade_volume_24h_btc": 6266.453837987336,
    "trade_volume_24h_btc_normalized": 723.1539532893588
  },
  {
    "id": "bitflyer",
    "name": "bitFlyer",
    "year_established": 2014,
    "country": "Japan",
    "description": "",
    "url": "https://bitflyereuropesa.pxf.io/c/2223866/858437/11990",
    "image": "https://assets.coingecko.com/markets/images/5/small/bitFlyer-logo.png?1643256033",
    "has_trading_incentive": "false",
    "trust_score": 8,
    "trust_score_rank": 34,
    "trade_volume_24h_btc": 595.6875594981332,
    "trade_volume_24h_btc_normalized": 595.6875594981332
  },
  {
    "id": "max_maicoin",
    "name": "Max Maicoin",
    "year_established": "null",
    "country": "Taiwan",
    "description": "",
    "url": "https://max.maicoin.com",
    "image": "https://assets.coingecko.com/markets/images/218/small/max.jpg?1533888641",
    "has_trading_incentive": "false",
    "trust_score": 8,
    "trust_score_rank": 35,
    "trade_volume_24h_btc": 679.1985150334997,
    "trade_volume_24h_btc_normalized": 679.1985150334997
  },
  {
    "id": "bitso",
    "name": "Bitso",
    "year_established": 2014,
    "country": "Mexico",
    "description": "",
    "url": "https://bitso.com",
    "image": "https://assets.coingecko.com/markets/images/8/small/Bitso-icon-dark.png?1581909156",
    "has_trading_incentive": "false",
    "trust_score": 8,
    "trust_score_rank": 36,
    "trade_volume_24h_btc": 656.3857556651238,
    "trade_volume_24h_btc_normalized": 656.3857556651238
  },
  {
    "id": "bittrex",
    "name": "Bittrex",
    "year_established": 2014,
    "country": "United States",
    "description": "",
    "url": "https://bittrex.com/",
    "image": "https://assets.coingecko.com/markets/images/10/small/BG-color-250x250_icon.png?1596167574",
    "has_trading_incentive": "false",
    "trust_score": 8,
    "trust_score_rank": 37,
    "trade_volume_24h_btc": 543.9581189996379,
    "trade_volume_24h_btc_normalized": 543.9581189996379
  },
  {
    "id": "bitbank",
    "name": "Bitbank",
    "year_established": 2016,
    "country": "Japan",
    "description": "",
    "url": "https://bitbank.cc/",
    "image": "https://assets.coingecko.com/markets/images/122/small/bitbank.jpg?1521186278",
    "has_trading_incentive": "false",
    "trust_score": 8,
    "trust_score_rank": 38,
    "trade_volume_24h_btc": 385.5767556315261,
    "trade_volume_24h_btc_normalized": 385.5767556315261
  },
  {
    "id": "nominex",
    "name": "Nominex",
    "year_established": 2019,
    "country": "Seychelles",
    "description": "New trading platform for convenient trading experience with low fees and numerous instruments. \r\n\r\nAbsolutely unique affiliate program that allows to earn from an infinite number of referral levels, compared to 2-3 levels at all other exchanges. \r\n\r\nA unique model for the free 2 phases distribution of the native NMX token.\r\n\r\nAdvanced Trading Instruments – using Stop, Stop Limit, Trailing Stop, Scaled and other types of orders brings some kind of trading automation without the need to develop a trading bot, which allows to easily get more profit while trading.",
    "url": "https://www.nominex.io",
    "image": "https://assets.coingecko.com/markets/images/530/small/logo-200x200.png?1587543672",
    "has_trading_incentive": "false",
    "trust_score": 8,
    "trust_score_rank": 39,
    "trade_volume_24h_btc": 501.62527639037853,
    "trade_volume_24h_btc_normalized": 333.12069536442726
  },
  {
    "id": "indodax",
    "name": "Indodax",
    "year_established": 2014,
    "country": "Indonesia",
    "description": "",
    "url": "https://indodax.com",
    "image": "https://assets.coingecko.com/markets/images/3/small/logogram-Indodax-new-_JPG_format.jpg?1580974378",
    "has_trading_incentive": "false",
    "trust_score": 8,
    "trust_score_rank": 40,
    "trade_volume_24h_btc": 310.48724792583704,
    "trade_volume_24h_btc_normalized": 310.48724792583704
  },
  {
    "id": "luno",
    "name": "Luno",
    "year_established": 2013,
    "country": "Singapore",
    "description": "",
    "url": "https://www.luno.com",
    "image": "https://assets.coingecko.com/markets/images/33/small/luno.jpg?1519996997",
    "has_trading_incentive": "false",
    "trust_score": 8,
    "trust_score_rank": 41,
    "trade_volume_24h_btc": 299.8661256710824,
    "trade_volume_24h_btc_normalized": 299.8661256710824
  },
  {
    "id": "itbit",
    "name": "itBit",
    "year_established": 2013,
    "country": "United States",
    "description": "null",
    "url": "https://www.itbit.com/",
    "image": "https://assets.coingecko.com/markets/images/26/small/itbit.png?1519810172",
    "has_trading_incentive": "false",
    "trust_score": 8,
    "trust_score_rank": 42,
    "trade_volume_24h_btc": 279.0358031174002,
    "trade_volume_24h_btc_normalized": 279.0358031174002
  },
  {
    "id": "wootrade",
    "name": "WOO Network",
    "year_established": 2019,
    "country": "null",
    "description": "WOO Network is a deep liquidity network connecting traders, exchanges, institutions, and DeFi platforms with democratized access to the best-in-class liquidity and trading execution at lower or zero cost. Its flagship, WOO X, is a professional trading platform featuring customizable modules and lower to zero fees complete with deep liquidity. WOO Network was founded by Kronos Research, a quantitative trading firm generating $5-10B in daily volume.",
    "url": "https://woo.org/",
    "image": "https://assets.coingecko.com/markets/images/683/small/wootrade.jpg?1624621149",
    "has_trading_incentive": "false",
    "trust_score": 8,
    "trust_score_rank": 43,
    "trade_volume_24h_btc": 851.8658711553055,
    "trade_volume_24h_btc_normalized": 268.6621990718181
  },
  {
    "id": "okcoin",
    "name": "Okcoin",
    "year_established": 2013,
    "country": "United States",
    "description": "About OKCoin:\r\nOKCoin is one of the largest and most trusted fiat-to-crypto trading platforms in the world. Founded in 2013, OKCoin offers advanced features for crypto beginners and high-volume traders alike, enabling users in 184 countries worldwide to exchange US dollars and the euro for Bitcoin, Tethers, USDK, Bitcoin Cash, Ethereum, Ethereum Classic, Decred, EOS, Litecoin, XRP, Cardano, 0x, Stellar, Zcash, TRX, and other digital assets. As a registered Money Services Business (MSB) with the Financial Crimes Enforcement Network (FinCEN) and a Virtual Financial Asset Act (VFAA) exchange with a transitory provision permissioned by the Malta Financial Services Authority, OKCoin is on a mission to make digital assets accessible to the world while complying with the highest of regulatory standards. For more information, visit www.okcoin.com. ",
    "url": "https://www.okcoin.com/",
    "image": "https://assets.coingecko.com/markets/images/415/small/okcoin_Logomark_SatoshiBlack.png?1619574335",
    "has_trading_incentive": "false",
    "trust_score": 8,
    "trust_score_rank": 44,
    "trade_volume_24h_btc": 212.39522465796514,
    "trade_volume_24h_btc_normalized": 212.39522465796514
  },
  {
    "id": "kuna",
    "name": "Kuna Exchange",
    "year_established":"null",
    "country": "United Kingdom",
    "description": "",
    "url": "https://kuna.io/",
    "image": "https://assets.coingecko.com/markets/images/97/small/kuna_exchange.png?1545126178",
    "has_trading_incentive": "false",
    "trust_score": 8,
    "trust_score_rank": 45,
    "trade_volume_24h_btc": 28.891147402648546,
    "trade_volume_24h_btc_normalized": 28.891147402648546
  },
  {
    "id": "delta_spot",
    "name": "Delta Exchange",
    "year_established": "null",
    "country": "null",
    "description": "",
    "url": "https://www.delta.exchange/app/spot/trade/",
    "image": "https://assets.coingecko.com/markets/images/642/small/delta_spot.jpg?1617283005",
    "has_trading_incentive": "false",
    "trust_score": 8,
    "trust_score_rank": 46,
    "trade_volume_24h_btc": 18.728455023026456,
    "trade_volume_24h_btc_normalized": 18.728455023026456
  },
  {
    "id": "coin_metro",
    "name": "Coinmetro",
    "year_established": 2018,
    "country": "Estonia",
    "description": "",
    "url": "https://coinmetro.com/",
    "image": "https://assets.coingecko.com/markets/images/386/small/Coinmetro_Exchange_Logo_%282%29.png?1646280101",
    "has_trading_incentive": "false",
    "trust_score": 8,
    "trust_score_rank": 47,
    "trade_volume_24h_btc": 17.042882303315487,
    "trade_volume_24h_btc_normalized": 17.042882303315487
  },
  {
    "id": "nice_hash",
    "name": "NiceHash",
    "year_established": "null",
    "country": "Slovenia",
    "description": "",
    "url": "https://www.nicehash.com",
    "image": "https://assets.coingecko.com/markets/images/546/small/logo_small_light.png?1637836622",
    "has_trading_incentive": "false",
    "trust_score": 8,
    "trust_score_rank": 48,
    "trade_volume_24h_btc": 8.01454461487659,
    "trade_volume_24h_btc_normalized": 8.01454461487659
  },
  {
    "id": "lbank",
    "name": "LBank",
    "year_established": 2017,
    "country": "British Virgin Islands",
    "description": "LBank Exchange, founded in 2015, is a global trading platform for various crypto assets. LBank Exchange provides its users with crypto trading, specialized financial derivatives, and professional asset management services. It has become one of the most popular and trusted crypto trading platforms with over 7 million users from now more than 210 regions around the world.",
    "url": "https://www.lbank.info/",
    "image": "https://assets.coingecko.com/markets/images/118/small/LBank_logo.png?1666234663",
    "has_trading_incentive": "false",
    "trust_score": 7,
    "trust_score_rank": 49,
    "trade_volume_24h_btc": 69950.8498690276,
    "trade_volume_24h_btc_normalized": 24552.087055818058
  },
  {
    "id": "coinsbit",
    "name": "Coinsbit",
    "year_established": "null",
    "country": "Estonia",
    "description": "",
    "url": "https://coinsbit.io/",
    "image": "https://assets.coingecko.com/markets/images/267/small/Coinsbit.png?1605153697",
    "has_trading_incentive": "false",
    "trust_score": 7,
    "trust_score_rank": 50,
    "trade_volume_24h_btc": 16803.917353551402,
    "trade_volume_24h_btc_normalized": 16803.917353551402
  },
  {
    "id": "upbit",
    "name": "Upbit",
    "year_established": 2017,
    "country": "South Korea",
    "description": "null",
    "url": "https://upbit.com",
    "image": "https://assets.coingecko.com/markets/images/117/small/upbit.png?1520388800",
    "has_trading_incentive": "false",
    "trust_score": 7,
    "trust_score_rank": 51,
    "trade_volume_24h_btc": 107274.49929976476,
    "trade_volume_24h_btc_normalized": 14802.773780510817
  },
  {
    "id": "bitrue",
    "name": "Bitrue",
    "year_established": 2018,
    "country": "Singapore",
    "description": "",
    "url": "https://www.bitrue.com/",
    "image": "https://assets.coingecko.com/markets/images/254/small/unnamed_%281%29.png?1656295820",
    "has_trading_incentive": "false",
    "trust_score": 7,
    "trust_score_rank": 52,
    "trade_volume_24h_btc": 73475.64277141957,
    "trade_volume_24h_btc_normalized": 7037.045514822628
  },
  {
    "id": "bigone",
    "name": "BigONE",
    "year_established": 2017,
    "country": "Seychelles",
    "description": "",
    "url": "https://bigone.com",
    "image": "https://assets.coingecko.com/markets/images/100/small/qcFFufEY_400x400.jpg?1561103345",
    "has_trading_incentive": "false",
    "trust_score": 7,
    "trust_score_rank": 53,
    "trade_volume_24h_btc": 14169.531491266041,
    "trade_volume_24h_btc_normalized": 5122.594122457758
  },
  {
    "id": "p2pb2b",
    "name": "P2B",
    "year_established": 2018,
    "country": "Lithuania",
    "description": "P2B Cryptocurrency Exchange is one of the biggest European digital assets exchanges that has successfully operated for over 5 years. It is now the most trusted platform offering the best go-to-market experience for crypto users and projects.\r\n\r\nThe platform tops the most trusted ratings worldwide - CoinMarketCap and CoinGecko - and permanently improves its position. We assure the safety of the trading activities, being ranked in the TOP-12 in Cer.Live security rate. \r\n\r\nThe users can easily explore the mature crypto market by investing in a wide variety of liquid tokens, buying cryptocurrencies with bank cards (via Simplex, Moon Pay, Koinal) and using attractive discounts or bonuses during fundraising campaigns. You can also choose the amount of your commission,  - use the level commission to raise your account opportunities and make your trading more profitable. \r\n\r\nBecome a part of the prosperous P2B community - #1 place to be in crypto.\r\nGet your exciting trading experience with 24/7 support, and gain quickly and securely.\r\n",
    "url": "https://p2pb2b.com/",
    "image": "https://assets.coingecko.com/markets/images/251/small/ow0xng56_400x400.jpeg?1664939403",
    "has_trading_incentive": "false",
    "trust_score": 7,
    "trust_score_rank": 54,
    "trade_volume_24h_btc": 25496.404869665323,
    "trade_volume_24h_btc_normalized": 4931.810405240973
  },
  {
    "id": "bitstamp",
    "name": "Bitstamp",
    "year_established": 2013,
    "country": "United Kingdom",
    "description": "",
    "url": "https://links.bitstamp.net/c/2223866/1100037/14006",
    "image": "https://assets.coingecko.com/markets/images/9/small/bitstamp.jpg?1519627979",
    "has_trading_incentive": "false",
    "trust_score": 7,
    "trust_score_rank": 55,
    "trade_volume_24h_btc": 3506.614393928459,
    "trade_volume_24h_btc_normalized": 2436.9866117054407
  },
  {
    "id": "bitcoin_com",
    "name": "FMFW.io",
    "year_established": 2019,
    "country": "Bahamas",
    "description": "The mission of FMFW.io is to empower people from all over the world to trade cryptocurrencies with ease and confidence, from first-time traders to advanced trading professionals. With high liquidity, 24/7 multilingual support and dozens of trading pairs, complemented with a high level of security, we offer an attractive platform for trading any cryptocurrency. Within one year since launch, on average, our exchange has been visited by more than 500K active traders per month, and this number continues to grow as you read this sentence. \r\n\r\nKey Features:\r\n\r\n- Enjoy more than 130 available trading pairs\r\n- Cutting-edge matching engine technologies\r\n- Up 5x and 10x leverage for more than 29 markets\r\n- Deep liquidity\r\n- User-friendly trading terminal\r\n- Tight spreads\r\n- Consistent trading competitions and giveaways",
    "url": "https://fmfw.io/",
    "image": "https://assets.coingecko.com/markets/images/467/small/fmfw.png?1635491491",
    "has_trading_incentive": "false",
    "trust_score": 7,
    "trust_score_rank": 56,
    "trade_volume_24h_btc": 35212.81016571983,
    "trade_volume_24h_btc_normalized": 865.947329183882
  },
  {
    "id": "bitbns",
    "name": "BitBNS",
    "year_established": 2017,
    "country": "Estonia",
    "description": "",
    "url": "https://ref.bitbns.com/",
    "image": "https://assets.coingecko.com/markets/images/541/small/HS7eNJdt_400x400.jpg?1592294824",
    "has_trading_incentive": "false",
    "trust_score": 7,
    "trust_score_rank": 57,
    "trade_volume_24h_btc": 785.4399468404282,
    "trade_volume_24h_btc_normalized": 664.4347177826533
  },
  {
    "id": "bullish_com",
    "name": "Bullish",
    "year_established": 2021,
    "country": "Gibraltar",
    "description": "",
    "url": "https://bullish.com/",
    "image": "https://assets.coingecko.com/markets/images/905/small/bullish_com.png?1655198360",
    "has_trading_incentive": "false",
    "trust_score": 7,
    "trust_score_rank": 58,
    "trade_volume_24h_btc": 1889.684517433686,
    "trade_volume_24h_btc_normalized": 461.8461427812656
  },
  {
    "id": "bitazza",
    "name": "Bitazza",
    "year_established": 2021,
    "country": "null",
    "description": "Bitazza is ASEAN's locally-based digital asset platform. ",
    "url": "https://trade.bitazza.com/gl/exchange/",
    "image": "https://assets.coingecko.com/markets/images/837/small/btzlogo200x200_darkgreen.png?1648702264",
    "has_trading_incentive": "false",
    "trust_score": 7,
    "trust_score_rank": 59,
    "trade_volume_24h_btc": 353.8533785302884,
    "trade_volume_24h_btc_normalized": 353.8533785302884
  },
  {
    "id": "gmo_japan",
    "name": "GMO Japan",
    "year_established": "null",
    "country": "Japan",
    "description": "",
    "url": "https://coin.z.com/jp/",
    "image": "https://assets.coingecko.com/markets/images/430/small/gmo_z_com.png?1561112572",
    "has_trading_incentive": "false",
    "trust_score": 7,
    "trust_score_rank": 60,
    "trade_volume_24h_btc": 178.40957091130844,
    "trade_volume_24h_btc_normalized": 178.40957091130844
  },
  {
    "id": "mercado_bitcoin",
    "name": "Mercado Bitcoin",
    "year_established": 2013,
    "country": "Brazil",
    "description": "",
    "url": "https://www.mercadobitcoin.com.br/",
    "image": "https://assets.coingecko.com/markets/images/34/small/logo_MB_hexagono.png?1657255217",
    "has_trading_incentive": "false",
    "trust_score": 7,
    "trust_score_rank": 61,
    "trade_volume_24h_btc": 134.60166710524115,
    "trade_volume_24h_btc_normalized": 134.60166710524115
  },
  {
    "id": "cex",
    "name": "CEX.IO",
    "year_established": 2013,
    "country": "United Kingdom",
    "description": "",
    "url": "https://cex.io/",
    "image": "https://assets.coingecko.com/markets/images/56/small/main-icon.png?1617267530",
    "has_trading_incentive": "false",
    "trust_score": 7,
    "trust_score_rank": 62,
    "trade_volume_24h_btc": 125.23198496133111,
    "trade_volume_24h_btc_normalized": 125.23198496133111
  },
  {
    "id": "independent_reserve",
    "name": "Independent Reserve",
    "year_established": 2013,
    "country": "Australia",
    "description": "",
    "url": "https://www.independentreserve.com/",
    "image": "https://assets.coingecko.com/markets/images/389/small/x_V5Jquo_400x400.png?1556071437",
    "has_trading_incentive": "false",
    "trust_score": 7,
    "trust_score_rank": 63,
    "trade_volume_24h_btc": 104.79207276059297,
    "trade_volume_24h_btc_normalized": 104.79207276059297
  },
  {
    "id": "blockchain_com",
    "name": "Blockchain.com",
    "year_established": 2012,
    "country": "United Kingdom",
    "description": "",
    "url": "https://www.blockchain.com/",
    "image": "https://assets.coingecko.com/markets/images/613/small/unnamedddd.png?1610503741",
    "has_trading_incentive": "false",
    "trust_score": 7,
    "trust_score_rank": 64,
    "trade_volume_24h_btc": 104.20164988647869,
    "trade_volume_24h_btc_normalized": 104.20164988647869
  },
  {
    "id": "maiar",
    "name": "Maiar",
    "year_established": 2021,
    "country": "null",
    "description": "The Maiar Decentralized Exchange (DEX) is the Automated Market Maker (AMM), rearchitecting some of the key elements to build a product that can leverage the entire \r\nperformance of the Elrond architecture, to offer global, near-instant, inexpensive transactions among an expanding suite of assets.\r\n\r\nThe essence of current versions of automated market makers is best expressed through the constant product equation: x * y = k\r\n\r\nBased on it, if a swap pool owns some units of token x and some units of token y, it prices trades so that the quantities of x and y resulting after the trade, when multiplied, are equal to a fixed constant, k.\r\n\r\nBut current AMM performance could be significantly improved by rebuilding them on \r\nvastly more scalable architectures.\r\n\r\nBy reimagining an automated market maker on top of a highly scalable architecture that is high bandwidth, low latency, and inexpensive, the performance of the swap processes can be drastically improved. With significantly better performance, the scope of AMMs can be rapidly expanded, giving birth to new mark",
    "url": "https://maiar.exchange/",
    "image": "https://assets.coingecko.com/markets/images/741/small/maiar-dex.png?1638433160",
    "has_trading_incentive": "false",
    "trust_score": 6,
    "trust_score_rank": 65,
    "trade_volume_24h_btc": 97.08939113741887,
    "trade_volume_24h_btc_normalized": 97.08939113741887
  },
  {
    "id": "bitpanda",
    "name": "Bitpanda Pro",
    "year_established": 2019,
    "country": "Austria",
    "description": "",
    "url": "https://exchange.bitpanda.com",
    "image": "https://assets.coingecko.com/markets/images/474/small/appicon-ios-pro.png?1622626638",
    "has_trading_incentive": "false",
    "trust_score": 7,
    "trust_score_rank": 66,
    "trade_volume_24h_btc": 90.85478732095613,
    "trade_volume_24h_btc_normalized": 90.85478732095613
  },
  {
    "id": "bitopro",
    "name": "BitoPro",
    "year_established": 2018,
    "country": "Taiwan",
    "description": "",
    "url": "https://www.bitopro.com/",
    "image": "https://assets.coingecko.com/markets/images/358/small/bitopro_coingecko_250x250_%281%29.png?1575884378",
    "has_trading_incentive": "false",
    "trust_score": 8,
    "trust_score_rank": 67,
    "trade_volume_24h_btc": 80.08488922483897,
    "trade_volume_24h_btc_normalized": 80.08488922483897
  },
  {
    "id": "korbit",
    "name": "Korbit",
    "year_established": 2013,
    "country": "South Korea",
    "description": "",
    "url": "https://www.korbit.co.kr/",
    "image": "https://assets.coingecko.com/markets/images/28/small/korbit-logo.png?1584091827",
    "has_trading_incentive": "false",
    "trust_score": 7,
    "trust_score_rank": 68,
    "trade_volume_24h_btc": 73.0047805105558,
    "trade_volume_24h_btc_normalized": 73.0047805105558
  },
  {
    "id": "emirex",
    "name": "Emirex",
    "year_established": 2014,
    "country": "United Arab Emirates",
    "description": "Emirex was launched in 2014 and became a network of enterprises using blockchain technology to ease asset trading and completely disrupt how people use crypto. Dubai, UAE, is a dynamic destination for Eastern and Western companies, and it's where Emirex helped develop a crypto culture. Emirex is an exchange and marketplace for trading digital assets that improve economic freedom by developing censorship-resistant public networks. Emirex has grown tremendously with its business and is eager to develop even more.\r\n \r\nThe EMRX Token\r\n\r\nEmirex offers B2C, B2B, and B2E payments and boasts over 20,000 active clients and a $10 million monthly income after growing 40-fold in a year. The exchange has over $25 million in daily volume. EMRX, the exchange's token, quadrupled last year due to ecosystem integration and active use. As the Emirex Ecosystem's native token, EMRX is used for listing fees for tokenized assets, buy/sell transaction fees, custody and servicing fees, and commission and partner incentive programs. You can also stake EMRX and other tokens to earn Ultra High APR on your tokens and withdraw anytime. Staking is your gateway to passive crypto income! Emirex also launched a tokenization section to help revolutionize the real estate market as well.\r\n\r\nQuick, Simple, Secure\r\n\r\nEmirex is a platform that simplifies, quickens, and secures digital asset trading. Newbies can trade digital assets easily as Emirex offers non-tech users secure, easy, compliant digital asset access on a  professional trading platform supporting AED, USD, and EUR FIATs. Emirex can process 1,000,000 orders per second. Experience speedy order books, extensive trade history, endless markets, and market depth, and make spot, margin, and futures order types. The Emirex Group offers top-tier financial services to bridge the gap between the current and future economic systems.\r\n\r\nWhy You Should Use Emirex\r\n\r\nEmirex simplifies crypto access and makes its site user-friendly. Emirex's UI is straightforward. A knowledge base guides newcomers through exchange operations. Emirex offers deep liquidity, hundreds of token pairs, and multiple trading orders. You won't get lost with Emirex's security, the convenience of access, and helpful experts. Receive and send tokens without an intermediary. Copy or Social trading lets you imitate the top traders' trades, and Emirex's referral code earns you up to 7% on your friend's and family's transactions.\r\n\r\nTrade Whenever, Wherever\r\n\r\nEmirex provides the most incredible trading experience, allowing you to trade on your terms. We want to help you pleasantly attain your financial goals. Emirex builds crypto economic infrastructure based on user experience and accessibility. The Emirex team launched the Emirex Android to offer all website features in your pocket, including easy bitcoin buying, selling, and trading and 24/7 support with one tap. Emirex makes crypto investment so easy that you'll want to do it all the time!\r\n\r\nSign Up and Keep Up\r\n \r\nSign up now to benefit from Emirex's low to 0% fees. Emirex offers Africa, Asia, and Europe exposure to digital assets and crypto and connects the Middle East with those markets. Decentralization and transparency in blockchain can encourage global value mobility and societal well-being, which is why emirex is dedicated to the digital economy.",
    "url": "https://www.emirex.com/",
    "image": "https://assets.coingecko.com/markets/images/592/small/Emirex.png?1602067691",
    "has_trading_incentive": "false" ,
    "trust_score": 7,
    "trust_score_rank": 69,
    "trade_volume_24h_btc": 50.08906883228179,
    "trade_volume_24h_btc_normalized": 21.339550610628255
  },
  {
    "id": "coinlist",
    "name": "Coinlist",
    "year_established": 2020,
    "country": "United States",
    "description": "CoinList is where early adopters invest and trade in high quality crypto assets before they land on other exchanges, including Filecoin, Celo, Solana, Nervos, Dfinity, Algorand, and many more.\r\n\r\nCoinList Trade is a fully-featured crypto spot exchange, built on battle-tested infrastructure and backed by some of the biggest names in the space. It will support the best new cryptoassets early in their lifecycles, as well as, most large cap established crypto. ",
    "url": "https://pro.coinlist.co/",
    "image": "https://assets.coingecko.com/markets/images/587/small/CoinList.png?1601540662",
    "has_trading_incentive": "false",
    "trust_score": 6,
    "trust_score_rank": 70,
    "trade_volume_24h_btc": 20.562880241811534,
    "trade_volume_24h_btc_normalized": 20.562880241811534
  },
  {
    "id": "zaif",
    "name": "Zaif",
    "year_established": 2015,
    "country": "Japan",
    "description": "null",
    "url": "https://zaif.jp/",
    "image": "https://assets.coingecko.com/markets/images/99/small/zaif.png?1519627467",
    "has_trading_incentive": "null",
    "trust_score": 7,
    "trust_score_rank": 71,
    "trade_volume_24h_btc": 18.32591498003682,
    "trade_volume_24h_btc_normalized": 18.32591498003682
  },
  {
    "id": "xt",
    "name": "XT.COM",
    "year_established": 2018,
    "country": "Seychelles",
    "description": "By consistently expanding its ecosystem, XT.COM is dedicated to providing users with the most secure, trusted, and hassle-free digital asset trading services. Our exchange is built from a desire to give everyone access to digital assets regardless where you are. \r\n\r\nFounded in 2018, XT.COM now serves more than 6 million registered users, over 500,000+ monthly active users and 40+ million users in the ecosystem. Covering a rich variety of  trading categories together with a NFT aggregated marketplace,  our platform strives to cater to its large user base by providing a secure, trusted and intuitive trading experience.\r\n\r\nAs the world’s first social-infused digital assets trading platform, XT.COM also supports social networking platform based transactions to make our crypto services more accessible to users all over the world. Furthermore, to ensure optimal data integrity and security, we see user security as our top priority at XT.COM. ",
    "url": "https://www.xt.com/",
    "image": "https://assets.coingecko.com/markets/images/404/small/logo400x400.png?1575881839",
    "has_trading_incentive": "false",
    "trust_score": 6,
    "trust_score_rank": 72,
    "trade_volume_24h_btc": 87211.09387879689,
    "trade_volume_24h_btc_normalized": 14692.353902827674
  },
  {
    "id": "bitforex",
    "name": "Bitforex",
    "year_established": 2018,
    "country": "Seychelles",
    "description": "",
    "url": "https://www.bitforex.com/",
    "image": "https://assets.coingecko.com/markets/images/214/small/BitForex-Logo.png?1573808227",
    "has_trading_incentive": "false",
    "trust_score": 6,
    "trust_score_rank": 73,
    "trade_volume_24h_btc": 36574.54887547172,
    "trade_volume_24h_btc_normalized": 9775.316123103612
  },
  {
    "id": "pancakeswap_new",
    "name": "PancakeSwap (v2)",
    "year_established": 2020,
    "country": "null",
    "description": "",
    "url": "https://pancakeswap.finance",
    "image": "https://assets.coingecko.com/markets/images/687/small/pancakeswap.jpeg?1626060212",
    "has_trading_incentive": "false",
    "trust_score": 6,
    "trust_score_rank": 74,
    "trade_volume_24h_btc": 9589.99988193983,
    "trade_volume_24h_btc_normalized": 9589.99988193983
  },
  {
    "id": "bitvavo",
    "name": "Bitvavo",
    "year_established": 2018,
    "country": "Netherlands",
    "description": "",
    "url": "https://bitvavo.com/en",
    "image": "https://assets.coingecko.com/markets/images/714/small/bitvavo-mark-square-black.png?1633688872",
    "has_trading_incentive": "false",
    "trust_score": 6,
    "trust_score_rank": 75,
    "trade_volume_24h_btc": 2774.093303928302,
    "trade_volume_24h_btc_normalized": 2774.093303928302
  },
  {
    "id": "uniswap_v3_polygon_pos",
    "name": "Uniswap (Polygon)",
    "year_established": 2021,
    "country": "null",
    "description": "",
    "url": "https://app.uniswap.org/#/swap",
    "image": "https://assets.coingecko.com/markets/images/752/small/uniswap-polygon.png?1640329417",
    "has_trading_incentive": "false",
    "trust_score": 6,
    "trust_score_rank": 76,
    "trade_volume_24h_btc": 2477.7950156547513,
    "trade_volume_24h_btc_normalized": 2477.7950156547513
  },
  {
    "id": "uniswap_v2",
    "name": "Uniswap (v2)",
    "year_established": 2018,
    "country": "null",
    "description": "",
    "url": "https://app.uniswap.org/#/swap?use=V2",
    "image": "https://assets.coingecko.com/markets/images/535/small/256x256_Black-1.png?1590893262",
    "has_trading_incentive": "false",
    "trust_score": 6,
    "trust_score_rank": 77,
    "trade_volume_24h_btc": 2485.655881839658,
    "trade_volume_24h_btc_normalized": 2485.655881839658
  },
  {
    "id": "paribu",
    "name": "Paribu",
    "year_established": "null",
    "country": "Turkey",
    "description": "null",
    "url": "https://www.paribu.com/",
    "image": "https://assets.coingecko.com/markets/images/136/small/paribu.jpg?1527734779",
    "has_trading_incentive": "null",
    "trust_score": 6,
    "trust_score_rank": 78,
    "trade_volume_24h_btc": 4894.928691739843,
    "trade_volume_24h_btc_normalized": 2273.040500858339
  },
  {
    "id": "coinone",
    "name": "Coinone",
    "year_established": 2016,
    "country": "South Korea",
    "description": "",
    "url": "https://coinone.co.kr/",
    "image": "https://assets.coingecko.com/markets/images/20/small/coinone_circle_500x500.png?1606460853",
    "has_trading_incentive": "false",
    "trust_score": 6,
    "trust_score_rank": 79,
    "trade_volume_24h_btc": 2712.730544129105,
    "trade_volume_24h_btc_normalized": 1770.180044492107
  },
  {
    "id": "uniswap_v3_arbitrum",
    "name": "Uniswap (Arbitrum One)",
    "year_established": "null",
    "country": "null",
    "description": "",
    "url": "https://app.uniswap.org/#/swap",
    "image": "https://assets.coingecko.com/markets/images/702/small/uniswap-v3.png?1631616149",
    "has_trading_incentive": "false",
    "trust_score": 5,
    "trust_score_rank": 80,
    "trade_volume_24h_btc": 1343.0347181305776,
    "trade_volume_24h_btc_normalized": 1343.0347181305776
  },
  {
    "id": "uniswap_v3_optimism",
    "name": "Uniswap (Optimism)",
    "year_established": "null",
    "country": "null",
    "description": "",
    "url": "https://app.uniswap.org/#/swap",
    "image": "https://assets.coingecko.com/markets/images/725/small/uniswap-v3.png?1634896204",
    "has_trading_incentive": "false",
    "trust_score": 6,
    "trust_score_rank": 81,
    "trade_volume_24h_btc": 1302.455538703287,
    "trade_volume_24h_btc_normalized": 1302.455538703287
  },
  {
    "id": "btse",
    "name": "BTSE",
    "year_established": 2018,
    "country": "British Virgin Islands",
    "description": "BTSE is a leading digital asset exchange that empowers users by offering a simple and secure way to trade. Its growing suite of financial services is designed to bridge traditional finance with digital assets solutions. BTSE's innovative technology offers a set of digital financial solutions featuring multi-currency spot and derivatives trading, in addition to NFT and exchange white labels, over-the-counter (OTC) trading, asset management, and payment gateways. Additionally, BTSE provides an all-in-one order book, strict security protocols, an insurance fund, cold storage for more than 99% of assets and no withdrawal limits on over 12 fiat currencies and 100 cryptocurrencies.",
    "url": "https://www.btse.com/",
    "image": "https://assets.coingecko.com/markets/images/464/small/BTSE.jpg?1568012415",
    "has_trading_incentive": "false",
    "trust_score": 6,
    "trust_score_rank": 82,
    "trade_volume_24h_btc": 20051.478753023657,
    "trade_volume_24h_btc_normalized": 1210.00974669762
  },
  {
    "id": "kyberswap_elastic_arbitrum",
    "name": "Kyberswap Elastic (Arbitrum)",
    "year_established": "null",
    "country": "null",
    "description": "",
    "url": "https://kyberswap.com/swap?networkId=42161",
    "image": "https://assets.coingecko.com/markets/images/963/small/kyberswap.jpeg?1662695820",
    "has_trading_incentive": "false",
    "trust_score": 6,
    "trust_score_rank": 83,
    "trade_volume_24h_btc": 965.2488664644453,
    "trade_volume_24h_btc_normalized": 965.2488664644453
  },
  {
    "id": "kyberswap_elastic_polygon",
    "name": "Kyberswap Elastic (Polygon)",
    "year_established": "null",
    "country": "null",
    "description": "",
    "url": "https://kyberswap.com/swap?networkId=137",
    "image": "https://assets.coingecko.com/markets/images/959/small/kyberswap.jpeg?1662616218",
    "has_trading_incentive": "false",
    "trust_score": 6,
    "trust_score_rank": 84,
    "trade_volume_24h_btc": 625.8978604544344,
    "trade_volume_24h_btc_normalized": 625.8978604544344
  },
  {
    "id": "orca",
    "name": "Orca",
    "year_established": "null",
    "country": "null",
    "description": "",
    "url": "https://www.orca.so/",
    "image": "https://assets.coingecko.com/markets/images/691/small/orca.png?1628047248",
    "has_trading_incentive": "false",
    "trust_score": 6,
    "trust_score_rank": 85,
    "trade_volume_24h_btc": 583.2876510002571,
    "trade_volume_24h_btc_normalized": 572.8524797453738
  },
  {
    "id": "kyberswap_elastic_optimism",
    "name": "Kyberswap Elastic (Optimism)",
    "year_established": "null",
    "country": "null",
    "description": "",
    "url": "https://kyberswap.com/swap?networkId=10",
    "image": "https://assets.coingecko.com/markets/images/962/small/kyberswap.jpeg?1662695089",
    "has_trading_incentive": "false",
    "trust_score": 5,
    "trust_score_rank": 86,
    "trade_volume_24h_btc": 571.7030541517839,
    "trade_volume_24h_btc_normalized": 571.7030541517839
  },
  {
    "id": "sushiswap",
    "name": "Sushiswap",
    "year_established": 2020,
    "country": "null",
    "description": "",
    "url": "https://app.sushi.com/swap",
    "image": "https://assets.coingecko.com/markets/images/576/small/2048x2048_Logo.png?1609208464",
    "has_trading_incentive": "false",
    "trust_score": 6,
    "trust_score_rank": 87,
    "trade_volume_24h_btc": 553.802201107724,
    "trade_volume_24h_btc_normalized": 553.802201107724
  },
  {
    "id": "coincheck",
    "name": "Coincheck",
    "year_established": 2014,
    "country": "Japan",
    "description": "null",
    "url": "https://coincheck.com/",
    "image": "https://assets.coingecko.com/markets/images/18/small/Coincheck.jpg?1519703836",
    "has_trading_incentive": "null",
    "trust_score": 6,
    "trust_score_rank": 88,
    "trade_volume_24h_btc": 487.31646358385586,
    "trade_volume_24h_btc_normalized": 487.31646358385586
  },
  {
    "id": "quickswap",
    "name": "Quickswap",
    "year_established": 2020,
    "country": "null",
    "description": "Next-gen Layer 2 DEX. Trade at lightning-fast speeds with near-zero gas fees. \r\n",
    "url": "https://quickswap.exchange/#/swap",
    "image": "https://assets.coingecko.com/markets/images/629/small/1_pOU6pBMEmiL-ZJVb0CYRjQ_%281%29.png?1614077691",
    "has_trading_incentive": "false",
    "trust_score": 6,
    "trust_score_rank": 89,
    "trade_volume_24h_btc": 467.5359302574976,
    "trade_volume_24h_btc_normalized": 467.5359302574976
  },
  {
    "id": "quickswap_v3",
    "name": "Quickswap (v3)",
    "year_established": 2020,
    "country": "null",
    "description": "",
    "url": "https://quickswap.exchange/#/swap",
    "image": "https://assets.coingecko.com/markets/images/982/small/quickswap.jpeg?1665633994",
    "has_trading_incentive": "false",
    "trust_score": 6,
    "trust_score_rank": 90,
    "trade_volume_24h_btc": 386.31080598296256,
    "trade_volume_24h_btc_normalized": 386.31080598296256
  },
  {
    "id": "velodrome",
    "name": "Velodrome Finance",
    "year_established": 2022,
    "country": "null",
    "description": "Velodrome Finance, at its core, is a solution for protocols on Optimism to properly incentivize liquidity for their own use cases. Building on top of the groundwork laid out by Solidly, our team has addressed that first iteration's core issues to realize its full potential.\r\n\r\nThe team behind Velodrome Finance previously launched veDAO, an initiative incubated by Information Token. veDAO's founding mandate was to engage with the Solidly ecosystem, a protocol launched on the Fantom network by Andre Cronje, while driving long-term value to the veDAO community.\r\n\r\nThe veDAO team has since developed deep subject matter expertise on both Solidly, the veNFT primitive, and the ve(3,3) mechanism, becoming the go-to resource for protocols and chains seeking support around these topics.",
    "url": "https://app.velodrome.finance/swap",
    "image": "https://assets.coingecko.com/markets/images/933/small/velodrome-finance.png?1660261754",
    "has_trading_incentive": "false",
    "trust_score": 6,
    "trust_score_rank": 91,
    "trade_volume_24h_btc": 361.54316494110435,
    "trade_volume_24h_btc_normalized": 361.54316494110435
  },
  {
    "id": "osmosis",
    "name": "Osmosis",
    "year_established": 2021,
    "country": "null",
    "description": "Osmosis is an automated market maker (AMM) protocol built for liquidity providers. It is built based on the Cosmos SDK and is the first dex for IBC tokens.",
    "url": "https://app.osmosis.zone/",
    "image": "https://assets.coingecko.com/markets/images/684/small/osmosis-dex.jpeg?1624850295",
    "has_trading_incentive": "false",
    "trust_score": 6,
    "trust_score_rank": 92,
    "trade_volume_24h_btc": 355.5270867671387,
    "trade_volume_24h_btc_normalized": 355.5270867671387
  },
  {
    "id": "currency",
    "name": "Currency.com",
    "year_established": 2019,
    "country": "Gibraltar",
    "description": "Currency.com is the world’s first regulated tokenised securities exchange enabling anyone with crypto and fiat to trade financial assets from the world’s biggest companies with up to 500x leverage. \r\n \r\nCurrency.com enables crypto holders to make the most of your investment by offering access to more than 1300 tokenised securities of the most traded global financial assets – all without putting your crypto holdings under price pressure or converting to fiat\" to the following one \"Currency.com enables crypto holders to make the most of your investment by offering access to more than 2000+ tokenised securities of the most traded global financial assets – all without putting your crypto holdings under price pressure or converting to fiat\r\n \r\nWith Currency.com you can:\r\n- Do more with less with up to 500x leverage (or buy and sell assets of your choice);\r\n- Manage your risk with sell at loss, guaranteed sell at loss, take profit orders;\r\n- Elevate your trading strategy with access to over 75 technical indicators;\r\n- Fund your account and withdraw via card, bank transfer or crypto wallet;\r\n- Step ahead of the pack with instant price alerts;\r\n- Never lose more than you put in with negative balance protection;\r\n- Trade confidently with a regulated platform and dedicated human support;\r\n- See where you stand with personalised trading reports.\r\n \r\nCurrency.com offers you a new generation financial app for both crypto and fiat. The free mobile platform is designed to buy and sell cryptos with fiat money, store holdings in a secure place and make cross-crypto exchanges. Competitive quotes are coupled with trusted regulatory standards to give users the best possible financial experience.\r\n \r\nCurrency.com – an exchange where crypto meets Wall St.",
    "url": "https://currency.com/?utm_source=COINGECKO&utm_campaign=listing",
    "image": "https://assets.coingecko.com/markets/images/512/small/Currency.com_200x200.png?1582086630",
    "has_trading_incentive": "false",
    "trust_score": 6,
    "trust_score_rank": 93,
    "trade_volume_24h_btc": 2392.3953316938773,
    "trade_volume_24h_btc_normalized": 338.2309312763918
  },
  {
    "id": "bit_com",
    "name": "Bit.com",
    "year_established": 2020,
    "country": "Seychelles",
    "description": "",
    "url": "https://www.bit.com/",
    "image": "https://assets.coingecko.com/markets/images/823/small/IMAGE_2022-04-01_09_36_23.jpg?1648777125",
    "has_trading_incentive": "false",
    "trust_score": 6,
    "trust_score_rank": 94,
    "trade_volume_24h_btc": 2398.6057846936405,
    "trade_volume_24h_btc_normalized": 315.78467524845695
  },
  {
    "id": "canto_dex",
    "name": "Canto Dex",
    "year_established": "null",
    "country": "null",
    "description": "",
    "url": "https://app.slingshot.finance/trade",
    "image": "https://assets.coingecko.com/markets/images/943/small/canto.jpeg?1661216713",
    "has_trading_incentive": "false",
    "trust_score": 6,
    "trust_score_rank": 95,
    "trade_volume_24h_btc": 201.31876129039472,
    "trade_volume_24h_btc_normalized": 201.31876129039472
  },
  {
    "id": "tokpie",
    "name": "Tokpie",
    "year_established": 2018,
    "country": "Hong Kong",
    "description": "",
    "url": "https://tokpie.io/",
    "image": "https://assets.coingecko.com/markets/images/436/small/logo_circle_100x100.png?1562226767",
    "has_trading_incentive": "false",
    "trust_score": 6,
    "trust_score_rank": 96,
    "trade_volume_24h_btc": 191.84917405628076,
    "trade_volume_24h_btc_normalized": 183.4482466943814
  },
  {
    "id": "traderjoe",
    "name": "Trader Joe",
    "year_established": "null",
    "country": "null",
    "description": "",
    "url": "https://www.traderjoexyz.com/#/home",
    "image": "https://assets.coingecko.com/markets/images/692/small/traderjoe.png?1628152581",
    "has_trading_incentive": "false",
    "trust_score": 6,
    "trust_score_rank": 97,
    "trade_volume_24h_btc": 158.70512561879153,
    "trade_volume_24h_btc_normalized": 158.70512561879153
  },
  {
    "id": "kickex",
    "name": "KickEX",
    "year_established": 2020,
    "country": "Estonia",
    "description": "KickEX is the exchange with the lowest trading fees on the market. It's the fastest-growing exchange with amazing iOS and Android apps available in stores. Buy crypto within a minute, trade without risk! Our Support Team will answer all your questions instantly, in 7 different languages. Simple and user-friendly interface and high-quality KickEX mobile apps make our customers’ trading more comfortable, without bothering themselves with a long search for information.",
    "url": "https://kickex.com/en",
    "image": "https://assets.coingecko.com/markets/images/635/small/KickEX_logo.png?1652324492",
    "has_trading_incentive": "false",
    "trust_score": 6,
    "trust_score_rank": 98,
    "trade_volume_24h_btc": 1829.2198480355423,
    "trade_volume_24h_btc_normalized": 147.48268538708473
  },
  {
    "id": "kyberswap_elastic",
    "name": "KyberSwap Elastic (Ethereum)",
    "year_established": "null",
    "country": "null",
    "description": "",
    "url": "https://kyberswap.com/swap?networkId=1",
    "image": "https://assets.coingecko.com/markets/images/957/small/kyberswap.jpeg?1662697416",
    "has_trading_incentive": "false",
    "trust_score": 6,
    "trust_score_rank": 99,
    "trade_volume_24h_btc": 134.6338223604666,
    "trade_volume_24h_btc_normalized": 134.6338223604666
  },
  {
    "id": "vvs",
    "name": "VVS Finance",
    "year_established": 2021,
    "country": "null",
    "description": "",
    "url": "https://vvs.finance/swap",
    "image": "https://assets.coingecko.com/markets/images/736/small/vvs-finance.jpeg?1636702806",
    "has_trading_incentive": "false",
    "trust_score": 6,
    "trust_score_rank": 100,
    "trade_volume_24h_btc": 135.7273770902678,
    "trade_volume_24h_btc_normalized": 135.7273770902678
  }
]
df = pd.DataFrame(data=data)
#Drop Uneccessary data
df=df.drop(['has_trading_incentive','description','image'], axis=1)

print(df.head())
# Create a list named 'logo/image'to store all the image paths
logo = [
    "https://assets.coingecko.com/markets/images/23/small/Coinbase_Coin_Primary.png?1621471875",
    "https://assets.coingecko.com/markets/images/61/small/kucoin.png?1640584259",
    "https://assets.coingecko.com/markets/images/698/small/bybit_spot.png?1629971794",
    "https://assets.coingecko.com/markets/images/25/small/Huobi.?1655200466",
    "https://assets.coingecko.com/markets/images/29/small/kraken.jpg?1584251255",
    "https://assets.coingecko.com/markets/images/589/small/Crypto.jpg?1629861084",
    "https://assets.coingecko.com/markets/images/469/small/Binance.png?1568875842",
    "https://assets.coingecko.com/markets/images/4/small/BItfinex.png?1615895883",
    "https://assets.coingecko.com/markets/images/50/small/gemini.png?1605704107",
    "https://assets.coingecko.com/markets/images/52/small/binance.jpg?1519353250",
    "https://assets.coingecko.com/markets/images/540/small/Bitget_new_logo_2.png?1630049618",
    "https://assets.coingecko.com/markets/images/96/small/WeChat_Image_20220117220452.png?1642428377",
    "https://assets.coingecko.com/markets/images/37/small/poloniex.png?1663310089",
    "https://assets.coingecko.com/markets/images/866/small/bitmex.jpeg?1652794708",
    "https://assets.coingecko.com/markets/images/409/small/WeChat_Image_20210622160936.png?1624349423",
    "https://assets.coingecko.com/markets/images/418/small/whitebit_final.png?1667923522",
    "https://assets.coingecko.com/markets/images/60/small/gate_io_logo1.jpg?1654596784",
    "https://assets.coingecko.com/markets/images/812/small/YtFwQwJr_400x400.jpg?1646056092",
    "https://assets.coingecko.com/markets/images/239/small/Bitmart.png?1628066397",
    "https://assets.coingecko.com/markets/images/753/small/C8tiQdwL_400x400.jpg?1641348961",
    "https://assets.coingecko.com/markets/images/564/small/Phemex_logo_4.png?1641357471",
    "https://assets.coingecko.com/markets/images/6/small/bithumb_BI.png?1573104549",
    "https://assets.coingecko.com/markets/images/201/small/hotbit.jpg?1531043195",
    "https://assets.coingecko.com/markets/images/59/small/exmo_logo_blue.png?1662098170",
    "https://assets.coingecko.com/markets/images/223/small/BTCTurk-exchange.jpg?1536726120",
    "https://assets.coingecko.com/markets/images/9/small/bitstamp.jpg?1519627979",
    "https://assets.coingecko.com/markets/images/277/small/%E5%8E%9F%E8%89%B2.png?1650557355",
    "https://assets.coingecko.com/markets/images/135/small/coinex.jpg?1527737297",
    "https://assets.coingecko.com/markets/images/249/small/bitkub.png?1537180687",
    "https://assets.coingecko.com/markets/images/5/small/bitFlyer-logo.png?1643256033",
    "https://assets.coingecko.com/markets/images/747/small/coinstore.jpeg?1639530357",
    "https://assets.coingecko.com/markets/images/10/small/BG-color-250x250_icon.png?1596167574",
    "https://assets.coingecko.com/markets/images/122/small/bitbank.jpg?1521186278",
    "https://assets.coingecko.com/markets/images/8/small/Bitso-icon-dark.png?1581909156",
    "https://assets.coingecko.com/markets/images/530/small/logo-200x200.png?1587543672",
    "https://assets.coingecko.com/markets/images/218/small/max.jpg?1533888641",
    "https://assets.coingecko.com/markets/images/3/small/logogram-Indodax-new-_JPG_format.jpg?1580974378",
    "https://assets.coingecko.com/markets/images/33/small/luno.jpg?1519996997",
    "https://assets.coingecko.com/markets/images/683/small/wootrade.jpg?1624621149",
    "https://assets.coingecko.com/markets/images/26/small/itbit.png?1519810172",
    "https://assets.coingecko.com/markets/images/389/small/x_V5Jquo_400x400.png?1556071437",
    "https://assets.coingecko.com/markets/images/56/small/main-icon.png?1617267530",
    "https://assets.coingecko.com/markets/images/415/small/okcoin_Logomark_SatoshiBlack.png?1619574335",
    "https://assets.coingecko.com/markets/images/638/small/LCX.jpg?1616748175",
    "https://assets.coingecko.com/markets/images/97/small/kuna_exchange.png?1545126178",
    "https://assets.coingecko.com/markets/images/642/small/delta_spot.jpg?1617283005",
    "https://assets.coingecko.com/markets/images/386/small/Coinmetro_Exchange_Logo_%282%29.png?1646280101",
    "https://assets.coingecko.com/markets/images/546/small/logo_small_light.png?1637836622",
    "https://assets.coingecko.com/markets/images/225/small/DF_logo.png?1594264355",
    "https://assets.coingecko.com/markets/images/118/small/LBank_logo.png?1666234663",
    "https://assets.coingecko.com/markets/images/267/small/Coinsbit.png?1605153697",
    "https://assets.coingecko.com/markets/images/293/small/New_BKEX_logo.png?1646724631",
    "https://assets.coingecko.com/markets/images/254/small/unnamed_%281%29.png?1656295820",
    "https://assets.coingecko.com/markets/images/100/small/qcFFufEY_400x400.jpg?1561103345",
    "https://assets.coingecko.com/markets/images/251/small/ow0xng56_400x400.jpeg?1664939403",
    "https://assets.coingecko.com/markets/images/124/small/LA_token.png?1605773251",
    "https://assets.coingecko.com/markets/images/380/small/Dex-Trade_logo_new.png?1599629803",
    "https://assets.coingecko.com/markets/images/467/small/fmfw.png?1635491491",
    "https://assets.coingecko.com/markets/images/541/small/HS7eNJdt_400x400.jpg?1592294824",
    "https://assets.coingecko.com/markets/images/905/small/bullish_com.png?1655198360",
    "https://assets.coingecko.com/markets/images/837/small/btzlogo200x200_darkgreen.png?1648702264",
    "https://assets.coingecko.com/markets/images/430/small/gmo_z_com.png?1561112572",
    "https://assets.coingecko.com/markets/images/613/small/unnamedddd.png?1610503741",
    "https://assets.coingecko.com/markets/images/741/small/maiar-dex.png?1638433160",
    "https://assets.coingecko.com/markets/images/358/small/bitopro_coingecko_250x250_%281%29.png?1575884378",
    "https://assets.coingecko.com/markets/images/474/small/appicon-ios-pro.png?1622626638",
    "https://assets.coingecko.com/markets/images/587/small/CoinList.png?1601540662",
    "https://assets.coingecko.com/markets/images/592/small/Emirex.png?1602067691",
    "https://assets.coingecko.com/markets/images/99/small/zaif.png?1519627467",
    "https://assets.coingecko.com/markets/images/117/small/upbit.png?1520388800",
    "https://assets.coingecko.com/markets/images/404/small/logo400x400.png?1575881839",
    "https://assets.coingecko.com/markets/images/214/small/BitForex-Logo.png?1573808227",
    "https://assets.coingecko.com/markets/images/687/small/pancakeswap.jpeg?1626060212",
    "https://assets.coingecko.com/markets/images/714/small/bitvavo-mark-square-black.png?1633688872",
    "https://assets.coingecko.com/markets/images/535/small/256x256_Black-1.png?1590893262",
    "https://assets.coingecko.com/markets/images/752/small/uniswap-polygon.png?1640329417",
    "https://assets.coingecko.com/markets/images/136/small/paribu.jpg?1527734779",
    "https://assets.coingecko.com/markets/images/702/small/uniswap-v3.png?1631616149",
    "https://assets.coingecko.com/markets/images/20/small/coinone_circle_500x500.png?1606460853",
    "https://assets.coingecko.com/markets/images/963/small/kyberswap.jpeg?1662695820",
    "https://assets.coingecko.com/markets/images/464/small/BTSE.jpg?1568012415",
    "https://assets.coingecko.com/markets/images/962/small/kyberswap.jpeg?1662695089",
    "https://assets.coingecko.com/markets/images/18/small/Coincheck.jpg?1519703836",
    "https://assets.coingecko.com/markets/images/576/small/2048x2048_Logo.png?1609208464",
    "https://assets.coingecko.com/markets/images/629/small/1_pOU6pBMEmiL-ZJVb0CYRjQ_%281%29.png?1614077691",
    "https://assets.coingecko.com/markets/images/982/small/quickswap.jpeg?1665633994",
    "https://assets.coingecko.com/markets/images/512/small/Currency.com_200x200.png?1582086630",
    "https://assets.coingecko.com/markets/images/684/small/osmosis-dex.jpeg?1624850295",
    "https://assets.coingecko.com/markets/images/823/small/IMAGE_2022-04-01_09_36_23.jpg?1648777125",
    "https://assets.coingecko.com/markets/images/933/small/velodrome-finance.png?1660261754",
    "https://assets.coingecko.com/markets/images/692/small/traderjoe.png?1628152581",
    "https://assets.coingecko.com/markets/images/318/small/finexbox20190920.jpg?1568959220",
    "https://assets.coingecko.com/markets/images/436/small/logo_circle_100x100.png?1562226767",
    "https://assets.coingecko.com/markets/images/943/small/canto.jpeg?1661216713",
    "https://assets.coingecko.com/markets/images/707/small/dodo_logo.png?1632849982",
    "https://assets.coingecko.com/markets/images/635/small/KickEX_logo.png?1652324492",
    "https://assets.coingecko.com/markets/images/608/small/CpDGk9Hn_400x400.png?1607582976",
    "https://assets.coingecko.com/markets/images/287/small/cryptology.png?1541390904",
    "https://assets.coingecko.com/markets/images/274/small/wazirx.jpg?1540450020",
    "https://assets.coingecko.com/markets/images/34/small/logo_MB_hexagono.png?1657255217"
    
]
# Assigning the new list as a new column of the dataframe
df["Logo"] = logo

# Converting links to html tags
def path_to_image_html(path):
    return '<img src="' + path + '" width="60" >'

@st.cache
def convert_df(input_df):
     # IMPORTANT: Cache the conversion to prevent computation on every rerun
     return input_df.to_html(escape=False, formatters=dict(Logo=path_to_image_html))

html = convert_df(df)

st.markdown(
    html,
    unsafe_allow_html=True,
    
)

# Saving the dataframe as a webpage

st.download_button(
     label="Download data as HTML",
     data=html,
     file_name='output.html',
     mime='text/html',
 )

# Adjust dataframe
st.checkbox("Use container width", value=False, key="use_container_width")
#st.dataframe(html,use_container_width=st.session_state.use_container_width)

with st.expander("Bybit"):
  st.write('''Bybit is a cryptocurrency exchange that 
          offers a professional platform featuring an 
          offers a professional platform featuring an 
          ultra-fast matching engine, excellent customer 
          service and multilingual community support for 
          crypto traders of all levels. Established in 
          March 2018, Bybit currently serves more than 10
          million users and institutions offering access 
          to over 100 assets and contracts across Spot,
          Futures and Options, launchpad projects, earn 
          products, an NFT Marketplace and more. Bybit is
          a proud partner of Formula One racing team, 
          Oracle Red Bull Racing, esports teams NAVI, 
          Astralis, Alliance, Virtus.pro, Made in Brazil 
          (MIBR), City Esports, and Oracle Red Bull Racing 
          Esports, and association football (soccer) 
          teams Borussia Dortmund and Avispa Fukuoka.
        ''')
with st.expander("mxc"):
  st.write('''Established in April 2018, MEXC Global is one
         of the world's leading digital-asset trading 
         platforms. The core team comes from world-class 
         enterprises and financial companies with rich 
         experience in blockchain and financial industries.
        ''')
with st.expander("Crypto.com"):
  st.write('''Crypto.com Exchange is the best place to trade 
         crypto, with deep liquidity, low fees and best 
         execution prices, users can trade major 
         cryptocurrencies like Bitcoin, Ethereum, and 
         many more and receive great CRO-powered rewards
         ''')
with st.expander("Bitmax"):
  st.write('''AscendEX (formerly BitMax) is a leading global 
                    digital asset financial platform founded by a group 
                    of Wall Street quantitative trading veterans in 2018,
                    building on core value of Efficiency, Resilience and
                    Transparency. Driven by its continuous innovative product 
                    development and early-mover advantage in strategic 
                    alignment with the leading projects from DeFi 
                    ecosystem, AscendEX offers trading services across 
                    over 200 trading pairs across cash, margin, and 
                    futures products, in particular margin trading of 
                    over 50 tokens in cross-asset collateral mode and 
                    futures trading in both cross-asset and isolated
                    margin modes.''')
with st.expander("Gate"):
  st.write('''Gate was established in 2013, and it is the top 10
                    exchanges in the world in terms of authentic trading 
                    volume. It is also the first choice of over 8 million
                    registered customers, covering 130+ countries
                    worldwide, as we are providing the most comprehensive
                    digital asset solutions.
                    ''')
with st.expander("Dextrade"):
  st.write('''Dex-Trade is a centralized cryptocurrency 
         exchange founded in 2017 and registered in Belize.
         This is a modern space for safe and comfortable 
         trading with minimal commissions. Dex-Trade is a 
         universal exchange for both beginners and 
         professional traders. The minimum spread and high 
         liquidity in order books allow you to trade 
         efficiently with orders of any volume. Along with 
         global opportunities, the exchange also provides
         a demo trading mode for risk-free testing of your
         trading strategies. Our dedicated support team is
         online 24/7 to assist you with any questions.
         ''')
with st.expander("Poloniex"):
  st.write('''Poloniex was founded in January 2014 as a 
         global cryptocurrency exchange. It provides spot
         trading, futures trading, staking, and various 
         services to users in nearly 100 countries and 
         regions with various languages available. In 2022,
         Poloniex launched a brand new trading system to 
         provide global retail and professional users with 
         higher speed, as well as better stability and 
         usability.
         ''')
with st.expander("BingX"):
  st.write('''Founded in 2018, BingX is a crypto social 
         trading exchange that offers spot, derivatives 
         and copy trading services to more than 100 
         countries worldwide.BingX prides itself as the
         people's exchange by unlocking the fast-growing 
         cryptocurrency market for everyone, connecting 
         users with experts traders and a platform to 
         invest in a simple, engaging and transparent way.
''')
with st.expander("PhemX"):
  st.write('''Launched in 2019, Phemex is a Singapore-based
         cryptocurrency and derivatives trading platform 
         led by former Morgan Stanley executives. Serving
         around 5 million active users in over 200 
         countries, Phemex supports 150+ trading pairs 
         with up to 100x leverage. Fee Structure: 0.1%
         for both maker and taker. Contract Fee Structure:
         0.01% for maker and 0.06% for taker. Up to $100 
         Welcome Bonus for new users. Earn up to 8.5% APY
         interest income on crypto assets. Free academy 
         with 450+ carefully curated articles about 
         crypto & trading.Security: Hierarchical 
         Deterministic Cold Wallet System with 2-level
         human scrutiny offline signatures.
''')
with st.expander("BTCEX"):
  st.write('''BTCEX is a highly extensible digital asset 
         trading platform, which provides spot, spot 
         leverage, futures, perpetual contracts, and 
         USDT-settled options. In addition, it also 
         supports multi-product portfolio margin models 
         to improve the utilization of user funds.
         ''')
with st.expander("P2B"):
  st.write('''P2B Cryptocurrency Exchange is one of the 
         biggest European digital assets exchanges that 
         has successfully operated for over 5 years. It is
         now the most trusted platform offering the best
         go-to-market experience for crypto users and 
         projects.The platform tops the most trusted 
         ratings worldwide - CoinMarketCap and CoinGecko -
         and permanently improves its position. We assure
         the safety of the trading activities, being 
         ranked in the TOP-12 in Cer.Live security rate.
         The users can easily explore the mature crypto 
         market by investing in a wide variety of liquid
         tokens, buying cryptocurrencies with bank cards 
         (via Simplex, Moon Pay, Koinal) and using 
         attractive discounts or bonuses during 
         fundraising campaigns. You can also choose the 
         amount of your commission,  - use the level 
         commission to raise your account opportunities 
         and make your trading more profitable. Become a
         part of the prosperous P2B community - #1 place 
         to be in crypto. Get your exciting trading 
         experience with 24/7 support, and gain quickly 
         and securely.
''')
with st.expander("Hotbit"):
  st.write('''Founded in 2018 and holding Estonian MTR 
         licence, American MSB licence, an Australian 
         AUSTRAC licence and a Canadian MSB licence，
         HotBit cryptocurrency exchange is known as a 
         cryptocurrency trading platofrm that continues 
         to develop and integrate various forms of 
         businesses such as spot trading, financial 
         derivatives, cryptocurrency investment and 
         DAPP into one platform. Currently, Hotbit's 
         businesses covers more than 210 countries and 
         areas. Based on its globalized and unified 
         strategies, HotBit continues to focus on world's
         emerging markets such as Russia, Turkey and 
         southeastern Asia markets, and was ranked one
         of the top 3 most welcomed exchanges by Russian 
         media in 2019.''')
with st.expander("Coinstore"):
  st.write('''Coinstore was founded in 2020. There are 180 
         employees worldwide distributed mainly in Asia, 
         Europe, and the Middle East, serving more than 
         1,500,000 registered users in 175 countries. 
         Coinstore provides global users with fast and 
         smooth cryptocurrency trading services, 
         derivatives business, OTC services, and NFT 
         services. Coinstore Labs provides project owners
         with integrated solutions of 'technology 
         development, compliance counseling, integrated
         marketing, community operations, investment 
         incubation' and much more. Coinstore supports 102 
         spot pairs and 34 futures pairs. 
         All features are available on Coinstore's mobile
         app for iOS and Android, and on desktop.
''')
with st.expander("Okcoin"):
  st.write('''About OKCoin: OKCoin is one of the largest and 
                     most trusted fiat-to-crypto trading platforms in the
                     world. Founded in 2013, OKCoin offers advanced 
                     features for crypto beginners and high-volume traders
                     alike, enabling users in 184 countries worldwide to 
                     exchange US dollars and the euro for Bitcoin, Tethers,
                     USDK, Bitcoin Cash, Ethereum, Ethereum Classic, 
                     Decred, EOS, Litecoin, XRP, Cardano, 0x, Stellar, 
                     Zcash, TRX, and other digital assets. As a registered
                     Money Services Business (MSB) with the Financial 
                     Crimes Enforcement Network (FinCEN) and a Virtual 
                     Financial Asset Act (VFAA) exchange with a 
                     transitory provision permissioned by the Malta F
                     inancial Services Authority, OKCoin is on a mission
                     to make digital assets accessible to the world while
                     complying with the highest of regulatory standards. 
                     For more information, visit www.okcoin.com.
                    ''')
with st.expander("Nominex"):
  st.write('''New trading platform for convenient trading 
                     experience with low fees and numerous instruments. 
                     Absolutely unique affiliate program that allows to 
                     earn from an infinite number of referral levels, 
                     compared to 2-3 levels at all other exchanges. A 
                     unique model for the free 2 phases distribution of 
                     the native NMX token. Advanced Trading Instruments –
                     using Stop, Stop Limit, Trailing Stop, Scaled and 
                     other types of orders brings some kind of trading 
                     automation without the need to develop a trading bot,
                     which allows to easily get more profit while trading.
                     ''')
with st.expander("Wootrade"):
  st.write('''WOO Network is a deep liquidity network connecting 
                     traders,exchanges, institutions, and DeFi platforms 
                     with democratized access to the best-in-class 
                     liquidity and trading execution at lower or zero 
                     cost. Its flagship, WOO X, is a professional trading
                     platform featuring customizable modules and lower to
                     zero fees complete with deep liquidity. WOO Network 
                     was founded by Kronos Research, a quantitative 
                     trading firm generating $5-10B in daily volume.
                     ''')
with st.expander("Emirex"):
  st.write('''Emirex was launched in 2014 and became a network 
                     of enterprises using blockchain technology to ease 
                     asset trading and completely disrupt how people use
                     crypto. Dubai, UAE, is a dynamic destination for 
                     Eastern and Western companies, and it's where Emirex
                     helped develop a crypto culture. Emirex is an 
                     exchange and marketplace for trading digital assets 
                     that improve economic freedom by developing 
                     censorship-resistant public networks. Emirex has 
                     grown tremendously with its business and is eager 
                     to develop even more. The EMRX Token Emirex offers 
                     B2C, B2B, and B2E payments and boasts over 20,000 
                     active clients and a $10 million monthly income after
                     growing 40-fold in a year. The exchange has over $25
                     million in daily volume. EMRX, the exchange's token,
                     quadrupled last year due to ecosystem integration 
                     and active use. As the Emirex Ecosystem's native 
                     token, EMRX is used for listing fees for tokenized 
                     assets, buy/sell transaction fees, custody and 
                     servicing fees, and commission and partner incentive
                     programs. You can also stake EMRX and other tokens 
                     to earn Ultra High APR on your tokens and withdraw 
                     anytime. Staking is your gateway to passive crypto 
                     income! Emirex also launched a tokenization section 
                     to help revolutionize the real estate market as well.
                     Quick, Simple, Secure. Emirex is a platform that
                     simplifies, quickens, and secures digital asset 
                     trading. Newbies can trade digital assets easily as
                     Emirex offers non-tech users secure, easy, compliant
                     digital asset access on a  professional trading 
                     platform supporting AED, USD, and EUR FIATs. Emirex
                     can process 1,000,000 orders per second. Experience 
                     speedy order books, extensive trade history, endless
                     markets, and market depth, and make spot, margin, 
                     and futures order types. The Emirex Group offers 
                     top-tier financial services to bridge the gap 
                     between the current and future economic systems.
                    Why You Should Use Emirex?Emirex simplifies crypto 
                    access and makes its site user-friendly. Emirex's UI
                    is straightforward. A knowledge base guides newcomers
                    through exchange operations. Emirex offers deep 
                    liquidity, hundreds of token pairs, and multiple 
                    trading orders. You won't get lost with Emirex's 
                    security, the convenience of access, and helpful 
                    experts. Receive and send tokens without an 
                    intermediary. Copy or Social trading lets you 
                    imitate the top traders' trades, and Emirex's 
                    referral code earns you up to 7% on your friend's 
                    and family's transactions. Trade Whenever, Wherever 
                    Emirex provides the most incredible trading 
                    experience, allowing you to trade on your terms. 
                    We want to help you pleasantly attain your financial
                    goals. Emirex builds crypto economic infrastructure 
                    based on user experience and accessibility. The 
                    Emirex team launched the Emirex Android to offer 
                    all website features in your pocket, including easy
                    bitcoin buying, selling, and trading and 24/7 support
                    with one tap. Emirex makes crypto investment so easy 
                    that you'll want to do it all the time! Sign Up and
                    Keep Up! Sign up now to benefit from Emirex's low
                    to 0% fees. Emirex offers Africa, Asia, and 
                    Europe exposure to digital assets and crypto and 
                    connects the Middle East with those markets. 
                    Decentralization and transparency in blockchain can
                    encourage global value mobility and societal
                    well-being, which is why emirex is dedicated to the 
                    digital economy.''')
with st.expander("XT"):
  st.write('''By consistently expanding its ecosystem, XT.COM 
                     is dedicated to providing users with the most secure,
                     trusted, and hassle-free digital asset trading 
                     services. Our exchange is built from a desire to 
                     give everyone access to digital assets regardless 
                     where you are. Founded in 2018, XT.COM now serves
                     more than 6 million registered users, over 500,000+
                     monthly active users and 40+ million users in the 
                     ecosystem. Covering a rich variety of  trading 
                     categories together with a NFT aggregated 
                     marketplace,  our platform strives to cater to its
                     large user base by providing a secure, trusted and 
                     intuitive trading experience. As the world's first
                     social-infused digital assets trading platform, 
                     XT.COM also supports social networking platform 
                     based transactions to make our crypto services more
                     accessible to users all over the world. Furthermore,
                     to ensure optimal data integrity and security, 
                     we see user security as our top priority at XT.COM.
                     ''')

st.sidebar.write('''Exchanges is when a party or parties 
                 gives something of value
                 and in return that party or parties is
                 expected to do the same. The same applies
                 in the wonderful world of Crypto! There
                 is an extensive selection that exists but,
                 not all exchanges are the same. For 
                 example, while all might offer bitcoin 
                 they cannot gurantee to provide other 
                 valuable altcoins or tokens that could 
                 possibly be a great investment. Another 
                 thing to consider is if the exchange is
                 certified. What does this mean? The 
                 crypto exchanges have been assessed by 
                 certified specialists and had met 3 
                 points 'penetration test, proof of funds,
                 and bug bounty.' But, don't fret! 
                 This application already
                 does the hard part. This table is a 
                 variety of exchanges that offers
                 certified platforms to trade on.
                 ''')
 #coins_list 
coins_list = ["bitcoin","eos","ethereum","litecoin","ripple","cardano","tether","binancecoin","usd-coin","binance-usd","ripple,dogecoin","matic-network","sola-token","staked-ether","shiba-inu,dai","okb,uniswap","stellar","monero","algorand","crypto-com-chain","vechain","decentraland","aave","eos","tezos"]
coin_id = st.sidebar.selectbox('Select a coin: ', coins_list)