"""
# src/data_cleaning.py
# Este módulo contiene funciones para cargar y limpiar los datos de películas desde un archivo CSV.
# Las funciones incluyen la eliminación de columnas irrelevantes, el manejo de valores nulos, la normalización de datos y la división de columnas en listas.
# Autor: [Kevin Santiago Silva Serna]
# Fecha: [12 de junio de 2025]
# """

import pandas as pd
import re
# -------------------------------------------------------Limpieza de datos-------------------------------------------------------

def cargar_y_limpiar_datos(ruta_archivo = "data/archive/movie_metadata.csv"):
    """
    Carga y limpia los datos de una película desde un archivo CSV.
    Args:
        ruta_archivo (str): Ruta al archivo CSV que contiene los datos de las películas.
    Returns:
        pd.DataFrame: Un DataFrame de pandas con los datos de las películas limpios.
    """
    # Cargar el Archivo CSV
    df = pd.read_csv(ruta_archivo)

    # --------------------------------------------------------Eliminación de columnas y filas nulas--------------------------------------------------------
    # Eliminar columnas nulas
    df = df.drop(columnas_irrelevantes(df), axis=1)
    df = df.dropna(axis=1, how='all')

    # Eliminar filas nulas
    df = df.dropna(how='all')
    df = df.dropna(how='any', subset=listar_columnas_relevantes(df)) # !!! Nota: Esta función debe ser definida antes de su uso
    
    # Reemplazar valores nulos
    df = df.fillna(reemplazo_valores_nulos(df)) # !!! Nota: Esta función debe ser definida antes de su uso
    
    #---------------------------------------------------------------Normalización de datos-----------------------------------------------------------------
    # Nota: Normalización de datos de tipo 'object'
    for col in df.columns:
        if df[col].dtype == 'object':
            # Normalizar minúsculas y espacios en blanco
            df[col] = df[col].str.lower().str.strip()

            # Normalizar caracteres especiales
            df[col] = df[col].str.replace(listar_caracteres_especiales(), '', regex=True)

    # -----------------------------------------------------------------División de datos-------------------------------------------------------------------
    # Dividir la columna 'genres' en una lista de géneros
    # Nota: La columna 'genres' contiene géneros separados por '|'
    df['genres'] = df['genres'].str.split('|')

    # Dividir la columna 'plot_keywords' en una lista de palabras clave
    # Nota: La columna 'plot_keywords' contiene palabras clave separadas por '|'
    df['plot_keywords'] = df['plot_keywords'].str.split('|')

    # Retornar el DataFrame limpio
    return df

#-------------------------------------------------------Metodos de limpieza-------------------------------------------------------
def columnas_irrelevantes(df):
    """
    Lista las columnas irrelevantes del DataFrame.
    args:
        df (pd.DataFrame): DataFrame de pandas con los datos de las películas.
    returns:
        columnas_irrelevantes (list): Una lista de nombres de columnas que son irrelevantes para el dataset.
    """
    # Lista de columnas irrelevantes
    # Nota: Estas columnas no son necesarias para el análisis posterior
    columnas_irrelevantes = {
        'color', 'num_critic_for_reviews', 'num_voted_users', 'gross', 
        'num_user_for_reviews', 'budget', 'movie_imdb_link', 'duration'
    }

    return columnas_irrelevantes

def listar_columnas_relevantes(df):
    """
    Lista las columnas del DataFrame que continen valores nulos.
    args:
        df (pd.DataFrame): DataFrame de pandas con los datos de las películas.
    returns:
        columnas_relevantes (list): Una lista de nombres de columnas que contienen valores nulos y sean necesarias.
    """
    # Lista de columnas que contienen valores nulos y son necesarias
    # Nota: Estas columnas son necesarias para el análisis posterior
    columnas_relevantes = ['movie_title', 'genres', 'plot_keywords', 'imdb_score']

    return columnas_relevantes

def reemplazo_valores_nulos(df):
    """
    Reemplaza los valores nulos en el DataFrame con un valor especifico.
    args:
        df (pd.DataFrame): DataFrame de pandas con los datos de las películas.
    returns:
        valores_reemplazo (dict): Un diccionario con los valores de reemplazo para cada columna. 
    """
    # Tabla de las columnas a reemplazar
    columnas_a_reemplazar = df[['director_name', 'actor_1_name', 'actor_2_name', 'actor_3_name', 'language', 'country', 'content_rating', 'title_year', 'director_facebook_likes', 'actor_1_facebook_likes', 'actor_2_facebook_likes', 'actor_3_facebook_likes', 'cast_total_facebook_likes', 'facenumber_in_poster', 'movie_facebook_likes', 'aspect_ratio']] # <--- Aquí debes especificar las columnas que deseas reemplazar

    # Diccionario para almacenar los valores de reemplazo
    # Reemplazar valores nulos con 0 para columnas numéricas y '' para otras columnas
    valores_reemplazo = {
        col: 0 if pd.api.types.is_numeric_dtype(columnas_a_reemplazar[col]) else ''
        for col in columnas_a_reemplazar.columns
    }

    return valores_reemplazo

def listar_caracteres_especiales():
    """
    Lista los caracteres especiales que se deben eliminar de las columnas de tipo 'object'.
    returns:
        caracteres_especiales (list): Una lista de caracteres especiales que se deben eliminar.
    """
    caracteres_especiales = {
        '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':',
        ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '}', '~'
    }
    return '[' + re.escape(''.join(caracteres_especiales)) + ']'

# -------------------------------------------------------Pruebas unitarias-------------------------------------------------------
"""
if __name__ == "__main__":
    # Cargar y limpiar los datos
    df = cargar_y_limpiar_datos()

    # Mostrar las primeras filas del DataFrame limpio
    print(df.head())

    # Mostrar las columnas del DataFrame limpio
    print(df.columns)

    # Mostrar el número de filas y columnas del DataFrame limpio
    print(f"Número de filas: {df.shape[0]}, Número de columnas: {df.shape[1]}")

    # Mostrar información del DataFrame limpio
    print(df.info())
"""