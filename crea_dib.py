from turtle import Turtle
from VALID import OKI, ns
import os
import subprocess

if not os.path.exists("Dibujos"):
	os.makedirs("Dibujos")
	os.chdir("Dibujos")

def ver(lii):
    try:
        lii[0]==int(lii[0])
        lii[1]==int(lii[1])
        t.color(lii[2])
        return lii
    except:
        return False

def col(lista):
    n=0
    res=[]
    for i in lista:
        if n>=3: #mejor "if n>3:"
            res.append(i)
        n+=1
    return res
            
    
def datt(li):
    li=li.split(",")
    lista=[]
    for i in li:
        try:
            i=int(i)
        except:
            try:
                i=float(i)
            except:
                i=str(i)
        lista.append(i)
    return lista

while True:
    t=Turtle()
    t.hideturtle()
    t.speed(0)
    print("Escoja opción.")
    print("A)Crear dibujo personalizado")
    print("B)Reproducir dibujo guardado")
    op=input("Introduzca aquí su opción: ")
    while op!=("A") and op!=("B"):
        op=input("Ecriba solo \'A\' o \'B\' según su opción: ")
    punt=ns(input("¿Mostrar flecha?: "))
    epec=ns(input("¿Especificar grosor de linea?: "))
    
    if op==("A"):
        if epec=="s":
            grosor=OKI(input("Introduzca grosor de la línea: "))
            while grosor<0:
                grosor=OKI(input("El grosor de la línea no puede ser menor que 0: "))
            t.pensize(grosor)
        atrib=ver(datt(input("Introduce nºciclos, grados de giro y color de fondo, separados por coma: ")))
        while atrib==False:
            atrib=ver(datt(input("Datos incorrectos: ")))
        colors=datt(input("Introduce colores separados por coma: "))
        
    elif op==("B"):
        if epec=="s":
            grosor=OKI(input("Introduzca grosor de la línea: "))
            while grosor<0:
                grosor=OKI(input("El grosor de la línea no puede ser menor que 0: "))
            t.pensize(grosor)
        import pickle
        fig=input("Introduzca el nombre de la figura guardada que desea ver: ")
        while True:
            try:
                atrib=pickle.load(open(fig,"rb"))
                colors=col(atrib)
                break
            except:
                fig=input("El archivo solicitado no se encontró o no es apto para este programa: ")

    try:
        if punt==("s"):
            t.showturtle()
        t.screen.bgcolor(atrib[2])
        for x in range(atrib[0]):
            t.color(colors[x%(len(colors))])
            t.fd(x)
            #t.forward(2*x)
            t.left(atrib[1])
        
        print("¡HECHO!",chr(7))
        
        if op==("A"):
            guard=ns(input("¿Desea guardar el dibujo creado?: "))
            if guard==("s"):
                import pickle
                dibujo=atrib+colors
                nom=input("¿Que nombre desea dar  al dibujo?: ")
                if nom in os.listdir():
                    seguir=ns(input("Yá existe un archivo con ese nombre ¿Desea sobreescribirlo?: "))
                    if seguir=="s":
                        pass
                    else:
                        subprocess.call(["cmd.exe","/C","cls"])
                        t.reset()
                        continue
                pickle.dump(dibujo,open(nom,"wb"))
                print("¡HECHO!",chr(7))
    except:
        print("El archivo solicitado o los datos introducidos no son aptos para su ejecución en este programa.")#intentar "fig"
        
    
    conti=ns(input("¿Continuar?: "))
    if conti==("s"):
        t.reset()
        t.hideturtle()
        subprocess.call(["cmd.exe","/C","cls"])
    else:
        break
#t.screen.exitonclick()
#t.screen.mainloop()
