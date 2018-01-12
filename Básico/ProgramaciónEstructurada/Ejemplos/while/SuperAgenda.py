#-*-coding:utf-8-*-
import os
os.system("cls")
#clear
#Declaramos nuestro diccionario vacio para guardar contactos
contactos={}
correos={}
print("\n\n\t\t\tBienvenido a la Super Agenda")

while True:
	print("\n\t1.-Agregar un contacto")
	print("\n\t2.-Búscar un contacto")
	print("\n\t3.-Ver todos los contactos")
	print("\n\t4.-Eliminar un contacto")
	print("\n\t5.-Salir")

	opcionMenu=int(input("Opcion: "))
	if opcionMenu==1:
		#Agregar un contacto
		nombre=input("\n\n\t Ingrese el nombre del contacto: ")
		numero=int(input("Ingresa el número de telefono: "))
		correo=input("Ingresa el correo: ")
		contactos[nombre]=numero
		correos[nombre]=correo
		os.system("cls")
	elif opcionMenu==2:
		#Buscar un número
		nombre=input("\n\n\t ¿Qué contacto quieres buscar?: ")
		os.system("cls")
		if nombre in contactos:
			print("\n Nombre: ", nombre)
			print("\n Teléfono: ",contactos[nombre])
			print("\n Correo: ",correos[nombre])
		else:
			print("\nError 404, contacto no encontrado")
	elif opcionMenu==3:
		#Ver todos los contactos
		os.system("cls")
		if len(contactos.items())==0:
			print("\n\n\t No hay contactos para mostrar :(")
		else:
			for persona in contactos.keys():
				print("\n\n\tEl numero de ",persona," es :", contactos[persona]," y su correo:", correos[persona])
	elif opcionMenu==4:
		#Eliminar contacto
		nombre=input("¿Qué contacto deseas borrar?: ")
		os.system("cls")
		if nombre in contactos:
			del contactos[nombre]
			del correos[nombre]
		else:
			print("\n Error 404, contacto no encontrado")
	elif opcionMenu==5:
		#Sailr
		os.system("cls")
		print("\n\n\tRegresa pronto!")
		break
	else:
		os.system("cls")
		print("\n\n\tOpcion no válida, intente otra vez!")

