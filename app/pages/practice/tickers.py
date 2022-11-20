import pandas as pd
import sqlalchemy 
import unicorn_binance_websocket_api

engine = sqlalchemy.create_engine('sqlite:///IndexDB.db')

symbols = ['btc', 'eth', 'bnb', 'xrp', 'ada','sol','dot','luna','AVAX','doge','shib','matic',
'ltc','atom','link','near','trx','algo','bch','ftt','xlm','ftm','uni','mana','hbar','sand',
'etc','axs','icp','vet','xtz','fil','egld','theta','xmr','klay','hnt','grt','gala','one','eos',
'flow','aave','cake','mkr','qnt','enj','ar','tfuel','xec','stx','neo','ksm','zec','amp','rune',
 'cvx','bat','celo','lrc','crv','rose','chz','dash','waves','scrt','slp','snx','mina']

symbols = [symbol + 'usdt' for symbol in symbols]
ubwa = unicorn_binance_websocket_api.BinanceWebSocketApiManager(exchange="binance.com")
ubwa.create_stream(['kline_1m'], symbols, output = "UnicornFy")

def SQLimport(data)
    klines = data['kline']
    frame = pd.DataFrame([klines])
    frame.close_price = frame.close_price.astype(float)
    if data['kline']['is_closed']:
        frame.to_sql(frame.symbol[0],engine,index=False,if_exists='append')      
while True:
    data = ubwa.pop_stream_data_from_stream_buffer()
    if data:
        if len(data) > 3:
            SQLimport(data)
            
    while True:
    data = ubwa.pop_stream_data_from_stream_buffer()
    if data:
        if len(data) > 3:
            SQLimport(data)