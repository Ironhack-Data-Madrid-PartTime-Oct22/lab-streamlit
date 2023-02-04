import sys
import pandas as pd
import numpy as np
import os
import math

def degree_of_endangered(df):
    degree= df['endangerment'].value_counts()
    degree_df= pd.DataFrame(degree)
    degree_df.reset_index(inplace=True)
    degree_df= degree_df.rename(columns={'index':'Degree',
                                   'endangerment':'Quantity'})
    return degree_df

def popular_countries(df):
    counts_sort=df["countries"].value_counts().sort_values(ascending=False)
    first_15= counts_sort.head(15)
    top15_df= pd.DataFrame(first_15)
    top15_df.reset_index(inplace=True)
    top15_df= top15_df.rename(columns={'index':'Country',
                                   'countries':'Languages'})
    return top15_df


def df_countries(df,country ):
    df_country=df[df['countries'].str.contains(country)]
    return df_country