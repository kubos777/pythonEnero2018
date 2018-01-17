##################
#Archivos
##################

#archivo=open("nombre.txt","a+")

archivo=open("prueba.txt","r+")

print("Nombre del archivo: ",archivo.name)
print("Modo de apertura: ",archivo.mode)
"""
if archivo.closed:
	print("El archivo esta cerrado")
else:
	print("El archivo esta abierto")
	#archivo.close()
"""
#El método read nos permite leer todo el contenido del archivo
texto=archivo.read()

print(texto)
print(type(texto))


texto=input("Ingrese el texto para escribirlo en el archivo ")

archivo.write("\n"+texto)

#Mover apuntador

archivo.seek(5)

print("Contenido del archivo: \n",archivo.read())

archivo.close()

#Manejador de contexto

with open(input("Ingrese el nombre del archivo: ")) as f :
	lineas=f.readlines()

print(lineas)

for linea in lineas:
	print(linea,end=" ")

	