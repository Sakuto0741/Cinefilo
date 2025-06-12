# src/recommender.py
# Este módulo contiene funciones para recomendar películas basadas en un título dado.
# Las funciones incluyen la recomendación de películas similares utilizando una matriz de similitud de coseno.
# Autor: [Kevin Santiago Silva Serna]
# Fecha: [12 de junio de 2025]

import pandas as pd

def recomendar_peliculas(titulo, df, sim_matrix, top_n=5):
    """
    Recomienda películas similares basadas en el titulo de una película.
    args:
        titulo(str): Título de la película para la cual se desean recomendaciones.
        df (DataFrame): DataFrame limpio que contiene los datos de las películas.
        sim_matrix (ndarray): Matriz de similitud de coseno.
        top_n (int): Número de recomendaciones a devolver. Por defecto es 5.
    returns:
        recomendaciones (DataFrame): DataFrame con las películas recomendadas.
    """

    #Normalizar el título de la película
    titulo = titulo.lower().strip()

    # Verificar que el título existe en el DataFrame
    if titulo not in df['movie_title'].values:
        raise ValueError(f"La película '{titulo}' no se encuentra en la base de datos.")
    
    # Obtener el índice de la película
    # Nota: Se asume que el título es único en el DataFrame
    idx = df[df['movie_title'] == titulo].index[0]

    # Obtener las puntuaciones de similitud para la película seleccionada y ordenarlos de mayor a menor
    sim_scores = list(enumerate(sim_matrix[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:top_n+1] #Excluir la misma película

    # Obtener los índices de las películas recomendadas
    movie_indices = [i[0] for i in sim_scores]

    # Retornar las películas recomendadas
    return df['movie_title'].iloc[movie_indices].tolist()

# Example usage:
# df = pd.read_csv('data/archive/movie_metadata.csv')
# sim_matrix = calcular_matriz_similitud(vectorizar_texto(crear_columna_sopa(df)))
# recomendaciones = recomendar_peliculas('The Matrix', df, sim_matrix)
#     sim_matrix (ndarray): Matriz de similitud de coseno.
#     """
#     from sklearn.metrics.pairwise import cosine_similarity
#     # Calcular la matriz de similitud de coseno
#     sim_matrix = cosine_similarity(vector_matrix, vector_matrix)
#     return sim_matrix
#     """
# print(recomendaciones)

# -------------------------------------------------------Pruebas unitarias-------------------------------------------------------
def test_recomendar_peliculas():
    """
    Prueba unitaria para la función recomendar_peliculas.
    """
    # Crear un DataFrame normalizado de ejemplo
    data = {
        'movie_title': ['the matrix', 'inception', 'interstellar', 'the godfather', 'pulp fiction'],
        'genres': [['scifi'], ['scifi'], ['scifi'], ['crime'], ['crime']],
        'plot_keywords': [['matrix'], ['dream'], ['space'], ['mafia'], ['gangster']]
    }
    df = pd.DataFrame(data)
            
    # Crear una matriz de similitud de ejemplo
    sim_matrix = [[1, 0.8, 0.6, 0.2, 0.1],
                  [0.8, 1, 0.5, 0.3, 0.2],
                  [0.6, 0.5, 1, 0.4, 0.3],
                  [0.2, 0.3, 0.4, 1, 0.9],
                  [0.1, 0.2, 0.3, 0.9, 1]]

    # Probar la función con una película existente
    recomendaciones = recomendar_peliculas('The Matrix', df, sim_matrix)
    assert 'inception' in recomendaciones
    assert len(recomendaciones) == 4

    # Probar la función con una película no existente
    try:
        recomendar_peliculas('Nonexistent Movie', df, sim_matrix)
    except ValueError as e:
        assert str(e) == "La película 'nonexistent movie' no se encuentra en la base de datos."
    print("Todas las pruebas de recomendar_peliculas han pasado correctamente.")

"""
if __name__ == "__main__":
    test_recomendar_peliculas()
    print("Pruebas unitarias completadas con éxito.")
"""