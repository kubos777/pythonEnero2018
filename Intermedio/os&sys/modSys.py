#############################
#Módulo SYS
#############################
#El módulo sys es el encargado de proveer variables,
#y funcionalidades, directamente relacionadas con el interpréte.
#Entre las variables más destacadas podemos encontrar las siguientes: 

#Importamos el módulo
import sys

print(sys.platform)
print(sys.version) #Me devuelve la versión del interprete

print(sys.argv) #Parámetros de la línea de comandos

contador=0

for parametro in sys.argv:
	#Imprimimos el parametro/elemento de la lista
	print("Parámetro %i : es: %s"%(contador,parametro))
	contador+=1

