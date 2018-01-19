##10/0
#hola = "hola"
#h = 2
#print(hola+h)
#while True:
#	x = int(input("por favor ingrese un numero: "))
"""
try:
	while True:
		x = int(input("ingrese un numero: "))
except ValueError:
	print("Eso no es un numero >:v")
	"""

##print("Dame el nombre de tu archivo")
##b=input()
while True:
	try:
		x= int(input("por favor ingrese un numero"))
	except ValueError:
		print("esto no es un numero")
	except KeyboardInterrupt:
		print("Estas atraapado y no puedes usa ctrl + c")