class NumeroComplejo:
	parteReal = 0
	parteImaginaria = 0

	def __init__(self, parteReal, parteImaginaria):
		self.parteReal = parteReal
		self.parteImaginaria = parteImaginaria

	def imprimirComplejo(self):
		print(str(self.parteReal) + '+' + str(self.parteImaginaria) + '*i')

	def suma(self, numeroC):
		real = self.parteReal + numeroC.parteReal
		img = self.parteImaginaria + numeroC.parteImaginaria

		resultado = NumeroComplejo(real, img)

		return resultado



real = float(input('Introduzca parte real del nuevo número: '))
img = float(input('Introduzca la parte imaginaria del nuevo número: '))

complejo = NumeroComplejo(real, img)
complejo.imprimirComplejo()

real = float(input('Introduzca parte real del nuevo número: '))
img = float(input('Introduzca la parte imaginaria del nuevo número: '))
complejo2 = NumeroComplejo(real, img) 
complejo2.imprimirComplejo()

sumaComplejoyComplejo2 = complejo.suma(complejo2)
sumaComplejoyComplejo2.imprimirComplejo()