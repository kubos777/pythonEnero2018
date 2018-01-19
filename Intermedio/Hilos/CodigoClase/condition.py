import threading
import time

condicion = threading.Condition()
listo = False

class Persona(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)

	def run(self):
		global listo
		condicion.acquire()
		while not listo:
			print('[%s] Deja que caliente el coche...' % time.strftime('%H:%M:%S'))
			condicion.wait()

		print('[%s] Amonos!' % time.strftime('%H:%M:%S'))
		condicion.notify()
		condicion.release()

class Auto(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)

	def run(self):
		global listo
		condicion.acquire()
		for i in range(3):
			time.sleep(1)

		print('[%s] El coche ya calentó' % time.strftime('%H:%M:%S'))
		listo = True
		condicion.notify()
		condicion.release()

persona1 = Persona()
auto1 = Auto()

persona1.start()
auto1.start()
