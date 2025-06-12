import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#-------------------------------------------------------Sopa de palabras-------------------------------------------------------
def crear_sopa_de_palabras(df):
    """
    Crea una columna de 'sopa' combinando texto clave de las columnas 'genres' y 'plot_keywords'.
    arfs:
        df (pd.DataFrame): DataFrame limpio de pandas con los datos de las películas.
    returns: 
        pd.DataFrame: DataFrame con una nueva columna 'sopa'.
    """

    def unir_listas(lista):
        """
        Une una lista de cadenas en una sola cadena separada por espacios.
        args:
            lista (list): Lista de cadenas.
        returns:
            str: Cadena unida.
        """
        return ' '.join(lista) if isinstance(lista,list) else ''
    
    # Crear la columna 'sopa' combinando en formato de texto las columnas 'genres' y 'plot_keywords'
    df['sopa'] = df['genres'].apply(unir_listas) + ' ' + df['plot_keywords'].apply(unir_listas)

    return df

#-------------------------------------------------------Vectorización de texto-------------------------------------------------------
def vectorizar_texto(df, columna='sopa', metodo='tfidf'):
    """
    Vectoriza la columna 'sopa' utilizando TF-IDF y CountVectorizer.
    args:
        df (pd.DataFrame): DataFrame con la columna 'sopa'.
        columna (str): Nombre de la columna a vectorizar. Por defecto es 'sopa'.
        metodo (str): Método de vectorización a utilizar. Puede ser 'tfidf' o 'count'. Por defecto es 'tfidf'.
    returns:
        vector_matrix (sparse matrix): Matriz resultante de la vectorización.
        vectorizador (object): El objeto vectorizador uzado (TfidfVectorizer o CountVectorizer).
    """
    if metodo == 'tfidf':
        # Usar TfidfVectorizer para vectorizar la columna 'sopa'
        vectorizador = TfidfVectorizer(stop_words='english')
    elif metodo == 'count':
        # Usar CountVectorizer para vectorizar la columna 'sopa'
        vectorizador = CountVectorizer(stop_words='english')
    else:
        # Si el método no es válido, lanzar un error
        raise ValueError("Método de vectorización no válido. Use 'tfidf' o 'count'.")
    
    # Vectorizar la columna 'sopa'
    vector_matrix = vectorizador.fit_transform(df['sopa'])

    return vector_matrix, vectorizador

#-------------------------------------------------------Similitud de coseno-------------------------------------------------------
def calcular_matriz_similitud(vector_matrix):
    """
    Calcula la matriz de similitud de coseno a partir de la matriz vactorizada.
    args:
        vector_matrix (sparse matrix): Matriz vectorizada de la columna 'sopa'.
    returns:
    sim_matrix (ndarray): Matriz de similitud de coseno.
    """
    # Calcular la matriz de similitud de coseno
    sim_matrix = cosine_similarity(vector_matrix, vector_matrix)

    return sim_matrix

#-------------------------------------------------------Pruebas unitarias-------------------------------------------------------
def test_feature_engineering():
    """
    Función de prueba para verificar el correcto funcionamiento de las funciones de ingeniería de características.
    """
    # Crear un DataFrame de ejemplo
    data = {
        'genres': [['Action', 'Adventure'], ['Drama'], ['Comedy', 'Romance']],
        'plot_keywords': [['hero', 'villain'], ['love', 'betrayal'], ['funny', 'romantic']]
    }

    df = pd.DataFrame(data)

    # Crear y verificar la sopa de palabras
    df = crear_sopa_de_palabras(df)
    assert 'sopa' in df.columns, "La columna 'sopa' no se ha creado correctamente."
    assert df['sopa'].iloc[0] == 'Action Adventure hero villain', "La sopa de palabras no se ha creado correctamente."

    # Vectotizar el texto
    vector_matrix, vectorizador = vectorizar_texto(df, metodo='tfidf')
    assert vector_matrix.shape[0] == df.shape[0], "La matriz vectorizada no tiene el mismo número de filas que el DataFrame original."
    assert vector_matrix.shape[1] > 0, "La matriz vectorizada no tiene columnas."
    assert isinstance(vectorizador, TfidfVectorizer), "El vectorizador no es del tipo correcto."

    # Calcular la matriz de similitud
    sim_matrix = calcular_matriz_similitud(vector_matrix)
    assert sim_matrix.shape[0] == df.shape[0], "La matriz de similitud no tiene el mismo número de filas que el DataFrame original."
    assert sim_matrix.shape[1] == df.shape[0], "La matriz de similitud no tiene el mismo número de columnas que el DataFrame original."
    print("Todas las pruebas de ingeniería de características han pasado correctamente.")

""""
if __name__ == "__main__":
    test_feature_engineering()
    print("Pruebas unitarias completadas con éxito.")
"""