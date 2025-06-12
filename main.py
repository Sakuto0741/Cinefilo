from src.data_cleaning import cargar_y_limpiar_datos 
from src.feature_engineering import crear_sopa_de_palabras, vectorizar_texto, calcular_matriz_similitud
from src.recommender import recomendar_peliculas

def main():
    print("🎬 Bienvenido a Cinélifo - Recomendador de Películas")

    # 1. Cargar y limpiar los datos
    df = cargar_y_limpiar_datos()

    # 2. Crear sopa de palabras
    df = crear_sopa_de_palabras(df)

    # 3. Vectorizar el tecto
    vector_matrix, _ = vectorizar_texto(df)

    #4. Calcular la matriz de similitud
    sim_matrix = calcular_matriz_similitud(vector_matrix)

    # 5. Solicitar entrada del usuario
    print("\n✅ ¡Listo! Ahora puedes pedir recomendaciones.")
    while True:
        titulo = input("\n🎥 Ingresa el título de una película (o 'salir' para terminar): ").strip()
        # Verificar si el usuario quiere salir
        if titulo.lower() == 'salir':
            print("👋 ¡Gracias por usar Cinélifo! Hasta luego.")
            break
        try:
            recomendaciones = recomendar_peliculas(titulo, df, sim_matrix)
            print("\n🎬 Recomendaciones para la película '{}':".format(titulo))
            for i, rec in enumerate(recomendaciones, 1):
                print(f"{i}. {rec}")
            print()
        except ValueError as e:
            print(f"⚠️ Error: {e}. Por favor, intenta con otro título. \n")

if __name__ == "__main__":
    main()