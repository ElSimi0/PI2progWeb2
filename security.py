# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 02:50:55 2024

@author: sameg
"""
import random
import os

def genP():
    alphaNum = "abcdefghijklmnopqrstuvwxyz" + "0123456789"
    longitud = 25
    password = ''.join(random.choices(alphaNum, k=longitud))
    return password

def storP(password):
    directory = os.path.join(os.getcwd(), "password")
    os.makedirs(directory, exist_ok=True)
    with open(fr"{os.getcwd()}\password\{password}.data", "w") as file:
        file.write(password)
def e():
    pwrd = genP()
    storP(pwrd)
    return pwrd
def installDependences():
    os.system("pip install")
def chk(ps):
    re = b'50415353574f5244'.decode('utf-8')
    t = bytes.fromhex(re).decode('utf-8')
    p = input(f"{t:^1}: ")
    os.remove(fr"password\{ps}.data")
    a = p
    binArguments = str(a)
    r = str(binArguments)
    if ps == r:
        return True
        
        

def ID(tipoUsuario: str, data: str):
    if tipoUsuario.lower() == "paciente" or tipoUsuario.lower() == "usuario":
        user = "PC"
    else:
        user = "MD"
    oldID = str(format(id(data)))
    ID = f"{user}{oldID}"
    return ID
