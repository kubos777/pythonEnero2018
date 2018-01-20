##Insertar imagen


from tkinter import *

ventana=Tk()

logo=PhotoImage(file="python.png")

label1=Label(ventana,image=logo).pack(side="right")

texto="Solamente podemos utilizar imagenes GIF o PNG para la funcion PhothoImage, para otro formato utilizamos el modulo PIL"

label2=Label(ventana,justify=LEFT,padx=10,text=texto).pack(side="left")
ventana.title("Imagen chida")
ventana.mainloop()