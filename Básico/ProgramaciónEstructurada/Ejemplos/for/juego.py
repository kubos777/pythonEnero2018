#-*-coding:utf-8-*-
import random

print("""
	Voy a pensar en un número
	del 1 al 20 y vas a tener
	hasta 3 intentos para poder 
	adivinarlo
	""")

numero = random.randint(1,20)

for i in range(3):#Número de intentos
	respuesta = int(input("Cual crees que es el número?"))
	if respuesta > numero:
		print("Es un número más pequeño")
	elif respuesta < numero:
		print("Es un número más grande")
	else:
		print("YAAAYY!!")
		break
