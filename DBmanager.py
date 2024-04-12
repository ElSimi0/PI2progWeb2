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
        print("Se va a abrir el txt")
        with open(self.file, "a") as db:
            """
            if tipoUsuario != "paciente" and tipoUsuario != "doctor":
                return "error"
            else:
            """
            
            doc = dict()
            data = list(args)
            ID = security.ID(data[-1], args[0:2])
            doc[ID] = data
            db.write(str(doc))
            print(str(doc))
            db.write("\n")
            print("Se pudo!!!!")
            db.close()
    
    def modify(self, line, newData): #modifica un elemento de la base de datos
        with open(self.file, "r+") as db:
            lines = db.readlines() #Lee el archivo, almacena cada linea como un elemento
                                   #de una lista (lines)
            doc = [] #crea una lista vacia
            data = newData.replace(" ", "").split(",") #guarda los nuevos datos como
                                                       #una lista
            print(data)
            doc.append(data) #la agrega a doc
            if line < 0 or line > len(lines):
                print("ERROR")
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
        for lines in db: # => "por cada linea en la base de datos:"
            i += 1 #Le aumento uno a la variable "i"
            #Texto = linea de la base de datos, uso replace() para dejar mas limpio el texto
            texto = lines.replace("[", "").replace("]", "").replace("'", "").replace("-", " ")
            mensaje = f"{texto}"
            if list(texto)[1] == "M":
                texto_coloreado = f"#{i} | \033[1;36m{mensaje}\033[0m"  # Aplicar color al texto
            else:
                texto_coloreado = f"#{i} | \033[1;33m{mensaje}\033[0m"  # Aplicar color al texto
            
            print(texto_coloreado, end="")
        db.close()
    return texto

def readLine(database, line): #Esta funcion le solo una linea de la base de datos
    with open(database.file, "r") as db:
        
        #Para que sea mas funcional, si la linea a modificar == -1, la funcion
        #- readLine() retornara el ultimo dato de la base.
        #si la linea a modificar NO es -1, le resto 1 a "line", ya que esta ultima
        #-se usa para ver los Indices, osea cuenta desde el 0
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
    return 

#------------------------------------------------------------
