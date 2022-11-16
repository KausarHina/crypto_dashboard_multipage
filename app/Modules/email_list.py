import sqlalchemy as sql
import streamlit as st


def verify_notification (coin_list):   # verifies whether or not the user wants to receive notifications
    print('''We keep track of market signals indicating potential buy/sell opportunities. 
    Would you like to be added to the notification email list to receive timely updates 
    in crypto coin market changes?
    ''')
    verify = st.checkbox("Yes!")
    if verify: 
        st.write('Great! Plese enter your email')
        new_email = st.text_input('youremail@gmail.com')
        st.write("Your email notification will be sent to:", new_email)
        coin_choices = coin_choice(coin_list)
        return new_email, coin_choices
    else:
        print('Invalid response')
        
# user selection 4 prefered coins to get notifications about returns list of coin choice
def coin_choice(coin_list):
    coin_choices = st.multiselect('Please choose your top 4 coins of interest', coin_list)
    st.write('You selected:', coin_choices)
    return coin_choices

# function to add emails to df and safe to database    
def add_email_and_coin(new_email, coin_choices):
        email = []
        email_list = email.append(new_email)
        email_and_coin_df = pd.DataFrame({'Email': [email_list], 'Coin Top 4': [coin_choices]})
        database_connection_string = 'sqlite:///'
        engine = sql.create_engine(database_connection_string, echo=True)
        email_and_coin_df.to_sql('member_emails_and_coins', engine, index=False, if_exists='append')


#################################################################

def email_list ():
    st.write("Email Notifications!!!")
    
    coin_list = ["bitcoin" "ethereum", "tether", "binancecoin", "usd-coin", "binance-usd", "ripple", "cardano", "dogecoin", "matic-network"]
    new_email, coin_choices = verify_notification(coin_list)
    
    add_email_and_coin(new_email, coin_choices)
     
st.set_page_config(page_title="Notifications", page_icon="")
st.markdown("# Notification Info")
st.sidebar.header("Notification Info")
st.write(
    """Notification information """
)

email_list()