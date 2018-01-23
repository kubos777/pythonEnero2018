class Animal:

	Especie = ''
	NombreCientifico= ''
	Alimentacion = ''

	def __init__(self, Especie, NombreCientifico, Alimentacion):
		self.Especie = Especie
		self.NombreCientifico = NombreCientifico
		self.Alimentacion = Alimentacion

	#Métodos

	def Comer(self, victima):
		print('El animal %s se está comiendo a: %s' % (self.NombreCientifico,victima))

	def Dormir(self):
		print('El animal %s está durmiendo' % self.NombreCientifico)


#perro=Animal('Perritu','Adorable','Come croquetas')
perro='Perritu :3'
lobo = Animal('Cannis', 'Cannis Lupus', 'Carnivoro')

lobo.Dormir()

lobo.Comer(perro)




