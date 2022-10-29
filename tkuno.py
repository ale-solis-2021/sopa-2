from tkinter import *
import tkinter.font as tkFont
from tkinter import messagebox
import tkinter
import random
import time

wind = Tk()
wind.geometry("1050x600")
wind.config(bg="#FFFFFF")
wind.title("SOPA DE LETRAS MAATRIX")
wind.iconbitmap("imagen.ico")

alfabeto=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']

nav = Frame(wind,bg="#AAC4FF",padx=6)
nav.pack(side="left",fill="y")

img = tkinter.PhotoImage(file="undraw_Books_re_8gea.png")# ABRIR CARPETA COMPLETA NO EL ARCHIVO 
portada = tkinter.Label(wind,image=img,background="#FFFFFF")
portada.pack()

marco = Frame(wind,padx=8,pady=8,bg="#B1B2FF")
marco1 = Frame(wind,padx=8,pady=8,bg="#B1B2FF")
marco2 = Frame(wind,padx=8,pady=8,bg="#B1B2FF")

Progreso = Frame(wind,padx=8,pady=8,bg="#B1B2FF")
Progreso1 = Frame(wind,padx=8,pady=8,bg="#B1B2FF")
Progreso2 = Frame(wind,padx=8,pady=8,bg="#B1B2FF")

fontStyle = tkFont.Font(size=10)

def ZoomIn():
    fontsize = fontStyle['size']
    fontStyle.configure(size=fontsize+2)

def ZoomOut():
    fontsize = fontStyle['size']
    fontStyle.configure(size=fontsize-2)

inp = Entry(Progreso,font=fontStyle,state=DISABLED)
inp1 = Entry(Progreso1,font=fontStyle,state=DISABLED)
inp2 = Entry(Progreso2,font=fontStyle,state=DISABLED)

def Comparar():
#                               ///P A L A B R A S\\\
    #EJEMPLO respuestas = ["CASA","HELADO","FRUTAS","POMELO"] LAS MISMAS DE LA CUADRICULA PARA COMPARAR
    respuestas = ["PICOS","COLMILLOS","HASTA","BRANQUIAS","CUERNOS","ESCAMAS","GARRAS","PLUMAS","PELAJE","PEZUÑAS","PATAS","ALAS","ALETAS"]
    
#                               ///P A L A B R A S\\\
    fila = 0
    for i in respuestas:
        if inp.get() == i:
            texto = Label(Progreso,text=i,font=fontStyle)
            texto.grid(row=fila,column=0,sticky=(W),padx=5,pady=2)
            fila = fila + 1
        else:
            fila = fila + 1

def Comparar1():
#                               ///P A L A B R A S\\\
    #EJEMPLO respuestas = ["CASA","HELADO","FRUTAS","POMELO"] LAS MISMAS DE LA CUADRICULA PARA COMPARAR
    respuestas = ["BANANA","POMELO","CIRUELA","UVA","PERA","NARANJA","MANDARINA","SANDIA"]
    
#                               ///P A L A B R A S\\\
    fila = 0

    for i in respuestas:
        if inp1.get() == i:
            texto = Label(Progreso1,text=i,font=fontStyle)
            texto.grid(row=fila,column=0,sticky=(W),padx=5,pady=2)
            fila = fila + 1
        else:
            fila = fila + 1

def Comparar2():
#                               ///P A L A B R A S\\\
    #EJEMPLO respuestas = ["CASA","HELADO","FRUTAS","POMELO"] LAS MISMAS DE LA CUADRICULA PARA COMPARAR
    respuestas = ["VIOLIN","GUITARRA","BOMBO","BAJO","BATERIA","FLAUTA","MARACAS","ACORDEON","PIANO"]
    
#                               ///P A L A B R A S\\\
    fila = 0

    for i in respuestas:
        if inp2.get() == i:
            texto = Label(Progreso2,text=i,font=fontStyle)
            texto.grid(row=fila,column=0,sticky=(W),pady=2)
            fila = fila + 1
        else:
            fila = fila + 1

acp = Button(Progreso,text="aceptar",font=fontStyle,padx=2,pady=2,command=Comparar,state=DISABLED)
acp1 = Button(Progreso1,text="aceptar",font=fontStyle,padx=2,pady=2,command=Comparar1,state=DISABLED)
acp2 = Button(Progreso2,text="aceptar",font=fontStyle,padx=2,pady=2,command=Comparar2,state=DISABLED)

minute=StringVar()
minute1=StringVar()
minute2=StringVar()

second=StringVar()
second1=StringVar()
second2=StringVar()

fin=BooleanVar()
fin1=BooleanVar()
fin2=BooleanVar()

fin.set(False)
fin1.set(False)
fin2.set(False)

minute.set("0")
minute1.set("0")
minute2.set("0")

second.set("0")
second1.set("0")
second2.set("0")

tiempo = Button(Progreso,text="Tiempo",font=fontStyle,command= lambda : fin.set(True))
tiempo1 = Button(Progreso1,text="Tiempo",font=fontStyle,command= lambda : fin1.set(True))
tiempo2 = Button(Progreso2,text="Tiempo",font=fontStyle,command= lambda : fin2.set(True))

minuteEntry= Entry(Progreso,width=3, font=fontStyle,textvariable=minute,state=DISABLED)
minuteEntry1= Entry(Progreso1,width=3, font=fontStyle,textvariable=minute1,state=DISABLED)
minuteEntry2= Entry(Progreso2,width=3, font=fontStyle,textvariable=minute2,state=DISABLED)

secondEntry= Entry(Progreso,width=3, font=fontStyle,textvariable=second,state=DISABLED)
secondEntry1= Entry(Progreso1,width=3, font=fontStyle,textvariable=second1,state=DISABLED)
secondEntry2= Entry(Progreso2,width=3, font=fontStyle,textvariable=second2,state=DISABLED)

def clock():
    comenzar.config(state=DISABLED)
    tiempo.grid(row=29,column=3,rowspan=32,sticky=(N,S,W,E))
    acp.config(state=NORMAL)
    inp.config(state=NORMAL)

    minute.set("3")# M I N U T O S
    second.set("20")# S E G U N D O S

    temp = int(minute.get()) * 60 + int(second.get())

    while temp > -1:
        mins,secs = divmod(temp,60)

        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))

        minuteEntry.update()
        secondEntry.update()
        time.sleep(1)

        if (temp == 0):
            messagebox.showinfo("","Tiempo")
            inp.config(state=DISABLED)
            acp.config(state=DISABLED)
        elif fin.get() == True:

            messagebox.showinfo("","Tiempo")
            inp.config(state=DISABLED)
            acp.config(state=DISABLED)
            break
         
        temp -= 1

def clock1():
    comenzar1.config(state=DISABLED)
    tiempo1.grid(row=29,column=3,rowspan=32,sticky=(N,S,W,E))
    acp1.config(state=NORMAL)
    inp1.config(state=NORMAL)

    minute1.set("2")# M I N U T O S
    second1.set("20")# S E G U N D O S

    temp = int(minute1.get()) * 60 + int(second1.get())

    while temp > -1:

        mins,secs = divmod(temp,60)

        minute1.set("{0:2d}".format(mins))
        second1.set("{0:2d}".format(secs))

        minuteEntry1.update()
        secondEntry1.update()
        time.sleep(1)

        if (temp == 0):
            messagebox.showinfo("","Tiempo")
            inp1.config(state=DISABLED)
            acp1.config(state=DISABLED)
        elif fin1.get() == True:
            messagebox.showinfo("","Tiempo")
            inp1.config(state=DISABLED)
            acp1.config(state=DISABLED)
            break
        
        temp -= 1

def clock2():
    comenzar2.config(state=DISABLED)
    tiempo2.grid(row=29,column=3,rowspan=32,sticky=(N,S,W,E))
    acp2.config(state=NORMAL)
    inp2.config(state=NORMAL)

    minute2.set("2")# M I N U T O S
    second2.set("20")# S E G U N D O S
    temp = int(minute2.get()) * 60 + int(second2.get())

    while temp > -1:

        mins,secs = divmod(temp,60)

        minute2.set("{0:2d}".format(mins))
        second2.set("{0:2d}".format(secs))

        minuteEntry2.update()
        secondEntry2.update()
        time.sleep(1)

        if (temp == 0):
            messagebox.showinfo("","Tiempo")
            inp2.config(state=DISABLED)
            acp2.config(state=DISABLED)
        elif fin2.get() == True:
            messagebox.showinfo("","Tiempo")
            inp2.config(state=DISABLED)
            acp2.config(state=DISABLED)
            break
         
        temp -= 1

comenzar = Button(Progreso,text="Comenzar",font=fontStyle,padx=5,pady=5,command=clock)
comenzar1 = Button(Progreso1,text="Comenzar",font=fontStyle,padx=5,pady=5,command=clock1)
comenzar2 = Button(Progreso2,text="Comenzar",font=fontStyle,padx=5,pady=5,command=clock2)


def Wel():
    portada.pack()

    marco.forget()
    marco1.forget()
    marco2.forget()

    Progreso.forget()
    Progreso1.forget()
    Progreso2.forget()

def Palabra(padre,eje,point,p = ""):
    if padre == marco:
        if eje == "y":
            for i,z in enumerate(p):
                btn = Label(padre,text=z,padx=5,pady=5,font=fontStyle,relief="solid",bd=1)
                btn.grid(row=i, column=point, sticky=N+S+E+W)
        elif eje == "x":
            for i,z in enumerate(p):
                btn = Label(padre,text=z,padx=5,pady=5,font=fontStyle,relief="solid",bd=1)
                btn.grid(row=point, column=i, sticky=N+S+E+W)
    elif padre == marco1:
        if eje == "y":
            for i,z in enumerate(p):
                btn = Label(padre,text=z,padx=5,pady=5,font=fontStyle,relief="solid",bd=1)
                btn.grid(row=i, column=point, sticky=N+S+E+W)
        elif eje == "x":
            for i,z in enumerate(p):
                btn = Label(padre,text=z,padx=5,pady=5,font=fontStyle,relief="solid",bd=1)
                btn.grid(row=point, column=i, sticky=N+S+E+W)
    elif padre == marco2:
        if eje == "y":
            for i,z in enumerate(p):
                btn = Label(padre,text=z,padx=5,pady=5,font=fontStyle,relief="solid",bd=1)
                btn.grid(row=i, column=point, sticky=N+S+E+W)
        elif eje == "x":
            for i,z in enumerate(p):
                btn = Label(padre,text=z,padx=5,pady=5,font=fontStyle,relief="solid",bd=1)
                btn.grid(row=point, column=i, sticky=N+S+E+W)

def Sopa():
    marco.pack(side="left",padx=10)

    Progreso.pack(side="left",padx=10)
    inp.grid(row=30,column=0,columnspan=2,padx=6,sticky=(N,S,W,E))
    acp.grid(row=30,column=2,sticky=(N,S,W,E))
    minuteEntry.grid(row=29,column=0)
    secondEntry.grid(row=29,column=1)
    comenzar.grid(row=29,column=2,sticky=(N,S,W,E))

#                       ///T E M A\\\

    Label(Progreso,text="Tema: características físicas de animales",font=fontStyle).grid(row=31,column=0,columnspan=3,sticky=(W,E),pady=4,padx=6)
    Label(Progreso,text="13 Palabras: MAYUSCULAS",font=fontStyle).grid(row=32,column=0,columnspan=3,sticky=(W,E),pady=4,padx=6)

#                       ///T E M A\\\

    for row_index in range(14):

        for col_index in range(14):
            btn = Label(marco,text=alfabeto[random.randint(0,25)],font=fontStyle,padx=5,pady=5,relief="solid",bd=1)
            btn.grid(row=row_index, column=col_index, sticky=N+S+E+W)

#                               ///P A L A B R A S\\\
    # recordar empujar palabras al centro de la cuadricula con letras sin sentido.
    Palabra(marco,"y",10,p = "AÑSLSLWDKPICOS")
    Palabra(marco,"y",7,p = "AÑSLSLWDKPATAS")
    Palabra(marco,"y",13,p = "AÑSCOLMILLOS")
    Palabra(marco,"y",11,p = "ESCAMASCUERNOS")
    Palabra(marco,"y",5,p = "ASKMDZIALETAS")
    Palabra(marco,"y",4,p = "ASIFWGARRAS")
    Palabra(marco,"y",2,p = "ZVAFTQPEZUÑAS")
    Palabra(marco,"y",12,p = "ÑMAZPLUMAS")

    Palabra(marco,"x",0,p = "JVHBRANQUIAS")
    Palabra(marco,"x",2,p = "PELAJE")
    Palabra(marco,"x",12,p = "XALAS")
    
#                               ///P A L A B R A S\\\
    portada.forget()

    marco1.forget()
    marco2.forget()

    Progreso1.forget()
    Progreso2.forget()

def Sopa1():
    marco1.pack(side="left",padx=10)
    Progreso1.pack(side="left",padx=10)
    inp1.grid(row=30,column=0,columnspan=2,padx=6,sticky=(N,S,W,E))
    acp1.grid(row=30,column=2,sticky=(N,S,W,E))
    minuteEntry1.grid(row=29,column=0)
    secondEntry1.grid(row=29,column=1)
    comenzar1.grid(row=29,column=2,sticky=(N,S,W,E))
#                       ///T E M A\\\

    Label(Progreso1,text="Tema: FRUTAS",font=fontStyle).grid(row=31,column=0,columnspan=3,sticky=(W,E),pady=4,padx=6)
    Label(Progreso1,text="8 Palabras: MAYUSCULAS",font=fontStyle).grid(row=32,column=0,columnspan=3,sticky=(W,E),pady=4,padx=6)

#                       ///T E M A\\\
    inp1.grid(row=30,column=0,columnspan=2,padx=6,sticky=(N,S,W,E))
    acp1.grid(row=30,column=2,sticky=(N,S,W,E))

    for row_index in range(14):

        for col_index in range(14):
            btn = Label(marco1,text=alfabeto[random.randint(0,25)],font=fontStyle,padx=5,pady=5,relief="solid",bd=1)
            btn.grid(row=row_index, column=col_index, sticky=N+S+E+W)

#                               ///P A L A B R A S\\\
    # recordar empujar palabras al centro de la cuadricula con letras sin sentido.
    # Ej: Palabra(padre,eje,point,p = "")
    # Palabra(marco1,x,0,p = "ABCFRUTAS")
    Palabra(marco1,"y",13,p = "AYTNCMANDARINA")
    Palabra(marco1,"y",11,p = "KXCDPOMELO")
    Palabra(marco1,"x",1,p = "AFEGTNSBANANA")
    Palabra(marco1,"x",4,p = "ÑNARANJA")
    Palabra(marco1,"x",6,p = "KXCIRUELA")
    Palabra(marco1,"y",9,p = "ANDERUIOSANDIA")
    Palabra(marco1,"x",12,p = "QSERPERA")
    Palabra(marco1,"x",9,p = "KSXTÑXUVA")
    
#                               ///P A L A B R A S\\\
    portada.forget()

    marco.forget()
    marco2.forget()

    Progreso.forget()
    Progreso2.forget()

def Sopa2():
    marco2.pack(side="left",padx=10)
    Progreso2.pack(side="left",padx=10)
    inp2.grid(row=30,column=0,columnspan=2,padx=6,sticky=(N,S,W,E))
    acp2.grid(row=30,column=2,sticky=(N,S,W,E))
    minuteEntry2.grid(row=29,column=0)
    secondEntry2.grid(row=29,column=1)
    comenzar2.grid(row=29,column=2,sticky=(N,S,W,E))
#                       ///T E M A\\\

    Label(Progreso2,text="Tema:INSTRUMENTOS MUSICALES",font=fontStyle).grid(row=31,column=0,columnspan=3,sticky=(W,E),pady=4,padx=6)
    Label(Progreso2,text="9 Palabras: MAYUSCULAS",font=fontStyle).grid(row=32,column=0,columnspan=3,sticky=(W,E),pady=4,padx=6)

#                       ///T E M A\\\
    inp2.grid(row=30,column=0,columnspan=2,padx=6,sticky=(N,S,W,E))
    acp2.grid(row=30,column=2,sticky=(N,S,W,E))

    for row_index in range(14):

        for col_index in range(14):
            btn = Label(marco2,text=alfabeto[random.randint(0,25)],font=fontStyle,padx=5,pady=5,relief="solid",bd=1)
            btn.grid(row=row_index, column=col_index, sticky=N+S+E+W)
    
#                               ///P A L A B R A S\\\
    # recordar empujar palabras al centro de la cuadricula con letras sin sentido.
    # Ej: Palabra(padre,eje,point,p = "")
    # Palabra(marco2,x,0,p = "ABCFRUTAS")
    Palabra(marco2,"y",1,p = "ÑVIOLIN")
    Palabra(marco2,"y",2,p = "KXCDGLGUITARRA")
    Palabra(marco2,"y",4,p = "AFBOMBO")
    Palabra(marco2,"x",2,p = "ÑIXLBHACORDEON")
    Palabra(marco2,"x",3,p = "KOCIOVSBLPIANO")
    Palabra(marco2,"y",7,p = "ANCFBAJO")
    Palabra(marco2,"y",12,p = "QSONNHZBATERIA")
    Palabra(marco2,"x",9,p = "AKTMZFLAUTA")
    Palabra(marco2,"x",11,p = "MLRZMARACAS")
#                               ///P A L A B R A S\\\
    portada.forget()

    marco.forget()
    marco1.forget()

    Progreso.forget()
    Progreso1.forget()

inicio = Button(nav,text="Inicio",padx=2,pady=2,font=20,command=Wel).pack(pady=8,fill="x")
desafio1 = Button(nav,text="Desafio 1",padx=2,pady=2,font=20,command=Sopa).pack(pady=8,fill="x")
desafio2 = Button(nav,text="Desafio 2",padx=2,pady=2,font=20,command=Sopa1).pack(pady=8,fill="x")
desafio3 = Button(nav,text="Desafio 3",padx=2,pady=2,font=20,command=Sopa2).pack(pady=8,fill="x")

Button(nav,text="ZOOM - ",padx=2,pady=2,command=ZoomOut).pack(side="bottom",pady=8,fill="x")
Button(nav,text="ZOOM + ",padx=2,pady=2,command=ZoomIn).pack(side="bottom",pady=8,fill="x")


wind.mainloop()