import streamlit as st

def Notification():
   
   st.write("Notification !!!")
   
st.set_page_config(page_title="Notification", page_icon="")
st.markdown("# Notification Info")
st.sidebar.header("Notification Info")
st.write(
    """Notification information """
)

Notification()
