###################
## Ejemplo regex ##
###################

import re

while(1):
	nombre = input("Dame tu nombre completo: ")
	patronNombre = "[A-Z][a-z]+\s[A-Z][a-z]+\s[A-Z][a-z]+(\s[A-Z][a-z]+)*"
	if re.match(patronNombre, nombre):
		print("Es un nombre correcto")
	else:
		print("No es un nombre válido")
		continue

	telefono = input("Dame tu teléfono celular: ")

	patronTelefono = "^55[0-9]{8}$"

	if re.match(patronTelefono, telefono):
		print("Es un teléfono correcto")
	else:
		print("No es un teléfono válido")
		continue

	correo = input("Dame tu correo electrónico: ")

	patronCorreo = "\w+@[a-z]+\.com$"

	if re.match(patronCorreo, correo):
		print("Es un correo correcto")
	else:

		print("No es un correo correcto")
		continue
	break
		


