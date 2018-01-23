from sklearn import tree
Datos=[[200,0],[800,1],[100,0],[900,1]]
fruta=["apple", "pineapple","apple","pineapple"]#[0, 1,0,1]
clasificar = tree.DecisionTreeClassifier()
clasificar = clasificar.fit(Datos, fruta)

while True:
	print("Programa que define entre manzanas y piñas")
	print("Escribe salir para cerrar el programa o entre para continuar")
	if input("")=="salir":
		break
	else:
		peso=int(input("Ingrese el peso de la fruta en gramos: "))
		color=int(input("Ingrese [0] si la fruta es roja o [1] si es amarilla: "))
		print("La fruta es: ",	clasificar.predict([[peso,color]]))