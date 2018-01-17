############
#Programa que busca si existe una palabra en un archivo,
#y cuantas veces
############

palabra=input("Ingresa la palabra que quieres buscar: ")

f=open("prueba.txt","r")

texto=f.read()
"""El método split() aplicado a un string,
crea una lista en la que cada elemento es una palabra del string.
No importa si son mil espacios, saltos de línea o tabuladoress,
la va a dividir."""
palabras=texto.split("\n")

print(palabras)

if palabra in palabras:
	print("La palabra se encuentra ",palabras.count(palabra)," veces en el archivo.")
else:
	print("La palabra no se encontró! :c lo siento")