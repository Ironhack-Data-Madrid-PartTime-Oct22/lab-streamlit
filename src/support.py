from src import support
import pandas as pd 
import streamlit as st
import warnings
warnings.filterwarnings("ignore")




def sacar_tripistas:
    df_top_10 = df.nlargest(10, "3PA")

    sns.barplot(x="PLAYER", y="3PA", data=df_top_10)
    plt.xlabel("Jugador")
    plt.ylabel("Triples por partido")
    plt.xticks(rotation = 45)
    st.pyplot()
def maximos_anotadores:
    
    
equipos = df["TEAM"].unique()

fig, ax = plt.subplots()
for equipo in equipos:
    df_equipo = df[df["TEAM"] == equipo]
    max_anotador = df_equipo[df_equipo["PTS"] == df_equipo["PTS"].max()]
    ax.bar(max_anotador["PLAYER"], max_anotador["PTS"], label=equipo)


ax.set_xlabel("Jugador")
ax.set_ylabel("Puntos por partido")
plt.xticks(rotation = 45)
ax.legend()
st.pyplot()