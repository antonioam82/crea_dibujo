import turtle
from tkinter import *
#from tkinter.filedialog import askopenfile

ventana=Tk()
ventana.geometry("860x800")
ventana.configure(background="gray80")
canvas = Canvas(master = ventana, width = 860, height = 735)
canvas.pack()

t = turtle.RawTurtle(canvas)


Button(master = ventana,text="Crear",bg="spring green",width=121).place(x=1,y=771)
ventana.mainloop()
