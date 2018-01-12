peso = float(input("Ingresar peso: "))
estatura = float(input("Ingresar estatura"))

imc = peso/(estatura**2)

if imc < 18.5:
	print("Bajo de peso")
elif imc < 24.9:
	print("Normal")
elif imc <29.9:
	print("Gordito")
else:
	print("Gordo")