import streamlit as st
import src.soporte as sp
import pandas as pd



st.title("NASA-Kepler Ironhack proyect")
st.image("images/NASA_logo.svg.png")
st.markdown("###### Este proyecto se centra en la mision del observatorio Kepler, que buscaba planetas dentro de la zona hablitable de las estrellas.La tabla es de los 10 exoplanetas mas parecidos a la Tierra por temperatura")
st.markdown("###### Puedes encontrar el proyecto aqui: https://github.com/ppastorcarrillo/NASA-ETL-Ironhack")



df= pd.read_csv("csv/top10temp.csv")
lista = df["name"].tolist()
seleccion = st.selectbox('Pick one',lista)
seleccion 


sp.tabla_1(seleccion)

sp.tabla_def()

sp.tabla_2(seleccion)

sp.tabla_def_2()




