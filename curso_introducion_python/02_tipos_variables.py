# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 16:55:25 2020

@author: EspinoLeandroo
"""

nombre = 'Leandro'
ocupacion = 'Desarrollador'
presentacion = "Hola me llamo {} y soy {}".format(nombre, ocupacion)
print(presentacion)
prensentacion = f"Hola me llamo {nombre} y soy {ocupacion}"
print(presentacion)
print(presentacion.upper())
print(presentacion.lower())

#%%
numero = 11
print(type(numero))
numero = str(numero)
print(type(numero))
numero = int(numero)
print(type(numero))
