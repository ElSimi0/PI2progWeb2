# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 01:37:43 2024

@author: sameg
"""
import DBmanager as bdd
import interfazConsola as iC
import security

if __name__ == "main":
    pass
else:
    pass

db = bdd.Database("db.txt")
ERROR = "ERROR"
edadMaximaDoctores = 75

class Menus():
    
    def Fichas(self, ID):
        bdd.readData(db)
        
    def Citas(self, nombre, apellido, edad, tipoSangre, historial, examenes, examen, 
              clinica, modulo, area, cubiculo, fecha):
       
        iC.citas(nombre, apellido, edad, tipoSangre, historial, examenes, examen, 
                 clinica, modulo, area, cubiculo, fecha)
        
    def Consultas():
        pass
    
    def Nuevo_doctor(self):
        print("POR FAVOR, EN VEZ DE USAR ESPACIOS USE GUIONES (-)")
        
        
        while True:
            tipoUsuario = input("Tipo de ingreso (doctor): ")
            if tipoUsuario.lower() != "doctor" or tipoUsuario.lower() != "medico" or tipoUsuario.lower() != "doc":
                print("error en tipoUsuario")
                return ERROR
            nombre = input("nombre: ")
            apellido = input("apellido: ")
            edad = input("edad: ")
            
            try:
                int(edad)
                if int(edad) < 18 or int(edad) > edadMaximaDoctores:
                    print("error en edad")
                    return ERROR
            except ValueError:
                return ERROR
            
            tipoSangre = input("Grupo Sanguineo: ").replace(" ", "")
            if tipoSangre.upper() != "A+" and tipoSangre.upper() != "A-" and tipoSangre.upper() != "B+" and tipoSangre.upper() != "B-" and tipoSangre.upper() != "AB+" and tipoSangre.upper() != "AB-" and tipoSangre.upper() != "O+" and tipoSangre.upper() != "O-":
                print(f"Error en el tipo de sangre: {tipoSangre.upper()}")
                return ERROR
            
            historial = input("historial: ")
            if len(historial) > 200:
                print("se dio un error en historial")
                return ERROR
            
            examenes = input("Tienes examenes? (true/false): ").lower()
            if examenes == "true" or examenes == "si":
                examenes = True
                ex = input("Examenes: ").replace(" ", "-").split(",")
                examen = dict()
                for i in ex:
                    print(f"{i}: ")
                    print("  *  FORMATO:   $datos  o  #")
                    examen[i] = input("  *  Resultado/Estado: ")
            else:
                examenes = False
                examen = dict()
            clinica = input("Clinica: ")
            modulo = input("Modulo: ")
            area = input("Area: ")
            cubiculo = input("Cubiculo: ")
            fecha = input("Fecha (DD-MM-AAAA): ")
            
            print("Dentro de Nuevo doctro, se va a añadir usuarios")
            db.add(nombre, apellido, edad, historial, examenes, examen, clinica, 
               modulo, area, cubiculo, fecha, tipoUsuario) 
            print("\n\n")
            bdd.readLine(db, -1)
            break
        
    def Nuevo_paciente(self):
        print("POR FAVOR, EN VEZ DE USAR ESPACIOS USE GUIONES (-)")
        
        
        while True:
            tipoUsuario = input("Tipo de ingreso (usuario): ")
            if tipoUsuario.lower().replace(" ", "") != "paciente" and tipoUsuario.lower().replace(" ", "") != "usuario":
                return ERROR
            nombre = input("nombre: ")
            apellido = input("apellido: ")
            edad = input("edad: ")
            
            try:
                int(edad)
                if int(edad) < 0 or int(edad) > 135:
                    print("error en edad")
                    return ERROR
            except ValueError:
                return ERROR
            
            tipoSangre = input("Grupo Sanguineo: ").replace(" ", "")
            if tipoSangre.upper() != "A+" and tipoSangre.upper() != "A-" and tipoSangre.upper() != "B+" and tipoSangre.upper() != "B-" and tipoSangre.upper() != "AB+" and tipoSangre.upper() != "AB-" and tipoSangre.upper() != "O+" and tipoSangre.upper() != "O-":
                print(f"Error en el tipo de sangre: {tipoSangre.upper()}")
                return ERROR
            
            historial = input("historial Medico: ")
            if len(historial) > 200:
                print("se dio un error en historial")
                return ERROR
            
            examenes = input("Tiene examenes? (true/false): ").lower()
            if examenes == "true" or examenes == "si":
                examenes = True
                ex = input("Examenes: ").replace(" ", "-").split(",")
                examen = dict()
                for i in ex:
                    print(f"{i}: ")
                    print("  *  FORMATO:   $datos  o  #")
                    examen[i] = input("  *  Resultado/Estado: ")
            else:
                examenes = False
                examen = dict()
            clinica = input("Clinica: ")
            modulo = input("Modulo: ")
            area = input("Area: ")
            cubiculo = input("Cubiculo: ")
            fecha = input("Fecha (DD-MM-AAAA): ")
            
            print("Dentro de Nuevo doctro, se va a añadir usuarios")
            db.add(nombre, apellido, edad, historial, examenes, examen, clinica, 
               modulo, area, cubiculo, fecha, tipoUsuario) 
            print("\n\n")
            bdd.readLine(db, -1)
            break
    def Modificar(self, line, newData):
        db.modify(line, newData)
    def LimpiarLinea(self, line):
        db.delete(line)
    def Salir(self):
        db.save()
    def Limpiar(self):
        re = b'50415353574f5244'.decode('utf-8')
        t = bytes.fromhex(re).decode('utf-8')
        p = input(f"{t:^1}: ")
        a = p
        binArguments = str(a)
        r = str(binArguments)
        with open(security.o, "r") as l:
            i = str(l.read())
            if i == r:
                db.deleteALL()

menu = Menus()




