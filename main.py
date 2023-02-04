import streamlit as st

#import src.soporte_api as sa
import src.soporte_imagenes as si
import pandas as pd
import numpy as np

st.title("Polluted Countries and their Living Cost")
st.subheader("_Relación entre el coste de vida y los niveles de polución_")
st.image("imagenes/calidad_aire.png")

st.markdown(" - Indicador de contaminación: hace referencia a la contaminación del aire debido a la presencia de sustancias nocivas en la atmósfera que dañan la salud de los seres vivos, clima o materiales.")
st.markdown(" - Coste de vida : indicador formado por consumo de productos básicos (IPC) incluyendo compra , suministros, transporte y restaurantes. Queda excluido el precio de la vivienda.")
st.markdown(" - Indice de natalidad: número de nacimientos ocurridos en un año entre su población total.")


#creación de mapa de Países más contaminados

coordp= pd.read_csv("datos/coord_countries.csv")
st.map(coordp)

#creación de mapa de Ciudades mas contaminadas

coord= pd.read_csv("datos/coord_cities.csv")
st.map(coord)


#Exportamos datos
cof= pd.read_csv("datos/cost_living.csv")
pcoun= pd.read_csv("datos/polluted_countries.csv")
pcit= pd.read_csv("datos/polluted_cities.csv")

#Creación barra lateral y filtros
st.sidebar.header("Opciones para filtrar")

pais= pcoun["Country/Region"].unique().tolist()
ciudad= pcit["City"].unique().tolist()

paises= st.sidebar.multiselect(
    "Selecciona un país 🌍",
    pais)

ciudades= st.sidebar.multiselect(
    "Selecciona una ciudad 📍",
    ciudad)

#Conector

mask= (pcoun["Country/Region"].isin(paises)) & (pcit["City"].isin(ciudades))

resultados= pcoun[mask].shape[0]


#Barra selección año información
opcion2 = st.selectbox( "Año Información",
 ("2020","2019","2018","2017"))



cof1 = pd.read_csv("datos/query3.csv")

st.dataframe(cof1)  # Same as st.write(df)



