import requests
import pandas as pd
url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false&price_change_percentage=1m%2C1h%2C24h%2C7d'
r = requests.get(url)
df = pd.DataFrame(r.json())
symbols = ['btc', 'eth', 'bnb', 'xrp', 'ada','sol','dot','luna','AVAX','doge','shib','matic',
'ltc','atom','link','near','trx','algo','bch','ftt','xlm','ftm','uni','mana','hbar','sand',
'etc','axs','icp','vet','xtz','fil','egld','theta','xmr','klay','hnt','grt','gala','one','eos',
'flow','aave','cake','mkr','qnt','enj','ar','tfuel','xec','stx','neo','ksm','zec','amp','rune',
 'cvx','bat','celo','lrc','crv','rose','chz','dash','waves','scrt','slp','snx','mina']
df[df.symbol.isin(symbols)].nlargest(10,'market_cap').symbol.to_list()
