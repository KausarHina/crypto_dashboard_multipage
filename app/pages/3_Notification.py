import datetime
import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
import sqlalchemy as sql
import streamlit as st
from Modules import data as data_utils

# def top_ten_list():
#     top_ten_coins = data_utils.get_top_ten_coins()

#     top_ten_coins_list = top_ten_coins[top_ten_coins['MARKET CAP RANK'] <= 10 ]
#     top_10_coins_name_list = list(top_ten_coins_list['NAME'])
#     return top_10_coins_name_list


def get_coin_data (coin_id):
    
    start_time = 1641042000 # end time 2022-01-01 1pmGMT
    end_time = 1668208735 #now datetime.now()?
  
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart/range?vs_currency=usd&from={start_time}&to={end_time}"
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
    coin_df = df
    pd.options.display.float_format = '{:.2f}'.format
    return coin_id, coin_df
    
    
def indicators (coin_df):
    coin_price_df = coin_df["price"]
    pd.options.display.float_format = '{:.2f}'.format
    return coin_price_df
  
def sma_plot(coin_price_df):  #Simple Moving Average
   sma_df = coin_price_df
   rolling_average = sma_df.loc["price"].rolling(7).mean()
   sma_df["SMA7"] = rolling_average
   #sma_df["SMA20"] = sma_df["price"].rolling(20).mean()
   sma_df.dropna(inplace=True)
   return sma_df

def wma_plot (sma_df):
    sma_df["WMA7"] = sma_df["price"].ewm(7).mean()
    sma_df.dropna(inplace=True)
    sma_wma7_df = sma_df[["price", "SMA7", "WMA7"]]
    return sma_wma7_df
    

def get_sma(prices, rate=7):
        return prices.rolling(rate).mean()

    
def get_bollinger_bands(prices, rate=20):
        sma = get_sma(prices, rate) # <-- Get SMA for 20 days
        std = prices.rolling(rate).std() # <-- Get rolling standard deviation for 20 days
    
        bollinger_up = sma + std * 2 # Calculate top band
        bollinger_down = sma - std * 2 # Calculate bottom band
        return bollinger_up, bollinger_down

    
###########################################################
def notification ():
    st.write("Investment Indicators !!!")
    
    #coins_list = top_ten_list()
    coins_list = ["bitcoin", "ethereum", "tether", "binancecoin", "usd-coin", "binance-usd", "ripple", "cardano", "dogecoin", "matic-network"]
    coin_id = st.sidebar.selectbox('Select a coin: ', coins_list)
    
    #gets historical coin data since 2022/01/01
    coin_id, coin_df = get_coin_data (coin_id)
    st.write('This data table shows the daily price of the coin you chose in the sidebar.')
    st.write (coin_df)

    # displays coin price as a dataframe and line graph
    coin_price_df = indicators (coin_df)
    st.line_chart(coin_price_df)
    st.write(f"Price trend of {coin_id}")
    
    #calculates Simple Moving Average (SMA), displays line chart and expains significance
    sma_df = sma_plot(coin_price_df)
    st.line_chart(sma_df)
    st.write('''
The Simple Moving Average (SMA) is calculated by taking the average price during the time
period of analaysis and dividing by the number of price data point during that time.  
It gives an idea of how the coin is performing in general through time without 
indicating the extremes of the highs and lows.  
As you can see the longer the period of our average the smoother the line.
Because crypto markets are active 24/7 looking at a shorter timeframe for a moving average
gives you a more accurate picture of coin performance.
''')
    

    #calculates Weighted Moving Average (SMA), displays line chart and expains significance
    sma_wma7_df = wma_plot (sma_df)
    st.line_chart(sma_wma7_df)
    st.write('''
The Weighted Moving Average (WMA), also called the Exponential Moving Average, 
uses the SMA in its calculations. The difference is that it gives more weight to recent prices
 in an attempt to make data more responsive to new information. In the plot above,
the green line indicating WMA over 7 days tracks closely to the simple moving average 
for the first 2/3 of 90 days, but then responds quicker to the change in price 
during the last 1/3 of the 90 days.
''')

    #calculates the bollinger bands, displays line chart and explains significance 
    prices = coin_price_df
    bollinger_up, bollinger_down = get_bollinger_bands(prices, rate=20)
    bb_df = prices + bollinger_up + bollinger_down
    st.line_chart(bb_df, x="timestamp", y='price')
    st.write('''
The Bolliger Bands are often used as indicators of buy/sell opportunities. This technical indicator allows traders
to analyze the volatility of a coin and whether the price is high or low on a relative basis.
The top band is typically two standard deviations above the SMA and the bottom band is typically two standard deviations
below the SMA. This means 95% of the high/low price variation fits between these two bands. You can see how they 
form ribbons around the price.
Areas where the blue price line touches or goes below the red, Bollinger low band, are times you would want to consider
buying opportunities, because the price is lower than 95% of it's usual performance.
Areas where the blue, price line touches or goes above the green, Bollinger hight band, are times you would want to 
consider selling opportunities, because the price is higher than 95% of it's usual performance
''')
    
st.set_page_config(page_title="Indicators", page_icon="")
st.markdown("# Indicator Info")
st.sidebar.header("Indicator Info")
st.write(
    """Indicator information """
)

notification()
