import streamlit as st
import inspect
import textwrap
import time
import numpy as np
import requests
import pandas as pd
import datetime
import json
import numpy as np
from bokeh.plotting import figure
from utils import show_code
from Modules import data as data_utils
from Modules import styles

#################################################################
#
#
#################################################################
def get_market_chart(coin_name, days):
    
    vs_currency='usd'
    
    if days == '1d' :
        num_of_days=1
    elif days == '7d':
        num_of_days=7
    elif days == '30d':    
        num_of_days=30
    elif days == '90d':    
        num_of_days=90 
    elif days == '1y':    
        num_of_days=365 
    else :   
        num_of_days='max'

    coin_id_df = data_utils.global_coins_ids_df[data_utils.global_coins_ids_df['name'] == coin_name] 
    coin_id = coin_id_df['id'].values.astype(str)
    coin_id_str = str(coin_id).replace('[', '').replace(']', '')
    coin_id_str = str(coin_id_str).replace('\'', '').replace('\'', '')
     
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id_str}/market_chart"
    payload={'vs_currency' : vs_currency, 'days' : num_of_days}
    
    response = requests.get(url, params=payload)
    data = response.json()
    
    timestamp_list = []
    price_list = []
    
    for row in data['prices'] :
        timestamp_list.append(datetime.datetime.fromtimestamp(row[0]/1000))
        price_list.append(row[1])
        
    raw_data = {
        'timestamp': timestamp_list,
        'price' : price_list
    }  
    
    df = pd.DataFrame(raw_data, columns=['timestamp','price']) 
    df = df.reset_index()
    df = df.set_index('timestamp')
    
    return df


#################################################################
#
#
#################################################################
def get_coin_price(coin_id) :
    
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true"
  
    response = requests.get(url)
    data = response.json()
    
    coin_price_df = pd.DataFrame(data)
    coin_price_df = coin_price_df.T   
    pd.options.display.float_format = '{:.2f}'.format
    
    coin_price_df = coin_price_df.reset_index()
    
    coin_price_df = coin_price_df.rename(columns = {'index' : 'id'})
    coin_price_df = coin_price_df.set_index('id')
    
    return coin_price_df

#################################################################
#
#
#################################################################
def get_coin_info(coin_id) :
    
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}?localization=false&tickers=false&market_data=false&community_data=false&developer_data=false&sparkline=false"
    response = requests.get(url)
    data = response.json()
    
    coin_all_info_df = pd.DataFrame([data], columns=['id', 'symbol', 'name', 'asset_platform_id', 'platforms',
       'detail_platforms', 'block_time_in_minutes', 'hashing_algorithm',
       'categories', 'public_notice', 'additional_notices', 'description',
       'links', 'image', 'country_origin', 'genesis_date',
       'sentiment_votes_up_percentage', 'sentiment_votes_down_percentage',
       'market_cap_rank', 'coingecko_rank', 'coingecko_score',
       'developer_score', 'community_score', 'liquidity_score',
       'public_interest_score', 'public_interest_stats', 'status_updates',
       'last_updated'])
    
    coin_info_df = coin_all_info_df.loc[:,['id', 'symbol', 'name', 'market_cap_rank' ]]

    coin_info_df = coin_info_df.set_index('id')
    return coin_info_df

#################################################################
#
#
#################################################################
def get_combined_coin_info(coin_id) :
    
    coin_info_df = get_coin_info(coin_id)
    
    coin_price_df = get_coin_price(coin_id)
    
    combined_info_df = pd.merge(coin_info_df, coin_price_df, on='id')
    
    return combined_info_df

#################################################################
#
#
#################################################################
def round_value(input_value):
    if input_value.values > 1:
        a = float(round(input_value, 2))
    else:
        a = float(round(input_value, 8))
    return a

def coin_price_plot():
   
    top_ten_coins = data_utils.get_top_ten_coins()

    top_ten_coins_list = top_ten_coins[top_ten_coins['MARKET CAP RANK'] <= 10 ]
    top_10_coins_name_list = list(top_ten_coins_list['NAME'])

    coins_list = top_10_coins_name_list
    days_list = ['1d', '7d', '30d', '90d', '1y', 'All']

    coin_id = st.sidebar.selectbox('Coins: ', coins_list)
    days = st.sidebar.selectbox('Time Frame', days_list)

    col1_df = top_ten_coins[top_ten_coins['NAME'] == coin_id ]
 
    coin_name = col1_df['NAME'].values.astype(str)
    coin_name_str = str(coin_name).replace('[', '').replace(']', '')
    coin_name_str = str(coin_name_str).replace('\'', '').replace('\'', '')

    title_str=f" ## {coin_name_str}"
    st.write(title_str, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    col1_name = 'PRICE CHANGE 1H'
    col1_price = round_value(col1_df.PRICE)
    col1_percent = f'{float(col1_df.VARIATION)}%'
    col1.metric(col1_name, col1_price, col1_percent)

    col2_name = "PRICE CHANGE 24H"
    col2_price = round_value(col1_df['PRICE CHANGE 24H'])
    val = col1_df['PRICE CHANGE PERCENTAGE 24H']
    col2_percent = f'{float(val)}%'

    col2.metric(col2_name, col2_price, col2_percent)

    coin_df = get_market_chart(coin_name_str, days)

    title = f"{coin_name_str} Price chart to USD for past {days}"
    p = figure(
        title=title,
        x_axis_label='Timestamp',
        y_axis_label='Price')

    x=coin_df.index
    y=coin_df['price']

    p.line(x, y, legend_label='Price')

    st.bokeh_chart(p, use_container_width=True)
    

st.set_page_config(page_title="CoinInfo", page_icon="📈", layout="wide")
st.markdown("# Coin Info")
st.sidebar.header("Coin Info")
st.write(
    """Crypto coin information and trend"""
)

coin_price_plot()

