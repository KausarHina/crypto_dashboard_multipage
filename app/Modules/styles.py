import pandas as pd
import numpy as np
import streamlit as st


def style_table(df):
    '''
    Set style for table view
    Parameters
    ----------
    page : Dataframe
        data to be displayed
    
    Returns
    ---------
    style object
    '''
    
    pd.set_option('display.precision', 3)

    def highlight_max(s):

        if s.dtype == np.object:
            is_neg = [False for _ in range(s.shape[0])]
        else:
            is_neg = s < 0
        return ['color: red;' if cell else 'color: #1a7e00' 
                for cell in is_neg]
        
    cols = [
        'VARIATION (%)',
        'PRICE CHANGE 24H',
        'PRICE CHANGE PERCENTAGE 24H',
        'MARKET CAP CHANGE 24H',
        'MARKET CAP CHANGE PERCENTAGE 24H',
        'HIGH 24H',
        'LOW 24H',
        ]

    names = []

    for col in cols:
        if col in df.columns:
            names.append(col)
        else:
            pass


    df = df.style. \
    set_properties(**{
    'font-size': '11pt',
    'font-family': 'Arial',
    'text-align': 'center',
    'font-weight': 'bold',
    }). \
    set_table_styles([
        dict(selector = 'th', props='text-align: center; font-size: 10pt; border: None'),
        ]). \
    apply(highlight_max, subset=names). \
    format(thousands=","). \
    hide_index(). \
    highlight_max(subset=names, props="color:white; background: rgb(5,62,1); background: linear-gradient(180deg, rgba(5,62,1,1) 0%, rgba(14,136,0,1) 35%, rgba(42,245,0,1) 100%);"). \
    highlight_min(subset=names, props="color:white; background: rgb(62,1,1); background: linear-gradient(180deg, rgba(62,1,1,1) 0%, rgba(136,0,0,1) 35%, rgba(245,0,0,1) 100%);")

    return df