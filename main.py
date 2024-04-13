# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 01:37:43 2024

@author: sameg
"""
import core

while True:
    opcion = input("FUNCION: ").lower()
    if opcion == "fichas":
        core.menu.Fichas()
    elif opcion == "citas":
        core.menu.Citas()
    elif opcion == "consultas":
        core.menu.Consultas()
    elif opcion == "nuevo doctor":
        core.menu.Nuevo_doctor()
    elif opcion == "nuevo paciente":
        core.menu.Nuevo_paciente()
    elif opcion == "modificar":
        core.menu.Modificar()
    elif opcion == "limpiar linea":
        core.menu.LimpiarLinea()
    elif opcion == "limpiar":
        core.menu.Limpiar()
    elif opcion == "salir":
        core.menu.Salir()
        break