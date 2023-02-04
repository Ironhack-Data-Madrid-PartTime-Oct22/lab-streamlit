import pandas as pd 
import sys
import os
from dotenv import load_dotenv
load_dotenv()
import requests
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import warnings


def abrir_csv(path): 
    return pd.read_csv(path, index_col = 0 )

def grafico_barras_1(df_column, xlabel, ylabel, title):
    #grafico de barras con una variable y su conteo
    df_column_count = df_column.value_counts()
    fig, ax = plt.subplots(figsize=(10,5))
    df_column_count.plot(kind='bar', color='green', ax=ax)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    st.pyplot(fig)

def barplot_grupos(df_group, variable_x, groupo_variables, xlabel, ylabel, title):
    df_graf = pd.melt(df_group, id_vars=variable_x, value_vars=groupo_variables)
    fig, ax = plt.subplots(figsize=(10,5))
    sns.barplot(x=variable_x, y='value', hue='variable', data=df_graf, ax=ax)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    plt.legend(loc="upper left", bbox_to_anchor=(1.05, 1), borderaxespad=0)
    st.pyplot(fig)


def token():
    token=os.getenv("token")
    return token
    

def tu_request_ticketmaster(Music_Genre, Countries, df_country, token): 
    events=[]
    dict_event = {"event_name": [], "event_city": [], "event_date": [], "sales_date":[], "min_price":[], "max_price":[], "currency":[], "event_url": [],}
    Genre = Music_Genre
    country= Countries
    countryCode= df_country.loc[country, "Country"]
    token=token
    url = "https://app.ticketmaster.com/discovery/v2/events/"
    params = {"keyword": Genre,
              "countryCode":countryCode,
           "apikey":token}   
    res = requests.get(url,params=params)
    if res.status_code == 200:
        
        events.append(res.json())
        
    try:
        api_events=events[0]['_embedded']["events"]
        for i in range(len(api_events)): 
            dict_event["event_name"].append(api_events[i]['name'])
            dict_event["event_url"].append(api_events[i]['url'])
            dict_event["event_city"].append(api_events[i]["_embedded"]['venues'][0]['city']["name"])
            dict_event["event_date"].append(api_events[i]['dates']["start"]["localDate"])
            dict_event["sales_date"].append(api_events[i]['dates']["start"]["localDate"])
            try:
                dict_event["min_price"].append(api_events[i]['priceRanges'][0]["min"])      
                dict_event["max_price"].append(api_events[i]['priceRanges'][0]["max"])
                dict_event["currency"].append(api_events[i]['priceRanges'][0]["currency"])
            except:
                dict_event["min_price"].append("Unknown")      
                dict_event["max_price"].append("Unknown") 
                dict_event["currency"].append("Unknown")

            df_your_events=pd.DataFrame(dict_event)
    except:
        df_your_events= "Sorry you dont have any events available for you request"
    
    return df_your_events



def filter_price_range(df, min_price, max_price):
    try:
        df.replace("Unknown", float("NaN"), inplace=True)
        df["min_price"] = pd.to_numeric(df["min_price"], errors='coerce')
        df["max_price"] = pd.to_numeric(df["max_price"], errors='coerce')

        filtered_df = df.loc[(df["min_price"] >= min_price) & (df["min_price"] <= max_price) & 
                        (df["max_price"] >= min_price) & (df["max_price"] <= max_price)]
        filtered_df["min_price"].fillna("Unknown", inplace=True)
        filtered_df["max_price"].fillna("Unknown", inplace=True)
        filtered_df["currency"].fillna("Unknown", inplace=True)
    except:
        filtered_df="Sorry you dont have any events available for you request"

    return filtered_df
