############################
#### Expresiones Regulares #
############################

"""
Lenguaje creado para facilitar analisis de texto
Es util para:
- Verificar que un String concuerde con un patron
- Realizar substituciones en strings

"""

#re.match(patron, string)
#se utiliza para ver si hay match al principio del texto


import re

texto = "Este es un texto y es uno muy sencillo"

patron1 = "Este es un"
patron2 = "texto"

if re.match(patron1,texto):
	print("Match1 :)")
if re.match(patron2,texto):
	print("Match2 :)")
#
objeto = re.match(patron1,texto)

print("Posición inicial: ", objeto.start())
print("Posición final: ", objeto.end())
print("En conjunto: ", objeto.span())
#Siendo un objeto, este tiene metodos

print()##########################
#re.search(patron, string)
#Se utiliza para ver si hay match en cualquier parte del texto

patron3 = "hola"

if re.search(patron1,texto):
	print("Match3 :)")
if re.search(patron2,texto):
	print("Match4 :)")

print()
#re.findall(patron, string)
#Regresa una lista ded todas las subcadenas que hayan hecho match

patron4 = "es"

lista = re.findall(patron4, texto)
print(lista)

print()###########################

texto1 = "Perro: 'Miaw'"

texto2 = re.sub("Miaw", "Woof", texto1)

print(texto2)

#re.sub(patron, remplazo, texto)
#regresa el texto con el reemplazo en vez del patron

texto = "Este no es un texto y no es muy sencillo"
print(re.sub("no es", "es", texto))

print(re.sub("no es", "es", texto, 1))

#re.sub(patorn, remplazo, texto, maximo de reemplazos)

