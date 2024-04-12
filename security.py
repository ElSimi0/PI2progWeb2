# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 02:50:55 2024

@author: sameg
"""
import random
import os

o = fr"{os.getcwd()}\password\ps.txt"
def e():
    alphaNum = "abcdefghijklmnopqrstuvwxyz1234567890!#$%&-_.+*"
    __password = ""
    longitud = 25
    
    try:
        os.mkdir(fr"{os.getcwd()}\password")
        os.system(fr"attrib +h {os.getcwd()}\password")
        with open(fr"{os.getcwd()}\password\ps.txt", "x") as e:
            for digitos in range(longitud):
                __password += str(random.sample(alphaNum, 1)).replace("[", "").replace("]", "").replace("'", "")
            e.write(__password)
            __password = ""
            e.close()
    except FileExistsError:
        with open(fr"{os.getcwd()}\password\ps.txt", "w") as e:
            for digitos in range(longitud):
                __password += str(random.sample(alphaNum, 1)).replace("[", "").replace("]", "").replace("'", "")
            e.write(__password)
            __password = ""
            e.close()

def installDependences():
    os.system("pip install")

def ID(tipoUsuario: str, data: str):
    if tipoUsuario.lower() == "paciente":
        user = "PC"
    else:
        user = "MD"
    oldID = str(format(id(data)))
    ID = f"{user}{oldID}"
    return ID
e()