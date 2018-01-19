import sqlite3

nombre=input("Nombre: ")
apellido=input("Apellidos: ")
sueldo=float(input("Sueldo: $ "))

conexion=sqlite3.connect("empleados.db")

cursor= conexion.cursor()
#Para que me de solo dos decimales  coloco %.2f o donde va el 2, el número de decimales que quiera
cursor.execute("INSERT INTO empleado(nombre,apellido,sueldo) VALUES ('%s','%s','%.2f')"%(nombre,apellido,sueldo))

conexion.commit()

print("Se ha insertado el registro, con id: ",cursor.lastrowid)

conexion.close()


