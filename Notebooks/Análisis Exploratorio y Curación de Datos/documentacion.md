## __Criterios de exclusión de ejemplos__

Se eliminaron outliers a través del criterio de los percentiles.

## __Características seleccionadas__
### Características categóricas

Para la codificación One-hot encoding se seleccionaron las siguientes variables categóricas:

- Suburb
- Type
- Regionname
- Date

A continuación se define cada variable categórica y sus valores posibles

1. Suburb: Se denominan de esta manera a las zonas residenciales en la periferia urbana menos dispersos. Los posibles valores son (Abbotsford, Blackburn,Clifton Hill, etc.)
2. Type: Es el tipo de propiedad.Los valores posibles pueden ser (h = house, u = unit, t = townhouse.)
3. Regionname: Región (West, North West, North, North east, etc.)
4. Date: Es la fecha de venta de la propiedad. El formato de las fechas se presenta de la siguiente forma (DD/MM/AA)


Todas las características categóricas fueron codificadas con un método OneHotEncoding utilizando como máximo sus 30 valores más frecuentes.


### Características numéricas

Luego de aplicar el OneHotEncoding, se utilizaron las variables numéricas que se detallan a continuación, las cuales se concatenaron a las categóricas a través de la implementación del método hstack de numpy.

1. Rooms: Representa el número de habitaciones. (1, 2, 3, 4, etc.)
2. Price: Precio de la vivienda en dolares (3300000, 2100500, 495000, etc.)
3. Distance: Distancia desde Central Business District (2.0, 2.5, 3.0, etc.)
4. Postcode: Código Postal (3067, 3018, 3147, etc.)
5. Bedroom2: Dormitorios (1, 2, 3, 4, etc.)
6. Bathroom: Número de baños (1, 2, 3, 4, etc.)
7. Car: Cantidad de estacionamientos (1, 2, 3, 4, etc.)
8. Landsize: Tamaño del terreno (156.0, 134.0, 202.0, etc.)
9. Propertycoun: Número de inmuebles que existen en el suburbio. (402, 320, 180, etc.)
10. Airbnb_record_count: Cantidad de registros por zipcode (4, 5, 7, etc.)
11. Airbnb_price_mean: Precio promedio diario de publicaciones de la plataforma AirBnB en el mismo código postal. (107.00, 73.00, 98.00, etc)
12. Airbnb_weekly_price_mean: Precio promedio semanal de publicaciones de la plataforma AirBnB en el mismo código postal. (700.00, 546.00, 612.00, etc)
13. Airbnb_monthly_price_mean: Precio promedio mensual de publicaciones de la plataforma AirBnB en el mismo código postal. (2006.0, 2012.0, 2120.0, etc)



## __Transformaciones__

Aplicamos una codificación **One-hot-encoding** a cada fila, tanto para variables numéricas como categóricas, utilizando como máximo sus 30 valores más frecuentes.

Utilizamos el método **hstack()** para concatemar el resultado de onehotenconding de las variables categóricas con las variables númericas del dataframe. El resultado obtenido es una matriz de tipo array.

Luego, agregamos las columnas `YearBuilt` y `BuildingArea` a la matriz obtenida. Realizamos un escalado lineal a ambas columnas para después utilizar el método **IterativeImputer()** con un estimador igual a **KNeighborsRegressor** y un **randomstate=32**, imputando los datos faltantes. Posteriormente, graficamos comparando las columnas imputadas frente a las columnas originales.

Aplicamos un **PCA** para reducir la dimensionalidad de la matriz. Decidimos escalar con un **MinMaxScaler(-1, 1)** con una cantidad de componentes principales igual a **n = min(20, X.shape[0])**. Además, utilizamos el método **StandardScaler()** para luego graficar la varianza capturada por los primeros n componentes para cada n; y así poder determinar la optimalidad entre escalar o estandarizar o ninguno.

Agregamos a la matriz dos columnas que contienen nuevos **features** basados en el **pca estandarizado**.

Finalmente, transformamos la matriz resultante en un dataframe.


## __Datos aumentados__

Se agregan las 2 primeras columnas obtenidas a través del método de PCA, aplicado sobre el conjunto de datos totalmente procesado.
