######################
#Copiar archivo a otro
######################

origen=open(input("Archivo origen: "),"r+")
destino=open(input("Archivo destino: "),"w")

#Con ciclo for

for  linea in origen.readlines():
	destino.write(linea)