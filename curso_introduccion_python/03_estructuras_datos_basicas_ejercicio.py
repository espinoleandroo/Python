# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 17:31:49 2020

@author: EspinoLeandroo
"""
semana = {
       'lunes':1,
       'martes':2,
       'miercoles':3}
print(semana)

semana['LUNES'] = semana.pop('lunes')
semana['MARTES'] = semana.pop('martes')
semana['MIERCOLES'] = semana.pop('miercoles')

print(semana)