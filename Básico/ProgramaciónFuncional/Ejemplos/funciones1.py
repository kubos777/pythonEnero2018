# -*- coding:utf-8-*-

###############################
#Programación funcional
###############################

"""
def soy_una_funcion():
	Aquí dentro va el código que deseamos
	que se realice al llamar a la función.
	Para llamar a una función, solamente basta
	con poner el nombre así:
	soy_una_funcion()
	"""

def hola():
	print("Hola amigos del curso de python, soy una función! :D")

hola()

def regresa():
	return "Soy el valor de regreso o retorno :3"
#Necesitamos capturar el valor de regreso de una función
#en una variable, de lo contrario no hace nada la función
valor_regreso=regresa()

print("Valor de regreso: ",valor_regreso)

def suma(a,b):
	resultado=a+b
	return resultado

resultado=suma(1000,1)

print("El resultado de la suma es: ", resultado)

print("El resultado es: ", suma(2,2))
