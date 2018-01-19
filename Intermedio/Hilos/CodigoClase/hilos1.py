import threading

def funcion():
	print('Aldo es mi adjunto favorito')

hilos = []

for i in range(11):
	hilos.append(threading.Thread(target=funcion))
	hilos[i].start()