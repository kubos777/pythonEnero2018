###ciclos While###
"""
suma = 0 
j = 1 ##inicio
N = 10 ##tope

while (j<=N):
	suma = suma + j
	j = j + 2
print("la suma es: ", suma)
"""
####Ejemplo 2 Contador
"""
contador = 0
while(contador < 5):
	print("El contador es: ", contador)
	contador = contador +1
"""
##ejemplo 3 Break
"""

contador = 0
while(contador < 5):
	print("El contador es: ", contador)
	contador = contador +1
	if(contador >3):
		print("Activate break, osea que acabe")
		break
print("Fin del progama")
"""


###ejemplo con "do-while"
numero =0

while True:
	numero = numero + 1
	if( numero % 2 ==1):
		print(numero)
	if numero == 20:
		break
	