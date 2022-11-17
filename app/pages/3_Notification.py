import datetime
import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
import sqlalchemy as sql
import streamlit as st
from bokeh.plotting import figure
from Modules import data as data_utils
from Modules import email_list as email_utils


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
        dt = datetime.datetime.fromtimestamp(row[0]/ 1000)
        formatted_time = dt.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        timestamp_list.append(formatted_time)
        price_list.append(row[1])
    
    raw_data = {'timestamp': timestamp_list, 'price' : price_list}
    df = pd.DataFrame(raw_data, columns=['timestamp','price'])
    df = df.reset_index()
    df = df.set_index('timestamp')
    #pd.options.display.float_format = '{:.2f}'.format
    return df
 #################
def slice_30day(coin_price_df):
    coin_price_30day_df = coin_price_df.loc['2022-10-01 17:00:00.000'  : '2022-11-10 16:00:00.000']
    return coin_price_30day_df
 # ###################   

def sma_plot(coin_price_30day_df):  #Simple Moving Average
   sma_df = coin_price_30day_df
   rolling_sev_average = sma_df.rolling(7).mean()
   sma_df["SMA7"] = rolling_sev_average
   #rolling_twen_average = sma_df.rolling(20).mean()
   #sma_df["SMA20"] = rolling_twen_average
   sma_df.dropna(inplace=True)
   return sma_df


def wma_plot (sma_df):
    sma_df["WMA7"] = sma_df.price.ewm(7).mean()
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
    st.markdown("## Price Trend")
    
    #coins_list = top_ten_list()
    coins_list = ["bitcoin", "ethereum", "tether", "binancecoin", "usd-coin", "binance-usd", "ripple", "cardano", "dogecoin", "matic-network"]
    coin_id = st.sidebar.selectbox('Select a coin: ', coins_list)
    
    #gets historical coin data current date to time (-) delta
    coin_df = get_coin_data (coin_id)  

    # displays coin price in line chart
    coin_price_df =pd.DataFrame(coin_df.price)  
    st.markdown('This data table shows the **daily price** of the **coin** you chose in the **sidebar**.')
    st.markdown(f'{coin_id} Price Trend')
    st.line_chart(coin_price_df)
############
    coin_price_30day_df = slice_30day(coin_price_df)
    st.markdown("**Let's take a closer look**")
    st.markdown(f'**{coin_id} Price Trend Last 30 Days**')
    st.line_chart(coin_price_30day_df)
##############    
    #calculates Simple Moving Average (SMA), displays line chart and expains significance
    sma_df = sma_plot(coin_price_30day_df)

    st.markdown('## Simple Moving Average!')
    st.markdown(f'**{coin_id} SMA over Last 30 Days**')
    st.line_chart(sma_df)
    with st.expander("See details of chart significance"):
        st.write('''The Simple Moving Average (SMA) is calculated by taking the average price during a specified period of time,
        divided by the number of price points during that time.  It gives an idea of how the coin performing through time 'on average',
        without indicating the extremes of the highs and lows.  \n
        * The longer the period of time over which you are averaging, the smoother the line - 7-days vs 12 days.
        Because crypto markets are active 24/7 looking at a moving average over a shorter 
        timeframe cleagives you a more accurate picture of coin performance.
        ''')
    

    #calculates Weighted Moving Average (SMA), displays line chart and expains significance
    sma_wma7_df = wma_plot (sma_df)
    sma_wma7_plot = sma_wma7_df.loc['2022-09-01 17:00:00.000'  : '2022-11-10 16:00:00.000']
    

    st.markdown('## Weighted vs Simple Moving Average!')
    st.markdown(f'**{coin_id} WMA vs SMA over Last 30 Days**')
    st.line_chart(sma_wma7_plot)
    with st.expander("See details of chart significance"):
        st.write('''The Weighted Moving Average (WMA), also called the Exponential Moving Average, uses the SMA in its 
        calculations. The difference is, it gives more weight to recent prices in an attempt to make data more responsive 
        to new information. \n
        * In the plot above, the light blue line indicating WMA over 7 days tracks closely 
        to the simple moving average for the first 2/3 of the plot, but then responds quicker 
        to the change in price during the last 1/3 of the plotted time period.
        ''')

    #calculates the bollinger bands, displays line chart and explains significance 
    prices = coin_price_df.price
    bollinger_up, bollinger_down = get_bollinger_bands(prices, rate=20)
    new_df = pd.DataFrame()

    new_df['prices'] = prices
    new_df['bollinger_up'] = bollinger_up
    new_df['bollinger_down'] = bollinger_down
    new_df = new_df.dropna()

    st.markdown('# Bollinger Bands!')
    st.markdown(f'**{coin_id} Bollinger Bands since Jan 2022**')
    st.line_chart(new_df)
    with st.expander("See details of chart significance"):
        st.write('''
        The Bolliger Bands are often used as indicators of buy/sell opportunities. \n 
        This technical indicator allows traders to analyze the volatility of a coin and whether the price is high or low on a relative basis. \n
        The top band is typically two standard deviations above the SMA, \n
        and the bottom band is typically two standard deviations below the SMA. \n
        This means 95% of the high/low price variation fits between these two bands. You can see how they form ribbons around the price.
        * Areas where the red 'price' line touches or goes below the dark blue 'bollinger down' band, are considered buying opportunities,\n
          because the price is lower than 95% of it's usual performance. 
        * Areas where the red 'price' line touches or goes above the light blue, 'bollinger up' band, are considered selling opportunities,\n
          because the price is higher than 95% of it's usual performance
        ''')
    
    #side bar checkbox widget to verify -get email notifications- calls email list function from Modules
    #to get email address and top 4 coins of choice
    st.sidebar.write('''\n
    \n
    \n''')
    st.sidebar.markdown("# Stay on top of the Latest in Crypto!")
    verify = st.sidebar.checkbox("Yes! I want email notifications!")
    if verify:
        email_and_coin_df = email_utils.email_list(coins_list)

    


st.set_page_config(page_title="Indicators", page_icon="")
st.markdown("# Indicator Info")
st.sidebar.header("Indicator Info")
st.markdown('***Trading Indicators*** ')
st.markdown('''*statistics often used in evaluating buy/sell opportunities in cryptocurrency*\n
-- Price Trend -- Simple Moving Average --  Weighted Moving Average --  Bollinger Bands --''')


notification()
