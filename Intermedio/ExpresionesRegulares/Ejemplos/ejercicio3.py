#####################
## Ejemplo regex 4 ##
#####################

import re

verbo = input("Dame un verbo: ")

patronVerbos = "([A-Za-z]*(ar|er|ir|ado|ido|endo|ando|to|so|cho))$"

if re.match(patronVerbos, verbo):
	print("Si es un verbo")
else:
	print("No es un verbo")