#####################
## Ejemplo Regex 2 ##
#####################
import re

fecha = input("Dame la fecha de tu nacimiento (dd/mm/aaa): ")

patronFecha = "\d{2}/\d{2}/\d{4}$"  #"\d{2}[/-]\d{2}[/-]\d{4}$" 

if re.match(patronFecha, fecha):
	print("Fecha correcta")
else:
	print("Fecha incorrecta")