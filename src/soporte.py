import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


url_github = "https://github.com/ppastorcarrillo/NASA-ETL-Ironhack"
intro = "###### Este proyecto se centra en la mision del observatorio Kepler, que buscaba planetas dentro de la zona hablitable de las estrellas. Hay 2 tablas de los 10 exoplanetas mas parecidos a la Tierra, por tamaño y temperatura"



"""
'Unnamed: 0.1', 'Unnamed: 0', 'index', 'row', 'name',
       'light years from earth', 'planet mass', 'stellar magnitude',
       'discovery date_x', 'planet type', 'planet radius', 'orbital period',
       'solar system name', 'planet discovery method', 'host temperature (Cº)',
       'host mass', 'host radius', 'Tª type', 'distance type',
       'planet radius [0]', 'indice masa', 'tipo tamaño', 'description',
       'discovery date_y', 'kepid', 'koi_impact', 'koi_prad'],
      dtype='object')
"""

def tabla_1(seleccion):
    df= pd.read_csv("csv/top10temp.csv")

    tab1, tab2 ,tab3, tab4 = st.tabs(["stellar magnitude", "discovery date_x","koi_impact","solar system name"])
    tab1.write(df["stellar magnitude"][df["name"] == seleccion])
    tab2.write(df["discovery date_x"][df["name"] == seleccion])
    tab3.write(df["koi_impact"][df["name"] == seleccion])
    tab4.write(df["solar system name"][df["name"] == seleccion])

def tabla_def():
    tab1_1, tab2_1 ,tab3_1, tab4_1 = st.tabs(["def stellar magnitude", "def discovery date_x","def parametro de impacto"," def solar system name"])
    tab1_1.write("La magnitud aparente cuantifica el brillo de una estrella o cuerpo celeste observado desde la Tierra. En consecuencia, la magnitud aparente depende de la luminosidad del objeto, la distancia observador-objeto y la posible extinción de la luz causada por polvo cósmico.")
    tab2_1.write("Año de descubrimiento")
    tab3_1.write("En física, el parámetro de impacto b se define como la distancia perpendicular entre la trayectoria de un proyectil y el centro de un campo potencial U(r) creado por un objeto al que se acerca el proyectil.")
    tab4_1.write("Sistema solar al que pertence este exoplaneta")


def tabla_2(seleccion):
    df= pd.read_csv("csv/top10temp.csv")

    tab1, tab2 ,tab3, tab4 = st.tabs(["host temperature (Cº)", "masa del exoplaneta","planet radius [0]","planet discovery method"])
    tab1.write(df["host temperature (Cº)"][df["name"] == seleccion])
    tab2.write(df["host mass"][df["name"] == seleccion])
    tab3.write(df["planet radius [0]"][df["name"] == seleccion])
    tab4.write(df["planet discovery method"][df["name"] == seleccion])


def tabla_def_2():
    tab1_1, tab2_1 ,tab3_1, tab4_1 = st.tabs(["def host temperature (Cº)", "def masa del exoplaneta","def planet radius [0]","def planet discovery method"])
    tab1_1.write("Temperatura promedio del exoplaneta en grados centígrados")
    tab2_1.write("Masa del exoplaneta en comparación con la tierra. La Tierra equivale a 1.")
    tab3_1.write("Radio del exoplaneta en comparación con la tierra. La Tierra equivale a 1.")
    tab4_1.write("Modelo de Tránsito: El tránsito se produce cuando un planeta se mueve entre nosotros y la estrella que está orbitando, entonces, el planeta bloquea algo de la luz de la estrella y disminuye la cantidad de luz de la misma. Con este método podemos determinar, entre otros aspecto, el tamaño del exoplaneta.")


   








    























    
