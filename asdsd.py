from tkinter import *
import tkinter.font as tkFont
from tkinter import messagebox
import tkinter
import random
import time

wind = Tk()
wind.geometry("1050x600")
wind.config(bg="#FFFFFF")
wind.title("")# DECIDAN EL TITULO QUE APARECE EN VENTANA
wind.iconbitmap("")# DECIDAN EL ICONO QUE APARECE EN VENTANA TIENE QUE SER '.ico'

alfabeto=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']

fontStyle1 = tkFont.Font(size=50)

nav = Frame(wind,bg="#AAC4FF",padx=6)
nav.pack(side="left",fill="y")

marco1 = Frame(wind,padx=8,pady=8,bg="#B1B2FF")


Progreso1 = Frame(wind,padx=8,pady=8,bg="#B1B2FF")

fontStyle = tkFont.Font(size=10)

def ZoomIn():
    fontsize = fontStyle['size']
    fontStyle.configure(size=fontsize+2)

def ZoomOut():
    fontsize = fontStyle['size']
    fontStyle.configure(size=fontsize-2)

inp1 = Entry(Progreso1,font=fontStyle,state=DISABLED)

def Comparar1():
#                               ///P A L A B R A S\\\
    #EJEMPLO respuestas = ["CASA","HELADO","FRUTAS","POMELO"] LAS MISMAS DE LA CUADRICULA PARA COMPARAR
    respuestas = ["CASA","HELADO","FRUTAS"]
#                               ///P A L A B R A S\\\
    for i in respuestas:
        if inp1.get() == i:

            if i == "CASA":
                Palabra(marco1,"x",0,color="green",Fcolor="#FFFFFF",p = "CASA")

            elif i == "HELADO":
                Palabra(marco1,"y",7,color="green",Fcolor="#FFFFFF",p = "HELADO")
                
            elif i == "FRUTAS":
                Palabra(marco1,"x",9,color="green",Fcolor="#FFFFFF",p = "FRUTAS")


acp1 = Button(Progreso1,text="aceptar",font=fontStyle,padx=2,pady=2,command=Comparar1,state=DISABLED)


minute1=StringVar()

second1=StringVar()

fin1=BooleanVar()

fin1.set(False)

minute1.set("0")

second1.set("0")

tiempo1 = Button(Progreso1,text="Tiempo",font=fontStyle,command= lambda : fin1.set(True))

minuteEntry1= Entry(Progreso1,width=3, font=fontStyle,textvariable=minute1,state=DISABLED)

secondEntry1= Entry(Progreso1,width=3, font=fontStyle,textvariable=second1,state=DISABLED)

def clock1():
    tiempo1.grid(row=29,column=3,rowspan=32,sticky=(N,S,W,E))
    acp1.config(state=NORMAL)
    inp1.config(state=NORMAL)

    minute1.set("03")
    second1.set("00")
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
            comenzar1.config(state=DISABLED)
        elif fin1.get() == True:
            messagebox.showinfo("","Tiempo")
            inp1.config(state=DISABLED)
            acp1.config(state=DISABLED)
            comenzar1.config(state=DISABLED)
            break
        
        temp -= 1

comenzar1 = Button(Progreso1,text="Comenzar",font=fontStyle,padx=5,pady=5,command=clock1)

def Palabra(padre,eje,point,color="",Fcolor="",p = ""):
    if padre == marco1:
        if eje == "y":
            for i,z in enumerate(p):
                btn = Label(padre,text=z,padx=5,pady=5,font=fontStyle,relief="solid",bd=1,bg=color,fg=Fcolor)
                btn.grid(row=i, column=point, sticky=N+S+E+W)
        elif eje == "x":
            for i,z in enumerate(p):
                btn = Label(padre,text=z,padx=5,pady=5,font=fontStyle,relief="solid",bd=1,bg=color,fg=Fcolor)
                btn.grid(row=point, column=i, sticky=N+S+E+W)

def Sopa1():
    marco1.pack()
    Progreso1.pack()
    inp1.grid(row=30,column=0,columnspan=2,padx=6,sticky=(N,S,W,E))
    acp1.grid(row=30,column=2,sticky=(N,S,W,E))
    minuteEntry1.grid(row=29,column=0)
    secondEntry1.grid(row=29,column=1)
    comenzar1.grid(row=29,column=2,sticky=(N,S,W,E))
    inp1.grid(row=30,column=0,columnspan=2,padx=6,sticky=(N,S,W,E))
    acp1.grid(row=30,column=2,sticky=(N,S,W,E))

    for row_index in range(15):

        for col_index in range(15):
            btn = Label(marco1,text=alfabeto[random.randint(0,25)],font=fontStyle,padx=5,pady=5,relief="solid",bd=1,bg="#FFFFFF",fg="black")
            btn.grid(row=row_index, column=col_index, sticky=N+S+E+W)

#                               ///P A L A B R A S\\\
    # recordar empujar palabras al centro de la cuadricula con letras sin sentido.
    # Ej: Palabra(padre,eje,point,p = "")
    # Palabra(marco1,x,0,p = "ABCFRUTAS")
    Palabra(marco1,"x",0,color="#FFFFFF",Fcolor="black",p = "CASA")
    Palabra(marco1,"y",7,color="#FFFFFF",Fcolor="black",p = "HELADO")
    Palabra(marco1,"x",9,color="#FFFFFF",Fcolor="black",p = "FRUTAS")

    
#                               ///P A L A B R A S\\\

desafio2 = Button(nav,text="Desafio 2",padx=2,pady=2,font=20,command=Sopa1).pack(pady=8,fill="x")

Button(nav,text="ZOOM - ",padx=2,pady=2,command=ZoomOut).pack(side="bottom",pady=8,fill="x")
Button(nav,text="ZOOM + ",padx=2,pady=2,command=ZoomIn).pack(side="bottom",pady=8,fill="x")


wind.mainloop()