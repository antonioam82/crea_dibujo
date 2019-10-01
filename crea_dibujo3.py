import turtle
from tkinter import *
from tkinter import colorchooser
#from tkinter.filedialog import askopenfile

ventana=Tk()
ventana.geometry("860x800")
ventana.configure(background="gray80")
numLados=StringVar()
grosor=StringVar()
lista_colores=[]
canvas = Canvas(master = ventana, width = 860, height = 735)
canvas.pack()

t = turtle.RawTurtle(canvas)

def color(m):
    global lista_colores
    color_selec=colorchooser.askcolor()
    if color_selec!=(None,None):
        bgrcolor=list(color_selec)
        if m == "f":
            t.screen.bgcolor(bgrcolor[1])
        else:
            lista_colores.append(bgrcolor[1])
    


etiLados=Label(master=ventana,text="Numero Lados",bg="gray80")
etiLados.place(x=1,y=744)
entLados=Entry(master=ventana,textvariable=numLados)
entLados.place(x=85,y=744)
etiGrosor=Label(master=ventana,text="Grosor",bg="gray80")
etiGrosor.place(x=220,y=744)
entGrosor=Entry(master=ventana,textvariable=grosor)
entGrosor.place(x=260,y=744)
btnColor=Button(master=ventana,text="Color Pincel",bg="gray74",command=lambda:color("c"))
btnColor.place(x=415,y=740)
btnFondo=Button(master=ventana,text="Color Fondo",bg="gray74",command=lambda:color("f"))
btnFondo.place(x=520,y=740)
btnClear=Button(master=ventana,text="Clear",bg="gray74")
btnClear.place(x=625,y=740)
btnGuardar=Button(master=ventana,text="Guardar",bg="gray74",width=21)
btnGuardar.place(x=700,y=740)
Button(master = ventana,text="Crear",bg="spring green",width=121).place(x=1,y=771)
ventana.mainloop()
