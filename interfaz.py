# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 17:37:36 2024

@author: sameg
"""

import customtkinter
import tkinter

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green


root = customtkinter.CTk()  # create CTk window like you do with the Tk window

root.geometry("1080x540")
root.title("M.D.B —Empty")
root.iconbitmap(r"C:\Users\sameg\Documents\1Prepa\SEMESTRE4\ProgramacionWeb\ActInt2\MDBlogo.ico")
root.resizable(False, False)

def radiobutton_event():
    print("radiobutton toggled, current value:", radio_var.get())

radio_var = tkinter.IntVar(value=0)
radiobutton_1 = customtkinter.CTkRadioButton(root, text="CTkRadioButton 1",
                                             command=radiobutton_event, variable= radio_var, value=1)
radiobutton_1.grid(row=1, column=1, padx=20, pady=20)
radiobutton_2 = customtkinter.CTkRadioButton(root, text="CTkRadioButton 2",
                                             command=radiobutton_event, variable= radio_var, value=2)
radiobutton_2.grid(row=2, column=2, padx=20, pady=20)

root.mainloop()

