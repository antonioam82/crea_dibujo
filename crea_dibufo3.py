import turtle
from tkinter import *
#from tkinter.filedialog import askopenfile

ventana=Tk()
ventana.geometry("860x800")
canvas = Canvas(master = ventana, width = 860, height = 760)
canvas.pack()

t = turtle.RawTurtle(canvas)


Button(master = ventana,text="Crear", width=8).place(x=430,y=770)
ventana.mainloop()
