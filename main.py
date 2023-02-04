import streamlit as st
import src.soporte as sr
import src.viz as viz
import pandas as pd 

df=  pd.read_csv("data/df_languages.csv",index_col=0)

st.header("Endangered Languages")

st.subheader("- Number of Languages ​​in Danger")

degree_df= sr.degree_of_endangered(df)
st.dataframe(degree_df)

viz.pie(degree_df,"Quantity","Degree")
st.image("images/pie_degree.png")


st.subheader("- Top 15 countries with most Endangered Languages")

top_15= sr.popular_countries(df)
st.dataframe(top_15, width = 700, height = 200)
