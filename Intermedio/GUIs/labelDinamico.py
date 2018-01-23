###############
# Label Dinamico 
################

from tkinter import *

contador=0

def incrementar(label):
	#Esta funcion manda a llamar a contar y le pasa el label
	def contar():
		global contador
		contador-=5
		label.config(text=str(contador))

		#la funcion after llama a un callback despues de un tiempo det6erminado esto en milisegundos
		#after(tiempo_ms, callback=None, *args) 
		label.after(100, contar)
		if contador==-100:
			contador=0
	contar()

v=Tk()
v.title("Cuenta hasta 100")
lb1=Label(v,fg="red",width=40,height=2)
lb1.pack()
incrementar(lb1)
b1=Button(v,text="salir",width=25,command=v.destroy)
b1.pack()
v.mainloop()
