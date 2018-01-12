import os
#Con esto limpiamos la pantalla
#cls es para windows y clear es para linux o mac 
os.system("cls")

vocales=["a","A","e","E","i","I","o","O","u","U"]

while True:
	res=""
	fraseUsuario=input("Ingresa una frase o una s´para salir: ")
	if fraseUsuario=="s" or fraseUsuario=="S":
		print("Regresa pronto :)")
		break
	else:
		print("Tu frase: ", fraseUsuario)
		fraseUsuario=list(fraseUsuario)
		for elemento in fraseUsuario:
				if elemento not in vocales:
					res += elemento
	print("Frase sin vocales: ",res)