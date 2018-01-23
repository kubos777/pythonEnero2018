#-*-coding: utf-8*-
import os
os.system("cls")
#Declarmos nuestro diccionario vacío para guardar contactos
contactos={}
correos={}
print("\n\n\t\t\t\t\t\t\tBienvenido a la Súper Agenda")

while True:
    print("\n\t1.-Agregar un contacto")
    print("\n\t2.-Buscar un número")
    print("\n\t3.-Ver todos los contactos")
    print("\n\t4.-Eliminar un contacto")
    print("\n\t5.-Agregar correo")
    print("\n\t6.-Salir")

    opcionMenu=int(input("Opcion: "))
    if opcionMenu==1:
        #Agregar un contacto
        nombre=input("\n\n\t Ingrese el nombre del contacto: ")
        numero=int(input("Ingrese el número de teléfono: "))
        contactos[nombre]=numero
        os.system("cls")
    elif opcionMenu==2:
        #Buscar un contacto
        nombre=input("\n\n\t ¿Qué contacto quieres buscar?: ")
        os.system("cls")
        if nombre in contactos:
            print("\n Nombre: ", nombre)
            print("\n Teléfono: ", contactos[nombre])
        if nombre in correos:
            print("\n Correo: ", correos[nombre])
        else:
            print("\nError 404, contacto no encontrado")
    elif opcionMenu==3:
        #Ver todos los contactos
        os.system("cls")
        if len(contactos.items())==0:
            print("\n\n\t No hay contactos para mostrar :(")
        else:
            for persona in contactos.keys():
                print("\n\n\tEl numero de ",persona,"es :",contactos[persona])
                if nombre in correos:
                    print("\n Correo: ",correos[nombre])
    elif opcionMenu==4:
        nombre=input("\n\n\t ¿Qué contacto deseas borrar?: ")
        os.system("cls")
        if nombre in contactos:
            del contactos[nombre]
        if nombre in correos:
            del correos[nombre]
        else:
            print("\n Error 404, usuario no encontrado")
        #Eliminar un contacto
    elif opcionMenu==5:
        #Agregar correo del contacto
        nombre=input("\n\n\t Ingrese el nombre del contacto: ")
        correo=input("\n\n\t Agregar correo de contacto: ")
        os.system("cls")
        if nombre in contactos:
            correos[nombre]=correo
        else:
            print("\nError 404, contacto no encontrado")

    elif opcionMenu==6:
        #Salir
        os.system("cls")
        print("\n\n\t¡Regresa pronto!")
        break
    else:
        os.system("cls")
        print("\n\n\t¡Opción no válida, mejor muéranse")



    """
    if condicion: instrucciones
    elif condicion: instrucciones
    else: ultima opcion
    \t tabulador
    #Para borrar atributo de diccionario usamos del
    """