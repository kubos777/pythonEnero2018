class Perro:
    def __init__(self, peso):
        self.peso = peso
        
    #se manda llamar cuando se intenta llamar el objeto como si fuera una funcion
    def __call__(self):
        print ("Guau!!!")

    #se manda llamar cuando se quiere comparar el objeto con <,>,==, etc
    #tiene que devolver 0 si son iguales, 1 si es mayor, -1 si es menor
    #def __cmp__(self,otro):
    #    if self.peso > otro.peso:
    #        return 1 
    #    elif self.peso < otro.peso:
    #        return -1
    #    elif self.peso == otro.peso:
    #        return 0
    #Esto no funcion para python 3... Ya que se ha eliminado el metodo __cmp__()

    #Tenemos que definir nosotros todas las comparaciones
    
    def __lt__(self, otro):
        return self.peso< otro.peso #< 0
    def __gt__(self, otro):
        return self.peso>otro.peso  #> 0
    def __eq__(self, otro):
        return self.peso==otro.peso #== 0
    def __le__(self, otro):
        return self.peso<=otro.peso #<= 0
    def __ge__(self, otro):
        return self.peso>=otro.peso #>= 0
    def __ne__(self, otro):
        return self.peso!=otro.peso #!= 0
#Ejemplo
p1 = Perro(34)
p2 = Perro(12)
p3 = Perro(20)
p4 = Perro(34)

#Esto era para Python 2 <---- Implementando los magicos del 3
print(p2 > p1)   # para todos estos se manda a llamar p2.__cmp__(p1)<--- Para python 3 manda a los magicos: 
print(p2 < p3)   # p2.__cmp__(p3) <--- Para python 3 manda a llamar a __lt__ o __gt__
print(p1 == p4)  # p1.__cmp__(p4) <--- Para python 3 manda a llamar a __eq__
print(p1 != p4)  # p2.__cmp__(p1) <--- Para python 3 manda a llamar a __ne__


p1() # se manda a llamar p1.__call__()