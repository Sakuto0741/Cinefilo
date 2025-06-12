#  Cinélifo – Recomendador de películas basado en contenido

**Cinélifo** es un sistema de recomendación de películas que sugiere títulos similares a partir de una entrada dada por el usuario, usando técnicas de procesamiento de lenguaje natural (NLP) y aprendizaje automático básico.

Construido desde cero con Python, este proyecto fue desarrollado como reto personal para fortalecer habilidades en análisis de datos, ingeniería de características y estructura modular de código.

---

##  Tecnologías utilizadas

- **Python 3.11+**
- **Pandas**
- **Scikit-learn**
- **TF-IDF Vectorizer**
- **Cosine Similarity**
- (Próximamente: Streamlit)

---

##  Estructura del proyecto

  ```bash
  cinelifo/
  ├── .venv/
  │
  ├── data/archive
  │ └── movie_metadata.csv # Dataset original (IMDb)
  │
  ├── env/
  │
  ├── src/
  │ ├── data_cleaning.py # Limpieza de datos y normalización textual
  │ ├── data_view.ipynb # Visualización de datos
  │ ├── feature_engineering.py # Creación de sopa de palabras y vectorización
  │ └── recommender.py # Lógica de recomendación basada en similitud
  │
  ├── main.py # Interfaz por consola
  └── README.md
  ```
---

##  ¿Cómo funciona?

1. Limpia y normaliza los datos del dataset de películas.
2. Crea una “sopa de palabras” combinando géneros y palabras clave.
3. Vectoriza el texto usando **TF-IDF**.
4. Calcula similitud entre todas las películas usando **cosine similarity**.
5. El usuario ingresa el título de una película y obtiene recomendaciones personalizadas.

---

##  ¿Cómo usarlo?

1. Clona este repositorio:
   ```bash
   git clone https://github.com/Sakuto0741/Cin-lifo.git
   cd Cin-lifo
   
2. Instala los requisitos:
   ```bash
   pip install -r requirements.txt
   
3. Ejecuta el programa:
   ```bash
   python main.py

4. Ingresa el título de una película (en ingles, como aparece en IMDb) y recibe sugerencias.

---

##  Dataset

Se usó el dataset movie_metadat.csv proveniente de IMDb, con columnas como:
- movie_title
- genres
- plot_keywords
- imdb_score

##  Proximos pasos

- Versión web con Streamlit
- Recomendador híbrido con puntuaciones + contenido
- Visualización de insights con gráficos interactivos

##  Autor

Desarrollado por Kevin Santiago Silva Serna como parte de un reto personal de 10 proyectos en 2 semanas.
Contacto LinkedIn: www.linkedin.com/in/kevin-silva-dev
