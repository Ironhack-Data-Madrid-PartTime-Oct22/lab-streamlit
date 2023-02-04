import streamlit as st
import src.support_Oscar as sp
import pandas as pd

st.title("Oscar Awards")

st.image("images/Portada.jpg")

st.header("Want to see the Oscar Nominees and Winners?")

df = sp.open_csv("data/Oscar_clean.csv")

year_ceremony = df["year_ceremony"].unique()
sel_year = st.selectbox("Select a year", year_ceremony)

df_filter = df[df["year_ceremony"] == sel_year]
film = df_filter["film"].unique()
sel_film = st.selectbox("Select a film", film)

st.write("The Nominees and Winners from the choosen film are;")

filtered_df = sp.Film_filter(df, sel_film)
st.dataframe(filtered_df)

st.write("Have it been nominated or won a Golden Globe?")

df2 = sp.open_csv("data/Golden_Globes_clean.csv")

gg = df2[df2["year_ceremony"] == sel_year]

filtered_df = sp.Film_filter(df2, sel_film)

st.dataframe(filtered_df)

st.write("As both of the award has correlation, as shown in the headmap, we could say that if a Golden Globe Nomination or Win, makes you more suitable for the Oscar")

st.image("images/output.png")