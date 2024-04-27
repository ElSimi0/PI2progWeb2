# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 01:33:11 2024

@author: sameg
"""

import customtkinter as ctk
from tkinter import ttk
import tkinter as tk
import os
import pyperclip as ppclp

class Ventanas(ctk.CTkTabview):
    def __init__(self, master):
        super().__init__(master)
        self.add("Usuarios")
        self.add("Nuevo Doctor")
        self.add("Nuevo Paciente")
        
        
        
        self.frameUsuarios = ctk.CTkFrame(self.tab("Usuarios"),
                                              border_width = 4,
                                              border_color = "#FCFF4D")
        self.frameUsuarios.grid(row=0, column=0, padx=20, pady=20)
        
        self.TreeviewUsers = ttk.Treeview(self.frameUsuarios)
        self.TreeviewUsers["columns"] = ("ID", "Nombre", "Apellido")
        
        self.TreeviewUsers.column("#0", width=50)
        self.TreeviewUsers.column("ID", width=120)
        self.TreeviewUsers.column("Nombre", width=200)
        self.TreeviewUsers.column("Apellido", width=200)
        
        self.TreeviewUsers.heading("#0", text="USR")
        self.TreeviewUsers.heading("ID", text="ID")
        self.TreeviewUsers.heading("Nombre", text="Nombre")
        self.TreeviewUsers.heading("Apellido", text="Apellido")
        
        self.TreeviewUsers.grid(row=0, column=0, padx=20, pady=20)
        
        self.scrollbar = ttk.Scrollbar(self.frameUsuarios, orient="vertical", command=self.TreeviewUsers.yview)
        self.scrollbar.grid(row=0, column=1, padx=20, pady=20, sticky="ns")
        
#python C:\Users\sameg\Documents\1Prepa\SEMESTRE4\ProgramacionWeb\AI2\int.py
        
        self.TreeviewUsers.configure(yscrollcommand=self.scrollbar.set)
        
        style = ttk.Style()
        #style.theme_use("default")  # Usar el tema por defecto de ttk

        # Configurar el estilo de la Scrollbar
        style.configure("Vertical.TScrollbar",
                background="#303030",
                darkcolor="#303030",
                lightcolor="#303030",
                troughcolor="#303030")

        # Aplicar el estilo a la Scrollbar
        self.scrollbar.configure(style="Vertical.TScrollbar")
        
        style.configure("Treeview",
                background="#333333",
                foreground="#FFFFFF",
                fieldbackground="#FF993F")
        style.map("Treeview",
                  background = [("selected", "#85B0B9")])
        self.TreeviewUsers.configure(style="Treeview")
        
        self.TreeviewUsers.bind("<Button-3>", self.menuClickD)
        
        self.borrarBase = ctk.CTkButton(self.tab("Usuarios"), text="Limpiar Base de Datos", 
                                    command=self.delete)
        self.borrarBase.grid(row=1, column=0, padx=20, pady=20)
        
        

        
        try:
            with open("db.txt", "r") as db:
                i = 0
                text = ""
                for lines in db:
                    text = lines.split(",", maxsplit=3)
                    userID = text[0]
                    if str(userID)[0:2] == "PC" or str(userID)[0:2] == "MC": 
                        userName = text[1]
                        userForename = text[2]
                        self.TreeviewUsers.insert(parent="", index="end", text=str(userID)[0:2],
                                                  iid=i, values=(userID, userName, userForename))
                    i += 1
        except:
            with open("db.txt", "a+") as db:
                i = 0
                text = ""
                for lines in db:
                    text = lines.split(",", maxsplit=3)
                    userID = text[0]
                    if str(userID)[0:2] == "PC" or str(userID)[0:2] == "MC": 
                        userName = text[1]
                        userForename = text[2]
                        self.TreeviewUsers.insert(parent="", index="end", text=str(userID)[0:2],
                                                  iid=i, values=(userID, userName, userForename))
                    i += 1
                    
        
                    
        
        
        # NUEVO DOCTOR
        #   INFO PERSONAL ########################################################
        
        self.frameInfoPersonal = ctk.CTkFrame(self.tab("Nuevo Doctor"), 
                                              border_width = 4,
                                              border_color = "#FCFF4D")
        self.frameInfoPersonal.grid(row=0, column=0, padx=20, pady=20)
        
        self.titulo1 = ctk.CTkLabel(self.frameInfoPersonal,text="Información Personal")
        self.titulo1.grid(row=0, column=0, padx=20, pady=10, columnspan=2)
        
        
        ctk.CTkLabel(self.frameInfoPersonal,text="Nombre(s)").grid(row=1, column=0, padx=10, pady=10)
        
        self.nombre = ctk.CTkEntry(self.frameInfoPersonal, placeholder_text="Nombre(s)")
        self.nombre.grid(row=2, column=0, padx=20, pady=10)
        
        ctk.CTkLabel(self.frameInfoPersonal,text="Apellidos").grid(row=1, column=1, padx=10, pady=10)
        
        self.apellidos = ctk.CTkEntry(self.frameInfoPersonal, placeholder_text="Apellidos")
        self.apellidos.grid(row=2, column=1, padx=20, pady=10)
        
        ctk.CTkLabel(self.frameInfoPersonal,text="Numero de Telefono").grid(row=3, column=0, padx=10, pady=10)
        
        self.numero = ctk.CTkEntry(self.frameInfoPersonal, placeholder_text="+52")
        self.numero.grid(row=4, column=0, padx=20, pady=10)
        
        ctk.CTkLabel(self.frameInfoPersonal,text="Correo").grid(row=3, column=1, padx=10, pady=10)
        
        self.correo = ctk.CTkEntry(self.frameInfoPersonal, placeholder_text="Correo")
        self.correo.grid(row=4, column=1, padx=20, pady=10)
        
        ctk.CTkLabel(self.frameInfoPersonal,text="Edad").grid(row=5, column=0, padx=10, pady=10)
        
        self.edad = ctk.CTkEntry(self.frameInfoPersonal, placeholder_text="Edad")
        self.edad.grid(row=6, column=0, padx=20, pady=10)
        
        #   INFO PROFESIONAL #####################################################
        
        self.frameInfoProfesional = ctk.CTkFrame(self.tab("Nuevo Doctor"), 
                                              border_width = 4,
                                              border_color = "#20E488")
        self.frameInfoProfesional.grid(row=0, column=1, padx=20, pady=20)
        
        self.titulo2 = ctk.CTkLabel(self.frameInfoProfesional, text="Información Profesional")
        self.titulo2.grid(row=0, column=0, padx=20, pady=10, columnspan=2)
        
        
        ctk.CTkLabel(self.frameInfoProfesional,text="Area").grid(row=1, column=0, padx=10, pady=10)
        
        #self.area = ctk.CTkEntry(self.frameInfoProfesional, placeholder_text="Area")
        self.area = ctk.CTkComboBox(self.frameInfoProfesional, 
                                    values=["Seleccione Area", "Anestesiología","UCI","Hematología","Nefrología","Oncología",
                                            "Neumología","Rehabilitación","Cardiología","Pediatría","Medicina interna",
                                            "Cirugía General","Dermatología","Ortopédica/traumatología","Oftalmología","Obstetricia/Ginecología",
                                            "Urología","Otorrinolaringología","Laboratorios clínicos","Farmacia","Radiodiagnóstico",
                                            "Medicina preventiva","Urgencias"],
                                    state="readonly")
        self.area.grid(row=2, column=0, padx=20, pady=10)
        self.area.set("Seleccione Area")
        
        ctk.CTkLabel(self.frameInfoProfesional,text="Centro Hospitalario").grid(row=3, column=0, padx=10, pady=10)
        
        self.centro = ctk.CTkEntry(self.frameInfoProfesional, placeholder_text="Hospital")
        self.centro.grid(row=4, column=0, padx=20, pady=10)
        
        ctk.CTkLabel(self.frameInfoProfesional,text="Turno").grid(row=5, column=0, padx=10, pady=10)
        
        self.turno = ctk.CTkComboBox(self.frameInfoProfesional, 
                                     values=["Seleccione Turno","Matutino","Vespertino","Nocturno"],
                                     state="readonly")
        self.turno.grid(row=6, column=0, padx=20, pady=10)
        self.turno.set("Seleccione Turno")
        
        #   INFO MEDICA #####################################################
        
        self.frameInfoMedica = ctk.CTkFrame(self.tab("Nuevo Doctor"), 
                                              border_width = 4,
                                              border_color = "#9D20E4")
        self.frameInfoMedica.grid(row=0, column=2, padx=20, pady=20)
        
        self.titulo2 = ctk.CTkLabel(self.frameInfoMedica, text="Información Medica")
        self.titulo2.grid(row=0, column=0, padx=20, pady=10, columnspan=2)
        
        
        ctk.CTkLabel(self.frameInfoMedica,text="Grupo Sanguineo").grid(row=1, column=0, padx=10, pady=10)
        
        self.gSangre = ctk.CTkComboBox(self.frameInfoMedica, 
                                       values=["Seleccione GS", "O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"],
                                       state="readonly")
        self.gSangre.grid(row=2, column=0, padx=20, pady=10)
        self.gSangre.set("Seleccione GS")
        
        ctk.CTkLabel(self.frameInfoMedica,text="Historial Medico").grid(row=3, column=0, padx=10, pady=10)
        
        self.historialMedico = ctk.CTkTextbox(self.frameInfoMedica, width=200, height=125)
        self.historialMedico.grid(row=4, column=0, padx=20, pady=10, sticky="nsew")
        
        # BOTON
        
        self.SubirNuDoc = ctk.CTkButton(self.tab("Nuevo Doctor"), text="Enviar",
                                        border_width = 4,
                                        fg_color="transparent",
                                        border_color = "#23A789", #138E58
                                        hover_color = "#0F9778",
                                        command=self.submitDoc)
        self.SubirNuDoc.grid(row=1, column=0, padx=20, pady=10, columnspan = 3)
        
        
        #----------------------------------------------------------------------
        
        ############################## NEW PATIENT ############################
        
        #----------------------------------------------------------------------
        
        
        # NUEVO PACIENTE
        #   INFO PERSONAL ########################################################
        
        self.frameInfoPersonalP = ctk.CTkFrame(self.tab("Nuevo Paciente"), 
                                              border_width = 4,
                                              border_color = "#FCFF4D")
        self.frameInfoPersonalP.grid(row=0, column=0, padx=20, pady=20)
        
        self.titulo1P = ctk.CTkLabel(self.frameInfoPersonalP,text="Información Personal")
        self.titulo1P.grid(row=0, column=0, padx=20, pady=10, columnspan=2)
        
        
        ctk.CTkLabel(self.frameInfoPersonalP,text="Nombre(s)").grid(row=1, column=0, padx=10, pady=10)
        
        self.nombreP = ctk.CTkEntry(self.frameInfoPersonalP, placeholder_text="Nombre(s)")
        self.nombreP.grid(row=2, column=0, padx=20, pady=10)
        
        ctk.CTkLabel(self.frameInfoPersonalP,text="Apellidos").grid(row=1, column=1, padx=10, pady=10)
        
        self.apellidosP = ctk.CTkEntry(self.frameInfoPersonalP, placeholder_text="Apellidos")
        self.apellidosP.grid(row=2, column=1, padx=20, pady=10)
        
        ctk.CTkLabel(self.frameInfoPersonalP,text="Numero de Telefono").grid(row=3, column=0, padx=10, pady=10)
        
        self.numeroP = ctk.CTkEntry(self.frameInfoPersonalP, placeholder_text="+52")
        self.numeroP.grid(row=4, column=0, padx=20, pady=10)
        
        ctk.CTkLabel(self.frameInfoPersonalP,text="Correo").grid(row=3, column=1, padx=10, pady=10)
        
        self.correoP = ctk.CTkEntry(self.frameInfoPersonalP, placeholder_text="Correo")
        self.correoP.grid(row=4, column=1, padx=20, pady=10)
        
        ctk.CTkLabel(self.frameInfoPersonalP,text="Edad").grid(row=5, column=0, padx=10, pady=10)
        
        self.edadP = ctk.CTkEntry(self.frameInfoPersonalP, placeholder_text="Edad")
        self.edadP.grid(row=6, column=0, padx=20, pady=10)
        
        #   INFO MEDICA #####################################################
        
        self.frameInfoMedicaP = ctk.CTkFrame(self.tab("Nuevo Paciente"), 
                                              border_width = 4,
                                              border_color = "#9D20E4")
        self.frameInfoMedicaP.grid(row=0, column=2, padx=20, pady=20)
        
        self.titulo2P = ctk.CTkLabel(self.frameInfoMedicaP, text="Información Medica")
        self.titulo2P.grid(row=0, column=0, padx=20, pady=10, columnspan=2)
        
        
        ctk.CTkLabel(self.frameInfoMedicaP,text="Grupo Sanguineo").grid(row=1, column=0, padx=10, pady=10)
        
        self.gSangreP = ctk.CTkComboBox(self.frameInfoMedicaP, 
                                       values=["Seleccione GS", "O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"],
                                       state="readonly")
        self.gSangreP.grid(row=2, column=0, padx=20, pady=10)
        self.gSangreP.set("Seleccione GS")
        
        ctk.CTkLabel(self.frameInfoMedicaP,text="Historial Medico").grid(row=3, column=0, padx=10, pady=10)
        
        self.historialMedicoP = ctk.CTkTextbox(self.frameInfoMedicaP, width=200, height=125)
        self.historialMedicoP.grid(row=4, column=0, padx=20, pady=10, sticky="nsew")
        
        # BOTON
        
        self.SubirNuDocP = ctk.CTkButton(self.tab("Nuevo Paciente"), text="Enviar",
                                        border_width = 4,
                                        fg_color="transparent",
                                        border_color = "#23A789", #138E58
                                        hover_color = "#0F9778",
                                        command=self.submitPa)
        self.SubirNuDocP.grid(row=1, column=0, padx=20, pady=10, columnspan = 3)
        
        self.error = None
    
    def openError(self, typeError):
        if self.error == None or not self.error.winfo_exists():
            self.error = ERROR(typeError)
        else:
            self.error.focus()
    def menuClickD(self, event):
        
        self.item = self.TreeviewUsers.identify('item', event.x, event.y)
        self.selection = self.TreeviewUsers.selection()
        
        
        if self.item:
            self.menuCD = tk.Menu(self.TreeviewUsers, tearoff=0)
            self.menuCD.add_command(label="Copy", command=self.copyID)
            self.menuCD.add_command(label="Nueva Cita", command=self.nuevaCita)
            self.menuCD.add_command(label="Nueva Consulta", command=self.nuevaConsulta)
            self.menuCD.add_separator()
            self.menuCD.add_command(label="Eliminar")
            self.menuCD.post(event.x_root, event.y_root)
            
            self.selection = self.TreeviewUsers.selection()
        
            
        if self.selection:
            self.objeto = self.selection[0]
            # Get the item's options
            self.options = self.TreeviewUsers.item(self.objeto)
    
            # Print the item's text and user data
            self.idTaken = self.options['values'][0]
    
    def nuCita(self):
        with open(fr"{os.getcwd()}\db.txt", "r") as db:
            #print("Sigue el FOR")
            allItems = db.readlines()
        for items in allItems:
            self.itemID = str(items).split(",")[0]
            #print(f"Current ID iterable:{self.itemID}\nItem Selected: {self.idTaken}")
            if self.itemID != self.idTaken:
                pass
            else:
                crearCita = Cita()
                break
    def nuConsulta(self):
        with open(fr"{os.getcwd()}\db.txt", "r") as db:
            #print("Sigue el FOR")
            allItems = db.readlines()
        for items in allItems:
            self.itemID = str(items).split(",")[0]
            #print(f"Current ID iterable:{self.itemID}\nItem Selected: {self.idTaken}")
            if self.itemID != self.idTaken:
                pass
            else:
                crearConsulta = Consultas()
                break
    
    def copyID(self):
        ppclp.copy(self.idTaken)
    def nuevaCita(self):
        self.nuCita()
    def nuevaConsulta(self):
        self.nuConsulta()
        
    def submitDoc(self):
        self.allGood = True
        self.name = str(self.nombre.get()).strip()
        self.forename = str(self.apellidos.get()).strip()
        self.number = str(self.numero.get()).replace(" ", "")
        self.mail = str(self.correo.get()).strip()
        self.age = str(self.edad.get()).replace(" ", "")
        
        self.areaDoc = str(self.area.get())
        self.hospitalCenter = str(self.centro.get()).strip()
        self.turn = str(self.turno.get())
        
        self.blood = str(self.gSangre.get())
        self.medicH = str(self.historialMedico.get("1.0",'end-1c')).strip()
        
        
        if self.name == "":
            self.openError("Nombre Invalido: Nombre Vacio")
            self.allGood = False
        elif len(self.name) >= 60:
            self.openError("Numero de letras en nombre excedida")
            self.allGood = False
            
        if self.forename == "":
            self.openError("Apellido Invalido: Apellido Vacio")
            self.allGood = False
        elif len(self.forename) >= 60:
            self.openError("Numero de letras en apellido excedida")
            self.allGood = False
        try:
            int(self.number)
        except ValueError:
            self.openError("Numero Invalido: Use Numeros\nPD: ¿Eres tonto (°_o)?")
            self.allGood = False
            
        if "@" in self.mail:
            pass
        else:
            self.openError("Email Invalido: Use '@'")
            self.allGood = False
            
        try:
            int(self.age)
            if int(self.age) < 22 or int(self.age) > 80:
                self.openError("Edad Invalida: Edad (22-80)")
                self.allGood = False
        except ValueError:
            self.openError("Edad Invalida: Use Numeros")
            self.allGood = False
            
        #---------
        
        if self.areaDoc == "Seleccione Area":
            self.openError("Seleccione Area")
            self.allGood = False
        if self.hospitalCenter == "":
            self.openError("Hospital Invalido: Hospital vacio")
            self.allGood = False
        if self.turn == "Seleccione Turno":
            self.openError("Seleccione Turno")
            self.allGood = False
        
        #---------
        
        if self.blood == "Seleccione GS":
            self.openError("Seleccione Grupo Sanguineo")
            self.allGood = False
        
        #######################################
        
        if self.allGood:    
            self.newDoc = Doctor(self.name, self.forename, self.number, self.mail, 
                  self.age, self.areaDoc, self.hospitalCenter, self.turn,
                  self.blood, self.medicH)
            try:
                with open(fr"{os.getcwd()}\db.txt", "a") as db:
                    db.write(str(self.newDoc) + "\n")
                    self.text = str(self.newDoc).split(",", maxsplit=3)
                    self.userID = self.text[0]
                    self.userName = self.text[1]
                    self.userForename = self.text[2]
                    self.TreeviewUsers.insert(parent="", index="end", text=str(self.userID)[0:2],
                                              iid=str(self.userID), values=(self.userID, self.userName, 
                                                              self.userForename))
                    db.close()
                    
            except FileNotFoundError:
                print("no existe")
                with open(fr"{os.getcwd()}\db.txt", "w") as db:
                    db.write(str(self.newDoc) + "\n")
                    self.text = str(self.newDoc).split(",", maxsplit=3)
                    self.userID = self.text[0]
                    self.userName = self.text[1]
                    self.userForename = self.text[2]
                    self.TreeviewUsers.insert(parent="", index="end", text=str(self.userID)[0:2],
                                              iid=str(self.userID), values=(self.userID, self.userName, 
                                                              self.userForename))
                    db.close()
            succes = ctk.CTkToplevel(self)        
            succes.geometry("200x100")
            succes.configure(fg_color="#FFFFFF")
            succes.title("SUCCES")
            succes.resizable(False, False)
            succesLabel = ctk.CTkLabel(succes, text="DOCTOR\nAÑADIDO",
                                       text_color="#21041A")
            succesLabel.grid(row=0, column=0, padx=20, pady=20)
            
            
        ############ GUARDAR DATOS ############
        
        
    def submitPa(self):
        self.allGood = True
        self.nameP = str(self.nombreP.get()).strip()
        self.forenameP = str(self.apellidosP.get()).strip()
        self.numberP = str(self.numeroP.get()).replace(" ", "")
        self.mailP = str(self.correoP.get()).strip()
        self.ageP = str(self.edadP.get()).replace(" ", "")
        
        self.bloodP = str(self.gSangreP.get())
        self.medicHP = str(self.historialMedicoP.get("1.0",'end-1c')).strip()
        
        
        if self.nameP == "":
            self.openError("Nombre Invalido: Nombre Vacio")
            self.allGood = False
        elif len(self.nameP) >= 60:
            self.openError("Numero de letras en nombre excedida")
            self.allGood = False
            
        if self.forenameP == "":
            self.openError("Apellido Invalido: Apellido Vacio")
            self.allGood = False
        elif len(self.forenameP) >= 60:
            self.openError("Numero de letras en apellido excedida")
            self.allGood = False
        try:
            int(self.numberP)
        except ValueError:
            self.openError("Numero Invalido: Use Numeros")
            self.allGood = False
            
        if "@" in self.mailP:
            pass
        else:
            self.openError("Email Invalido: Use '@'")
            self.allGood = False
            
        try:
            int(self.ageP)
            if int(self.ageP) < 0 or int(self.ageP) > 130:
                self.openError("Edad Invalida: Edad (0-130)")
                self.allGood = False
        except ValueError:
            self.openError("Edad Invalida: Use Numeros")
            self.allGood = False
        
        #---------
        
        if self.bloodP == "Seleccione GS":
            self.openError("Seleccione Grupo Sanguineo")
            self.allGood = False
            
        
        if self.allGood:    
            newPa = Paciente(self.nameP, self.forenameP, self.numberP, self.mailP, 
                  self.ageP, self.bloodP, self.medicHP)
            try:
                with open(fr"{os.getcwd()}\db.txt", "a") as db:
                    db.write(str(newPa) + "\n")
                    self.text = str(newPa).split(",", maxsplit=3)
                    self.userID = self.text[0]
                    self.userName = self.text[1]
                    self.userForename = self.text[2]
                    self.TreeviewUsers.insert(parent="", index="end", text=str(self.userID)[0:2],
                                              iid=str(self.userID), values=(self.userID, self.userName, 
                                                              self.userForename))
                    db.close()
                    
            except FileNotFoundError:
                print("no existe")
                with open(fr"{os.getcwd()}\db.txt", "w") as db:
                    db.write(str(self.newPa) + "\n")
                    self.text = str(self.newPa).split(",", maxsplit=3)
                    self.userID = self.text[0]
                    self.userName = self.text[1]
                    self.userForename = self.text[2]
                    self.TreeviewUsers.insert(parent="", index="end", text=str(self.userID)[0:2],
                                              iid=str(self.userID), values=(self.userID, self.userName, 
                                                              self.userForename))
                    db.close()
            succes = ctk.CTkToplevel(self)        
            succes.geometry("200x100")
            succes.configure(fg_color="#FFFFFF")
            succes.title("SUCCES")
            succes.resizable(False, False)
            succesLabel = ctk.CTkLabel(succes, text="PACIENTE\nAÑADIDO\n(งò⏠ó)ง",
                                       text_color="#21041A")
            
            succesLabel.grid(row=0, column=0, padx=20, pady=20)
        
    def delete(self):
        self.passwordInput = EliminarDBwindow()
        
class EliminarDBwindow(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.geometry("400x250")
        self.configure(fg_color="#FF5C5C")
        self.title("Limpiar Base de Datos")
        self.resizable(False, False)
        self.attributes('-topmost',1)
        ctk.CTkLabel(self, text="Ingrese la contraseña",
                     text_color="#000000").grid(row=0, column=0, padx=20, pady=20)
        self.password = ctk.CTkEntry(self, show="*",
                                     placeholder_text="CONTRASEÑA")
        self.password.grid(row=1, column=0, padx=20, pady=20)
        
        self.delDBbutton = ctk.CTkButton(self, text="Send", command=self.eliminar)
        self.delDBbutton.grid(row=2, column=0, padx=20, pady=20)
    def eliminar(self):
        if self.password.get() == "password":
            with open(fr"{os.getcwd()}\db.txt", "w") as db:
                db.write("")
                db.close()
            self.destroy()
        else:
            self.destroy()

class ERROR(ctk.CTkToplevel):
    def __init__(self, typeError):
        super().__init__()
        self.geometry("200x100")
        self.configure(fg_color="#FFFFFF")
        self.title("(งツ)ว")
        self.resizable(False, False)
        
        ctk.CTkLabel(self, text=f"ERROR (งツ)ว :\n{typeError}\n  (ง︡'-'︠)ง",
                     text_color="#000000").grid(row=0, column=0, padx=20, pady=20)
        self.focus()
        
        
class Doctor():
    def __init__(self, nombre, apellido, numero, correo, edad, area, centro, turno, gs, historial):
        self.nombre = nombre
        self.apellido = apellido
        self.numero = numero
        self.correo = correo
        self.edad = edad
        self.area = area
        self.centroMedico = centro
        self.turno = turno
        self.grupoSanguineo = gs
        self.historialMedico = historial
        self.citas = ""
        self.consultas = ""
        
        self.idAT = str(format(id(self.nombre + self.apellido + self.edad + self.area)))
        self.ID = f"MC{self.idAT}"
        
    def __str__(self):
        return f"{self.ID}, {self.nombre}, {self.apellido}, {self.numero}, {self.correo}, {self.edad} años, {self.area}, {self.centroMedico}, {self.turno}, {self.grupoSanguineo}, ({self.historialMedico})"
    
class Paciente():
    def __init__(self, nombre, apellido, numero, correo, edad, gs, historial):
        self.nombre = nombre
        self.apellido = apellido
        self.numero = numero
        self.correo = correo
        self.edad = edad
        self.grupoSanguineo = gs
        self.historialMedico = historial
        self.citas = ""
        self.consultas = ""
        
        self.idAT = str(format(id(self.nombre + self.apellido + self.edad + self.grupoSanguineo)))
        self.ID = f"PC{self.idAT}"
        
    def __str__(self):
        return f"{self.ID}, {self.nombre}, {self.apellido}, {self.numero}, {self.correo}, {self.edad} años, {self.grupoSanguineo}, ({self.historialMedico})"
        
class Cita(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.geometry("720x400")
        self.configure(fg_color="#3E554E")
        self.title("Nueva Cita")
        self.resizable(False, False)
        self.focus()
        
        self.idPaciente = ctk.CTkEntry(self, placeholder_text="ID DEL PACIENTE")
        self.idPaciente.grid(row=1, column=0, padx=20, pady=10)
        
        self.idDoctor = ctk.CTkEntry(self, placeholder_text="ID DEL DOCTOR")
        self.idDoctor.grid(row=1, column=1, padx=20, pady=10)
        
        self.problemas = ctk.CTkTextbox(self, width=200, height=125)
        self.problemas.grid(row=2, column=0, padx=20, pady=10, sticky="nsew", columnspan=2)
        
        self.submitIDs = ctk.CTkButton(self, text="Send", command=self.sendIDs)
        self.submitIDs.grid(row=3, column=0, padx=20, pady=10)
    
    def sendIDs(self):
        self.idsRGood = False
        if str(self.idPaciente.get())[0:2] == "PC":
            self.idsRGood = True
        else:
            self.idsRGood = False
        
        if str(self.idDoctor.get())[0:2] == "MC":
            self.idsRGood = True
        else:
            self.idsRGood = False
        
        if self.idsRGood:
            with open(fr"{os.getcwd()}\db.txt", "a") as db:
                db.write(f"CITA, Paciente: {self.idPaciente.get()}, Doctor: {self.idDoctor.get()}, [{self.problemas.get('1.0','end-1c')}]\n")
                db.close()
        self.destroy()

class Consultas(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.geometry("720x400")
        self.configure(fg_color="#3E554E")
        self.title("Nueva Consulta")
        self.resizable(False, False)
        self.focus()
        
        self.idPaciente = ctk.CTkEntry(self, placeholder_text="ID DEL PACIENTE")
        self.idPaciente.grid(row=1, column=0, padx=20, pady=10)
        
        self.idDoctor = ctk.CTkEntry(self, placeholder_text="ID DEL DOCTOR")
        self.idDoctor.grid(row=1, column=1, padx=20, pady=10)
        
        self.problemas = ctk.CTkTextbox(self, width=200, height=125)
        self.problemas.grid(row=2, column=0, padx=20, pady=10, sticky="nsew", columnspan=2)
        
        self.submitIDs = ctk.CTkButton(self, text="Send", command=self.sendIDs)
        self.submitIDs.grid(row=3, column=0, padx=20, pady=10)
    
    def sendIDs(self):
        self.idsRGood = False
        if str(self.idPaciente.get())[0:2] == "PC":
            self.idsRGood = True
        else:
            self.idsRGood = False
        
        if str(self.idDoctor.get())[0:2] == "MC":
            self.idsRGood = True
        else:
            self.idsRGood = False
        
        if self.idsRGood:
            with open(fr"{os.getcwd()}\db.txt", "a") as db:
                db.write(f"CONSULTA, Paciente: {self.idPaciente.get()}, Doctor: {self.idDoctor.get()}, [{self.problemas.get('1.0','end-1c')}]\n")
                db.close()
        self.destroy()

class Fichas(ctk.CTkToplevel):
    def __init__(self):
        self.
        
        