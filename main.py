import streamlit as st
import pymongo
from pymongo import MongoClient
import pandas as pd
import numpy as np 

import sys 
sys.path.append("src")
import src.soporte as sp


#Margen de la página

receta_seleccion=st.sidebar.selectbox(
    '**Seleccione una receta:**',
    options=set(sp.query_inicial()["Nombre"]),
    key='macro_options')


df_filtro=sp.query_receta_info(receta_seleccion)[sp.query_receta_info(receta_seleccion)["Nombre"] == receta_seleccion]


valoracion=(df_filtro.iloc[0, 0])
tiempo_preparacion=(df_filtro.iloc[0, 2])
tiempo_total=(df_filtro.iloc[0, 3])
imagen_url=(df_filtro.iloc[0, 4])

st.sidebar.write(f"")
st.sidebar.write(f"")
st.sidebar.write(f":star: Valoración: **{valoracion}**")
st.sidebar.write(f":timer_clock: Tiempo de preparación: **{tiempo_preparacion} min**")
st.sidebar.write(f":cooking: Tiempo total de cocinado: **{tiempo_total} min**")
st.sidebar.write(f"")
st.sidebar.write(f"")
st.sidebar.image(imagen_url, width=290, caption='Imagen del resultado final')


#Cuerpo de la página

title=(f"<p style='font-family:sans-serif; color:#d90429; font-size: 42px;'>{receta_seleccion.capitalize()}</p>")
st.markdown(title, unsafe_allow_html=True)
st.write(f"")

st.subheader(f"Instrucciones e ingredientes:")

instrucciones_filtro=sp.query_receta_instrucciones(receta_seleccion)
instrucciones=(instrucciones_filtro.iloc[0, 0])
st.write(f"{instrucciones}")

id_receta=(sp.query_info(receta_seleccion).iloc[0, 0])

for i in range(0, len(sp.query_ingredientes(id_receta))):
    st.write(f"{sp.query_ingredientes(id_receta).iloc[i, 5]} {sp.query_ingredientes(id_receta).iloc[i, 3]}")

st.write(f"")
st.write(f"")
st.subheader(f"Estimación coste del carrito:")

super_info=(f"<p style='font-family:sans-serif; color:#d90429; font-size: 15px;'>{'Información de precios de productos procedente del Supermercado Ahorramás. El precio se estima según el coste unitario de los productos que contiene la receta, no según las cantidades'}</p>")
st.markdown(super_info, unsafe_allow_html=True)

#id_receta=(sp.query_info(receta_seleccion).iloc[0, 0])


producto_seleccion=[]
productos_precios=[]

for i in range(0, len(sp.query_ingredientes(id_receta))):
    st.write(f"{sp.query_ingredientes(id_receta).iloc[i, 3]}")
    try:
        producto_seleccion=st.selectbox('_Seleccione un producto:_',
        options=set(sp.query_productos(sp.query_ingredientes(id_receta),i)["producto_desc"]),key=f'prod_options{i}')
        productos_precios.append(sp.query_productos(sp.query_ingredientes(id_receta),i)[sp.query_productos(sp.query_ingredientes(id_receta),i)["producto_desc"] == f"{producto_seleccion}"].iloc[0, 1])
    except:
        no_enc=(f"<p style='font-family:sans-serif; color:#2B2D42; font-size: 14px;'>{'🔴 Producto no encontrado'}</p>")
        st.markdown(no_enc, unsafe_allow_html=True)
        pass



st.write(f"")
coste=(f"<p style='font-family:sans-serif; color:#d90429; font-size: 20px;'>{'💶 Coste total:  '+ str(round(sp.coste_receta(productos_precios) ,2)) + ' €'}</p>")
st.markdown(coste, unsafe_allow_html=True)
st.image("imagenes/carrito.png", width=70)  

st.write(f"")

        
