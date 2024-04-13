# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 01:43:47 2024

@author: sameg
"""
import security

class Database():
    def __init__(self, file: str):
        self.file = file
        try:
            with open(file, "x") as db:
                db.close()
        except FileExistsError:
            pass
    def add(self, *args):
        with open(self.file, "a") as db:
            doc = dict()
            data = list(args)
            ID = security.ID(data[-1], args[0:2])
            doc[ID] = data
            db.write(str(doc) + "\n")
            db.close()
    
    def modify(self, line, *args): #modifica un elemento de la base de datos
        with open(self.file, "r+") as db:
            lines = db.readlines() #Lee el archivo, almacena cada linea como un elemento
                                   #de una lista (lines)
            doc = dict() #crea una lista vacia
            data = list(args) #guarda los nuevos datos como
                                                       #una lista
            ID = security.ID(data[-1], args[0:2])
            doc[ID] = data
            if line < 0 or line > len(lines):
                print("ERROR => Tipo de Error: Linea fuera de Rango")
            else:
                lines[line - 1] = str(doc) + "\n"
                db.seek(0)
                db.truncate() 
                db.writelines(lines)
            db.close()
            
    def delete(self, line): #Borra solo una linea de la base de datos
        with open(self.file, "r+") as db:
            lines = db.readlines() #Lee el archivo, almacena cada linea como un elemento
                                   #de una lista (lines)
            if line < 0 or line > len(lines): #Comprueba que se ingrese un numero valido
                print("ERROR")
            else:
                lineaBorrada = str(lines[line - 1]).replace("[", "").replace("]", "").replace("'", "").replace("-", " ")
                del lines[line - 1] #Esto borra la linea dada. Se le resta 1 porque
                                    #line porque se va a leer como lista (desde 0)
                db.seek(0) #Se regresa al inicio del archivo
                db.truncate() #Elimina TODO
                print(f"Linea borrada: {line} |  {lineaBorrada}") #Imprime en consola la db (Este print podria molestar
                             #-en bases de datos largas)
                db.writelines(lines) # vuelve a escribir la db
            db.close()
            
    def deleteALL(self): # Borra toda la base de datos
        with open(self.file, "w") as docum:
            docum.writelines("")
            docum.close()
            
            
    def save(self): #Salva el archivo, es solo una funcion de control
        with open(self.file, "r") as docum:
            docum.read()
            docum.close()
            
#-------------------------------------------------------------
#READ DATA

def readData(database): #Esta funcion lee toda la base de datos
    with open(database.file, "r") as db:
        i = 0 #"i" es un contador, asi puedo enumerar cada linea de la base de datos
        texto = ""
        for lines in db: # => "por cada linea en la base de datos:"
            i += 1 #Le aumento uno a la variable "i"
            #Texto = linea de la base de datos, uso replace() para dejar mas limpio el texto
            texto = lines.replace("[", "").replace("]", "").replace("'", "").replace("-", " ")
            linea = f"{texto}"
            texto_color = ""
            if list(texto)[1] == "M":
                texto_color = f"#{i} | \033[1;36m{linea}\033[0m"  # Aplicar color al texto
            else:
                texto_color = f"#{i} | \033[1;33m{linea}\033[0m"  # Aplicar color al texto
            
            print(texto_color, end="")


def readLine(database, line=0):
    texto = ""
    with open(database.file, "r") as file:
        lines = file.readlines()
        if line < 0 or line > len(lines):
            print("ERROR")
        else:
            texto = eval(lines[line-1])
        print(texto)
        return texto
    
    
    """
    if ID == "":
        
        if line == -1:
            pass
        else:
            line -= 1
        try:
            lineRead = str(db.readlines()[line]).replace("]", "").replace("[", "").replace("'", "").replace("-", " ").replace("{", "").replace("}", "")
        except IndexError:
            lineRead = None
        print(lineRead)
        db.close()
    else:
        pass
    """

#------------------------------------------------------------
