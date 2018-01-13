######################################
# Recursividad
###################################
"""
def factorialIterativo(n):
	acum=1
	if n==1 or n==0:
		return 1
	else:
			for num in range(1,n+1):
				acum=acum*num
				#acum*=acum Forma corta de hacer lo de arriba
			return acum
print("El factorial de %d es %d"%(0,factorialIterativo(0)))
print("El factorial de %d es %d"%(1,factorialIterativo(1)))
print("El factorial de %d es %d"%(2,factorialIterativo(2)))
print("El factorial de %d es %d"%(3,factorialIterativo(3)))
print("El factorial de %d es %d"%(10,factorialIterativo(10)))
"""
"""
def factorialRecursivo(n):
	if n<2:
		return 1
	return n*factorialRecursivo(n-1)
#El %d hace referencia a que en ese lugar, se va a imprimir un dato de tipo entero
print("El factorial de %d es %d"%(0,factorialRecursivo(0)))
print("El factorial de %d es %d"%(2,factorialRecursivo(2)))
print("El factorial de %d es %d"%(3,factorialRecursivo(3)))
print("El factorial de %d es %d"%(4,factorialRecursivo(4)))
print("El factorial de %d es %d"%(5,factorialRecursivo(5)))
print("El factorial de %d es %d"%(998,factorialRecursivo(998)))

print("\nEl factorial de 0 es: ",factorialRecursivo(0))
"""


def fiboRecursivo(n):
	if n==0:
		return 0
	elif n==1:
		return 1
	return(fiboRecursivo(n-1)+fiboRecursivo(n-2))

print("El fibonacci de %d es %d"%(0,fiboRecursivo(0)))
print("El fibonacci de %d es %d"%(1,fiboRecursivo(1)))
print("El fibonacci de %d es %d"%(2,fiboRecursivo(2)))
print("El fibonacci de %d es %d"%(3,fiboRecursivo(3)))
print("El fibonacci de %d es %d"%(10,fiboRecursivo(10)))
print("El fibonacci de %d es %d"%(100,fiboRecursivo(100)))