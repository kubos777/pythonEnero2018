
# coding: utf-8

# # Usando Simpy
# Simpy es un módulo que nos permite el manejo de computacion matematica y simbólica
# Entres sus funciones destaca:
# 1. Simplificar Terminos
# 2. Hacer Derivadas
# 3. Hacer integrales con y sin intervalos
# 4. Hacer Matrices

# ## Simplificacion
# 

# In[8]:

from sympy import *
x, y, z = symbols('x y z')
init_printing(use_unicode = True)
pitagoras = simplify(sin(x)**2 + cos(x)**2)
print(pitagoras)
a = simplify((x**3+x**2-x-1)/(x**2+2*x+1))
print(a)
b = simplify(gamma(x)/gamma(x-2))
#print(b)


# ## Expand
# Con esta función expandimos las funciones polionominales

# In[15]:

termino = expand((x+1)**2)
print(termino)
termino_2 = expand((x+2)*(x-3))
print(termino_2)


# ## Factor
# Esta funcion es lo opuesto a "Expandir", esta funcion reduce los terminos hasta un valor irreducibe

# In[18]:

factor(x**3 - x**2 + x-1)
factor(x**2*z + 4*x*y*z + 4*y**2*z)


# ## Cancel
# La funcion cancel tomará cualquier función racional y la colocará en la forma estándar (canónica)

# In[29]:

expresion = 1/x + (3*x/2-2)/(x-4)
print("Expresion normal")
#print(expresion)
print("Expresion usando Cancel")
cancel(expresion)
#print(b)


# In[34]:

funcion = (x*y**2 - 2*x*y*z + x*z**2 + y**2 - 2*y*z + z**2)/ (x**2-1)
funcion
cancel(funcion)


# In[41]:

funcion_2 = (4*x**3 + 21*x**2 + 10*x+12)/(x**4 + 5*x**3+5*x**2+4*x)
funcion_2
#cancel(funcion_2)
###Solo efectúa cambios si la funcion así lo permite


# ## Apart
# La funcion apart realizará una descomposición parcial de una función racional
# 

# In[48]:

funcion_3 = (4*x**3 +21*x**2 +10*x+12)/(x**4+5*x**3+5*x**2+4*x)
#funcion = (x*y**2 - 2*x*y*z + x*z**2 + y**2 - 2*y*z + z**2)/ (x**2-1)
funcion_3
apart(funcion_3)
#apart(funcion)


# ## Usando Derivadas
# 

# In[51]:

diff(cos(x), x)
diff(exp(x**2), x)
diff(x**2, x)


# In[52]:

diff(x**4,x,3)
diff


# In[55]:

funcion= (x**2+3)
funcion_3 = (4*x**3 +21*x**2 +10*x+12)/(x**4+5*x**3+5*x**2+4*x)
derivada = Derivative(funcion_3)
derivada


# ## Usando Integrales
# 

# In[57]:

integrate(cos(x), x)
integrate(x**2,x)


# In[61]:

###integrar por intervalos
integrate(x**2,(x, 0, 900))
##para integrar con intervalos "infinitos" se escribe con 2 letras "o" = oo


# In[63]:

Integral(sqrt(1/x), x)
Integral(x**2+3,x)


# ## Matrices

# In[64]:

Matrix([[1,2],[3,4]])


# # Usando Numpy

# In[68]:

import numpy as np
a = np.array([1,2,3,4])
b = np.array([(1,2),(2,3)])
b


# In[72]:

####areglo del 1 al 15
arreglo = np.arange(15).reshape(3,5)
print(arreglo)
forma = arreglo.shape ###forma matricial
tamaño = arreglo.size ## Tamaño de la matriz ¿Cuiantos elementos tiene?
print("El tamaño de la matrz de  forma matricial es:")
print(forma)
print("los elemntos dentro de la matriz son: ")
print(tamaño)


# In[73]:

Matriz_complex = np.array([[2,3],[5,6]], dtype= complex)
print("matriz compleja")
Matriz_complex


# ## Variantes de matrices

# In[74]:

a = np.zeros((3,4))
print("MAtriz de ceros")
print(a)


# In[75]:

a = np.ones((2,2))
print("Matriz de unos")
print(a)


# In[78]:

##c = np.array([[1,2],[3,4]], dtype=int16)
###Matriz vacia
c = np.empty((3,3))
print(c)


# In[84]:

####Secuencia de numeros con "arange"
mz = np.arange(10,6000000, 2)
print("Matriz que inicia en 10 y termina en 60, con paso de 2 en 2")
print(mz)
###La sentencia Linspace no da la cantidad de elementos que deseamos imprimir
ms = np.linspace(0, 2, 900)
print("de 0 a 2 que me improma 3 numeros")
print(ms)


# ## Operaciones con matricex
# Para realizar operacion con matrices se debe asegurar que se cumplan con las propiedades de las mismas, de manera contraria python no permitirá hacer la operación y nos marcará algún error. a resolución de matrices se hace de manera automática

# In[96]:

a = np.array([[1,2], [2,3]])
b = np.array([[5,6],[7,8]])
print("Matrices originales")
print(a)
print(b)
print("Resta de matrices")
c = b-a
print(c)
print("suma de matrices")
c = b+a
print(c)
print("¿Multiplicacion si, pero elemento a elemento no de manera operacion matricial")
c = np.multiply(a,b) ###multiplicacion
print(c)
print("Factorial usanod asterisco *")
print(a*b) ##factorial?
print("Multiplicacion de matrices de manera matricial")
c = np.dot(a,b) ### Manera matricial mutiplicacion
print(c)


# ## Usando Álgebra Lineal
# Se puede implementar algunas opperaciones de Álgebra Lineal Básica
# 

# In[105]:

a = np.matrix([[1,2,3],[4,5,6],[7,8,9]])
print("Matriz original")
print(a)
transpuesta = a.T ###Matriz traspuesta
print("Matriz traspuesta")
print(transpuesta)
print("Matriz inversa")
##inversa = a.linalg.inv() ##matriz inversa
##print(inversa)
print("Determinante de la matriz")
deter= np.linalg.det(a)
print(deter)
print("Traza de una matriz")
traza = np.trace(a)
print(traza)


# ## Ejercicio:
# Usando numpy y/o sympy
# realizar:
# 1. 2 derivadas
# 2. 2 integrales
# 3. 2 simplificaciones de terminos
# 4. 2 operacione con matrices

# In[ ]:



