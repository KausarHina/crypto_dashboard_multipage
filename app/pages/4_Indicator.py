import datetime
import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
import sqlalchemy as sql
import streamlit as st
import bokeh.models as bk_models
from bokeh.plotting import figure
from bokeh.models import DatetimeTickFormatter
from Modules import data as data_utils
  
  
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
        #formatted_time = dt.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3] 
        formatted_time = dt.strftime('%Y-%m-%d %H')[:-3] #skip the time
        timestamp_list.append(formatted_time)
        price_list.append(row[1])
    raw_data = {'timestamp': timestamp_list, 'price' : price_list}
    df = pd.DataFrame(raw_data, columns=['timestamp','price'])
    df = df.reset_index()
    df = df.set_index('timestamp')
    #pd.options.display.float_format = '{:.2f}'.format
    return df
  
def madf_df(price, slow, fast, smooth):# madf_df finding by data

    exp1 = price.ewm(span = fast, adjust = False).mean()
    exp2 = price.ewm(span = slow, adjust = False).mean()
    
    macd = pd.DataFrame(exp1 - exp2).rename(columns = {'price':'macd'})
    signal = pd.DataFrame(macd.ewm(span = smooth, adjust = False).mean()).rename(columns = {'macd':'signal'})
    hist = pd.DataFrame(macd['macd'] - signal['signal']).rename(columns = {0:'hist'})
    #print(hist.head())
    frames =  [macd, signal, hist]
    df = pd.concat(frames, join = 'inner', axis = 1)
    #print(df)
    return df

def madf_plot(prices,coin_macd):#prices: dataframe of price, coin_macd dataframe from madf_df function
    macd_fig = plt.figure()
    #point the plot to macd_fig
    ax1 = plt.subplot2grid((8,1), (0,0), rowspan = 5, colspan = 1, fig = macd_fig)
    ax2 = plt.subplot2grid((8,1), (5,0), rowspan = 4, colspan = 1, fig = macd_fig)

    ax1.plot(prices)
    ax2.plot(coin_macd['macd'], color = 'grey', linewidth = 1.5, label = 'MACD')
    ax2.plot(coin_macd['signal'], color = 'skyblue', linewidth = 1.5, label = 'SIGNAL')

    for i in range(len(prices)):
        #Hist bar
        if str(coin_macd['hist'][i])[0] == '-':
            ax2.bar(prices.index[i], coin_macd['hist'][i], color = '#ef5350')
        else:
            ax2.bar(prices.index[i], coin_macd['hist'][i], color = '#26a69a')

    plt.legend(loc = 'lower right')
    st.pyplot(macd_fig)

def get_rsi_df(df, periods = 14, ema = True): 
    diff = df.diff()
    up = diff.clip(lower=0)
    down = -1 * diff.clip(upper=0)
    
    if ema == True:
        # Use exponential moving average
        ma_up = up.ewm(com=periods - 1, adjust=True, min_periods = periods).mean()
        ma_down = down.ewm(com=periods - 1, adjust=True, min_periods = periods).mean()
    else:
        # Use simple moving average
        ma_up = up.rolling(window = periods, adjust=False).mean()
        ma_down = down.rolling(window = periods, adjust=False).mean()
    rs = ma_up / ma_down
    rsi = 100 - (100/(1 + rs))
    
    return rsi

def rsi_plot(prices, coin_rsi, coin_name):
    rsi_plot = plt.figure()
    #point the plot to rsi_plot
    ax1 = plt.subplot2grid((10,1), (0,0), rowspan = 5, colspan = 1, fig = rsi_plot)
    ax2 = plt.subplot2grid((10,1), (6,0), rowspan = 5, colspan = 1, fig = rsi_plot)
    
    ax1.plot(prices, linewidth = 2.5)
    ax1_title_str = coin_name.upper() + ' CLOSE PRICE'
    ax1.set_title(ax1_title_str)

    ax2.plot(coin_rsi, color = 'orange', linewidth = 2.5)
    ax2.axhline(30, linestyle = '--', linewidth = 1.5, color = 'grey')
    ax2.axhline(70, linestyle = '--', linewidth = 1.5, color = 'grey')
    ax2_title_str = coin_name.upper() + ' RELATIVE STRENGTH INDEX'
    ax2.set_title(ax2_title_str)
    ax2.set_xlabel("Time", rotation=90)
    st.pyplot(rsi_plot)

def get_indicator_description(indicator_name):
    text = ""
    if indicator_name == "MACD":
        text = "Moving average convergence/divergence is an indicator that shows the relationship between two exponential moving averages.The MACD line is calculated by subtracting the 26-period EMA from the 12-period EMA. The Signal line is a 9-period EMA line. MACD signal trigger to buy or sell when the MACD line crosses above the signal line (to buy) or falls below it (to sell)."
    elif indicator_name == "RSI":
        text = "The Relative Strength Index (RSI) monitors changes in recent price to determine if the price is worth buying or not. RSI fluctuates on a scale  between  0-100. When it reaches a peak and turns down, it identifies a top. When it falls and turns up, it identifies a bottom. If the reading is 70 or above the price is ‘overbought’. If the reading is 30 or below the price ‘oversold'."
    return text

def indicator():

    ######Side bar
    #Coins list
    coins_list = ["bitcoin", "ethereum", "tether", "binancecoin", "usd-coin", "binance-usd", "ripple", "cardano", "dogecoin", "matic-network"]
    coin_id = st.sidebar.selectbox('Select a coin: ', coins_list)
    
    #indicator list
    indicator_list = ["None", "MACD", "RSI"]
    indicator_name = st.sidebar.selectbox('Select a indicator :', indicator_list)

    #page content
    pricetrend_title = "## Price Trend with" + " " + indicator_name
    st.markdown(pricetrend_title)
    info_description = get_indicator_description(indicator_name)
    st.markdown(info_description)

    #find the coin data depend on the indicator's selectbox
    coin_df = get_coin_data (coin_id)
    coin_price_df = pd.DataFrame(coin_df.price)
    prices = coin_price_df.price

    ######### plot
    plt.set_loglevel('WARNING')
    if indicator_name == "MACD":
        coin_macd = madf_df(prices, 26, 12, 9)
        madf_plot(prices, coin_macd)
        #macd_text = "Green bar means "
        #st.markdown(macd_text)
    elif indicator_name == "RSI":
        coin_rsi = get_rsi_df(prices)
        rsi_plot(prices, coin_rsi, coin_id)
        
    ##### intetative plot

    #print(coin_rsi.head())
    #rsi_df = pd.DataFrame()
    #rsi_df['prices'] = prices
    #rsi_df['rsi'] = coin_rsi
    #rsi_df = rsi_df.dropna()
    #print(rsi_df.tail())
    #p = figure(
    #    x_axis_label='Timestamp',
    #    y_axis_label='Price')
    #p.xaxis.major_label_orientation = 90
    #st.line_chart(rsi_df)

    else: #without indicator
        p = figure(
        x_axis_label='Timestamp',
        y_axis_label='Price')
        
        default_df = coin_df['price'] 
        p.xaxis.major_label_orientation = 90
        st.line_chart(default_df)


########
st.set_page_config(page_title="Indicators", page_icon="")
st.markdown("# Indicator")
st.sidebar.header("Indicator")


indicator()
