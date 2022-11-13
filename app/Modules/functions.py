import pandas as pd
import requests
import json
from pathlib import Path
import sqlalchemy as sql
import questionary
import schedule
import time

#timer function to run api call every x minutes
coin_list = ["bitcoin", "ethereum", "tether", "binancecoin", "usd-coin", "binance-usd", "ripple", "cardano", "dogecoin", "matic-network"]

def api_timer():
    schedule.every(2).minutes.do(get_live_data(coin_list))
    
    while True:
        schedule.run_pending()
        time.sleep(2)

#function loops through coin list to call api data from coingecko and returns a datafranme all_coin_info_df
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
        def clean_coin_data (all_coinN_info_df):  #cleans dataframe data
            all_coin_info_df = all_coiN_info_df.drop(['image', 'fully_diluted_valuation',
                                 'ath', 'ath_change_percentage', 'ath_date',
                                 'atl', 'atl_change_percentage', 'atl_date', 'roi'], axis=1)
            all_coin_info_df = all_coin_info_df.sort_values(by='market_cap_rank', ascending=True)
            all_coin_info_df = all_coin_info_df.rename(columns = {'index' : 'id'})
            all_coin_info_df.set_index('id', inplace = True)
            all_coin_info_df["last_updated"] = pd.to_datetime(all_coin_info_df["last_updated"])
            return all_coin_info_df
    
       
        def save_coin_data (all_coin_info_df):    #saves all_coin_info_df to sql database
            database_connection_string = 'sqlite:///' #../Resources/all_coin_info.db'
            engine = sql.create_engine(database_connection_string, echo=True)
            # Create a database connection string
            all_coin_info_df.to_sql('coin_info', engine, index=False, if_exists='append')

#####################################################################
#
#
####################################################################


def verify_notification (coin_list):   # verifies whether or not the user wants to receive notifications
    verify = questionary.checkbox("We keep track of market signals indicating potential buy/sell opportunities. Would you like to be added to the notification email list to receive timely updates in crypto coin market changes?", choices=["Yes!", "Not at this time"]).ask()
    if verify == "Yes!":
        new_email = questionary.text("Please enter your email address").ask()
        coin_choice = coin_choice(coin_list)
        return new_email, coin_choice
    else:
        print('Invalid response')
        
        
new_email, coin_choice = verify_notification(coin_list)


# user selection 4 prefered coins to get notifications about returns list of coin choice
def coin_choice(coin_list):
    print("We keep track of market signals indicating potential buy/sell opportunities. Please choose 4 different coins you would like to receive email notifications about.")
    coin1 = questionary.select("Coin 1", choices=coin_list).ask()
    coin2 = questionary.select("Coin 2", choices=coin_list).ask()
    coin3 = questionary.select("Coin 3", choices=coin_list).ask()
    coin4 = questionary.select("Coin 4", choices=coin_list).ask()
    coin_choice = [coin1, coin2, coin3, coin4]
    return coin_choice
coin_choice = coin_choice(coin_list)

# function to add emails to df and safe to database    
def add_email_and_coin(new_email, coin_choice):
        email = []
        email_list = email.append(new_email)
        email_and_coin_df = pd.DataFrame({'Email': [email_list], 'Coin Top 4': [coin_choice]})
        database_connection_string = 'sqlite:///'
        engine = sql.create_engine(database_connection_string, echo=True)
        email_and_coin_df.to_sql('member_emails and coins', engine, index=False, if_exists='append')

#function to coordinate with Marissa's code on what to send in notifications
global email_msg

def notification_body(parameters from Marissa):
    notification_body = f'''
    The world of cypto currency is always changing, keep and eye open for our emails on all the latest changes. 
    Here are the lowest price exchanges for your prefered coins: {coin1}: {exchange1}, {coin1}: {exchange1}, {coin1}: {exchange1},{coin1}: {exchange1}
    '''
    return notificaiton_body
#when we call this function set it = email_msg which fits into my emai_send.py file as body of the email
email_msg = notification_body(parameters from Marissa)


 
