import datetime
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

alcohol = pd.read_csv("data/alcohol.csv", index_col = 0)
alcohol["insert_date"]= pd.to_datetime(alcohol["insert_date"])

st.markdown("""# A todos nos gusta el alcohol... ¿no?
Pero no todo el mundo tiene el ni el mismo paladar ni los mismos gustos🍷
- En esta miniapp puedes selecionar los tipos de alcohol que te gustan🍾
- A continuación se realizará un análisis de la evolución del precio por litro🥂
- Después, juzga por ti mismo los resultados 🍻""")

st.title("¿Qué tipo de alcohol te gusta?")
options = st.multiselect("Selecciona uno o varios tipos de alcohol 👍✨", ["Cerveza", "Vino tinto","Vino blanco", "Vino rosado", "Sangría", "Licores y destilados"])

if len(options) == 0:
    st.stop()

meses = [x for x in range(1,13)]
a2021 = [f"2021-{x}" for x in meses[2:]]
a2022 = [f"2022-{x}" for x in meses[:8]]
a2021.extend(a2022)
dictio = {"Cerveza": {"nombre" : "cervezas", "color" : "gold"},
    "Vino tinto": {"nombre" : "vinos_tintos", "color" : "purple"},
    "Vino blanco": {"nombre" : "vinos_blancos", "color" : "grey"},
    "Vino rosado": {"nombre" : "vinos_rosados", "color" : "salmon"},
    "Sangría": {"nombre" : "sangrias", "color" : "red"},
    "Licores y destilados" : {"nombre" : "destilados_licores", "color" : "skyblue"}}

for tipo in options:
    df = alcohol[alcohol["subcategoria"] == dictio[tipo]["nombre"]]
    dfdatos = df.groupby([df["insert_date"].dt.year, df["insert_date"].dt.month]).mean()
    plt.plot(a2021, dfdatos["reference_price"],
        linewidth = 3,
        marker = "p",
        color = dictio[tipo]["color"],
        label = tipo)
plt.grid(which='major', axis='x', zorder=-1.0)
plt.title("Evolucion del precio promedio")
plt.xlabel("Fecha")
plt.ylabel("Precio medio por litro")
plt.xticks(a2021, a2021, rotation = 45)
plt.legend()
plt.savefig("images/imagen.png")

st.image("images/imagen.png")