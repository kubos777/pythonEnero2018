# -*- coding:utf-8-*-

###############################
#Programación funcional: Funciones 2
###############################
"""
a=5
#Definimos las variables que se van a utilizar en la función
#cuando colocamos los parametros de la función
def resta(a,b):
	return a-b 
print(resta(a,53))
"""
#Parámetros por omisión, keywords
"""def saludar(nombre,mensaje='gfadgfadgfadgfa'):
	print(mensaje,nombre)
saludar(nombre=input("Cómo te llamas?"))
"""
def recorre_parametros_arbitrarios(parametro_fijo,*arbitrarios):
#Los parametros "arbitrarios" se guardaran en una tupla
	 for argumento in arbitrarios:
	 	print(argumento)
recorre_parametros_arbitrarios('Soy fijo','Soy arbitrario 1','Soy arbitrario 2','Soy arbitrario 3','ar4','ar5')

# **kwargs
def recorre_parametros_arbitrarios(parametro_fijo,*arbitrarios,**kwargs):
#Los parametros "arbitrarios" se guardaran en una tupla
	 for argumento in arbitrarios:
	 	print(argumento)
	 for clave in kwargs:
	 	print("El valor de", clave, "es", kwargs[clave])

recorre_parametros_arbitrarios('Soy fijo','Soy arbitrario 1','Soy arbitrario 2','Soy arbitrario 3',clave1='valor uno',clave2="valor dos")

#Desempaquetar
#Va a esperar una lista fija de parámetros
"""def calcular(importe, descuento):
	return importe -(importe*descuento/100)
datos=[1500,10]

print(calcular(*datos))
"""
#La función esperará un diccionario(clave=valor)
def calcular(importe, descuento):
	return importe -(importe*descuento/100)
datos={"descuento":10,"importe":1500}

print(calcular(**datos))







