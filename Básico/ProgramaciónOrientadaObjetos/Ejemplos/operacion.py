class Operacion:
	###Atributos de la clase
	valor1 = 0
	valor2 = 0
	##metodos de la clase
	###Metodo Constructor de la clase
	def __init__ (self, numero1, numero2):
		self.valor1 = numero1
		self.valor2 = numero2

	###Obtener valor 1(getter)
	def obtenerValor1(self):
		return self.valor1

	#obtener Valor 2 (getter)
	def obtenerValor2(self):
		return self.valor2

	###Cambiar el valor 1(setter)
	def cambiarValor1(self, nuevovalor1):
		self.valor1 = nuevovalor1

	#Cambiar el valor2 (setter)
	def cambiarValor2(self, nuevovalor2):
		self.valor2 = nuevovalor2

	#imprimir numero
	def imprimirvalor(self, numero):
		print(numero)

class Suma(Operacion):
	##Llamar al constructor de la clase padre(operacion) para inicializar los numeros
	def __init__ (self, numero1, numero2):
		super().__init__(numero1, numero2)

	##se agrega el metodo nuevo a la clase suma (este metodo no esta dentro de la clase padre(clase "operacion"))
	def sumar(self):
		self.imprimirvalor(self.valor1 + self.valor2)

suma1 = Suma(10,5)
print("operando 1 de la suma")
suma1.imprimirvalor(suma1.obtenerValor1())
print("operando 2 de la suma")
suma1.imprimirvalor(suma1.obtenerValor2())
print("Resultado de la suma")
suma1.sumar()

