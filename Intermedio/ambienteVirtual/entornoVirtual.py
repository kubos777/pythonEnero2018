from cx_Freeze import setup,Executable
#La base se refiere a si se ejecutará en consola o si existe alguna GUI(Graphical User Interface)
base=None

#Declaramos una lista la cual contendrá la base y los scripts que 
#se convertirán a .exe o .bin
executables=[Executable("magicos.py",base=base)]
#Si se incluyen modulos o paquetes externos debemos crear una lista con
#ellos, por ejemplo: packages=['numpy','scipy']
packages=['os']

#Debemos crear un diccionario para indicar los paquetes con los que
#se construirá el ejecutable
options={
	'build_exe':{
	'packages':packages,
	},
}

#Finalmente configuramos por medio de una tupla
#los siguientes parámetros o atributos

setup(
	name='Métodos mágicos',
	options=options,
	version='1.1',
	description="Programa que enseña los métodos mágicos",
	executables=executables
	)