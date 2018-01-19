def Modulos():
	try:
		import os
		import Tkinter
	except ModuleNotFoundError as error:
		print("Este modulo es para python 2.7, para la nueva version se usa tkinter")
		print(error.args)
		b=input()
		import tkinter
	finally:
		os.system("cls")
		print("hay que corregir el error")

def LeerArchivos():
	leer = input("Dime el nombre e tu archivo")
	archi = leer + ".txt"
	try:
		f = open(archi)
		cadena = f.read()
		print(cadena)
	except FileNotFoundError:
		print("No existe")
	else:
		print("No ocurrio error alguno")
		
	finally:
		print("Se ha acabado la secuencia")

LeerArchivos()
