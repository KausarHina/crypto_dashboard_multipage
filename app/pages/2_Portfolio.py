#import modules
import streamlit as st
import pandas as pd

#def portfolio_plot():
#   st.write("Portfolio !!!")
#   st.write("Pycoingecko")
#st.set_page_config(page_title="Portfolio", page_icon="💰")
#st.markdown("# Portfolio Info")
#st.sidebar.header("Portfolio Info")
#st.write(
#    """Portfolio information and Simulation"""
#)


#portfolio_plot()

#create dataframe

data = [
  {
    "id": "binance",
    "name": "Binance",
    "year_established": 2017,
    "country": "Cayman Islands",
    "description": "",
    "url": "https://www.binance.com/",
    "image": "https://assets.coingecko.com/markets/images/52/small/binance.jpg?1519353250",
    "has_trading_incentive": False,
    "trust_score": 10,
    "trust_score_rank": 1,
    "trade_volume_24h_btc": 780953.834021476,
    "trade_volume_24h_btc_normalized": 447568.60086289997
  },
  {
    "id": "gdax",
    "name": "Coinbase Exchange",
    "year_established": 2012,
    "country": "United States",
    "description": "",
    "url": "https://www.coinbase.com",
    "image": "https://assets.coingecko.com/markets/images/23/small/Coinbase_Coin_Primary.png?1621471875",
    "has_trading_incentive": False,
    "trust_score": 10,
    "trust_score_rank": 2,
    "trade_volume_24h_btc": 97274.05151772423,
    "trade_volume_24h_btc_normalized": 97274.05151772423
  },
  {
    "id": "kucoin",
    "name": "KuCoin",
    "year_established": 2014,
    "country": "Seychelles",
    "description": "",
    "url": "https://www.kucoin.com/",
    "image": "https://assets.coingecko.com/markets/images/61/small/kucoin.png?1640584259",
    "has_trading_incentive": False,
    "trust_score": 10,
    "trust_score_rank": 3,
    "trade_volume_24h_btc": 99931.38302669437,
    "trade_volume_24h_btc_normalized": 53925.56011337699
  },
  {
    "id": "okex",
    "name": "OKX",
    "year_established": 2013,
    "country": "Belize",
    "description": "",
    "url": "https://www.okx.com",
    "image": "https://assets.coingecko.com/markets/images/96/small/WeChat_Image_20220117220452.png?1642428377",
    "has_trading_incentive": False,
    "trust_score": 10,
    "trust_score_rank": 4,
    "trade_volume_24h_btc": 51564.54179454194,
    "trade_volume_24h_btc_normalized": 39026.18180420945
  },
  {
    "id": "kraken",
    "name": "Kraken",
    "year_established": 2011,
    "country": "United States",
    "description": "",
    "url": "https://r.kraken.com/c/2223866/687155/10583",
    "image": "https://assets.coingecko.com/markets/images/29/small/kraken.jpg?1584251255",
    "has_trading_incentive": False,
    "trust_score": 10,
    "trust_score_rank": 5,
    "trade_volume_24h_btc": 39835.17730946683,
    "trade_volume_24h_btc_normalized": 29103.426861774144
  },
  {
    "id": "bybit_spot",
    "name": "Bybit",
    "year_established": 2018,
    "country": "null",
    "description": "Bybit is a cryptocurrency exchange that offers a professional platform featuring an ultra-fast matching engine, excellent customer service and multilingual community support for crypto traders of all levels. Established in March 2018, Bybit currently serves more than 10 million users and institutions offering access to over 100 assets and contracts across Spot, Futures and Options, launchpad projects, earn products, an NFT Marketplace and more. Bybit is a proud partner of Formula One racing team, Oracle Red Bull Racing, esports teams NAVI, Astralis, Alliance, Virtus.pro, Made in Brazil (MIBR), City Esports, and Oracle Red Bull Racing Esports, and association football (soccer) teams Borussia Dortmund and Avispa Fukuoka.",
    "url": "https://www.bybit.com",
    "image": "https://assets.coingecko.com/markets/images/698/small/bybit_spot.png?1629971794",
    "has_trading_incentive": False,
    "trust_score": 10,
    "trust_score_rank": 6,
    "trade_volume_24h_btc": 28767.908746105943,
    "trade_volume_24h_btc_normalized": 28767.908746105943
  },
  {
    "id": "binance_us",
    "name": "Binance US",
    "year_established": 2019,
    "country": "United States",
    "description": "",
    "url": "https://www.binance.us/",
    "image": "https://assets.coingecko.com/markets/images/469/small/Binance.png?1568875842",
    "has_trading_incentive": False,
    "trust_score": 10,
    "trust_score_rank": 7,
    "trade_volume_24h_btc": 14834.03991992847,
    "trade_volume_24h_btc_normalized": 14091.268925120903
  },
  {
    "id": "bitfinex",
    "name": "Bitfinex",
    "year_established": 2014,
    "country": "British Virgin Islands",
    "description": "",
    "url": "https://www.bitfinex.com",
    "image": "https://assets.coingecko.com/markets/images/4/small/BItfinex.png?1615895883",
    "has_trading_incentive": False,
    "trust_score": 10,
    "trust_score_rank": 8,
    "trade_volume_24h_btc": 11918.904515899896,
    "trade_volume_24h_btc_normalized": 7875.300404422468
  },
  {
    "id": "gemini",
    "name": "Gemini",
    "year_established": 2014,
    "country": "United States",
    "description": "",
    "url": "https://gemini.sjv.io/bZ49k",
    "image": "https://assets.coingecko.com/markets/images/50/small/gemini.png?1605704107",
    "has_trading_incentive": False,
    "trust_score": 10,
    "trust_score_rank": 9,
    "trade_volume_24h_btc": 6886.517094370879,
    "trade_volume_24h_btc_normalized": 6886.517094370879
  },
  {
    "id": "blockchain_com",
    "name": "Blockchain.com",
    "year_established": 2012,
    "country": "United Kingdom",
    "description": "",
    "url": "https://www.blockchain.com/",
    "image": "https://assets.coingecko.com/markets/images/613/small/unnamedddd.png?1610503741",
    "has_trading_incentive": False,
    "trust_score": 10,
    "trust_score_rank": 10,
    "trade_volume_24h_btc": 227.59023008867544,
    "trade_volume_24h_btc_normalized": 227.59023008867544
  },
  {
    "id": "mxc",
    "name": "MEXC Global",
    "year_established": 2018,
    "country": "null",
    "description": "Established in April 2018, MEXC Global is one of the world's leading digital-asset trading platforms. The core team comes from world-class enterprises and financial companies with rich experience in blockchain and financial industries.",
    "url": "https://www.mexc.com/",
    "image": "https://assets.coingecko.com/markets/images/409/small/WeChat_Image_20210622160936.png?1624349423",
    "has_trading_incentive": False,
    "trust_score": 9,
    "trust_score_rank": 11,
    "trade_volume_24h_btc": 68110.06644414224,
    "trade_volume_24h_btc_normalized": 64909.69399452852
  },
  {
    "id": "gate",
    "name": "Gate.io",
    "year_established": "null",
    "country": "Hong Kong",
    "description": "Gate was established in 2013, and it is the top 10 exchanges in the world in terms of authentic trading volume. It is also the first choice of over 8 million registered customers, covering 130+ countries worldwide, as we are providing the most comprehensive digital asset solutions.",
    "url": "https://gate.io/",
    "image": "https://assets.coingecko.com/markets/images/60/small/gate_io_logo1.jpg?1654596784",
    "has_trading_incentive": False,
    "trust_score": 9,
    "trust_score_rank": 12,
    "trade_volume_24h_btc": 54785.98674363786,
    "trade_volume_24h_btc_normalized": 41294.66644316797
  },
  {
    "id": "bitget",
    "name": "Bitget",
    "year_established": 2018,
    "country": "Singapore",
    "description": "",
    "url": "https://www.bitget.com/",
    "image": "https://assets.coingecko.com/markets/images/540/small/Bitget_new_logo_2.png?1630049618",
    "has_trading_incentive": False,
    "trust_score": 9,
    "trust_score_rank": 13,
    "trade_volume_24h_btc": 30111.070700927066,
    "trade_volume_24h_btc_normalized": 30111.070700927066
  },
  {
    "id": "crypto_com",
    "name": "Crypto.com Exchange",
    "year_established": 2019,
    "country": "Cayman Islands",
    "description": "Crypto.com Exchange is the best place to trade crypto, with deep liquidity, low fees and best execution prices, users can trade major cryptocurrencies like Bitcoin, Ethereum, and many more and receive great CRO-powered rewards",
    "url": "https://crypto.com/exchange",
    "image": "https://assets.coingecko.com/markets/images/589/small/Crypto.jpg?1629861084",
    "has_trading_incentive": False,
    "trust_score": 9,
    "trust_score_rank": 14,
    "trade_volume_24h_btc": 22102.177690514098,
    "trade_volume_24h_btc_normalized": 22102.177690514098
  },
  {
    "id": "huobi",
    "name": "Huobi Global",
    "year_established": 2013,
    "country": "Seychelles",
    "description": "",
    "url": "https://www.huobi.com",
    "image": "https://assets.coingecko.com/markets/images/25/small/Huobi.?1655200466",
    "has_trading_incentive": False,
    "trust_score": 9,
    "trust_score_rank": 15,
    "trade_volume_24h_btc": 15667.77394683881,
    "trade_volume_24h_btc_normalized": 15667.77394683881
  },
  {
    "id": "bitmax",
    "name": "AscendEX (BitMax)",
    "year_established": 2018,
    "country": "Singapore",
    "description": "AscendEX (formerly BitMax) is a leading global digital asset financial platform founded by a group of Wall Street quantitative trading veterans in 2018, building on core value of 'Efficiency, Resilience and Transparency.' \r\n \r\nDriven by its continuous innovative product development and early-mover advantage in strategic alignment with the leading projects from DeFi ecosystem, AscendEX offers trading services across over 200 trading pairs across cash, margin, and futures products, in particular margin trading of over 50 tokens in cross-asset collateral mode and futures trading in both cross-asset and isolated margin modes.",
    "url": "https://ascendex.com/en/global-digital-asset-platform",
    "image": "https://assets.coingecko.com/markets/images/277/small/%E5%8E%9F%E8%89%B2.png?1650557355",
    "has_trading_incentive": False,
    "trust_score": 9,
    "trust_score_rank": 16,
    "trade_volume_24h_btc": 5121.808733243612,
    "trade_volume_24h_btc_normalized": 5121.808733243612
  },
  {
    "id": "dextrade",
    "name": "Dex-Trade",
    "year_established": 2019,
    "country": "Belize",
    "description": "Dex-Trade is a centralized cryptocurrency exchange founded in 2017 and registered in Belize. This is a modern space for safe and comfortable trading with minimal commissions.\r\n\r\nDex-Trade is a universal exchange for both beginners and professional traders. The minimum spread and high liquidity in order books allow you to trade efficiently with orders of any volume.\r\nAlong with global opportunities, the exchange also provides a demo trading mode for risk-free testing of your trading strategies. Our dedicated support team is online 24/7 to assist you with any questions.\r\n\r\nYou can learn more about Dex-Trade on the website.\r\nhttps://dex-trade.com/info/about\r\n\r\nIf you are looking for listing and promotion options with Dex-Trade please visit our listing page and a personal manager will help you to utilize our proven tools and intelligent market-making system to engage with the vast exchange community in the best possible way. https://dex-trade.com/listing",
    "url": "https://dex-trade.com/",
    "image": "https://assets.coingecko.com/markets/images/380/small/Dex-Trade_logo_new.png?1599629803",
    "has_trading_incentive": False,
    "trust_score": 9,
    "trust_score_rank": 17,
    "trade_volume_24h_btc": 6821.0050155617155,
    "trade_volume_24h_btc_normalized": 4926.138068325914
  },
  {
    "id": "poloniex",
    "name": "Poloniex",
    "year_established": 2014,
    "country": "Seychelles",
    "description": "Poloniex was founded in January 2014 as a global cryptocurrency exchange. It provides spot trading, futures trading, staking, and various services to users in nearly 100 countries and regions with various languages available.\r\n\r\nIn 2022, Poloniex launched a brand new trading system to provide global retail and professional users with higher speed, as well as better stability and usability.",
    "url": "https://poloniex.com/",
    "image": "https://assets.coingecko.com/markets/images/37/small/poloniex.png?1663310089",
    "has_trading_incentive": False,
    "trust_score": 9,
    "trust_score_rank": 18,
    "trade_volume_24h_btc": 3549.3716258679524,
    "trade_volume_24h_btc_normalized": 3549.3716258679524
  },
  {
    "id": "digifinex",
    "name": "DigiFinex",
    "year_established": 2018,
    "country": "Seychelles",
    "description": "",
    "url": "https://www.digifinex.com/",
    "image": "https://assets.coingecko.com/markets/images/225/small/DF_logo.png?1594264355",
    "has_trading_incentive": False,
    "trust_score": 8,
    "trust_score_rank": 19,
    "trade_volume_24h_btc": 58620.12329377731,
    "trade_volume_24h_btc_normalized": 58620.12329377731
  },
  {
    "id": "whitebit",
    "name": "WhiteBIT",
    "year_established": 2018,
    "country": "Estonia",
    "description": "",
    "url": "https://whitebit.com",
    "image": "https://assets.coingecko.com/markets/images/418/small/whitebit_final.png?1667923522",
    "has_trading_incentive": False,
    "trust_score": 8,
    "trust_score_rank": 20,
    "trade_volume_24h_btc": 44592.05857032475,
    "trade_volume_24h_btc_normalized": 44592.05857032475
  },
  {
    "id": "coinsbit",
    "name": "Coinsbit",
    "year_established": "null",
    "country": "Estonia",
    "description": "",
    "url": "https://coinsbit.io/",
    "image": "https://assets.coingecko.com/markets/images/267/small/Coinsbit.png?1605153697",
    "has_trading_incentive": False,
    "trust_score": 8,
    "trust_score_rank": 21,
    "trade_volume_24h_btc": 39835.74043912926,
    "trade_volume_24h_btc_normalized": 39835.74043912926
  },
  {
    "id": "upbit",
    "name": "Upbit",
    "year_established": 2017,
    "country": "South Korea",
    "description": "null",
    "url": "https://upbit.com",
    "image": "https://assets.coingecko.com/markets/images/117/small/upbit.png?1520388800",
    "has_trading_incentive": False,
    "trust_score": 8,
    "trust_score_rank": 22,
    "trade_volume_24h_btc": 80544.18073388886,
    "trade_volume_24h_btc_normalized": 38520.87959698876
  },
  {
    "id": "bkex",
    "name": "BKEX",
    "year_established": 2018,
    "country": "British Virgin Islands",
    "description": "",
    "url": "https://www.bkex.com/",
    "image": "https://assets.coingecko.com/markets/images/293/small/New_BKEX_logo.png?1646724631",
    "has_trading_incentive": False,
    "trust_score": 8,
    "trust_score_rank": 23,
    "trade_volume_24h_btc": 35028.4028306043,
    "trade_volume_24h_btc_normalized": 35028.4028306043
  },
  {
    "id": "bingx",
    "name": "BingX",
    "year_established": "null",
    "country": "null",
    "description": "Founded in 2018, BingX is a crypto social trading exchange that offers spot, derivatives and copy trading services to more than 100 countries worldwide.\r\n\r\nBingX prides itself as the people's exchange by unlocking the fast-growing cryptocurrency market for everyone, connecting users with experts traders and a platform to invest in a simple, engaging and transparent way.",
    "url": "https://bingx.com/",
    "image": "https://assets.coingecko.com/markets/images/812/small/YtFwQwJr_400x400.jpg?1646056092",
    "has_trading_incentive": False,
    "trust_score": 8,
    "trust_score_rank": 24,
    "trade_volume_24h_btc": 32345.240363495242,
    "trade_volume_24h_btc_normalized": 32345.240363495242
  },
  {
    "id": "bitmart",
    "name": "BitMart",
    "year_established": 2017,
    "country": "Cayman Islands",
    "description": "",
    "url": "https://www.bitmart.com/en",
    "image": "https://assets.coingecko.com/markets/images/239/small/Bitmart.png?1628066397",
    "has_trading_incentive": False,
    "trust_score": 8,
    "trust_score_rank": 25,
    "trade_volume_24h_btc": 28455.2814473308,
    "trade_volume_24h_btc_normalized": 28455.2814473308
  },
  {
    "id": "phemex",
    "name": "Phemex",
    "year_established": 2019,
    "country": "Singapore",
    "description": "Launched in 2019, Phemex is a Singapore-based cryptocurrency and derivatives trading platform led by former Morgan Stanley executives. Serving around 5 million active users in over 200 countries, Phemex supports 150+ trading pairs with up to 100x leverage.\r\n\r\n-  Fee Structure: 0.1% for both maker and taker\r\n-  Contract Fee Structure: 0.01% for maker and 0.06% for taker\r\n-  Up to $100 Welcome Bonus for new users\r\n-  Earn up to 8.5% APY interest income on crypto assets\r\n-  Free academy with 450+ carefully curated articles about crypto & trading\r\n-  Security: Hierarchical Deterministic Cold Wallet System with 2-level human scrutiny offline signatures.",
    "url": "https://phemex.com/",
    "image": "https://assets.coingecko.com/markets/images/564/small/Phemex_logo_4.png?1641357471",
    "has_trading_incentive": False,
    "trust_score": 8,
    "trust_score_rank": 26,
    "trade_volume_24h_btc": 20642.45815777989,
    "trade_volume_24h_btc_normalized": 20642.45815777989
  },
  {
    "id": "bitrue",
    "name": "Bitrue",
    "year_established": 2018,
    "country": "Singapore",
    "description": "",
    "url": "https://www.bitrue.com/",
    "image": "https://assets.coingecko.com/markets/images/254/small/unnamed_%281%29.png?1656295820",
    "has_trading_incentive": False,
    "trust_score": 8,
    "trust_score_rank": 27,
    "trade_volume_24h_btc": 98107.65510372989,
    "trade_volume_24h_btc_normalized": 18312.323556001676
  },
  {
    "id": "btcex",
    "name": "BTCEX",
    "year_established": 2021,
    "country": "Canada",
    "description": "BTCEX is a highly extensible digital asset trading platform, which provides spot, spot leverage, futures, perpetual contracts, and USDT-settled options. In addition, it also supports multi-product portfolio margin models to improve the utilization of user funds.",
    "url": "https://www.btcex.com",
    "image": "https://assets.coingecko.com/markets/images/753/small/C8tiQdwL_400x400.jpg?1641348961",
    "has_trading_incentive": False,
    "trust_score": 8,
    "trust_score_rank": 28,
    "trade_volume_24h_btc": 16399.185573715662,
    "trade_volume_24h_btc_normalized": 16399.185573715662
  },
  {
    "id": "p2pb2b",
    "name": "P2B",
    "year_established": 2018,
    "country": "Lithuania",
    "description": "P2B Cryptocurrency Exchange is one of the biggest European digital assets exchanges that has successfully operated for over 5 years. It is now the most trusted platform offering the best go-to-market experience for crypto users and projects.\r\n\r\nThe platform tops the most trusted ratings worldwide - CoinMarketCap and CoinGecko - and permanently improves its position. We assure the safety of the trading activities, being ranked in the TOP-12 in Cer.Live security rate. \r\n\r\nThe users can easily explore the mature crypto market by investing in a wide variety of liquid tokens, buying cryptocurrencies with bank cards (via Simplex, Moon Pay, Koinal) and using attractive discounts or bonuses during fundraising campaigns. You can also choose the amount of your commission,  - use the level commission to raise your account opportunities and make your trading more profitable. \r\n\r\nBecome a part of the prosperous P2B community - #1 place to be in crypto.\r\nGet your exciting trading experience with 24/7 support, and gain quickly and securely.\r\n",
    "url": "https://p2pb2b.com/",
    "image": "https://assets.coingecko.com/markets/images/251/small/ow0xng56_400x400.jpeg?1664939403",
    "has_trading_incentive": False,
    "trust_score": 8,
    "trust_score_rank": 29,
    "trade_volume_24h_btc": 52035.98678747952,
    "trade_volume_24h_btc_normalized": 12833.924076147576
  },
  {
    "id": "bithumb",
    "name": "Bithumb",
    "year_established": 2014,
    "country": "South Korea",
    "description": "",
    "url": "https://www.bithumb.com/",
    "image": "https://assets.coingecko.com/markets/images/6/small/bithumb_BI.png?1573104549",
    "has_trading_incentive": False,
    "trust_score": 8,
    "trust_score_rank": 30,
    "trade_volume_24h_btc": 12788.169234128465,
    "trade_volume_24h_btc_normalized": 12788.169234128465
  },
  {
    "id": "bitstamp",
    "name": "Bitstamp",
    "year_established": 2013,
    "country": "United Kingdom",
    "description": "",
    "url": "https://links.bitstamp.net/c/2223866/1100037/14006",
    "image": "https://assets.coingecko.com/markets/images/9/small/bitstamp.jpg?1519627979",
    "has_trading_incentive": False,
    "trust_score": 8,
    "trust_score_rank": 31,
    "trade_volume_24h_btc": 12058.842951789618,
    "trade_volume_24h_btc_normalized": 6341.707928589274
  },
  {
    "id": "hotbit",
    "name": "Hotbit",
    "year_established": 2018,
    "country": "Estonia",
    "description": "Founded in 2018 and holding Estonian MTR licence, American MSB licence, an Australian AUSTRAC licence and a Canadian MSB licence，HotBit cryptocurrency exchange is known as a cryptocurrency trading platofrm that continues to develop and integrate various forms of businesses such as spot trading, financial derivatives, cryptocurrency investment and DAPP into one platform. Currently, Hotbit's businesses covers more than 210 countries and areas. Based on its globalized and unified strategies, HotBit continues to focus on world's emerging markets such as Russia, Turkey and southeastern Asia markets, and was ranked one of the top 3 most welcomed exchanges by Russian media in 2019.",
    "url": "https://www.hotbit.io/",
    "image": "https://assets.coingecko.com/markets/images/201/small/hotbit.jpg?1531043195",
    "has_trading_incentive": False,
    "trust_score": 8,
    "trust_score_rank": 32,
    "trade_volume_24h_btc": 5835.645323326378,
    "trade_volume_24h_btc_normalized": 5835.645323326378
  },
  {
    "id": "btcturk",
    "name": "BtcTurk PRO",
    "year_established": 2013,
    "country": "Turkey",
    "description": "",
    "url": "https://pro.btcturk.com/",
    "image": "https://assets.coingecko.com/markets/images/223/small/BTCTurk-exchange.jpg?1536726120",
    "has_trading_incentive": False,
    "trust_score": 8,
    "trust_score_rank": 33,
    "trade_volume_24h_btc": 5215.560726593681,
    "trade_volume_24h_btc_normalized": 5215.560726593681
  },
  {
    "id": "latoken",
    "name": "LATOKEN",
    "year_established": 2017,
    "country": "Cayman Islands",
    "description": "",
    "url": "https://latoken.com/",
    "image": "https://assets.coingecko.com/markets/images/124/small/LA_token.png?1605773251",
    "has_trading_incentive": False,
    "trust_score": 8,
    "trust_score_rank": 34,
    "trade_volume_24h_btc": 3583.921391796913,
    "trade_volume_24h_btc_normalized": 3583.921391796913
  },
  {
    "id": "exmo",
    "name": "EXMO",
    "year_established": 2013,
    "country": "United Kingdom",
    "description": "",
    "url": "https://exmo.com/",
    "image": "https://assets.coingecko.com/markets/images/59/small/exmo_logo_blue.png?1662098170",
    "has_trading_incentive": False,
    "trust_score": 8,
    "trust_score_rank": 35,
    "trade_volume_24h_btc": 2687.086332842887,
    "trade_volume_24h_btc_normalized": 2687.086332842887
  },
  {
    "id": "bitflyer",
    "name": "bitFlyer",
    "year_established": 2014,
    "country": "Japan",
    "description": "",
    "url": "https://bitflyereuropesa.pxf.io/c/2223866/858437/11990",
    "image": "https://assets.coingecko.com/markets/images/5/small/bitFlyer-logo.png?1643256033",
    "has_trading_incentive": False,
    "trust_score": 8,
    "trust_score_rank": 36,
    "trade_volume_24h_btc": 2217.394312699432,
    "trade_volume_24h_btc_normalized": 2217.394312699432
  },
  {
    "id": "bitkub",
    "name": "Bitkub",
    "year_established": 2018,
    "country": "Thailand",
    "description": "",
    "url": "https://www.bitkub.com",
    "image": "https://assets.coingecko.com/markets/images/249/small/bitkub.png?1537180687",
    "has_trading_incentive": False,
    "trust_score": 8,
    "trust_score_rank": 37,
    "trade_volume_24h_btc": 2188.5185648437964,
    "trade_volume_24h_btc_normalized": 2188.5185648437964
  },
  {
    "id": "coinstore",
    "name": "Coinstore",
    "year_established": 2020,
    "country": "Singapore",
    "description": "Coinstore was founded in 2020. There are 180 employees worldwide distributed mainly in Asia, Europe, and the Middle East, serving more than 1,500,000 registered users in 175 countries. Coinstore provides global users with fast and smooth cryptocurrency trading services, derivatives business, OTC services, and NFT services. Coinstore Labs provides project owners with integrated solutions of 'technology development, compliance counseling, integrated marketing, community operations, investment incubation' and much more.\r\n\r\nCoinstore supports 102 spot pairs and 34 futures pairs. All features are available on Coinstore's mobile app for iOS and Android, and on desktop.",
    "url": "https://www.coinstore.com/#/",
    "image": "https://assets.coingecko.com/markets/images/747/small/coinstore.jpeg?1639530357",
    "has_trading_incentive": False,
    "trust_score": 8,
    "trust_score_rank": 38,
    "trade_volume_24h_btc": 6663.283770537396,
    "trade_volume_24h_btc_normalized": 1881.8450364634664
  },
  {
    "id": "coinex",
    "name": "CoinEx",
    "year_established": 2017,
    "country": "United Kingdom",
    "description": "",
    "url": "https://www.coinex.com/",
    "image": "https://assets.coingecko.com/markets/images/135/small/coinex.jpg?1527737297",
    "has_trading_incentive": False,
    "trust_score": 8,
    "trust_score_rank": 39,
    "trade_volume_24h_btc": 1691.8645810178261,
    "trade_volume_24h_btc_normalized": 1691.8645810178261
  },
  {
    "id": "bitso",
    "name": "Bitso",
    "year_established": 2014,
    "country": "Mexico",
    "description": "",
    "url": "https://bitso.com",
    "image": "https://assets.coingecko.com/markets/images/8/small/Bitso-icon-dark.png?1581909156",
    "has_trading_incentive": False,
    "trust_score": 8,
    "trust_score_rank": 40,
    "trade_volume_24h_btc": 1580.8222804658253,
    "trade_volume_24h_btc_normalized": 1580.8222804658253
  },
  {
    "id": "okcoin",
    "name": "Okcoin",
    "year_established": 2013,
    "country": "United States",
    "description": "About OKCoin:\r\nOKCoin is one of the largest and most trusted fiat-to-crypto trading platforms in the world. Founded in 2013, OKCoin offers advanced features for crypto beginners and high-volume traders alike, enabling users in 184 countries worldwide to exchange US dollars and the euro for Bitcoin, Tethers, USDK, Bitcoin Cash, Ethereum, Ethereum Classic, Decred, EOS, Litecoin, XRP, Cardano, 0x, Stellar, Zcash, TRX, and other digital assets. As a registered Money Services Business (MSB) with the Financial Crimes Enforcement Network (FinCEN) and a Virtual Financial Asset Act (VFAA) exchange with a transitory provision permissioned by the Malta Financial Services Authority, OKCoin is on a mission to make digital assets accessible to the world while complying with the highest of regulatory standards. For more information, visit www.okcoin.com. ",
    "url": "https://www.okcoin.com/",
    "image": "https://assets.coingecko.com/markets/images/415/small/okcoin_Logomark_SatoshiBlack.png?1619574335",
    "has_trading_incentive": False,
    "trust_score": 8,
    "trust_score_rank": 41,
    "trade_volume_24h_btc": 1431.4963091849143,
    "trade_volume_24h_btc_normalized": 1364.3338053473362
  },
  {
    "id": "bitbank",
    "name": "Bitbank",
    "year_established": 2016,
    "country": "Japan",
    "description": "",
    "url": "https://bitbank.cc/",
    "image": "https://assets.coingecko.com/markets/images/122/small/bitbank.jpg?1521186278",
    "has_trading_incentive": False,
    "trust_score": 8,
    "trust_score_rank": 42,
    "trade_volume_24h_btc": 1235.3946615922532,
    "trade_volume_24h_btc_normalized": 1235.3946615922532
  },
  {
    "id": "independent_reserve",
    "name": "Independent Reserve",
    "year_established": 2013,
    "country": "Australia",
    "description": "",
    "url": "https://www.independentreserve.com/",
    "image": "https://assets.coingecko.com/markets/images/389/small/x_V5Jquo_400x400.png?1556071437",
    "has_trading_incentive": False,
    "trust_score": 8,
    "trust_score_rank": 43,
    "trade_volume_24h_btc": 1349.2385834470874,
    "trade_volume_24h_btc_normalized": 1081.206295062522
  },
  {
    "id": "bittrex",
    "name": "Bittrex",
    "year_established": 2014,
    "country": "United States",
    "description": "",
    "url": "https://bittrex.com/",
    "image": "https://assets.coingecko.com/markets/images/10/small/BG-color-250x250_icon.png?1596167574",
    "has_trading_incentive": False,
    "trust_score": 8,
    "trust_score_rank": 44,
    "trade_volume_24h_btc": 905.8949382963661,
    "trade_volume_24h_btc_normalized": 905.8949382963661
  },
  {
    "id": "nominex",
    "name": "Nominex",
    "year_established": 2019,
    "country": "Seychelles",
    "description": "New trading platform for convenient trading experience with low fees and numerous instruments. \r\n\r\nAbsolutely unique affiliate program that allows to earn from an infinite number of referral levels, compared to 2-3 levels at all other exchanges. \r\n\r\nA unique model for the free 2 phases distribution of the native NMX token.\r\n\r\nAdvanced Trading Instruments – using Stop, Stop Limit, Trailing Stop, Scaled and other types of orders brings some kind of trading automation without the need to develop a trading bot, which allows to easily get more profit while trading.",
    "url": "https://www.nominex.io",
    "image": "https://assets.coingecko.com/markets/images/530/small/logo-200x200.png?1587543672",
    "has_trading_incentive": False,
    "trust_score": 8,
    "trust_score_rank": 45,
    "trade_volume_24h_btc": 1668.5371167583837,
    "trade_volume_24h_btc_normalized": 866.8714652853029
  },
  {
    "id": "max_maicoin",
    "name": "Max Maicoin",
    "year_established": "null",
    "country": "Taiwan",
    "description": "",
    "url": "https://max.maicoin.com",
    "image": "https://assets.coingecko.com/markets/images/218/small/max.jpg?1533888641",
    "has_trading_incentive": False,
    "trust_score": 8,
    "trust_score_rank": 46,
    "trade_volume_24h_btc": 829.450159804647,
    "trade_volume_24h_btc_normalized": 829.450159804647
  },
  {
    "id": "luno",
    "name": "Luno",
    "year_established": 2013,
    "country": "Singapore",
    "description": "",
    "url": "https://www.luno.com",
    "image": "https://assets.coingecko.com/markets/images/33/small/luno.jpg?1519996997",
    "has_trading_incentive": False,
    "trust_score": 8,
    "trust_score_rank": 47,
    "trade_volume_24h_btc": 805.0887261417695,
    "trade_volume_24h_btc_normalized": 805.0887261417695
  },
  {
    "id": "wootrade",
    "name": "WOO Network",
    "year_established": 2019,
    "country": "null",
    "description": "WOO Network is a deep liquidity network connecting traders, exchanges, institutions, and DeFi platforms with democratized access to the best-in-class liquidity and trading execution at lower or zero cost. Its flagship, WOO X, is a professional trading platform featuring customizable modules and lower to zero fees complete with deep liquidity. WOO Network was founded by Kronos Research, a quantitative trading firm generating $5-10B in daily volume.",
    "url": "https://woo.org/",
    "image": "https://assets.coingecko.com/markets/images/683/small/wootrade.jpg?1624621149",
    "has_trading_incentive": False,
    "trust_score": 8,
    "trust_score_rank": 48,
    "trade_volume_24h_btc": 2893.335260584398,
    "trade_volume_24h_btc_normalized": 699.132769044492
  },
  {
    "id": "indodax",
    "name": "Indodax",
    "year_established": 2014,
    "country": "Indonesia",
    "description": "",
    "url": "https://indodax.com",
    "image": "https://assets.coingecko.com/markets/images/3/small/logogram-Indodax-new-_JPG_format.jpg?1580974378",
    "has_trading_incentive": False,
    "trust_score": 8,
    "trust_score_rank": 49,
    "trade_volume_24h_btc": 467.59536774419956,
    "trade_volume_24h_btc_normalized": 467.59536774419956
  },
  {
    "id": "itbit",
    "name": "itBit",
    "year_established": 2013,
    "country": "United States",
    "description": "null",
    "url": "https://www.itbit.com/",
    "image": "https://assets.coingecko.com/markets/images/26/small/itbit.png?1519810172",
    "has_trading_incentive": False,
    "trust_score": 8,
    "trust_score_rank": 50,
    "trade_volume_24h_btc": 463.74923950345953,
    "trade_volume_24h_btc_normalized": 463.74923950345953
  },
  {
    "id": "bitopro",
    "name": "BitoPro",
    "year_established": 2018,
    "country": "Taiwan",
    "description": "",
    "url": "https://www.bitopro.com/",
    "image": "https://assets.coingecko.com/markets/images/358/small/bitopro_coingecko_250x250_%281%29.png?1575884378",
    "has_trading_incentive": False,
    "trust_score": 8,
    "trust_score_rank": 51,
    "trade_volume_24h_btc": 314.5215722106434,
    "trade_volume_24h_btc_normalized": 314.5215722106434
  },
  {
    "id": "bitpanda",
    "name": "Bitpanda Pro",
    "year_established": 2019,
    "country": "Austria",
    "description": "",
    "url": "https://exchange.bitpanda.com",
    "image": "https://assets.coingecko.com/markets/images/474/small/appicon-ios-pro.png?1622626638",
    "has_trading_incentive": False,
    "trust_score": 8,
    "trust_score_rank": 52,
    "trade_volume_24h_btc": 235.0789255115348,
    "trade_volume_24h_btc_normalized": 235.0789255115348
  },
  {
    "id": "emirex",
    "name": "Emirex",
    "year_established": 2014,
    "country": "United Arab Emirates",
    "description": "Emirex was launched in 2014 and became a network of enterprises using blockchain technology to ease asset trading and completely disrupt how people use crypto. Dubai, UAE, is a dynamic destination for Eastern and Western companies, and it's where Emirex helped develop a crypto culture. Emirex is an exchange and marketplace for trading digital assets that improve economic freedom by developing censorship-resistant public networks. Emirex has grown tremendously with its business and is eager to develop even more.\r\n \r\nThe EMRX Token\r\n\r\nEmirex offers B2C, B2B, and B2E payments and boasts over 20,000 active clients and a $10 million monthly income after growing 40-fold in a year. The exchange has over $25 million in daily volume. EMRX, the exchange's token, quadrupled last year due to ecosystem integration and active use. As the Emirex Ecosystem's native token, EMRX is used for listing fees for tokenized assets, buy/sell transaction fees, custody and servicing fees, and commission and partner incentive programs. You can also stake EMRX and other tokens to earn Ultra High APR on your tokens and withdraw anytime. Staking is your gateway to passive crypto income! Emirex also launched a tokenization section to help revolutionize the real estate market as well.\r\n\r\nQuick, Simple, Secure\r\n\r\nEmirex is a platform that simplifies, quickens, and secures digital asset trading. Newbies can trade digital assets easily as Emirex offers non-tech users secure, easy, compliant digital asset access on a  professional trading platform supporting AED, USD, and EUR FIATs. Emirex can process 1,000,000 orders per second. Experience speedy order books, extensive trade history, endless markets, and market depth, and make spot, margin, and futures order types. The Emirex Group offers top-tier financial services to bridge the gap between the current and future economic systems.\r\n\r\nWhy You Should Use Emirex\r\n\r\nEmirex simplifies crypto access and makes its site user-friendly. Emirex's UI is straightforward. A knowledge base guides newcomers through exchange operations. Emirex offers deep liquidity, hundreds of token pairs, and multiple trading orders. You won't get lost with Emirex's security, the convenience of access, and helpful experts. Receive and send tokens without an intermediary. Copy or Social trading lets you imitate the top traders' trades, and Emirex's referral code earns you up to 7% on your friend's and family's transactions.\r\n\r\nTrade Whenever, Wherever\r\n\r\nEmirex provides the most incredible trading experience, allowing you to trade on your terms. We want to help you pleasantly attain your financial goals. Emirex builds crypto economic infrastructure based on user experience and accessibility. The Emirex team launched the Emirex Android to offer all website features in your pocket, including easy bitcoin buying, selling, and trading and 24/7 support with one tap. Emirex makes crypto investment so easy that you'll want to do it all the time!\r\n\r\nSign Up and Keep Up\r\n \r\nSign up now to benefit from Emirex's low to 0% fees. Emirex offers Africa, Asia, and Europe exposure to digital assets and crypto and connects the Middle East with those markets. Decentralization and transparency in blockchain can encourage global value mobility and societal well-being, which is why emirex is dedicated to the digital economy.",
    "url": "https://www.emirex.com/",
    "image": "https://assets.coingecko.com/markets/images/592/small/Emirex.png?1602067691",
    "has_trading_incentive": False,
    "trust_score": 8,
    "trust_score_rank": 53,
    "trade_volume_24h_btc": 66.82718241209282,
    "trade_volume_24h_btc_normalized": 55.53136675020461
  },
  {
    "id": "bitmex_spot",
    "name": "BitMEX",
    "year_established": "null",
    "country": "null",
    "description": "",
    "url": "https://www.bitmex.com/spot/",
    "image": "https://assets.coingecko.com/markets/images/866/small/bitmex.jpeg?1652794708",
    "has_trading_incentive": False,
    "trust_score": 9,
    "trust_score_rank": 54,
    "trade_volume_24h_btc": 45.76622999720636,
    "trade_volume_24h_btc_normalized": 45.76622999720636
  },
  {
    "id": "coin_metro",
    "name": "Coinmetro",
    "year_established": 2018,
    "country": "Estonia",
    "description": "",
    "url": "https://coinmetro.com/",
    "image": "https://assets.coingecko.com/markets/images/386/small/Coinmetro_Exchange_Logo_%282%29.png?1646280101",
    "has_trading_incentive": False,
    "trust_score": 8,
    "trust_score_rank": 55,
    "trade_volume_24h_btc": 33.73314527672247,
    "trade_volume_24h_btc_normalized": 33.73314527672247
  },
  {
    "id": "delta_spot",
    "name": "Delta Exchange",
    "year_established": "null",
    "country": "null",
    "description": "",
    "url": "https://www.delta.exchange/app/spot/trade/",
    "image": "https://assets.coingecko.com/markets/images/642/small/delta_spot.jpg?1617283005",
    "has_trading_incentive": False,
    "trust_score": 8,
    "trust_score_rank": 56,
    "trade_volume_24h_btc": 24.521578297945744,
    "trade_volume_24h_btc_normalized": 24.521578297945744
  },
  {
    "id": "nice_hash",
    "name": "NiceHash",
    "year_established": "null",
    "country": "Slovenia",
    "description": "",
    "url": "https://www.nicehash.com",
    "image": "https://assets.coingecko.com/markets/images/546/small/logo_small_light.png?1637836622",
    "has_trading_incentive": False,
    "trust_score": 8,
    "trust_score_rank": 57,
    "trade_volume_24h_btc": 8.224492202662745,
    "trade_volume_24h_btc_normalized": 8.224492202662745
  },
  {
    "id": "xt",
    "name": "XT.COM",
    "year_established": 2018,
    "country": "Seychelles",
    "description": "By consistently expanding its ecosystem, XT.COM is dedicated to providing users with the most secure, trusted, and hassle-free digital asset trading services. Our exchange is built from a desire to give everyone access to digital assets regardless where you are. \r\n\r\nFounded in 2018, XT.COM now serves more than 6 million registered users, over 500,000+ monthly active users and 40+ million users in the ecosystem. Covering a rich variety of  trading categories together with a NFT aggregated marketplace,  our platform strives to cater to its large user base by providing a secure, trusted and intuitive trading experience.\r\n\r\nAs the world's first social-infused digital assets trading platform, XT.COM also supports social networking platform based transactions to make our crypto services more accessible to users all over the world. Furthermore, to ensure optimal data integrity and security, we see user security as our top priority at XT.COM. ",
    "url": "https://www.xt.com/",
    "image": "https://assets.coingecko.com/markets/images/404/small/logo400x400.png?1575881839",
    "has_trading_incentive": False,
    "trust_score": 7,
    "trust_score_rank": 58,
    "trade_volume_24h_btc": 129983.87850925174,
    "trade_volume_24h_btc_normalized": 38233.536773514235
  },
  {
    "id": "bigone",
    "name": "BigONE",
    "year_established": 2017,
    "country": "Seychelles",
    "description": "",
    "url": "https://bigone.com",
    "image": "https://assets.coingecko.com/markets/images/100/small/qcFFufEY_400x400.jpg?1561103345",
    "has_trading_incentive": False,
    "trust_score": 7,
    "trust_score_rank": 59,
    "trade_volume_24h_btc": 23018.165299005173,
    "trade_volume_24h_btc_normalized": 13330.395663766483
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
    "trust_score": 7,
    "trust_score_rank": 60,
    "trade_volume_24h_btc": 4830.26859296176,
    "trade_volume_24h_btc_normalized": 4830.26859296176
  },
  {
    "id": "coinone",
    "name": "Coinone",
    "year_established": 2016,
    "country": "South Korea",
    "description": "",
    "url": "https://coinone.co.kr/",
    "image": "https://assets.coingecko.com/markets/images/20/small/coinone_circle_500x500.png?1606460853",
    "has_trading_incentive": False,
    "trust_score": 7,
    "trust_score_rank": 61,
    "trade_volume_24h_btc": 4463.503769366247,
    "trade_volume_24h_btc_normalized": 4463.503769366247
  },
  {
    "id": "btse",
    "name": "BTSE",
    "year_established": 2018,
    "country": "British Virgin Islands",
    "description": "BTSE is a leading digital asset exchange that empowers users by offering a simple and secure way to trade. Its growing suite of financial services is designed to bridge traditional finance with digital assets solutions. BTSE's innovative technology offers a set of digital financial solutions featuring multi-currency spot and derivatives trading, in addition to NFT and exchange white labels, over-the-counter (OTC) trading, asset management, and payment gateways. Additionally, BTSE provides an all-in-one order book, strict security protocols, an insurance fund, cold storage for more than 99% of assets and no withdrawal limits on over 12 fiat currencies and 100 cryptocurrencies.",
    "url": "https://www.btse.com/",
    "image": "https://assets.coingecko.com/markets/images/464/small/BTSE.jpg?1568012415",
    "has_trading_incentive": False,
    "trust_score": 7,
    "trust_score_rank": 62,
    "trade_volume_24h_btc": 16386.218513767482,
    "trade_volume_24h_btc_normalized": 3148.777415290165
  },
  {
    "id": "bitcoin_com",
    "name": "FMFW.io",
    "year_established": 2019,
    "country": "Bahamas",
    "description": "The mission of FMFW.io is to empower people from all over the world to trade cryptocurrencies with ease and confidence, from first-time traders to advanced trading professionals. With high liquidity, 24/7 multilingual support and dozens of trading pairs, complemented with a high level of security, we offer an attractive platform for trading any cryptocurrency. Within one year since launch, on average, our exchange has been visited by more than 500K active traders per month, and this number continues to grow as you read this sentence. \r\n\r\nKey Features:\r\n\r\n- Enjoy more than 130 available trading pairs\r\n- Cutting-edge matching engine technologies\r\n- Up 5x and 10x leverage for more than 29 markets\r\n- Deep liquidity\r\n- User-friendly trading terminal\r\n- Tight spreads\r\n- Consistent trading competitions and giveaways",
    "url": "https://fmfw.io/",
    "image": "https://assets.coingecko.com/markets/images/467/small/fmfw.png?1635491491",
    "has_trading_incentive": False,
    "trust_score": 7,
    "trust_score_rank": 63,
    "trade_volume_24h_btc": 63718.50414868675,
    "trade_volume_24h_btc_normalized": 2253.43258631324
  },
  {
    "id": "bullish_com",
    "name": "Bullish",
    "year_established": 2021,
    "country": "Gibraltar",
    "description": "",
    "url": "https://bullish.com/",
    "image": "https://assets.coingecko.com/markets/images/905/small/bullish_com.png?1655198360",
    "has_trading_incentive": False,
    "trust_score": 7,
    "trust_score_rank": 64,
    "trade_volume_24h_btc": 5149.7472882416305,
    "trade_volume_24h_btc_normalized": 1201.8504046744195
  },
  {
    "id": "bitbns",
    "name": "BitBNS",
    "year_established": 2017,
    "country": "Estonia",
    "description": "",
    "url": "https://ref.bitbns.com/",
    "image": "https://assets.coingecko.com/markets/images/541/small/HS7eNJdt_400x400.jpg?1592294824",
    "has_trading_incentive": False,
    "trust_score": 7,
    "trust_score_rank": 65,
    "trade_volume_24h_btc": 807.0038538670199,
    "trade_volume_24h_btc_normalized": 807.0038538670199
  },
  {
    "id": "gmo_japan",
    "name": "GMO Japan",
    "year_established": "null",
    "country": "Japan",
    "description": "",
    "url": "https://coin.z.com/jp/",
    "image": "https://assets.coingecko.com/markets/images/430/small/gmo_z_com.png?1561112572",
    "has_trading_incentive": False,
    "trust_score": 7,
    "trust_score_rank": 66,
    "trade_volume_24h_btc": 577.4416596340494,
    "trade_volume_24h_btc_normalized": 577.4416596340494
  },
  {
    "id": "bitazza",
    "name": "Bitazza",
    "year_established": 2021,
    "country": "null",
    "description": "Bitazza is ASEAN's locally-based digital asset platform. ",
    "url": "https://trade.bitazza.com/gl/exchange/",
    "image": "https://assets.coingecko.com/markets/images/837/small/btzlogo200x200_darkgreen.png?1648702264",
    "has_trading_incentive": False,
    "trust_score": 7,
    "trust_score_rank": 67,
    "trade_volume_24h_btc": 406.9124048562189,
    "trade_volume_24h_btc_normalized": 406.9124048562189
  },
  {
    "id": "kickex",
    "name": "KickEX",
    "year_established": 2020,
    "country": "Estonia",
    "description": "KickEX is the exchange with the lowest trading fees on the market. It's the fastest-growing exchange with amazing iOS and Android apps available in stores. Buy crypto within a minute, trade without risk! Our Support Team will answer all your questions instantly, in 7 different languages. Simple and user-friendly interface and high-quality KickEX mobile apps make our customers' trading more comfortable, without bothering themselves with a long search for information.",
    "url": "https://kickex.com/en",
    "image": "https://assets.coingecko.com/markets/images/635/small/KickEX_logo.png?1652324492",
    "has_trading_incentive": False,
    "trust_score": 7,
    "trust_score_rank": 68,
    "trade_volume_24h_btc": 1760.5892117544827,
    "trade_volume_24h_btc_normalized": 383.79042000332566
  },
  {
    "id": "cryptology",
    "name": "Cryptology",
    "year_established": 2018,
    "country": "Estonia",
    "description": "",
    "url": "https://cryptology.com/",
    "image": "https://assets.coingecko.com/markets/images/287/small/cryptology.png?1541390904",
    "has_trading_incentive": False,
    "trust_score": 7,
    "trust_score_rank": 69,
    "trade_volume_24h_btc": 2332.9667473824284,
    "trade_volume_24h_btc_normalized": 314.99773949573074
  },
  {
    "id": "cex",
    "name": "CEX.IO",
    "year_established": 2013,
    "country": "United Kingdom",
    "description": "",
    "url": "https://cex.io/",
    "image": "https://assets.coingecko.com/markets/images/56/small/main-icon.png?1617267530",
    "has_trading_incentive": False,
    "trust_score": 8,
    "trust_score_rank": 70,
    "trade_volume_24h_btc": 253.4033922895971,
    "trade_volume_24h_btc_normalized": 253.4033922895971
  },
  {
    "id": "lcx",
    "name": "LCX Exchange",
    "year_established": 2020,
    "country": "Liechtenstein",
    "description": "The LCX Exchange Is a Regulated Trading Venue Offering a Range of Digital Currencies. LCX aims to build the new infrastructure for digital finance, focusing on all aspects of compliance and regulation. Investing to build AML and KYC technology solutions at the institutional and consumer level, including on-chain analytics and surveillance for all crypto deposits and withdrawals. LCX is continuously engaging with policy makers, regulators and financial institutions and will routinely participate in financial and security audits, as well as regulatory compliance reviews. In 2020 LCX secured approvals of 8 blockchain registrations with the registration Nr 288159. Allowing LCX to offer the broadest scope of blockchain services – alongside our sophisticated crypto compliance suite.",
    "url": "https://exchange.lcx.com/",
    "image": "https://assets.coingecko.com/markets/images/638/small/LCX.jpg?1616748175",
    "has_trading_incentive": False,
    "trust_score": 7,
    "trust_score_rank": 71,
    "trade_volume_24h_btc": 211.44714181270027,
    "trade_volume_24h_btc_normalized": 211.44714181270027
  },
  {
    "id": "mercado_bitcoin",
    "name": "Mercado Bitcoin",
    "year_established": 2013,
    "country": "Brazil",
    "description": "",
    "url": "https://www.mercadobitcoin.com.br/",
    "image": "https://assets.coingecko.com/markets/images/34/small/logo_MB_hexagono.png?1657255217",
    "has_trading_incentive": False,
    "trust_score": 7,
    "trust_score_rank": 72,
    "trade_volume_24h_btc": 211.45921381756568,
    "trade_volume_24h_btc_normalized": 211.45921381756568
  },
  {
    "id": "korbit",
    "name": "Korbit",
    "year_established": 2013,
    "country": "South Korea",
    "description": "",
    "url": "https://www.korbit.co.kr/",
    "image": "https://assets.coingecko.com/markets/images/28/small/korbit-logo.png?1584091827",
    "has_trading_incentive": False,
    "trust_score": 7,
    "trust_score_rank": 73,
    "trade_volume_24h_btc": 190.76096857207006,
    "trade_volume_24h_btc_normalized": 190.76096857207006
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
    "trust_score_rank": 74,
    "trade_volume_24h_btc": 51.503198268685075,
    "trade_volume_24h_btc_normalized": 51.503198268685075
  },
  {
    "id": "kuna",
    "name": "Kuna Exchange",
    "year_established": "null",
    "country": "United Kingdom",
    "description": "",
    "url": "https://kuna.io/",
    "image": "https://assets.coingecko.com/markets/images/97/small/kuna_exchange.png?1545126178",
    "has_trading_incentive": False,
    "trust_score": 8,
    "trust_score_rank": 75,
    "trade_volume_24h_btc": 48.24209512643461,
    "trade_volume_24h_btc_normalized": 48.24209512643461
  },
  {
    "id": "lbank",
    "name": "LBank",
    "year_established": 2017,
    "country": "British Virgin Islands",
    "description": "LBank Exchange, founded in 2015, is a global trading platform for various crypto assets. LBank Exchange provides its users with crypto trading, specialized financial derivatives, and professional asset management services. It has become one of the most popular and trusted crypto trading platforms with over 7 million users from now more than 210 regions around the world.",
    "url": "https://www.lbank.info/",
    "image": "https://assets.coingecko.com/markets/images/118/small/LBank_logo.png?1666234663",
    "has_trading_incentive": False,
    "trust_score": 7,
    "trust_score_rank": 76,
    "trade_volume_24h_btc": 136984.5170419677,
    "trade_volume_24h_btc_normalized": 63891.26817415411
  },
  {
    "id": "bitforex",
    "name": "Bitforex",
    "year_established": 2018,
    "country": "Seychelles",
    "description": "",
    "url": "https://www.bitforex.com/",
    "image": "https://assets.coingecko.com/markets/images/214/small/BitForex-Logo.png?1573808227",
    "has_trading_incentive": False,
    "trust_score": 6,
    "trust_score_rank": 77,
    "trade_volume_24h_btc": 33477.20589571886,
    "trade_volume_24h_btc_normalized": 25438.05512290839
  },
  {
    "id": "pancakeswap_new",
    "name": "PancakeSwap (v2)",
    "year_established": 2020,
    "country": "null",
    "description": "",
    "url": "https://pancakeswap.finance",
    "image": "https://assets.coingecko.com/markets/images/687/small/pancakeswap.jpeg?1626060212",
    "has_trading_incentive": False,
    "trust_score": 6,
    "trust_score_rank": 78,
    "trade_volume_24h_btc": 9418.800321149847,
    "trade_volume_24h_btc_normalized": 9418.800321149847
  },
  {
    "id": "bitvavo",
    "name": "Bitvavo",
    "year_established": 2018,
    "country": "Netherlands",
    "description": "",
    "url": "https://bitvavo.com/en",
    "image": "https://assets.coingecko.com/markets/images/714/small/bitvavo-mark-square-black.png?1633688872",
    "has_trading_incentive": False,
    "trust_score": 6,
    "trust_score_rank": 79,
    "trade_volume_24h_btc": 4786.131914956154,
    "trade_volume_24h_btc_normalized": 4786.131914956154
  },
  {
    "id": "probit",
    "name": "ProBit Global",
    "year_established": 2017,
    "country": "Seychelles",
    "description": "",
    "url": "https://www.probit.com/",
    "image": "https://assets.coingecko.com/markets/images/370/small/probit.png?1594886584",
    "has_trading_incentive": False,
    "trust_score": 6,
    "trust_score_rank": 80,
    "trade_volume_24h_btc": 3566.8085005501534,
    "trade_volume_24h_btc_normalized": 3566.8085005501534
  },
  {
    "id": "uniswap_v2",
    "name": "Uniswap (v2)",
    "year_established": 2018,
    "country": "null",
    "description": "",
    "url": "https://app.uniswap.org/#/swap?use=V2",
    "image": "https://assets.coingecko.com/markets/images/535/small/256x256_Black-1.png?1590893262",
    "has_trading_incentive": False,
    "trust_score": 6,
    "trust_score_rank": 81,
    "trade_volume_24h_btc": 2648.1481696692285,
    "trade_volume_24h_btc_normalized": 2648.1481696692285
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
    "trust_score_rank": 82,
    "trade_volume_24h_btc": 2143.662108335139,
    "trade_volume_24h_btc_normalized": 2143.662108335139
  },
  {
    "id": "uniswap_v3_optimism",
    "name": "Uniswap (Optimism)",
    "year_established": "null",
    "country": "null",
    "description": "",
    "url": "https://app.uniswap.org/#/swap",
    "image": "https://assets.coingecko.com/markets/images/725/small/uniswap-v3.png?1634896204",
    "has_trading_incentive": False,
    "trust_score": 6,
    "trust_score_rank": 83,
    "trade_volume_24h_btc": 1569.1762624869973,
    "trade_volume_24h_btc_normalized": 1569.1762624869973
  },
  {
    "id": "sushiswap",
    "name": "Sushiswap",
    "year_established": 2020,
    "country": "null",
    "description": "",
    "url": "https://app.sushi.com/swap",
    "image": "https://assets.coingecko.com/markets/images/576/small/2048x2048_Logo.png?1609208464",
    "has_trading_incentive": False,
    "trust_score": 6,
    "trust_score_rank": 84,
    "trade_volume_24h_btc": 2176.174315385006,
    "trade_volume_24h_btc_normalized": 1535.272447367193
  },
  {
    "id": "osmosis",
    "name": "Osmosis",
    "year_established": 2021,
    "country": "null",
    "description": "Osmosis is an automated market maker (AMM) protocol built for liquidity providers. It is built based on the Cosmos SDK and is the first dex for IBC tokens.",
    "url": "https://app.osmosis.zone/",
    "image": "https://assets.coingecko.com/markets/images/684/small/osmosis-dex.jpeg?1624850295",
    "has_trading_incentive": False,
    "trust_score": 6,
    "trust_score_rank": 85,
    "trade_volume_24h_btc": 960.9434790995969,
    "trade_volume_24h_btc_normalized": 960.9434790995969
  },
  {
    "id": "currency",
    "name": "Currency.com",
    "year_established": 2019,
    "country": "Gibraltar",
    "description": "Currency.com is the world's first regulated tokenised securities exchange enabling anyone with crypto and fiat to trade financial assets from the world's biggest companies with up to 500x leverage. \r\n \r\nCurrency.com enables crypto holders to make the most of your investment by offering access to more than 1300 tokenised securities of the most traded global financial assets – all without putting your crypto holdings under price pressure or converting to fiat\" to the following one \"Currency.com enables crypto holders to make the most of your investment by offering access to more than 2000+ tokenised securities of the most traded global financial assets – all without putting your crypto holdings under price pressure or converting to fiat\r\n \r\nWith Currency.com you can:\r\n- Do more with less with up to 500x leverage (or buy and sell assets of your choice);\r\n- Manage your risk with sell at loss, guaranteed sell at loss, take profit orders;\r\n- Elevate your trading strategy with access to over 75 technical indicators;\r\n- Fund your account and withdraw via card, bank transfer or crypto wallet;\r\n- Step ahead of the pack with instant price alerts;\r\n- Never lose more than you put in with negative balance protection;\r\n- Trade confidently with a regulated platform and dedicated human support;\r\n- See where you stand with personalised trading reports.\r\n \r\nCurrency.com offers you a new generation financial app for both crypto and fiat. The free mobile platform is designed to buy and sell cryptos with fiat money, store holdings in a secure place and make cross-crypto exchanges. Competitive quotes are coupled with trusted regulatory standards to give users the best possible financial experience.\r\n \r\nCurrency.com – an exchange where crypto meets Wall St.",
    "url": "https://currency.com/?utm_source=COINGECKO&utm_campaign=listing",
    "image": "https://assets.coingecko.com/markets/images/512/small/Currency.com_200x200.png?1582086630",
    "has_trading_incentive": False,
    "trust_score": 6,
    "trust_score_rank": 86,
    "trade_volume_24h_btc": 10082.71938169726,
    "trade_volume_24h_btc_normalized": 880.16970149399
  },
  {
    "id": "bit_com",
    "name": "Bit.com",
    "year_established": 2020,
    "country": "Seychelles",
    "description": "",
    "url": "https://www.bit.com/",
    "image": "https://assets.coingecko.com/markets/images/823/small/IMAGE_2022-04-01_09_36_23.jpg?1648777125",
    "has_trading_incentive": False,
    "trust_score": 6,
    "trust_score_rank": 87,
    "trade_volume_24h_btc": 4459.961328538348,
    "trade_volume_24h_btc_normalized": 821.7583835426443
  },
  {
    "id": "orca",
    "name": "Orca",
    "year_established": "null",
    "country": "null",
    "description": "",
    "url": "https://www.orca.so/",
    "image": "https://assets.coingecko.com/markets/images/691/small/orca.png?1628047248",
    "has_trading_incentive": False,
    "trust_score": 6,
    "trust_score_rank": 88,
    "trade_volume_24h_btc": 674.7015890357758,
    "trade_volume_24h_btc_normalized": 674.7015890357758
  },
  {
    "id": "quickswap",
    "name": "Quickswap",
    "year_established": 2020,
    "country": "null",
    "description": "Next-gen Layer 2 DEX. Trade at lightning-fast speeds with near-zero gas fees. \r\n",
    "url": "https://quickswap.exchange/#/swap",
    "image": "https://assets.coingecko.com/markets/images/629/small/1_pOU6pBMEmiL-ZJVb0CYRjQ_%281%29.png?1614077691",
    "has_trading_incentive": False,
    "trust_score": 6,
    "trust_score_rank": 89,
    "trade_volume_24h_btc": 610.0487317183257,
    "trade_volume_24h_btc_normalized": 610.0487317183257
  },
  {
    "id": "quickswap_v3",
    "name": "Quickswap (v3)",
    "year_established": 2020,
    "country": "null",
    "description": "",
    "url": "https://quickswap.exchange/#/swap",
    "image": "https://assets.coingecko.com/markets/images/982/small/quickswap.jpeg?1665633994",
    "has_trading_incentive": False,
    "trust_score": 6,
    "trust_score_rank": 90,
    "trade_volume_24h_btc": 550.4766853397606,
    "trade_volume_24h_btc_normalized": 550.4766853397606
  },
  {
    "id": "kanga",
    "name": "Kanga",
    "year_established": "null",
    "country": "null",
    "description": "",
    "url": "https://kanga.exchange/",
    "image": "https://assets.coingecko.com/markets/images/852/small/kanga_logo.png?1650269423",
    "has_trading_incentive": False,
    "trust_score": 6,
    "trust_score_rank": 91,
    "trade_volume_24h_btc": 535.7441600232537,
    "trade_volume_24h_btc_normalized": 535.7441600232537
  },
  {
    "id": "btcmarkets",
    "name": "BTCMarkets",
    "year_established": "null",
    "country": "Australia",
    "description": "",
    "url": "https://www.btcmarkets.net/",
    "image": "https://assets.coingecko.com/markets/images/237/small/btcmarkets-exchange.jpg?1536726060",
    "has_trading_incentive": False,
    "trust_score": 6,
    "trust_score_rank": 92,
    "trade_volume_24h_btc": 494.15234810674315,
    "trade_volume_24h_btc_normalized": 494.15234810674315
  },
  {
    "id": "kyberswap_elastic_polygon",
    "name": "Kyberswap Elastic (Polygon)",
    "year_established": "null",
    "country": "null",
    "description": "",
    "url": "https://kyberswap.com/swap?networkId=137",
    "image": "https://assets.coingecko.com/markets/images/959/small/kyberswap.jpeg?1662616218",
    "has_trading_incentive": False,
    "trust_score": 6,
    "trust_score_rank": 93,
    "trade_volume_24h_btc": 490.296571753911,
    "trade_volume_24h_btc_normalized": 490.296571753911
  },
  {
    "id": "velodrome",
    "name": "Velodrome Finance",
    "year_established": 2022,
    "country": "null",
    "description": "Velodrome Finance, at its core, is a solution for protocols on Optimism to properly incentivize liquidity for their own use cases. Building on top of the groundwork laid out by Solidly, our team has addressed that first iteration's core issues to realize its full potential.\r\n\r\nThe team behind Velodrome Finance previously launched veDAO, an initiative incubated by Information Token. veDAO's founding mandate was to engage with the Solidly ecosystem, a protocol launched on the Fantom network by Andre Cronje, while driving long-term value to the veDAO community.\r\n\r\nThe veDAO team has since developed deep subject matter expertise on both Solidly, the veNFT primitive, and the ve(3,3) mechanism, becoming the go-to resource for protocols and chains seeking support around these topics.",
    "url": "https://app.velodrome.finance/swap",
    "image": "https://assets.coingecko.com/markets/images/933/small/velodrome-finance.png?1660261754",
    "has_trading_incentive": False,
    "trust_score": 6,
    "trust_score_rank": 94,
    "trade_volume_24h_btc": 445.0007104213682,
    "trade_volume_24h_btc_normalized": 445.0007104213682
  },
  {
    "id": "exmarkets",
    "name": "ExMarkets",
    "year_established": 2018,
    "country": "British Virgin Islands",
    "description": "",
    "url": "https://exmarkets.com",
    "image": "https://assets.coingecko.com/markets/images/363/small/42200149_2115011248752220_3911078373144657920_n.jpg?1551247813",
    "has_trading_incentive": False,
    "trust_score": 6,
    "trust_score_rank": 95,
    "trade_volume_24h_btc": 2067.5360501959863,
    "trade_volume_24h_btc_normalized": 397.99941001066423
  },
  {
    "id": "traderjoe",
    "name": "Trader Joe",
    "year_established": "null",
    "country": "null",
    "description": "",
    "url": "https://www.traderjoexyz.com/#/home",
    "image": "https://assets.coingecko.com/markets/images/692/small/traderjoe.png?1628152581",
    "has_trading_incentive": False,
    "trust_score": 6,
    "trust_score_rank": 96,
    "trade_volume_24h_btc": 326.1351659488415,
    "trade_volume_24h_btc_normalized": 326.1351659488415
  },
  {
    "id": "canto_dex",
    "name": "Canto Dex",
    "year_established": "null",
    "country": "null",
    "description": "",
    "url": "https://app.slingshot.finance/trade",
    "image": "https://assets.coingecko.com/markets/images/943/small/canto.jpeg?1661216713",
    "has_trading_incentive": False,
    "trust_score": 6,
    "trust_score_rank": 97,
    "trade_volume_24h_btc": 267.1139685387099,
    "trade_volume_24h_btc_normalized": 267.1139685387099
  },
  {
    "id": "stormgain",
    "name": "Stormgain",
    "year_established": "null",
    "country": "null",
    "description": "StormGain is a crypto trading platform for everyone. It's a convenient solution for those who want to profit from either the growth or decline of the cryptocurrency market and from long-term investments in crypto assets.\r\nAvailable on any device, StormGain allows you to start trading the most popular and most capitalised coins with a multiplier of up to 200x, or you can just buy and hodl crypto.",
    "url": "https://stormgain.com/?utm_id=1DSE&utm_source=coingecko_storm&utm_medium=media&utm_campaign=listing&utm_country=en",
    "image": "https://assets.coingecko.com/markets/images/608/small/CpDGk9Hn_400x400.png?1607582976",
    "has_trading_incentive": False,
    "trust_score": 6,
    "trust_score_rank": 98,
    "trade_volume_24h_btc": 233.04293319692823,
    "trade_volume_24h_btc_normalized": 233.04293319692823
  },
  {
    "id": "vvs",
    "name": "VVS Finance",
    "year_established": 2021,
    "country": "null",
    "description": "",
    "url": "https://vvs.finance/swap",
    "image": "https://assets.coingecko.com/markets/images/736/small/vvs-finance.jpeg?1636702806",
    "has_trading_incentive": False,
    "trust_score": 6,
    "trust_score_rank": 99,
    "trade_volume_24h_btc": 229.9401886806091,
    "trade_volume_24h_btc_normalized": 229.9401886806091
  },
  {
    "id": "dodo_polygon",
    "name": "Dodo (Polygon)",
    "year_established": "null",
    "country": "null",
    "description": "",
    "url": "https://app.dodoex.io/",
    "image": "https://assets.coingecko.com/markets/images/709/small/dodo_logo.png?1633078678",
    "has_trading_incentive": False,
    "trust_score": 5,
    "trust_score_rank": 100,
    "trade_volume_24h_btc": 210.16054923928962,
    "trade_volume_24h_btc_normalized": 210.16054923928962
  }
]

df = pd.DataFrame(data=data)
df=df.drop(['has_trading_incentive','description'], axis=1)
# df['image'] = ["<img src='" + r + '" width ="60" >' for ir, r in df.image.items()]
df['image'] = df.image.apply(lambda x: "<img src='" + x + '" width ="60" >')
#df2 = df[['assests', 'html', 'market']].pivot(index='rank', columns="model", values="html")

print(df.head())

st.set_page_config(page_title="Exchanges", page_icon="💵")
st.checkbox("Use container width", value=False, key="use_container_width")
st.dataframe(df, use_container_width=st.session_state.use_container_width)
#st.write(df.to_html(escape=False), unsafe_allow_html=True)


tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12, tab13, tab14, tab15, tab16, tab17, tab18 = st.tabs(["Bybit","mxc", "Crypto.com", "Bitmax","Gate", "Dextrade", "Poloniex", "BingX", "PhemX", "BTCEX", "P2B", "Hotbit", "Coinstore", "Okcoin", "Nominex", "Wootrade", "Emirex", "XT"])
with tab1: st.write('''Bybit is a cryptocurrency exchange that 
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
with tab2: st.write('''Established in April 2018, MEXC Global is one
         of the world's leading digital-asset trading 
         platforms. The core team comes from world-class 
         enterprises and financial companies with rich 
         experience in blockchain and financial industries.
        ''')
with tab3: st.write('''Crypto.com Exchange is the best place to trade 
         crypto, with deep liquidity, low fees and best 
         execution prices, users can trade major 
         cryptocurrencies like Bitcoin, Ethereum, and 
         many more and receive great CRO-powered rewards
         ''')
with tab4: st.write('''AscendEX (formerly BitMax) is a leading global 
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
with tab5: st.write('''Gate was established in 2013, and it is the top 10
                    exchanges in the world in terms of authentic trading 
                    volume. It is also the first choice of over 8 million
                    registered customers, covering 130+ countries
                    worldwide, as we are providing the most comprehensive
                    digital asset solutions.
                    ''')
with tab6: st.write('''Dex-Trade is a centralized cryptocurrency 
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
with tab7: st.write('''Poloniex was founded in January 2014 as a 
         global cryptocurrency exchange. It provides spot
         trading, futures trading, staking, and various 
         services to users in nearly 100 countries and 
         regions with various languages available. In 2022,
         Poloniex launched a brand new trading system to 
         provide global retail and professional users with 
         higher speed, as well as better stability and 
         usability.
         ''')
with tab8: st.write('''Founded in 2018, BingX is a crypto social 
         trading exchange that offers spot, derivatives 
         and copy trading services to more than 100 
         countries worldwide.BingX prides itself as the
         people's exchange by unlocking the fast-growing 
         cryptocurrency market for everyone, connecting 
         users with experts traders and a platform to 
         invest in a simple, engaging and transparent way.
''')
with tab9: st.write('''Launched in 2019, Phemex is a Singapore-based
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
with tab10: st.write('''BTCEX is a highly extensible digital asset 
         trading platform, which provides spot, spot 
         leverage, futures, perpetual contracts, and 
         USDT-settled options. In addition, it also 
         supports multi-product portfolio margin models 
         to improve the utilization of user funds.
         ''')
with tab11: st.write('''P2B Cryptocurrency Exchange is one of the 
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
with tab12: st.write('''Founded in 2018 and holding Estonian MTR 
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
with tab13: st.write('''Coinstore was founded in 2020. There are 180 
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
with tab14: st.write('''About OKCoin: OKCoin is one of the largest and 
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
with tab15: st.write('''New trading platform for convenient trading 
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
with tab16: st.write('''WOO Network is a deep liquidity network connecting 
                     traders,exchanges, institutions, and DeFi platforms 
                     with democratized access to the best-in-class 
                     liquidity and trading execution at lower or zero 
                     cost. Its flagship, WOO X, is a professional trading
                     platform featuring customizable modules and lower to
                     zero fees complete with deep liquidity. WOO Network 
                     was founded by Kronos Research, a quantitative 
                     trading firm generating $5-10B in daily volume.
                     ''')
with tab17: st.write('''Emirex was launched in 2014 and became a network 
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
with tab18: st.write('''By consistently expanding its ecosystem, XT.COM 
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
 #coins_list = top_ten_list()
coins_list = ["bitcoin","eos","ethereum","litecoin","ripple","cardano","tether","binancecoin","usd-coin","binance-usd","ripple,dogecoin","matic-network","sola-token","staked-ether","shiba-inu,dai","okb,uniswap","stellar","monero","algorand","crypto-com-chain","vechain","decentraland","aave","eos","tezos"]
coin_id = st.sidebar.selectbox('Select a coin: ', coins_list)
