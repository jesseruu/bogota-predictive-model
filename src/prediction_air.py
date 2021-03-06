import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn import metrics
import numpy as np

# Importamos el dataset limpio
ica_quality = pd.read_csv('train/minambiente_train_data.csv')

# Definimos las variables de X, y dependiendo de la particula 
X = ica_quality['FECHA'].values
op = input("[PM25, PM10, O3, NO2, CO] \nSeleccione una opcion: ").upper()
y = ica_quality[op].values

X = np.array(X).reshape(-1,1)

# Dividimos el dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Se entrena el modelo
rfr = RandomForestRegressor(n_estimators=200)
rfr.fit(X_train, y_train)

# Una vez entrenado, se establece el modelo predictivo
y_pred = rfr.predict(X_test)

# Prediccion para algunas fechas
print("La prediccion del modelo para la particula", op,
      "el 6 de julio y 31 de diciembre es de 2021 es: ", rfr.predict([[202176], [20211231]]))

# Rendimiento del modelo
print('\nError Medio Absoluto:', metrics.mean_absolute_error(y_test, y_pred))
print('Error medio cuadratico:', metrics.mean_squared_error(y_test, y_pred))
print('Raiz error medio cuadrático:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

# Precision
print('\nPrecision:', rfr.score(X_train, y_train))