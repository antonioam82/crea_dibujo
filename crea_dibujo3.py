#!/usr/bin/env python
# -*- coding: utf-8 -*-
import turtle
from tkinter import *
from tkinter import colorchooser
#from tkinter.filedialog import askopenfile
from tkinter import messagebox

ventana=Tk()
ventana.geometry("860x800")
ventana.configure(background="gray80")
st=True
grosor=""

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
            t.color(lista_colores[0])
def hide():
    global st
    if st==True:
        t.hideturtle()
        st=False
    else:
        t.showturtle()
        st=True

def clear():
    global lista_colores
    t.reset()
    lista_colores=[]

def crear():
    global grosor
    d=1
    t.speed(0)
    grosor=entGrosor.get()
    if grosor!="":
        t.pensize(int(grosor))
    try:
        for i in range(int(entLados.get())):
            if len(lista_colores)>1:
                t.color(lista_colores[i%(len(lista_colores))])
            t.left(int(entGrados.get()))
            t.fd(d)
            d+=1
    except:
        messagebox.showwarning("ERROR","Datos introducidos erroneos o insuficientes")
        
        
    
etiLados=Label(master=ventana,text="Numero Mov",bg="gray80")
etiLados.place(x=1,y=744)
etiGrados=Label(master=ventana,text="Grados",bg="gray80")
etiGrados.place(x=160,y=744)
entGrados=Entry(master=ventana,width=10)
entGrados.place(x=200,y=744)
entLados=Entry(master=ventana,width=10)
entLados.place(x=85,y=744)
etiGrosor=Label(master=ventana,text="Grosor",bg="gray80")
etiGrosor.place(x=267,y=744)
entGrosor=Entry(master=ventana,width=10)
entGrosor.place(x=310,y=744)
btnColor=Button(master=ventana,text="Color Pincel",bg="gray74",command=lambda:color("c"))
btnColor.place(x=415,y=740)
btnFondo=Button(master=ventana,text="Color Fondo",bg="gray74",command=lambda:color("f"))
btnFondo.place(x=520,y=740)
btnClear=Button(master=ventana,text="Clear",bg="gray74",command=clear)
btnClear.place(x=739,y=740)
btnGuardar=Button(master=ventana,text="Guardar",bg="gray74",width=10)
btnGuardar.place(x=778,y=740)
btnHide=Button(master=ventana,text="Hide/Show",bg="gray74",command=hide)
btnHide.place(x=650,y=740)
Button(master = ventana,text="Crear",bg="spring green",width=121,command=crear).place(x=1,y=771)

ventana.mainloop()




