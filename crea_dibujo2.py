import turtle
import tkinter as tk

ventana = tk.Tk()
ventana.title("CREA DIBUJO 2")
canvas = tk.Canvas(master = ventana, width = 800,  height = 800)
canvas.pack()

t = turtle.RawTurtle(canvas)
#t.pencolor("black")

ventana.mainloop()
