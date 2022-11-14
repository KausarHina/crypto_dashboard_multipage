import pandas as pd
import requests as rq
import numpy as np
import streamlit as st
import json
import os
import pathlib

global_top_10_coins_df = pd.DataFrame()
global_coins_ids_df = pd.DataFrame()

def set_top_ten_coins(top_10_coins_df):
    global global_top_10_coins_df
    global_top_10_coins_df = top_10_coins_df
    return

def get_top_ten_coins():
    return global_top_10_coins_df 

@st.cache
def get_all_coins_from_json():

    parent_path = pathlib.Path(__file__).parent.parent.resolve() 
    data_path = os.path.join(parent_path, "data/coins_ids.json")

    data_df = pd.read_json(data_path)
    global global_coins_ids_df 
    global_coins_ids_df = data_df

    return  

@st.cache
def get_all_coins():
    url = "https://api.coingecko.com/api/v3/coins/list?include_platform=false"
    response = rq.get(url)
    data = response.json()
    parent_path = pathlib.Path(__file__).parent.parent.resolve() 
    data_path = os.path.join(parent_path, "data/coins_ids.json")
   
    with open(data_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    global global_coins_ids_df 
    global_coins_ids_df = pd.DataFrame(data)  

    return    


@st.cache
def get_data(page, coins=None):
    '''
    Extract data and transform from API
    Parameters
    ----------
    page : int
        Number used as query parameter
    
    Doc
    ----------
    https://www.coingecko.com/en/api/documentation
    
    Returns
    ---------
    DataFrame
    '''
    
    if coins == None:
        pass
    else:
        coins = str(coins).replace("'", '')

    params = {
    'vs_currency': 'usd',
    'ids': coins,
    'order':'market_cap_desc',
    'per_page':50,
    'page':page,
    'sparkline': False,
    'price_change_percentage': '1h'
    }

    url = 'https://api.coingecko.com/api/v3/coins/markets'

    response = rq.get(url, params=params).json()

    cols = [
        'image',
        'name',
        'symbol',
        'market_cap_rank',
        'current_price',
        'price_change_percentage_1h_in_currency',
        'high_24h',
        'low_24h',
        'market_cap',
        'price_change_24h',
        'price_change_percentage_24h',
        'market_cap_change_24h',
        'market_cap_change_percentage_24h',
        'circulating_supply',
        'last_updated',]

    df = pd.DataFrame(response, columns=cols)
    df['image'] = df['image'].apply(lambda x: '<img src=' + x + ', width=35>')
    rename = {
        'image': 'LOGO',
        'name': 'NAME',
        'symbol': 'SYMBOL',
        'current_price': 'PRICE',
        'price_change_percentage_1h_in_currency': 'VARIATION',
        'high_24h': 'HIGH 24H',
        'low_24h': 'LOW 24H',
        'market_cap': 'MARKET CAP',
        'market_cap_rank': 'MARKET CAP RANK',
        'price_change_24h': 'PRICE CHANGE 24H',
        'price_change_percentage_24h': 'PRICE CHANGE PERCENTAGE 24H',
        'market_cap_change_24h': 'MARKET CAP CHANGE 24H',
        'market_cap_change_percentage_24h': 'MARKET CAP CHANGE PERCENTAGE 24H',
        'circulating_supply': 'CIRCULATING SUPPLY',
        'last_updated': 'LAST UPDATED',
        }

    df = df.rename(columns=rename)
    df['VARIATION'] = df['VARIATION'].fillna(0)
    df['LAST UPDATED'] = pd.to_datetime(df['LAST UPDATED']).dt.strftime('%H:%M:%S')

    for i in df.select_dtypes(include=[np.int64]):
        df[i] = df[i].astype(float)

    return df