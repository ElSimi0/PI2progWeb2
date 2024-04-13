# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 09:15:12 2024

@author: sameg
"""
import DBmanager as bdd
import interfazConsola as iC
from random import choice
from datetime import datetime
import security

if __name__ == "main":
    pass
else:
    pass

db = bdd.Database("db.txt")
ERROR = "ERROR => Tipo de Error"
edadMaximaDoctores = 75

class Menus():
    
    def Fichas(self):
        bdd.readData(db)
        
    def Citas(self):
        bdd.readData(db)
        while True:
            while True:
                linea = input("Linea de Usuario: ")
                try:
                    linea = int(linea)
                    datos = bdd.readLine(db, linea)
                    break
                except ValueError:
                    print(f"{ERROR}: Solo puedes usar Numeros .-.")
            while True:
                fecha = input("Ingrese fecha de consulta\nEn formato de DD-MM-AAAA: ").replace(" ", "-").replace(".", "-")
                try:
                    day = datetime.strptime(fecha, "%d-%m-%Y")
                    day = str(day)[0:10]
                    break
                except ValueError:
                    print(f"{ERROR}: Fecha Invalida")
            i = 0
            for doctores in datos:
                ky = str(list(dict(datos).keys())).replace("[", "").replace("]", "").replace("'", "")
                doctorList = list()
                isDoc = False
                if ky[0] == "P":
                    isDoc = False
                elif ky[0] == "M":
                    doctorList[i] += ky[0]
                    isDoc = True
                else:
                    isDoc = False
                    
                i+=1
            key = str(list(dict(datos).keys())).replace("[", "").replace("]", "").replace("'", "")
            if isDoc:
                doc = str(choice(doctorList)).replace("[", "").replace("]", "").replace("'", "")
                iC.citas(datos[key][0], datos[key][1], datos[key][2], datos[key][3], datos[key][4], datos[key][5], datos[key][6], datos[key][7], day, datos[doc][0], datos[doc][1])
            else:
                doc = "N/A"
                iC.citas(datos[key][0], datos[key][1], datos[key][2], datos[key][3], datos[key][4], datos[key][5], datos[key][6], datos[key][7], day, doc, doc)    
            break
        
    def Consultas():
        bdd.readData(db)
        while True:
            while True:
                linea = input("Linea de Usuario: ")
                try:
                    linea = int(linea)
                    datos = bdd.readLine(db, linea)
                    break
                except ValueError:
                    print(f"{ERROR}: Solo puedes usar Numeros .-.")
            while True:
                fecha = input("Ingrese fecha de consulta\nEn formato de DD-MM-AAAA: ").replace(" ", "-").replace(".", "-")
                try:
                    day = datetime.strptime(fecha, "%d-%m-%Y")
                    day = str(day)[0:10]
                    break
                except ValueError:
                    print(f"{ERROR}: Fecha Invalida")
            i = 0
            for doctores in datos:
                ky = str(list(dict(datos).keys())).replace("[", "").replace("]", "").replace("'", "")
                doctorList = list()
                isDoc = False
                if ky[0] == "P":
                    isDoc = False
                elif ky[0] == "M":
                    doctorList[i] += ky[0]
                    isDoc = True
                else:
                    isDoc = False
                    
                i+=1
            key = str(list(dict(datos).keys())).replace("[", "").replace("]", "").replace("'", "")
            if isDoc:
                doc = str(choice(doctorList)).replace("[", "").replace("]", "").replace("'", "")
                iC.citas(datos[key][0], datos[key][1], datos[key][2], datos[key][3], datos[key][4], datos[key][5], datos[key][6], datos[key][7], day, datos[doc][0], datos[doc][1])
            else:
                doc = "N/A"
                iC.citas(datos[key][0], datos[key][1], datos[key][2], datos[key][3], datos[key][4], datos[key][5], datos[key][6], datos[key][7], day, doc, doc)    
            break
    
    def Nuevo_doctor(self):
        print("\nPOR FAVOR, EN VEZ DE USAR ESPACIOS USE GUIONES (-)\n")
        
        while True:
            tipoUsuario = "usuario"
            nombre = input("nombre: ")
            apellido = input("apellido: ")
            
            while True:
                edad = input("edad: ")
                try:
                    int(edad)
                    if int(edad) < 0 or int(edad) > 135:
                        print("error en edad")
                        print(f"{ERROR}: Edad Invalida")
                    else:
                        break
                except ValueError:
                    print(f"{ERROR}: Solo puedes usar numeros ._.")
            while True:
                print("GRUPOS SANGUINEOS:\nO+    A+    B+    AB+\nO-    A-    B-    AB-\n")
                tipoSangre = input("Grupo Sanguineo: ").replace(" ", "")
                if tipoSangre.upper() != "A+" and tipoSangre.upper() != "A-" and tipoSangre.upper() != "B+" and tipoSangre.upper() != "B-" and tipoSangre.upper() != "AB+" and tipoSangre.upper() != "AB-" and tipoSangre.upper() != "O+" and tipoSangre.upper() != "O-":
                    print(f"{ERROR}: Grupo Sanguineo inexistente: \n{tipoSangre.upper()} <- ¿y esto que?")
                else:
                    break
            while True:
                historial = input("historial Medico: ")
                if len(historial) > 200:
                    print(f"{ERROR}: Maximo de caracteres superado ->\n    {len(historial)} caracteres de 200")
                else:
                    break
            while True:
                examenes = input("Tiene examenes? (true/false): ").lower()
                if examenes == "true" or examenes == "si":
                    examenes = True
                    ex = input("Examenes: ").replace(" ", "-").split(",")
                    examen = dict()
                    for i in ex:
                        print(f"{i}: ")
                        print("  *  FORMATO:   $datos  o  #")
                        examen[i] = input("  *  Resultado/Estado: ")
                    break
                elif examenes == "false" or examenes == "no":
                    examenes = False
                    examen = dict()
                    break
                else:
                    print(f"{ERROR}: Solo se aceptan booleanos (true/false)")
            clinica = input("Clinica: ")
            db.add(nombre, apellido, edad, historial, examenes, examen, clinica, tipoUsuario) 
            break
        
    def Nuevo_paciente(self):
        print("\nPOR FAVOR, EN VEZ DE USAR ESPACIOS USE GUIONES (-)\n")
        
        while True:
            tipoUsuario = "usuario"
            nombre = input("nombre: ")
            apellido = input("apellido: ")
            
            while True:
                edad = input("edad: ")
                try:
                    int(edad)
                    if int(edad) < 0 or int(edad) > 135:
                        print("error en edad")
                        print(f"{ERROR}: Edad Invalida")
                    else:
                        break
                except ValueError:
                    print(f"{ERROR}: Solo puedes usar numeros ._.")
            while True:
                print("GRUPOS SANGUINEOS:\nO+    A+    B+    AB+\nO-    A-    B-    AB-\n")
                tipoSangre = input("Grupo Sanguineo: ").replace(" ", "")
                if tipoSangre.upper() != "A+" and tipoSangre.upper() != "A-" and tipoSangre.upper() != "B+" and tipoSangre.upper() != "B-" and tipoSangre.upper() != "AB+" and tipoSangre.upper() != "AB-" and tipoSangre.upper() != "O+" and tipoSangre.upper() != "O-":
                    print(f"{ERROR}: Grupo Sanguineo inexistente: \n{tipoSangre.upper()} <- ¿y esto que?")
                else:
                    break
            while True:
                historial = input("historial Medico: ")
                if len(historial) > 200:
                    print(f"{ERROR}: Maximo de caracteres superado ->\n    {len(historial)} caracteres de 200")
                else:
                    break
            while True:
                examenes = input("Tiene examenes? (true/false): ").lower()
                if examenes == "true" or examenes == "si":
                    examenes = True
                    ex = input("Examenes: ").replace(" ", "-").split(",")
                    examen = dict()
                    for i in ex:
                        print(f"{i}: ")
                        print("  *  FORMATO:   $datos  o  #")
                        examen[i] = input("  *  Resultado/Estado: ")
                    break
                elif examenes == "false" or examenes == "no":
                    examenes = False
                    examen = dict()
                    break
                else:
                    print(f"{ERROR}: Solo se aceptan booleanos (true/false)")
            clinica = input("Clinica: ")
            db.add(nombre, apellido, edad, historial, examenes, examen, clinica, tipoUsuario) 
            break
    def Modificar(self):
        while True:
            while True:
                print("BASE DE DATOS: \n")
                if bdd.readData(db) == "":
                    print(f"{ERROR}: Base de Datos Vacia")
                    return
                print("\n\ningrese 'c' o 'cancel' para cancelar\n")
                line = input("¿Que linea desea modificar? : ").lower()
                try:
                    line = int(line)
                    break
                except:
                    if line == "c" or line == "cancel" or line == "cancelar":
                        break
                    else:
                        print(f"{ERROR}: Solo se pueden usar datos int")
            
            tipoUsuario = "usuario"
            nombre = input("nombre: ")
            apellido = input("apellido: ")
            
            while True:
                edad = input("edad: ")
                try:
                    int(edad)
                    if int(edad) < 0 or int(edad) > 135:
                        print("error en edad")
                        print(f"{ERROR}: Edad Invalida")
                    else:
                        break
                except ValueError:
                    print(f"{ERROR}: Solo puedes usar numeros ._.")
            while True:
                print("GRUPOS SANGUINEOS:\nO+    A+    B+    AB+\nO-    A-    B-    AB-\n")
                tipoSangre = input("Grupo Sanguineo: ").replace(" ", "")
                if tipoSangre.upper() != "A+" and tipoSangre.upper() != "A-" and tipoSangre.upper() != "B+" and tipoSangre.upper() != "B-" and tipoSangre.upper() != "AB+" and tipoSangre.upper() != "AB-" and tipoSangre.upper() != "O+" and tipoSangre.upper() != "O-":
                    print(f"{ERROR}: Grupo Sanguineo inexistente: \n{tipoSangre.upper()} <- ¿y esto que?")
                else:
                    break
            while True:
                historial = input("historial Medico: ")
                if len(historial) > 200:
                    print(f"{ERROR}: Maximo de caracteres superado ->\n    {len(historial)} caracteres de 200")
                else:
                    break
            while True:
                examenes = input("Tiene examenes? (true/false): ").lower()
                if examenes == "true" or examenes == "si":
                    examenes = True
                    ex = input("Examenes: ").replace(" ", "-").split(",")
                    examen = dict()
                    for i in ex:
                        print(f"{i}: ")
                        print("  *  FORMATO:   $datos  o  #")
                        examen[i] = input("  *  Resultado/Estado: ")
                    break
                elif examenes == "false" or examenes == "no":
                    examenes = False
                    examen = dict()
                    break
                else:
                    print(f"{ERROR}: Solo se aceptan booleanos (true/false)")
            clinica = input("Clinica: ")
            
            db.modify(line, nombre, apellido, edad, historial, examenes, examen, clinica, tipoUsuario)
            break
            
        
    def LimpiarLinea(self):
        while True:
            if bdd.readData(db) == "":
                print(f"{ERROR}: Base de Datos Vacia")
                return
            bdd.readData(db)
            print("\n\ningrese 'c' o 'cancel' para cancelar\n")
            line = input("¿Que linea desea eliminar? : ").lower()
            try:
                line = int(line)
                db.delete(line)
                break
            except:
                if line == "c" or line == "cancel" or line == "cancelar":
                    break
        
    def Salir(self):
        db.save()
    def Limpiar(self):
        ps = security.e()
        d = security.chk(ps)
        if d == True:
            db.deleteALL()
            print("Hecho\n")

menu = Menus()




