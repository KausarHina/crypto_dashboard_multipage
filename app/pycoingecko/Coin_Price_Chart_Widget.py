Bitcoin:
    @st. cache
def get all
Follow link (cmd + click)
url="https://widgets.coingecko.com/coingecko-coin-price-chart-widget.js"
response = rq.get(url)
data = response.json()
parent_path = pathlib.Path(__file_).parent.parent.resolve()
data_path = os.path.join(parent_path,
"data/coins_ids.json")
with open (data path,
'W', encoding='utf-8') as f:
json.dump(data, f, ensure ascii=false, indent=4)
global global_coins_ids_df
global_coins_ids_df = pd.Dataframe(data)
return
html = <script src="https://widgets.coingecko.com/coingecko-coin-price-chart-widget.js"></script>
<coingecko-coin-price-chart-widget  coin-id="bitcoin" currency="usd" height="300" locale="en"></coingecko-coin-price-chart-widget>

Ethereum: 
html = <script src="https://widgets.coingecko.com/coingecko-coin-price-chart-widget.js"></script>
<coingecko-coin-price-chart-widget  coin-id="ethereum" currency="usd" height="300" locale="en"></coingecko-coin-price-chart-widget>

EOS:
html = <script src="https://widgets.coingecko.com/coingecko-coin-price-chart-widget.js"></script>
<coingecko-coin-price-chart-widget  coin-id="eos" currency="usd" height="300" locale="en"></coingecko-coin-price-chart-widget>

Litecoin:
html = <script src="https://widgets.coingecko.com/coingecko-coin-price-chart-widget.js"></script>
<coingecko-coin-price-chart-widget  coin-id="litecoin" currency="usd" height="300" locale="en"></coingecko-coin-price-chart-widget>

Ripple:
html = <script src="https://widgets.coingecko.com/coingecko-coin-price-chart-widget.js"></script>
<coingecko-coin-price-chart-widget  coin-id="ripple" currency="usd" height="300" locale="en"></coingecko-coin-price-chart-widget>


Cardano:
html = <script src="https://widgets.coingecko.com/coingecko-coin-price-chart-widget.js"></script>
<coingecko-coin-price-chart-widget  coin-id="cardano" currency="usd" height="300" locale="en"></coingecko-coin-price-chart-widget>


Polkadot:
html = <script src="https://widgets.coingecko.com/coingecko-coin-price-chart-widget.js"></script>
<coingecko-coin-price-chart-widget  coin-id="polkadot" currency="usd" height="300" locale="en"></coingecko-coin-price-chart-widget>


Tether:
html = <script src="https://widgets.coingecko.com/coingecko-coin-price-chart-widget.js"></script>
<coingecko-coin-price-chart-widget  coin-id="tether" currency="usd" height="300" locale="en"></coingecko-coin-price-chart-widget>



BinanceCoin:
html = <script src="https://widgets.coingecko.com/coingecko-coin-price-chart-widget.js"></script>
<coingecko-coin-price-chart-widget  coin-id="binancecoin" currency="usd" height="300" locale="en"></coingecko-coin-price-chart-widget>


USD Coin: 
html = <script src="https://widgets.coingecko.com/coingecko-coin-price-chart-widget.js"></script>
<coingecko-coin-price-chart-widget  coin-id="usd-coin" currency="usd" height="300" locale="en"></coingecko-coin-price-chart-widget>

Dogecoin:
html = <script src="https://widgets.coingecko.com/coingecko-coin-price-chart-widget.js"></script>
<coingecko-coin-price-chart-widget  coin-id="dogecoin" currency="usd" height="300" locale="en"></coingecko-coin-price-chart-widget>

Polygon:
html = <script src="https://widgets.coingecko.com/coingecko-coin-price-chart-widget.js"></script>
<coingecko-coin-price-chart-widget  coin-id="matic-network" currency="usd" height="300" locale="en"></coingecko-coin-price-chart-widget>