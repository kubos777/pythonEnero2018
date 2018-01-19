#####################
## Ejemplo regex 3 ##
#####################

import re

correo = "Mi correo es lagarridom@gmail.com y pamela.33_2@gmail.com"
patron = "[\.\w]+@[a-z]+\.com"

correo=re.sub(patron, "l@gmail.com", correo)
print(correo)

telefono = "Mi telefono es 5534467029 y 5534467029"
patron1 = "55[0-9]{8}"
telefono=re.sub(patron1, "5533225544",telefono)
print(telefono)