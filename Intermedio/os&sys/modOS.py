###########
# Modulo OS
###########

"""
El modulo OS nos provee de métodos para trabajar de forma portable
con las funcionalidades del sistema operativo.
A continuación veremos los métodos más destacados de este modulo:
"""
#Importamos el modulo
import os

#Lista todo el contenido del modulo, funciones, métodos etc...
#print(dir(os))
#Windows: nt,Linux: posix,Mac: darwin
print("Nombre del sistema operativo: ",os.name)
#Nos permiet invocar un comando externo
os.system("dir")

#Ese método es equivalente a pwd en Linux
print("La carpeta actual en la que estas es: ",os.getcwd())
#Un punto se refiere a la carpecta actual y dos puntos a una carpeta antes
print("Listar contenido: ",os.listdir(".."))
#El método listdir recibe como argumento una ruta
#Necesitamos escapar la doble comilla del final con una antidiagonal \
#print("Todo lo que hay en el disco: ",os.listdir('C:\\'))
directorios=os.listdir('C:\\')
i=0
for directorio in directorios:
	print("Directorio %i: %s"%(i,directorio))
	#i=i+1
	i+=1
#Crear carpeta
#os.mkdir("Nueva carpeta") #Si creamos una carpeta con el mismo nombre, causa error
print(os.listdir("."))
#Borrar carpeta
#os.rmdir("Nueva carpeta")#Si intentamos borrar una carpeta que no existe, causa error

#os.chdir("Nueva Carpeta")
print("La carpeta actual en la que estas es: ",os.getcwd())

os.rename("Nueva","Nueva nueva Carpeta")

print(os.listdir("."))


