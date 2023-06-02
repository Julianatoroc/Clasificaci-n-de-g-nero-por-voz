# Clasificacion-de-genero-por-voz
Este proyecto se enfoca en el análisis y clasificación de datos de voz para la identificación del género. Se utilizan técnicas de aprendizaje automático y minería de datos para desarrollar modelos predictivos que puedan determinar el género a partir de las características acústicas de una muestra de voz.

El conjunto de datos utilizado en este proyecto contiene mediciones de diferentes características de la voz, como la frecuencia fundamental, la intensidad, entre otras. Se realiza un preprocesamiento de los datos, que incluye la eliminación de filas con valores faltantes y la transformación de la variable categórica de género en una variable numérica.

Se aplican diferentes algoritmos de clasificación, como SVM (Support Vector Machines), KNN (K-Nearest Neighbors) y Decision Tree, para comparar su rendimiento en la tarea de clasificación de género. Se evalúa la precisión de los modelos utilizando métricas como el F1-score y el MCC (Matthews Correlation Coefficient).

Además, se realiza un análisis de reducción de dimensionalidad utilizando PCA (Principal Component Analysis) para visualizar la varianza explicada por los componentes principales y evaluar su impacto en la precisión de los modelos.

Finalmente, se incluye un modelo de regresión lineal para explorar la relación entre las características de la voz y el género. Se calcula el coeficiente de determinación (R^2) para evaluar la capacidad del modelo para explicar la variabilidad de los datos.
