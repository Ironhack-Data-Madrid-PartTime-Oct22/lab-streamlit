import streamlit as st
import pymongo
from pymongo import MongoClient
import pandas as pd
import numpy as np    


client = MongoClient("mongodb://localhost:27017")

mydb = client["bbdd_etl_recipes"]
coleccion_recipes = mydb.recipes
coleccion_ingredients = mydb.ingredients
coleccion_supermarket = mydb.supermarket


def query_inicial():
    '''
    Query que devuelve los nombres de las recetas para que el usuario pueda seleccionar la que desee
    '''
    filtro_info = pd.DataFrame(coleccion_recipes.find({"RecipeId": {"$exists": True}}, {"etiqueta":1,"_id":0,"Nombre":1}))

    return filtro_info


def query_receta_info(receta_seleccion):
    '''
    Query con la información de la receta seleccionada
    '''
    receta_info = pd.DataFrame(coleccion_recipes.find({"Nombre": {"$eq": receta_seleccion}}, {"etiqueta":1,"_id":0,"Nombre":1,"valoracion":1,"tiempo_preparacion":1, "tiempo_total":1, "imagenes":1}))

    return receta_info


def query_receta_instrucciones(receta_seleccion):
    '''
    Query para extraer las instrucciones de la receta seleccionada
    '''
    receta_inst = pd.DataFrame(coleccion_recipes.find({"Nombre": {"$eq": receta_seleccion}}, {"etiqueta":1,"_id":0,"intrucciones":1}))

    return receta_inst


def query_info(receta_seleccion):
    '''
    Query para extraer el id de la receta 
    '''
    id_info = pd.DataFrame(coleccion_recipes.find({"Nombre": {"$eq": receta_seleccion}}, {"etiqueta":1,"_id":0,"RecipeId":1}))

    return id_info


def query_ingredientes(id_receta):
    '''
    Query para extraer la información de los ingredientes
    '''
    filtro_ingredientes = pd.DataFrame(coleccion_ingredients.find({"RecipeId": {"$eq": id_receta}}, {"etiqueta":1,"_id":0,"raciones":1,"etiqueta_raciones":1,"medida":1,"ingredientes":1,"id_ingrediente":1,"cantidad":1}))

    return filtro_ingredientes



def query_productos(query,iterator):
    '''
    Query para extraer la información de los productos del supermercado que matchean con los ingredientes
    '''
    filtro_productos = pd.DataFrame(coleccion_supermarket.find({"id_ingrediente": {"$eq": f"{query.iloc[iterator, 4]}"}}, {"etiqueta":1,"_id":0,"producto_desc":1,"precio_ud":1}))

    return filtro_productos


def coste_receta(productos_precios):
    '''
    Cálculo del coste del carrito de la compra para realizar la receta según los ingredientes seleccionados por el usuario
    '''
    coste_receta=0

    for i in range(0, len(productos_precios)):
        coste_receta +=  float(productos_precios[i])

    return coste_receta


