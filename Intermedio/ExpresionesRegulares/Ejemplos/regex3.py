###########
## Rangos #
###########

#[0-9] -> 0, 1, 2, 3, ..., 9
#[a-z] -> a, b, c, d, ..., z
#[A-Z] -> A, B, C, D, ..., Z
#[0-9a-zA-Z] -> Se puede conmbinar
#[a-f5-8] -> de la a a la f o del 5 al 8
#[az-] -> a, z, -

import re

def buscar(patrones, texto):
	for patron in patrones:
		print( re.findall(patron, texto))

patrones = ['h[ou]la', 'h[aio]la', 'h[aeiou]la']
texto = "hala hela hila hola hula"

buscar(patrones, texto)

print()

patrones = ['h^[a-z]la', 'h[0-9]', '[a-z]{4}', '[A-Z][A-z0-9]{3}']
texto = "h0la Hola aaaa bbbb hala hzla hbla hola"

buscar(patrones, texto)

print()########## Negacion ^

# ^ -> nos da el grupo contrario

if re.match("python[^0-9a-z]", "pythonZ"):
	print("Hizo match :')")

else:
	print(":'(")

if re.match("python[^0-9a-z]", "pythonZ", re.IGNORECASE):
	print("Hizo match :)")

else:
	print(":'(")

print()


#Alias
# digitos
# \d -> equivale [0-9]

# no digitos
# \D -> equivale [^0-9]

# \A -> iniciar con el match

# palabra
# \w -> equivale [a-zA-Z_]

# no palabra
# \W -> equivale [^a-zA-Z_]

# salto de linea o tabulacion
# \s -> equivale a cualquier caracter en blanco [ \n\t]

#no salto de linea ni tabulacion
# \S -> equivale a cualquier caracter no en blanco

texto = "2 33 444 43 hola"
patrones = ["\d", "\d\d", "\d\d\d"]

buscar(patrones, texto)

print()

patornes = ["\D\D\D\D\D"]
buscar(patornes, texto)

print()

texto = "hola! 10 h0la"
patrones = ["\w\w\w\w", "\w\w"]
buscar(patrones, texto)

print()

patrones = ["\w{4}\W"]
buscar(patrones, texto)

#Escape
#Para que un metacaracter pierda su cualidad de metacaracter, se debe "escapar" con una "\"
#Asi el metacaracter1 "." al escaparse "\." simplemente es el caracter punto

