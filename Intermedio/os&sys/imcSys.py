import sys
#Imprimimos el número de los argumentos que hemos pasado
print(len(sys.argv))
#Si el tamaño de numero de argumentos es menor a 2
if len(sys.argv)<=2:
	print("Te hacen falta parámetros!")
	exit(1)

while True:
	#Recibimos como argumentos desde la línea de comandos el peso
	peso=float(sys.argv[1])
	#Recibimos como argumento desde línea de comandos la altura
	altura=float(sys.argv[2])
	IMC=peso/altura**2

	if IMC<18:
		print("Infrapeso")
	elif IMC<24.9:
		print("Andas chido!")
	else:
		print("Bajale a los tamales, gordito!")

	a=input('Escribe "salir" para terminar')
	if a=='salir':
		break
