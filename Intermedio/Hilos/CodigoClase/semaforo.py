import threading
import time

n = 8
sem = threading.Semaphore(3)

class miHilo(threading.Thread):
	def __init__(self, id):
		threading.Thread.__init__(self)
		self.id = id

	def run(self):
		sem.acquire()
		print('Hilo %d en la hora %s' % (self.id, time.strftime('%H:%M:%S')))
		time.sleep(self.id + 2)
		sem.release()

hilos =[]

for i in range (n):
	actual = miHilo(n+1)
	hilos.append(actual)
	actual.start()

for actual in hilos:
	actual.join()
