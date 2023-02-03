import matplotlib.pyplot as plt

def pie_plot(data):
    
    plt.pie(data["rating"],
        labels = ["Nota del libro", "Nota de la película"],
        colors = ["gold","orange"],
        autopct = "%1.2f%%")
    plt.title("Rating libros vs peliculas")
    plt.legend(bbox_to_anchor=(0.8, 1))
    plt.savefig("imagenes/pie.jpg");