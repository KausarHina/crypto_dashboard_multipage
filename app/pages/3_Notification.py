import streamlit as st
import pandas as pd
import numpy as np
import requests
import json
import sqlalchemy as sql
import datetime
import matplotlib.pyplot as plt


coin_id = ["bitcoin", "ethereum", "tether", "binancecoin", "usd-coin", "binance-usd", "ripple", "cardano", "dogecoin", "matic-network"]
#coin_id = st.sidebar.selectbox(label="Select Coin of Interest: ", coin_list)
c = 'bitcoin'

def get_coin_data (coin_id):

    start_time = 1641042000 # end time 2022-01-01 1pmGMT
    end_time = 1668208735 #now datetime.now()?
  
   
    url = f"https://api.coingecko.com/api/v3/coins/{c}/market_chart/range?vs_currency=usd&from={start_time}&to={end_time}"
    response = requests.get(url)
    data = response.json()
    timestamp_list = []
    price_list = []
    for row in data['prices'] :
        timestamp_list.append(datetime.datetime.fromtimestamp(row[0]/1000))
        price_list.append(row[1])
    
    raw_data = {'timestamp': timestamp_list, 'price' : price_list}
    df = pd.DataFrame(raw_data, columns=['timestamp','price'])
    df = df.set_index('timestamp')
    pd.options.display.float_format = '{:.2f}'.format
    return df
    
    
def indicators (df, coin_id, rate):
    prices = df["price"]
  
def sma_plot(df):  #Simple Moving Average
        sma_df = df
        sma_df["SMA7"] = sma_df["price"].rolling(7).mean()
        sma_df.dropna(inplace=True)
        sma_df["SMA20"] = sma_df["price"].rolling(20).mean()
        sma_df.dropna(inplace=True)
        return sma_df
    
#st.line_chart(sma_df)
    
def get_sma(prices, rate):
        return prices.rolling(rate).mean()

    
def get_bollinger_bands(prices, rate=20):
        sma = get_sma(prices, rate) # <-- Get SMA for 20 days
        std = prices.rolling(rate).std() # <-- Get rolling standard deviation for 20 days
    
        bollinger_up = sma + std * 2 # Calculate top band
        bollinger_down = sma - std * 2 # Calculate bottom band
        return bollinger_up, bollinger_down

    # symbol = coin_id
    # daily_prices = df['price']
    #bollinger_up, bollinger_down = get_bollinger_bands(daily_prices)
    
# #plots the daily price with the bollinger bands
#     plt.title(symbol + ' Bollinger Bands for 2022')
#     plt.xlabel('timestamp')
#     plt.ylabel('Daily Prices')
#     plt.plot(daily_prices, label='Daily Price')
#     plt.plot(bollinger_up, label='Bollinger Up', c='g')
#     plt.plot(bollinger_down, label='Bollinger Down', c='r')
#     plt.legend()
#     plt.xticks(rotation = 45)
#     plt.show()

    
    #st.line_chart(daily_prices, bollinger_up, bollinger_down)
    
###########################################################
def notification ():
    st.write("Notification !!!")
    coin_df = get_coin_data (coin_id)
    st.write (coin_df)
   
st.set_page_config(page_title="Notification", page_icon="")
st.markdown("# Notification Info")
st.sidebar.header("Notification Info")
st.write(
    """Notification information """
)

notification()
