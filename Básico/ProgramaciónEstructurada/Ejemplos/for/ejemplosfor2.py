#####Ejemplos con el ciclo "for"
"""
for contador in range(11):
	print(contador)
"""
"""
####ejemplos con el ciclo for "2"
for contador in range(100):
	print("No hare chistes de la fox :'v por 	", contador+1)


###ejemplo con el ciclo for "3"
for contador in range(100):
	print("La clase de ciencias no debe de terminar en tragedia por", contador+1)
"""
"""
for i in range(10):
	b = input("Digame la frase del dia :'v: ")
	print("Esta es al frase numero", i+1)
	print(b)
	print()
"""
####Ejemplo con un rango  y con un paso :D(no de baile)
"""for i in range(1,20,5):
	print(i)	
"""
"""
for ALDO in range(1,100, 200):
	print(ALDO)
"""

palabra = "ALDO DALTO ALDO IS MY FRIEND :D"
palabra2 ="JORGE"
palabra3 = "Julio"
palabra4 = "Gali >:c"
palabra5 = "Luis"

lista = [palabra, palabra2, palabra3, palabra4, palabra5]

"""
for i in palabra:
	print(i)
"""
"""
for i in range(len(lista)):
	for j in lista[i]:
		print(j)
"""
"""
contador=0
cadena = "What is love, baby don´t hurt me, don´t hurt, no more"
vocales= "aeiouAEIOU"
for i in cadena:
	if i in vocales:
		contador=contador+1
print("el numero de vocales es: ", contador)


contador2=0
cadena2 = "What is love baby dont hurt me dont hurt me no more"
consonantes= "bcdfghjklmnpqrstvwxyzW"
for i in cadena2:
	if i in consonantes:
		contador2=contador2+1
print("el numero de consonanes es: ", contador2)
"""

###ejemplo e Switch-Case
"""
print("Maquina dispensadra de dulces automagica musical fantabulosa")
print("1.- Chocolates\n2.-Palomitas\n3.-Helado\n4.-Esquites\n5.-Peluches")
b=int(input("Opcion: "))
if(b == 1):
	print("Teienes un rico chocolate")
if(b == 2):
	print("tienes unas deliciosas palomitas")
if(b == 3):
	print("Helaooo shocolate")
if(b == 4):
	print("Esquites :3")
if(b == 5):
	print("Esta maquina tiene de todo :v")
"""

###ejemplo e Switch-Case con "elif"
print("Maquina dispensadra de dulces automagica musical fantabulosa")
print("1.- Chocolates\n2.-Palomitas\n3.-Helado\n4.-Esquites\n5.-Peluches")
b=int(input("Opcion: "))
if(b == 1):
	print("Teienes un rico chocolate")
elif(b == 2):
	print("tienes unas deliciosas palomitas")
elif(b == 3):
	print("Helaooo shocolate")
