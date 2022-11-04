import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Crypto Dashboard",
        page_icon="./Resources/icons8-cryptocurrency-64.png",
    )

    st.write("# Welcome to Crypto Dashboard! ")

    st.sidebar.success("Select a option above.")

    st.markdown(
        """
        
        """
    )


if __name__ == "__main__":
    run()
