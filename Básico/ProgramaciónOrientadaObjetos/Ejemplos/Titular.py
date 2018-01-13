import random
import time
alumnos = ['Juanito', 'Pedro', 'Gonzalo', 'Luis', 'Pánfilo', 'Mary', 'Karla']
class Titular:
	__ID = ''
	Nombre = ''
	CursosQueImparte = ''

	def __init__(self, ID, Nombre, CursosQueImparte):
		self.__ID = ID
		self.Nombre = Nombre
		self.CursosQueImparte = CursosQueImparte

	def darClase(self):
		print('%s está dando clase...' % self.Nombre)

	def revisarTarea(self):
		for i in range(10):
			print('%s está revisando la tarea... un asistente sacó %i' % (self.Nombre, random.randint(0, 10)))

	def pasarLista(self):
		for i in range(len(alumnos)):
			print('%s: %s!' % (self.Nombre, alumnos[i]))
			time.sleep(1)
			if random.randint(0, 1):
				print("%s: Presente!" % i)

			else:
				print('%s: Tiene falta...' % self.Nombre)

	def getID(self):
		return self.__ID

	def setID(self, ID):
		self.__ID = ID


Jorge = Titular('1', 'Jorge', ['Python', 'Diseño Web'])

'''Jorge.pasarLista()
Jorge.revisarTarea()
Jorge.darClase()'''

print(Jorge.getID())

