# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 19:09:32 2024

@author: sameg
"""
import customtkinter as ctk
import ventanasForm as vF
        

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.geometry("1080x540")
        self.title("M.D.B")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        
        self.form = vF.Ventanas(master=self)
        self.form.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        
        
        


if __name__ == "__main__":
    app = App()
    app.mainloop()
else:
    pass