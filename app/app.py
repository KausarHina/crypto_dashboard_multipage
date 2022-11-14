import streamlit as st
from streamlit.logger import get_logger
from Modules import data as utils
from Modules.styles import style_table

LOGGER = get_logger(__name__)

def run():
    st.set_page_config(
        page_title="Crypto Dashboard",
        page_icon="./Resources/icons8-cryptocurrency-64.png",
        layout="wide"
    )

    st.write("# Welcome to Crypto Dashboard! ")

    st.sidebar.success("Select a option above.")

    st.markdown(
        """
        
        """
    )

    data_coins_df = utils.get_data(1, coins=None) 
    coins_df = style_table(data_coins_df)

    top_10_coins = data_coins_df.head(10)
    utils.set_top_ten_coins(top_10_coins)
    
    table = st.empty()
    table.write(coins_df.to_html(), unsafe_allow_html=True)   

    utils.get_all_coins() 

    
    

if __name__ == "__main__":
    run()
