'''
Sistema de prediccion del indice de calidad del aire de la ciudad de bogotá D.C
La prediccion se hara dependiendo de cada particula registrada
'''

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

# Importamos los datos de nuestra carpeta dataset
air_data = pd.read_csv("dataset/minambiente-bogota-airQuality.csv")

# Reemplazamos los valores vacios con valores nulos
air_data.replace(r'^\s*$', np.NaN, regex=True, inplace= True)

# Renombramos las columnas
columns_air = ["FECHA","PM25","PM10","O3","NO2","SO2","CO"]
air_data.columns = columns_air

# INFORMACION DE LOS DATOS | Descripcion general
print("\nDESCRIPCION GENERAL DE LOS DATOS\n\n",air_data.describe())

# Tamaño de los datos
print("\nFORMA DE LOS DATOS\n\n",air_data.shape)

# Verificar los valores nulos
# Como se puede ver, la columna SO2 esta casi vacia
print("\nVALORES NULOS POR COLUMNA\n\n",air_data.isnull().sum())

# LIMPIEZA DE DATOS
# La columma de SO2 tambien se debe eliminar, debido que hay pocos registros 
air_data.drop(['SO2'], axis = 1, inplace = True)

# Eliminamos los valores con registros en 0
# En este caso gracias a la informacion shape, sabemos que hay de 2200 registros
# La columna con menos registros es CO seguido de NO2, el cual son 650
# Los cuales son muchos para generarlos usando metodos estadisticos
# Por ello, directamente se eliminaran todos los datos nulos
air_data.dropna(subset=["CO","O3","NO2","PM25","PM10"],axis=0, inplace=True)

# Visualizando los datos
X = air_data['PM25']
y = air_data['FECHA']
plt.figure(figsize=[14,9])
plt.scatter(X,y)
plt.xlabel('Particula PM')
plt.ylabel('Fechas')
plt.show() # Esta bastante roto porque me coge los mas de 1500 datos del CSV

# Una vez que tenemos todos los datos limpios
# Guardamos el dataframe en otro CSV para realizar el entrenamiento

if os.path.exists('train'):
    air_data.to_csv('train/minambiente_train_data.csv')
else:
    os.mkdir('train')
    air_data.to_csv('train/minambiente_train_data.csv')