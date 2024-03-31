# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 17:51:21 2024

@author: sameg
"""

import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title("Ventana")
root.geometry("900x600")

def newFunc():
    pass


menu = tk.Menu(root)
root.config(menu=menu)

archivo = tk.Menu(menu)
menu.add_cascade(label="Hola", menu=archivo)

edicion = tk.Menu(menu)
menu.add_cascade(label="edicion", menu=edicion)

edicion.add_command(label="NOSEEEE", command = newFunc)

root.mainloop()


