class Operacion:
	"""Esta es una clase operacion

	Solo hace operaciones xd

	"""
	###Atributos de la clase
	valor1 = 0
	valor2 = 0
	##metodos de la clase
	###Metodo Constructor de la clase
	def __init__ (self, numero1, numero2):
		'Es el constructor de nuestra clase'
		self.valor1 = numero1
		self.valor2 = numero2

	###Obtener valor 1(getter)
	def obtenerValor1(self):
		"""Regresa el valor del atributo Valor1

		Para una instancia de la clase Operacion se definen dos atributos
		Valor1 y Valor2, los cuales van a ser operados

		"""
		return self.valor1

	#obtener Valor 2 (getter)
	def obtenerValor2(self):
		"""Regresa el valor del atributo Valor2

		Para una instancia de la clase Operacion se definen dos atributos
		Valor1 y Valor2, los cuales van a ser operados
		
		"""
		return self.valor2

	###Cambiar el valor 1(setter)
	def cambiarValor1(self, nuevovalor1):
		'Cambia el valor de Valor1'
		self.valor1 = nuevovalor1

	#Cambiar el valor2 (setter)
	def cambiarValor2(self, nuevovalor2):
		'Cambia el valor de Valor1'
		self.valor2 = nuevovalor2

	#imprimir numero
	def imprimirvalor(self, numero):
		"""Imprime el valor que pidamos

		Simpelemente recibe el valor numero el y lo muestra en 
		la pantalla

		"""
		print(numero)

class Suma(Operacion):

	"""Es una clase 

	Hereda de la clase operación y trabajará con dos números para 
	regresar algún resultado

	"""
	##Llamar al constructor de la clase padre(operacion) para inicializar los numeros
	def __init__ (self, numero1, numero2):
		'Es el constructor de nuestra clase suma'
		super().__init__(numero1, numero2)

	##se agrega el metodo nuevo a la clase suma (este metodo no esta dentro de la clase padre(clase "operacion"))
	def sumar(self):
		"""A mi también me choca documentar 

		Pero me tocó dar clase de esto, sorry :c

		"""
		self.imprimirvalor(self.valor1 + self.valor2)

suma1 = Suma(10,5)
print("operando 1 de la suma")
suma1.imprimirvalor(suma1.obtenerValor1())
print("operando 2 de la suma")
suma1.imprimirvalor(suma1.obtenerValor2())
print("Resultado de la suma")
suma1.sumar()

print("Aqui inicia la multiplicacion")
#############clase multi´plicacion
class Multiplicacion(Operacion):
	def __init__ (self, numero1, numero2):
		'Es el constructor de la clase multiplicación'
		super().__init__(numero1, numero2)

	def	multiplicar(self):
		"""Va a multiplicar dos números

		Sin embargo, la documentación es realmenet útil
		Ya hay herramientas externas a python que permiten agilizar la documentación
		Pero por ahora PyDoc es la más sencilla y básica
		
		"""
		self.imprimirvalor(self.valor1*self.valor2)

	######Se sobreeescribe un metodo de la clase padre##
	def imprimirvalor(self, numero):
		'Imprime un valor'
		print("el numero es: "+str(numero))

########################################
multiplicacion1 = Multiplicacion(10,5)
multiplicacion1.imprimirvalor(multiplicacion1.obtenerValor1())
multiplicacion1.imprimirvalor(multiplicacion1.obtenerValor2())
print("Resultado de la multiplicacion:")
multiplicacion1.multiplicar()




