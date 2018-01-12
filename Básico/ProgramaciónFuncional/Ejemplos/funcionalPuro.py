#################################
#Funciones lambdas
#################################

#Sintaxis de una función lamda
#funcion=( lambda  args : operación )
#No hay ciclos
cubo=(lambda x:x**3)
print(cubo(3))
suma=(lambda a,b,c:a+b+c)
print(suma(1,2,3))

#Fibonacci con lambda
fib =(lambda n: n if n<2 else fib(n-1)+fib(n-2))

print(fib(10))


# map() aplica una funcion a cada elemento de una secuencia y nos crea una
# nueva lista con los valores devuelto por la funcion

li=[1,2,3,4,5,6,7,8]

li2= map(lambda n: n**2,li) #usando lambda ponemos una funcion que eleva al cuadrado

print("Los elementos de la lista 1 elevados al cuadrado: ",list(li2))


# ahora exactamente lo mismo pero con una funcion normal

def cuadrado(a):
    return a**2
li2=map(cuadrado,li)
print("Los elementos de la lista 1 elevados al cuadrado: ",list(li2))



# filter() hace lo mismo que map solo que la funcion debe ser verdadera o falsa
# si es falsa, no añade el valor a la nueva lista

li2=filter(lambda n: n%4==0,li)   # multiplos de 4
print("Los multiplos de la lista 1: ",list(li2))


# reduce() aplica la funcion a dos elementos de la lista, los remueve y añade el
# valor obtenido por la funcion, sigue asi hasta que haya un solo valor
import functools

li2=functools.reduce(lambda a,b:a+b,li)  # suma todos los elementos de li
print("La suma de todos los elementos de la lista 1: ",li2)



