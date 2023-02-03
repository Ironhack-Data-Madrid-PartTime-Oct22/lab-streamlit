import streamlit as st
import src.soporte_imagenes as si
import pandas as pd

df = pd.read_csv("datos/pelis_libros.csv", index_col = 0)
st.markdown("# Bienvenido.")

st.write("Introduce el nombre de una pelicula/libro que te guste, y te devolveré la comparación de la nota promedio entre los dos")

names = []
for i in df["Series_Title"]:
    names.append(i)

option = st.selectbox(
    "Elige:", (names))

df2 = df[df["Series_Title"] == option].drop("Series_Title",axis = 1)
df2 = df2.T.reset_index()
df2.columns = ["name","rating"]
si.pie_plot(df2)
st.image("imagenes/pie.jpg")