###############################
#PANDAS: OBJETO SERIES
###############################

#Un conjunto de datos de una dimensión
# Las series se pueden crear tanto a partir de listas como de diccionarios
#De manera opcional podemos especificar una lista con etiquetas de las filas

from pandas import Series

#forma de crear una serie

serie=Series(['a','b','c'])

print(serie)

#print(type(serie))

#Podemos definir los indices de una serie pasandolos como parámetros
#en la funcion Series()
serie=Series(['a','b','c'],index=['Pregunta1','Pregunta2','Pregunta3'])
print("la serie es: \n", serie)

#Tambien podemos pasar un diccionario a la funcion series
#Tomara como indices las keys

dicc = {'Pregunta1':'a','Pregunta2':'b','Pregunta3':'c'}
serie = Series(dicc)
print(serie)

#Podemos controlar que queremos incluir, como su orden especificando
# en el index
