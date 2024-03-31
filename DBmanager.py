# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 01:43:47 2024

@author: sameg
"""

class Database():
    def __init__(self, file: str):
        self.file = file
        try:
            with open(file, "x") as db:
                db.close()
        except FileExistsError:
            pass
    def add(self, doctorData: str):
        with open(self.file, "a") as db:
            doc = []
            data = doctorData.replace(" ", "").split(",")
            print(data)
            doc.append(data)
            db.write(str(doc))
            db.write("\n")
            db.close()
            
            
    def modify(self, dato: str):
        with open(self.file, "r+") as db:
            
            db.close()
            
            
    def delete(self):
        with open(self.file, "r+") as db:
            db.close()
    def deleteALL(self):
        with open(self.file, "w") as docum:
            docum.writelines("")
            docum.close()
    def save(self):
        with open(self.file, "r") as docum:
            docum.read()
            docum.close()
            
#-------------------------------------------------------------
#READ DATA

def readData(database):
    with open(database.file, "r") as db:
        i = 0
        for lines in db:
            i += 1
            texto = lines.replace("[", "").replace("]", "").replace("'", "").replace("-", " ")
            print(f"#{i} | ", texto, end="")
        db.close()
    return None

def readLine(database, line):
    with open(database.file, "r") as db:
        texto = str(db.readline(line)).replace("[", "").replace("]", "").replace("'", "").replace("-", " ")
        print(texto)
        db.close()
    return None

#------------------------------------------------------------


p = Database("db.txt")


while True:
    comando = str(input("Que deseas hacer: ")).lower()
    if comando == "w":
        while True:
            Exit = str(input("Desea imprimir datos?: ")).lower()
            if Exit == "n":
                break
            elif Exit == "y":
                data = str(input("Ingrese el Nombre, Apellido\nArea y Cubiculo: "))
                p.add(data)
            else:
                print("Notentiendo\n")
    elif comando == "delall":
        p.deleteALL()
        print("\nHecho\n")
    elif comando == "mod":
        readData(p)
        datoMod = str(input("¿Que dato desea modificar?: "))
        p.modify(datoMod)
    elif comando == "del":
        pass
    elif comando == "break" or comando == "b":
        p.save()
        print("\nGuardado\n")
        break

print("LEYENDO DATOS........\n")

readData(p)

