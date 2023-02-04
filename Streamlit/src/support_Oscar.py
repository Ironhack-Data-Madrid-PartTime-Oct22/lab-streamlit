import streamlit as st
import src.support_Oscar as sp
import pandas as pd

def open_csv(f_path):  
    """ 
    Open a .csv.
    Needs the path.
    Return the df.
    """
    df = pd.read_csv(f_path, sep=',', encoding='UTF-8', index_col=0)
    return df

def Film_filter(df, sel_film):
    """
    Filter the df by film.
    Needs the df.
    return the df filtered
    """
    return df[df["film"] == sel_film]