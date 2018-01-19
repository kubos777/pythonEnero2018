import random
###Creamos nuestras propias excepciones
class ValorMuyBajo(Exception):
	pass
class ValorMuyAlto(Exception):
	pass
##############################
y=0
x = random.randint(1,30)

while True:
	try:
		a = int(input("ingresa un numero"))
		y+=1
		if y==5:
			print("Perdiste :C")
			break

		elif a>x :
			raise ValorMuyAlto

		elif a<x:
			raise ValorMuyBajo

		elif a ==x:
			print("Ganaste")
	except ValorMuyBajo:
		print("Valor mnuy Bajo")

	except ValorMuyAlto:
		print("Valor Muy Alto")

	except:
		print("fue otro error")


	