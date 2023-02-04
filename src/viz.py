from turtle import color
import pandas as pd
from IPython.display import display
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


def hist (df,column):
    plt.figure(figsize = (10,5)) 

    plt.hist(df[column], edgecolor = "black", 
                        facecolor = "#0072BD", 
                        bins = 10)
    plt.xticks(rotation=45, fontsize=12)
    plt.tight_layout()
    plt.savefig("images/barplot.png")
    
#degree= df['endangerment'].value_counts()

def pie(df,column1,column2):

    colors = ['darkorange', 'orangered', 'red', 'firebrick', 'darkred']

    explode = (0.1, 0.1, 0.1, 0.1, 0.1) # para sacar los quesitos hacia fuera

    plt.pie(df[column1], 
       labels = df[column2], 
       colors = colors, # para cambiar el color de la gráfica
       explode = explode)  # para sacar los quesitos hacia fuera

    plt.title("Number of endangered languages") # para poner el título
    plt.legend(bbox_to_anchor=(1.2, 1)) # sacar leyenda y donde colocarla. El primer índice (derecha-izquierda), segundo índice(arriba, abajo) )
    plt.savefig("images/pie_degree.png")
