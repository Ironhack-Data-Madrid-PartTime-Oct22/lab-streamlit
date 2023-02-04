
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from skimage import io

import sqlalchemy as alch

from getpass import getpass


def inicio(password, db_name):
    
    # creamos la conexipn con MySQL
    conexion = f"mysql+pymysql://root:{password}@localhost/{db_name}"

    # Crearemos un motor con SQLAlchemy para usara la interfaz común a la base de datos para ejecutar sentencias SQL.
    base = alch.create_engine(conexion)

    return base


def stats(peleadores, base):

    for peleador in peleadores:
        q_1 = f"""

        select peleador, round(((sum(c_sig_str)/sum(i_sig_str))*100), 2) as "SIG. STR.", round(((sum(c_total_str)/sum(i_total_str))*100), 2) as "TOTAL STR.",
        round(((sum(c_td)/sum(i_td))*100), 2) as "TD", round(((sum(c_cabeza)/sum(i_cabeza))*100), 2) as "CABEZA", 
        round(((sum(c_cuerpo)/sum(i_cuerpo))*100), 2) as "CUERPO", round(((sum(c_piernas)/sum(i_piernas))*100), 2) as "PIERNA", 
        round(((sum(c_clinch)/sum(i_clinch))*100), 2) as "CLINCH", round(((sum(c_ground)/sum(i_ground))*100), 2) as "GROUND"
        from se_pelean
        where peleador = "{peleador}";

        """

        df_1 = pd.read_sql(q_1, base)

        q_2 = f"""

        select 100 - round(((sum(c_sig_str)/sum(i_sig_str))*100), 2) as "D. SIG. STR.", 100 - round(((sum(c_total_str)/sum(i_total_str))*100), 2) as "D. TOTAL STR.",
        100 - round(((sum(c_td)/sum(i_td))*100), 2) as "D. TD", 100 - round(((sum(c_cabeza)/sum(i_cabeza))*100), 2) as "D. CABEZA", 
        100 - round(((sum(c_cuerpo)/sum(i_cuerpo))*100), 2) as "D. CUERPO", 100 - round(((sum(c_piernas)/sum(i_piernas))*100), 2) as "D. PIERNA", 
        100 - round(((sum(c_clinch)/sum(i_clinch))*100), 2) as "D. CLINCH", 100 - round(((sum(c_ground)/sum(i_ground))*100), 2) as "D. GROUND"
        from se_pelean
        where combate in (select combate from se_pelean
                        where peleador = "{peleador}") and 
                        peleador != "{peleador}"
        order by combate;

        """

        df_2 = pd.read_sql(q_2, base)


        if peleador == peleadores[0]:
            df_sum1 = pd.concat([df_1, df_2], axis=1)
            df_sum1 = df_sum1.set_index('peleador')
        elif peleador == peleadores[1]:
            df_sum2 = pd.concat([df_1, df_2], axis=1)
            df_sum2 = df_sum2.set_index('peleador')
        
    df_fin = pd.concat([df_sum1, df_sum2], axis=0).T
    
    #-------------------------------------------------------------Gráfica------------------------------------------------------------------
    
    grafic = df_fin.plot.bar(figsize=(20, 10))

    grafic.figure.savefig("images/comparacion_total.png")

def comparate(peleadores, base):
    q_1 = f"""
    select round(((sum(c_sig_str)/sum(i_sig_str))*100), 2) as "sig str", round(((sum(c_total_str)/sum(i_total_str))*100), 2) as "total str",
    round(((sum(c_td)/sum(i_td))*100), 2) as "td", round(((sum(c_clinch)/sum(i_clinch))*100), 2) as "clinch", 
    round(((sum(c_ground)/sum(i_ground))*100), 2) as "ground"
    from se_pelean
    where peleador = "{peleadores[0]}";
    """

    df_1 = pd.read_sql(q_1, base)

    q_2 = f"""
    select round(((sum(c_sig_str)/sum(i_sig_str))*100), 2) as "sig str", round(((sum(c_total_str)/sum(i_total_str))*100), 2) as "total str",
    round(((sum(c_td)/sum(i_td))*100), 2) as "td", round(((sum(c_clinch)/sum(i_clinch))*100), 2) as "clinch", 
    round(((sum(c_ground)/sum(i_ground))*100), 2) as "ground"
    from se_pelean
    where peleador = "{peleadores[1]}";
    """

    df_2= pd.read_sql(q_2, base)


    #-------------------------------------------------------------------Gráfica---------------------------------------------------------------------
    #Creamos una lista con las estadisticas que se van a comparar
    categorias = ['sig_str', 'total_str', 'td' ,'clinch', 'ground']
    
    #Creamos una lista con los argumentos de la primera y con el primer argumento en ultimo lugar par que se cierre gráfica.
    categorias = [*categorias, categorias[0]]
    
    #Creamos una lista con las estadisticas de los peleadores extraidas anteriormente de la BBDD.
    peleador_1 = [df_1["sig str"][0], df_1["total str"][0], df_1["td"][0], df_1["clinch"][0], df_1["ground"][0]]
    peleador_2 = [df_2["sig str"][0], df_2["total str"][0], df_2["td"][0], df_2["clinch"][0], df_2["ground"][0]]
    
    #Creamos una lista con los argumentos de la primera y con el primer argumento en ultimo lugar par que se cierre gráfica.
    peleador_1 = [*peleador_1, peleador_1[0]]
    peleador_2 = [*peleador_2, peleador_2[0]]
    
    #Generamos los angulos en los que se ubicara cada porcentaje, queremos que esten separados de forma uniforme 
    # y para eso utilizamos "linspace".
    angulos = np.linspace(start=0, stop=2 * np.pi, num=len(peleador_1))
    
    #Decidimos el tamaño de la figura.
    plt.figure(figsize=(10, 10))
    
    #Creamos el primer trazado de lineas, correspondiente al primer peleador.
    plt.polar(angulos, peleador_1, 'o-',
              label = f"{peleadores[0]}")
    
    #Creamos el segundo trazado de lineas, correspondiente al segundo peleador peleador.
    plt.polar(angulos, peleador_2, 'o-',
              label = f"{peleadores[1]}")

    # Rellenando las figuras y asignando color
    plt.fill(angulos,peleador_1,alpha=0.5, facecolor='#3386FF')
    plt.fill(angulos,peleador_2,alpha=0.5, facecolor='#FF0000')
    
    #Para asignar los nombres de las estadisticas a los angulos.
    lines, labels = plt.thetagrids(np.degrees(angulos), labels=categorias)
    
    #Generamos ul titulo para la figura.
    plt.title(f"Porcentaje de acierto {peleadores[0]} vs {peleadores[1]}", size=20, y=1.05)
    
    #Y por ultimo generamos una leyenda para la figura.
    plt.legend()
    
    plt.savefig("images/radar.png")



def m_golpeo(peleadores, base):

    q_1 = f"""
    select sum(c_cabeza) as cabeza, sum(c_cuerpo) as cuerpo, sum(c_piernas) as piernas
    from se_pelean
    where w_l = "W" and peleador = "{peleadores[0]}";
    """
    df_1 = pd.read_sql(q_1, base)

    q_2 = f"""
    select sum(c_cabeza) as cabeza, sum(c_cuerpo) as cuerpo, sum(c_piernas) as piernas
    from se_pelean
    where w_l = "W" and peleador = "{peleadores[1]}";
    """
    df_2 = pd.read_sql(q_2, base)



    imagen1 = io.imread("images/cuerpo2.png")/255.0 # imread lee las imagenes con los pixeles codificados como enteros 
    imagen2 = imagen1.copy()
    # en el rango 0-255. Por eso la convertimos a flotante y en el rango 0-1
    fig, ax = plt.subplots(1,2,figsize=(10,10))

    total_1 = df_1["cabeza"]+df_1["cuerpo"]+df_1["piernas"]
    imagen1[:1100,:,0]=1
    imagen1[:1100,:,1]=1-df_1["cabeza"]/total_1
    imagen1[:1100,:,2]=1-df_1["cabeza"]/total_1
    imagen1[1100:4000,:,0]=1
    imagen1[1100:4000,:,1]=1-df_1["cuerpo"]/total_1
    imagen1[1100:4000,:,2]=1-df_1["cuerpo"]/total_1
    imagen1[4000:,:,0]=1
    imagen1[4000:,:,1]=1-df_1["piernas"]/total_1
    imagen1[4000:,:,2]=1-df_1["piernas"]/total_1
    ax[0].imshow(imagen1)
    
    total_2 = df_2["cabeza"]+df_2["cuerpo"]+df_2["piernas"]
    imagen2[:1100,:,0]=1
    imagen2[:1100,:,1]=1-df_2["cabeza"]/total_2
    imagen2[:1100,:,2]=1-df_2["cabeza"]/total_2
    imagen2[1100:4000,:,0]=1
    imagen2[1100:4000,:,1]=1-df_2["cuerpo"]/total_2
    imagen2[1100:4000,:,2]=1-df_2["cuerpo"]/total_2
    imagen2[4000:,:,0]=1
    imagen2[4000:,:,1]=1-df_2["piernas"]/total_2
    imagen2[4000:,:,2]=1-df_2["piernas"]/total_2
    ax[1].imshow(imagen2)

    ax[0].set_title(f"{peleadores[0]}")
    ax[1].set_title(f"{peleadores[1]}")

    plt.savefig("images/golpeo.png")

