# -*- coding:utf-8-*-

###############################
#Programación funcional: Ejercicio1
###############################

def datos():
	datos=[]
	nombre=input("Ingresa tu nombre: ")
	datos.append(nombre)
	apPat=input("Ingresa tu apellido paterno: ")
	datos.append(apPat)
	apMat=input("Ingresa tu apellido materno: ")
	datos.append(apMat)
	direc= input("Ingresa tu dirección: ")
	datos.append(direc)
	numCel=int(input("Ingresa tu número: "))
	datos.append(numCel)
	numCta=int(input("Ingresa tu número de cuenta: "))
	datos.append(numCta)

	return datos

datos_recibidos= datos()

for i in datos_recibidos:
	print("*",i,end=" ")


def formato(datos_recibidos):
	print("Datos sin formato: ",datos_recibidos)
	print("Datos con formato: ")

	for i in datos_recibidos:
		print(datos_recibidos.index(i),i)


formato(datos_recibidos)