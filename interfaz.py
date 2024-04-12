# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 17:51:21 2024

@author: sameg
"""

import customtkinter



customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green


root = customtkinter.CTk()  # create CTk window like you do with the Tk window

root.geometry("720x360")
root.title("M.D.B —Empty")
root.iconbitmap(r"C:\Users\sameg\Documents\1Prepa\SEMESTRE4\ProgramacionWeb\ActInt2\MDBlogo.ico")
root.resizable(False, False)

mode="dark"

def button_function(data="Bueenass"):
    my_label.configure(text=data)

# ☀︎ ☾ ◯
appearance_mode = {"dark": "☾", "light": "☀︎"}

def changeColor():
    global mode
    global appearance_mode
    if mode == "dark":
        customtkinter.set_appearance_mode("light")
        root.iconbitmap(r"C:\Users\sameg\Documents\1Prepa\SEMESTRE4\ProgramacionWeb\ActInt2\MDBlogoB.ico")
        mode = "light"
    else:
        customtkinter.set_appearance_mode("dark")
        root.iconbitmap(r"C:\Users\sameg\Documents\1Prepa\SEMESTRE4\ProgramacionWeb\ActInt2\MDBlogo.ico")
        mode = "dark"
    button_text.set(appearance_mode[mode])

def change_appearance_mode_event(new_appearance: str):
    customtkinter.set_appearance_mode(new_appearance.lower())
    

# Use CTkButton instead of tkinter Button                                                      for light, for dark
button = customtkinter.CTkButton(master=root, text="CTkButton", command=button_function, fg_color=("red", "blue"))
button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

button_text = customtkinter.StringVar(root, appearance_mode[mode])
buttonColorTheme = customtkinter.CTkButton(master=root, textvariable=button_text, command=changeColor)
buttonColorTheme.place(relx=0.1, rely=0.1, anchor=customtkinter.CENTER)


appearance_mode_label = customtkinter.CTkLabel(root, text="Tema: ", anchor="w")
appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
appearance_mode_optionemenu = customtkinter.CTkOptionMenu(root, values=["light", "dark"],
                                                                       command=change_appearance_mode_event)
appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))


my_label = customtkinter.CTkLabel(master=root, text="")
my_label.grid(row=3, column= 2, padx=30, pady=(10, 10))

root.mainloop()

