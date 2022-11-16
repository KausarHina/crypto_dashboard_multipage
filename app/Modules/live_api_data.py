import pandas as pd
import requests
import json
import sqlalchemy as sql
import schedule
import time

#timer function to call function get_live_data() every 5 minutes
def api_timer(coin_list):
    schedule.every(2).minutes.do(get_live_data(coin_list))
    
    while True:
        schedule.run_pending()
        time.sleep(3)

#function loops through coin list to call api data from coingecko, clean dat and return a dataframe all_coin_info_df
def get_live_data (coin_list):
    all_coiN_info_df = pd.DataFrame()
    try:
        for c in coin_list:
            url = (f'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids={c}&order=market_cap_desc&per_page=10&page=1&sparkline=false&price_change_percentage=1h')
            response = requests.get(url).json()
            all_coiN_info_df = all_coiN_info_df.append(response) 
    except json.JSONDecodeError:
        pass
    finally:
        #cleans dataframe data
        all_coin_info_df = all_coiN_info_df.drop(['image', 'fully_diluted_valuation',
                                 'ath', 'ath_change_percentage', 'ath_date',
                                 'atl', 'atl_change_percentage', 'atl_date', 'roi'], axis=1)
        all_coin_info_df = all_coin_info_df.sort_values(by='market_cap_rank', ascending=True)
        all_coin_info_df = all_coin_info_df.rename(columns = {'index' : 'id'})
        all_coin_info_df["last_updated"] = pd.to_datetime(all_coin_info_df["last_updated"])
        return all_coin_info_df
    
       
def save_coin_data (all_coin_info_df):    #saves all_coin_info_df to sql database appends every call
    database_connection_string = 'sqlite:///'
    engine = sql.create_engine(database_connection_string, echo=True)
    all_coin_info_df.to_sql('coin_info', engine, index=False, if_exists='append')

#######################################################################################

#######################################################################################
def get_save_live_data ():
    coin_list = ["bitcoin" "ethereum", "tether", "binancecoin", "usd-coin", "binance-usd", "ripple", "cardano", "dogecoin", "matic-network"]
    all_coin_info_df = api_timer(coin_list)

    save_coin_data (all_coin_info_df)
    
get_save_live_data()
            