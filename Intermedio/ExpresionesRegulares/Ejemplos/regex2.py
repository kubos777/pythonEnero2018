###################
## Metacaracteres #
###################

#Caracteres que tomán valor dependiendo del contexto

""" Ir haciendo y luego completando la tabla
. -> cualquier caracter (uno)

* -> cero o mas veces

+ -> una o mas veces

? -> cero o una vez

{n} -> n veces exactas

{n,m} -> de n a m veces
	n = minimo de veces, m = maximo de veces

| -> "or" puede ser cualquiera de los dos dados

^ -> hace match con el principio del string

$ -> hace match con el final

"""

import re

def buscar(patrones, texto):
	for patron in patrones:
		print(re.findall(patron, texto))

#Le vamos a dar una lista de patrones y un texto
#Por cada patron va a imprimir una lista de
#concordancias con el texto

print()###########  .

texto = "ola ala ula pla alo ilo"
patrones = [".la",".lo"]

buscar(patrones, texto)

print()###########  *

texto="hla hola hoola hoola hoooooooola hulo huuuulo hlo"
patrones = ["ho*la","hu*lo"]

buscar(patrones, texto)

print()###########  +

patrones = ["ho+la","hu+lo"]

buscar(patrones, texto)

print()########### ?

texto = "hla hola hooola hola hooooooooooooola hlo holo"
patrones = ["ho?la", "ho?lo"]

buscar(patrones,texto)

print()############ {}

patrones = ["ho{3}la", "ho{0,3}la", "ho{,2}la", "ho{3,}la"]
buscar(patrones, texto)

print()############  |

texto1 = "HOLA"
texto2 = "HOLO"
texto3 = "HOLE"

if(re.search("HOL(A|O)", texto1)):
	print("Match!")

if(re.search("HOL(A|O)", texto2)):
	print("Otro match!")

if(re.search("HOL(A|O)", texto3)):
	print("Otro otro match!")

# () grupos -> permite englobar otros metacaracteres

print()

texto = "no lo haga compa"

if(re.search("^no", texto)):
	print(":D")
else:
	print("D:")
	
if(re.search("^compa", texto)):
	print(":D")
else:
	print("D:")

if(re.search("compa$", texto)):
	print(":D")
else:
	print("D:")