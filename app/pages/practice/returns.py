import streamlit as st
import pandas as pd
import altair as alt
import sqlalchemy 

database_connection_string = 'sqlite:///IndexDB.db'

engine = sqlalchemy.create_engine(database_connection_string)

st.title('Cryptocurrency Indices')

top_10 = ['btc', 'eth', 'bnb', 'xrp', 'doge', 'ada', 'matic', 'dot', 'shib', 'trx']

def retcalc(cryptolist):
    returns = []
    for coin in top_10:
        df = pd.read_sql((coin+'usdt').upper(), engine)
        ret = df.close_price.pct_change() / len(top_10)
        ret.index = pd.to_datetime(df.kline_close_time, unit ='ms')
        returns.append(ret)
    retfram = pd.concat(returns,axis=1)
    indexseries = 1000*(1+retfram.sum(axis=1)).cumprod()
    indexseries.name = 'Indexvalue'
    return indexseries
    
retcalc(top_10).plot()


stobj = retcalc(top_10).reset_index()

if st.button('Update'):
    stobj = retcalc(top_10).reset_index()
    
def chartcreator(obj):
    chart = alt.Chart(obj).mark_line().encode(
    x='kline_close_time',
    y=alt.Y('Indexvalue',
            scale=alt.Scale(domain=[obj.Indexvalue.min(),
                                obj.Indexvalue.max()]))).properties(width=800)
    return chart
        
st.title('Top 10 Market Caps Index')
st.altair_chart(chartcreator(stobj))
    
    
