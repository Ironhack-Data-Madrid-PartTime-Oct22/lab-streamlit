import streamlit as st
import pandas as pd
import src.soporte as sr

df=  pd.read_csv("data/df_languages.csv",index_col=0)

st.write("On this page you can choose the country of which you want to know how many endangered languages it has")
country = st.text_input("Choose a country , the first letter has to be in capitals")
df_country=sr.df_countries(df,country)
st.dataframe(df_country, width = 700, height= 200)

