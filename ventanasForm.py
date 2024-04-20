# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 01:33:11 2024

@author: sameg
"""

import customtkinter as ctk
import os

class Ventanas(ctk.CTkTabview):
    def __init__(self, master):
        super().__init__(master)
        self.add("Nuevo Doctor")
        self.add("Nuevo Paciente")

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
            self.openError("Numero Invalido: Use Numeros")
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
            newDoc = Doctor(self.name, self.forename, self.number, self.mail, 
                  self.age, self.areaDoc, self.hospitalCenter, self.turn,
                  self.blood, self.medicH)
            try:
                with open(fr"{os.getcwd()}\db.txt", "a") as db:
                    db.write(str(newDoc) + "\n")
                    db.close()
                    
            except FileNotFoundError:
                print("no existe")
                with open(fr"{os.getcwd()}\db.txt", "w") as db:
                    db.write(str(newDoc) + "\n")
                    db.close()
            succes = ctk.CTkToplevel(self)        
            succes.geometry("200x100")
            succes.configure(fg_color="#FFFFFF")
            succes.title("SUCCES")
            succes.resizable(False, False)
            succesLabel = ctk.CTkLabel(succes, text="DOCTOR\nAÑADIDO")
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
                    db.close()
                    
            except FileNotFoundError:
                print("no existe")
                with open(fr"{os.getcwd()}\db.txt", "w") as db:
                    db.write(str(newPa) + "\n")
                    db.close()
            succes = ctk.CTkToplevel(self)        
            succes.geometry("200x100")
            succes.configure(fg_color="#FFFFFF")
            succes.title("SUCCES")
            succes.resizable(False, False)
            succesLabel = ctk.CTkLabel(succes, text="DOCTOR\nAÑADIDO")
            succesLabel.grid(row=0, column=0, padx=20, pady=20)
        
        ############ GUARDAR DATOS ############

class ERROR(ctk.CTkToplevel):
    def __init__(self, typeError):
        super().__init__()
        self.geometry("200x100")
        self.configure(fg_color="#FFFFFF")
        self.title("ERROR")
        self.resizable(False, False)
        
        ctk.CTkLabel(self, text=f"ERROR:\n{typeError}",
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
        
        self.idAT = str(format(id(self.nombre + self.apellido + self.edad + self.area)))
        self.ID = f"MC{self.idAT}"
        
    def __str__(self):
        return f"{self.ID}: {self.nombre}, {self.apellido}, {self.numero}, {self.correo}, {self.edad} años, {self.area}, {self.centroMedico}, {self.turno}, {self.grupoSanguineo}, ({self.historialMedico})"
    
class Paciente():
    def __init__(self, nombre, apellido, numero, correo, edad, gs, historial):
        self.nombre = nombre
        self.apellido = apellido
        self.numero = numero
        self.correo = correo
        self.edad = edad
        self.grupoSanguineo = gs
        self.historialMedico = historial
        
        self.idAT = str(format(id(self.nombre + self.apellido + self.edad + self.grupoSanguineo)))
        self.ID = f"PC{self.idAT}"
        
    def __str__(self):
        return f"{self.ID}, {self.nombre}, {self.apellido}, {self.numero}, {self.correo}, {self.edad} años, {self.grupoSanguineo}, ({self.historialMedico})"
        
        
        
        