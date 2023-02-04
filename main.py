from src import support
import pandas as pd 
import streamlit as st
import warnings
warnings.filterwarnings("ignore")


st.title("Exploración de Jugadores de la NBA")
df = pd.read_csv("datos/NBAPLAYERS.csv")

st.dataframe(df)

import matplotlib.pyplot as plt
import seaborn as sns

st.title("Máximos Anotadores de cada Equipo de la NBA")


    
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


st.title("10 Mejores Triplistas de la NBA")

df_top_10 = df.nlargest(10, "3PA")

sns.barplot(x="PLAYER", y="3PA", data=df_top_10)
plt.xlabel("Jugador")
plt.ylabel("Triples por partido")
plt.xticks(rotation = 45)
st.pyplot()


st.title("Equipos que Anotan más Triples")


df_equipos = df.groupby("TEAM")["3PA"].sum().reset_index()

df_equipos = df_equipos.sort_values("3PA", ascending=False)

sns.barplot(x="TEAM", y="3PA", data=df_equipos.head(10))
plt.xlabel("Equipo")
plt.ylabel("Triples Anotados")
plt.xticks(rotation = 40)
st.pyplot()
