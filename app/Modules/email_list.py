import sqlalchemy as sql
import pandas as pd
import streamlit as st


def verify_notification (coins_list):   # verifies whether or not the user wants to receive notifications
        st.sidebar.write('Plese enter your email')
        new_email = st.sidebar.text_input('youremail@gmail.com')
        st.write(f"Your email notification will be sent to: {new_email}")
        coin_choices = coin_choice(coins_list)
        return new_email, coin_choices
   
        
# user selection 4 prefered coins to get notifications about returns list of coin choice
def coin_choice(coins_list):

    coin_choices = st.sidebar.multiselect('Please choose your TOP 4 COINS of interest', coins_list)
    st.sidebar.write('''\n \n''')
    st.sidebar.write('You selected:', coin_choices)
    st.sidebar.write("\n Be sure to check your email for updates!")
    return coin_choices

# function to add emails to df and safe to database    
def add_email_and_coin(new_email, coin_choices):
        dict = {'email':new_email,
        'coin1': coin_choices[1],
        'coin2': coin_choices[2], 
        'coin3': coin_choices[3],
        'coin4': coin_choices[4]}

        email_and_coin_df = pd.DataFrame({dict})
        database_connection_string = 'sqlite:///'
        engine = sql.create_engine(database_connection_string, echo=True)
        email_and_coin_df.to_sql('member_emails_and_coins', engine, index=False, if_exists='append')
        return email_and_coin_df
                
#################################################################

def email_list (coins_list):
    
    new_email, coin_choices = verify_notification(coins_list)
    
    email_and_coin_df = add_email_and_coin(new_email, coin_choices)
    st.sidebar.write(email_and_coin_df)
