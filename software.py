from tkinter import *
import tkinter as tk
from tkinter import font
from tkinter import PhotoImage
from typing import List
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import filedialog
import os

raiz = Tk()
raiz.geometry("600x600")
raiz.title("NOVA")
font = ("Arial Bold", 20)
img1 = PhotoImage(file=r"./imagen/foto3.png")
imagen1 = img1.subsample(2)
etiquetaa = Label(raiz, bg="#fd7e36", width=500, height=500).place(x=0, y=0)
etiqueta = Label(raiz, image=imagen1).place(x=100, y=30)
img4 = PhotoImage(file=r"./imagen/remera.png")
img2 = PhotoImage(file=r"./imagen/taza.png")
img3 = PhotoImage(file=r"./imagen/gorra.png")

imagen4 = img4.subsample(7)
imagen2 = img2.subsample(7)
imagen3 = img3.subsample(5)


def tienda():
    ventan3 = Toplevel()
    ventan3.geometry("600x600")
    ventan3.title("NOVA")
    etiquetaa = Label(ventan3, bg="#fd7e36", width=500, height=500).place(x=0, y=0)

    etiqueta = Label(ventan3, image=imagen4, width=150, height=150).place(x=30, y=30)
    etiqueta = Label(ventan3, image=imagen2, width=150, height=150).place(x=220, y=30)
    etiqueta = Label(ventan3, image=imagen3, width=150, height=150).place(x=410, y=30)

    boton1 = Button(ventan3, text="Comprar", width=11, height=2).place(x=60, y=210)
    boton1 = Button(ventan3, text="Comprar", width=11, height=2).place(x=260, y=210)
    boton1 = Button(ventan3, text="Comprar", width=11, height=2).place(x=440, y=210)

    def cierre():
        ventan3.destroy()
    tk.Button(ventan3, text="Salir", width=10, height=2, command=cierre).pack(side=BOTTOM)

def sublimado():
    def openfn():
        filename = filedialog.askopenfilename(title='open')
        return filename
    def open_img():
        x = openfn()
        img = Image.open(x)
        img = img.resize((250, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = Label(ventan2, image=img)
        panel.image = img
        panel.pack()
    ventan2 = Toplevel()
    ventan2.geometry("500x350")
    ventan2.title("NOVA")
    font = ("Arial Bold", 20)
    etiquetaa = Label(ventan2, bg="#fd7e36", width=500, height=500).place(x=0, y=0)
    btn = Button(ventan2, text='seleccione la imagen',command=open_img).pack()
    boton22 =Button(ventan2, text="Enviar", width=10, height=2).pack(side=BOTTOM)

boton1 = Button(raiz, text="Producto", width=11, height=2, command=tienda).place(x=184, y=430)
boton2 = Button(raiz, text="Sublimado", width=11, height=2,command=sublimado).place(x=324, y=430)

def cierre():
    raiz.destroy()
tk.Button(raiz, text="Salir", width=10, height=2, command=cierre).pack(side=BOTTOM)
raiz.mainloop()