
import streamlit as st
import os
import pandas as pd
import sqlalchemy as alch
import sys
import src.graficas as gr
from dotenv import load_dotenv

load_dotenv()

st.markdown('<h1>Super fight</h1>', unsafe_allow_html=True)

st.image("images/cinturon.png")

name_bd = os.getenv("base_datos")
password = os.getenv("password")
#st.write(name_bd)

base = gr.inicio(password, name_bd)

peleadores = []

col1, col2 = st.columns(2)

with col1:
    peleador_a = st.text_input("Helija el primer luchador para analizar.", "")

with col2:
    peleador_b = st.text_input("Helija el segundo luchador para analizar.", "")


if peleador_a and peleador_b != "":

    with col1:
        q_1 = f"""
        select * from peleador
        where peleador REGEXP "{peleador_a}";

        """
        df_1 = pd.read_sql(q_1, base)

        options = df_1['peleador'].tolist()

        peleador_1 =  st.selectbox("Elige el peleador", options)

        st.write("Has elegido:", peleador_1)

    with col2:
        q_2 = f"""
        select * from peleador
        where peleador REGEXP "{peleador_b}";

        """
        df_2 = pd.read_sql(q_2, base)

        options = df_2['peleador'].tolist()

        peleador_2 =  st.selectbox("Elige el peleador", options)

        st.write("Has elegido:", peleador_2)

    grafic = st.radio("Seleciona la gráfica que quieres analizar 👉", ["radar", "barplot", "img_golpeo"])

    if st.button("Visualizar"):

        peleadores.append(peleador_1)
        peleadores.append(peleador_2)

        if grafic == "radar":
            gr.comparate(peleadores, base)
            st.image("images/radar.png")

        elif grafic == "barplot":
            gr.stats(peleadores, base)
            st.image("images/comparacion_total.png")

        elif grafic == "img_golpeo":
            gr.m_golpeo(peleadores, base)
            st.image("images/golpeo.png")
        else:
            st.write("No se ha podido generar la gráfica 😢😢")
            

else:
    st.write("Generando desplegable...")

