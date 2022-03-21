from tkinter import *
import tkinter as tk
from tkinter import font
from tkinter import PhotoImage
from typing import List
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import filedialog
import os

ventan3 = Tk()
ventan3.geometry("600x600")
ventan3.title("NOVA")
etiquetaa = Label(ventan3, bg="#fd7e36", width=500, height=500).place(x=0, y=0)

img1 = PhotoImage(file=r"imagen/remera.png")
img2 = PhotoImage(file=r"imagen/taza.png")
img3 = PhotoImage(file=r"imagen/gorra.png")

imagen1 = img1.subsample(7)
imagen2 = img2.subsample(7)
imagen3 = img3.subsample(5)


etiqueta = Label(ventan3, image=imagen1, width=150, height=150).place(x=30, y=30)
etiqueta = Label(ventan3, image=imagen2, width=150, height=150).place(x=220, y=30)
etiqueta = Label(ventan3, image=imagen3, width=150, height=150).place(x=410, y=30)

boton1 = Button(ventan3, text="Comprar", width=11, height=2).place(x=60, y=210)
boton1 = Button(ventan3, text="Comprar", width=11, height=2).place(x=260, y=210)
boton1 = Button(ventan3, text="Comprar", width=11, height=2).place(x=440, y=210)

def cierre():
    ventan3.destroy()
tk.Button(ventan3, text="Salir", width=10, height=2, command=cierre).pack(side=BOTTOM)

ventan3.mainloop()

