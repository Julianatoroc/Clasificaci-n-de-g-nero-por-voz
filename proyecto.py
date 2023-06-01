# -*- coding: utf-8 -*-
"""Proyecto.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lCkKvb7Fg1uhmpwwVxMKbdluHj7Fg-6J
"""

# Commented out IPython magic to ensure Python compatibility.
#Import libraries

# %matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import matthews_corrcoef, f1_score
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.metrics import silhouette_samples
from sklearn.linear_model import ElasticNet
from sklearn.model_selection import GridSearchCV
import numpy as np
#Cargar dataset
voice = pd.read_csv('voice.csv')
voice
voice.info()
#Pre procesamiento
#Verificar valores null
voice.isnull().values.any() 
# Eliminar filas con valores NaN o NULL
voice = voice.dropna()
# Verificar si aún hay valores NaN o NULL
voice.isnull().values.any()
# Crear una instancia de LabelEncoder
label_encoder = LabelEncoder()
# Convertir la columna 'label' de categórica a numérica
#0 male 1 female
voice['label'] = label_encoder.fit_transform(voice['label'])
# Crear un nuevo DataFrame con los datos limpios
voice_clean = voice.dropna()
# Guardar las características en una variable X y las etiquetas en una variable y
X = voice_clean.iloc[:, :-1]  # Todas las columnas excepto la última
y = voice_clean.iloc[:, -1]   # Última columna
# Combinar X y y en un nuevo DataFrame
voice_clean_with_labels = pd.concat([X, y], axis=1)
# Guardar el DataFrame en un archivo CSV
voice_clean_with_labels.to_csv('voice_clean.csv', index=False)
# Dividir los datos en conjuntos de entrenamiento y validación
train_size = 0.8  # Porcentaje para el conjunto de entrenamiento
X_train, X_val, y_train, y_val = train_test_split(X, y, train_size=train_size, random_state=42)
# Verificar los tamaños de los conjuntos de entrenamiento y validación
print("Tamaño del conjunto de entrenamiento:", len(X_train))
print("Tamaño del conjunto de validación:", len(X_val))
# Crear una instancia de StandardScaler
scaler = StandardScaler()
# Ajustar el escalador a los datos de entrenamiento y transformarlos
X_train_normalized = scaler.fit_transform(X_train)
# Aplicar la misma transformación a los datos de validación
X_val_normalized = scaler.transform(X_val)
# Crear una instancia de PCA con el número de componentes deseado
n_components = 2  # Número de componentes principales a extraer
pca = PCA(n_components=n_components)
# Ajustar PCA al conjunto de entrenamiento y transformar los datos
X_train_pca = pca.fit_transform(X_train)
# Aplicar la misma transformación a los datos de validación
X_val_pca = pca.transform(X_val)
# Crear una instancia de PCA con el número de componentes deseados
n_components = 10  # Número de componentes principales a extraer
pca = PCA(n_components=n_components)
# Ajustar PCA al conjunto de entrenamiento
pca.fit(X_train)
# Obtener la varianza explicada
variance_ratio = pca.explained_variance_ratio_
cumulative_variance_ratio = np.cumsum(variance_ratio)
print(cumulative_variance_ratio)
# Visualizar la proporción acumulada de la varianza explicada
plt.plot(range(1, n_components+1), cumulative_variance_ratio, marker='o', linestyle='-')
plt.xlabel('Número de componentes principales')
plt.ylabel('Proporción acumulada de varianza explicada')
plt.title('Proporción acumulada de varianza explicada por componentes principales')
plt.grid(True)
plt.show()
#la varianza explicada por los primeros componentes principales es alta
#la reducción de dimensionalidad utilizando PCA puede ser beneficiosa

# Crear el modelo SVM
svm_model = SVC()
svm_model.fit(X_train, y_train)
svm_predictions = svm_model.predict(X_val)

# Crear el modelo KNN
knn_model = KNeighborsClassifier()
knn_model.fit(X_train, y_train)
knn_predictions = knn_model.predict(X_val)

# Crear el modelo Decision Tree
dt_model = DecisionTreeClassifier()
dt_model.fit(X_train, y_train)
dt_predictions = dt_model.predict(X_val)

# Evaluar los clasificadores

svm_f1 = f1_score(y_val, svm_predictions, average='weighted')
knn_f1 = f1_score(y_val, knn_predictions, average='weighted')
dt_f1 = f1_score(y_val, dt_predictions, average='weighted')

# Calcular el MCC para cada clasificador
svm_mcc = matthews_corrcoef(y_val, svm_predictions)
knn_mcc = matthews_corrcoef(y_val, knn_predictions)
dt_mcc = matthews_corrcoef(y_val, dt_predictions)

# Imprimir los resultados

print("SVM")
print("F1-score:", svm_f1)
print("MCC:", svm_mcc)
print()

print("KNN")
print("F1-score:", knn_f1)
print("MCC:", knn_mcc)
print()

print("DT")
print("F1-score:", dt_f1)
print("MCC:", dt_mcc)

# Crear y entrenar un modelo de regresión lineal
model = LinearRegression()
model.fit(X_train, y_train)
# Realizar predicciones en el conjunto de prueba
y_pred = model.predict(X_val)
# Calcular el coeficiente de determinación
r2 = r2_score(y_val, y_pred)
print("Coeficiente de Determinación (R^2):", r2)
# Crear una gráfica de regresión
sns.regplot(x=y_val, y=y_pred)
plt.xlabel('Valores reales')
plt.ylabel('Valores predichos')
plt.title('Regresión Lineal')
plt.show()
# Calcular los coeficientes de silueta para cada muestra
silhouette_values = silhouette_samples(X, y)
# Imprimir los coeficientes de silueta para cada muestra
for i in range(len(X)):
    print("Muestra", i+1, " - Coeficiente de Silueta:", silhouette_values[i])
# Definir los hiperparámetros a evaluar en el grid-search
parameters = {
    'alpha': [0.1, 1.0, 10.0],  # Coeficiente de regularización
    'l1_ratio': [0.25, 0.5, 0.75]  # Proporción de regularización L1 (lasso) y L2 (ridge)
}
# Crear el modelo ElasticNet
model = ElasticNet()
# Realizar el grid-search
grid_search = GridSearchCV(estimator=model, param_grid=parameters, scoring='r2')
grid_search.fit(X, y)
# Obtener los mejores hiperparámetros encontrados
best_params = grid_search.best_params_
print("Mejores Hiperparámetros:", best_params)
# Obtener el mejor score (en este caso, coeficiente de determinación R^2)
best_score = grid_search.best_score_
print("Mejor Coeficiente de Determinación (R^2):", best_score)