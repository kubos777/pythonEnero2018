import threading

indice = 1

def funcion():
	global indice
	print('Aldo es mi adjunto favorito x%i' % indice)
	indice += 1

hilos = []

for i in range(11):
	hilos.append(threading.Thread(target=funcion))
	hilos[i].start()