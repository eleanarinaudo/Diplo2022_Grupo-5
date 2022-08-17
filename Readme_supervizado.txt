Este documento es a cerca de las diferencias de curacion de datos que presentan las 3 notebooks presentadas.
La idea de diferenciar la curacion de datos para cada modelo fue una busqueda de mejorar la performance de cada uno con sus parametros por defecto antes de modificar los mismos.
A continuacion destacaremos las diferencias en la curacion de cada notebook.


XGBoostClf

	Utilizacion del LabelEncoder para la codificacion de datos categoricos.

Perceptron Multicapa

	Utilizacion de OneHotEncoder para la codificacion de variables categoricas 	y generacion de nuevas features.

RandomForestClassifier

