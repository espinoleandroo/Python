# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 18:03:33 2020

@author: EspinoLeandroo
"""
semana = {
       'lunes':1,
       'martes':2,
       'miercoles':3,
       'jueves':4,
       'viernes':5,
       'sabado':6,
       'domingo':7}
SEMANA = {}
for dia, valor in semana.items():
    SEMANA[(dia.upper())] = valor

print(SEMANA)

for dia in SEMANA:
    if("O" in dia):
        print (dia)
