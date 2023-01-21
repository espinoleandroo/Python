# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 18:16:24 2020

@author: EspinoLeandroo
"""

#%%
def saludar():
    print('Hola mundo')

saludar()

#%%
def saludar(nombre):
    print('Hola {}'.format(nombre))
    
saludar('leandro')

#%%
def sumar(a,b):
    return a + b

print(sumar(2,3))

#%%
def suma_y_resta(a,b):
    suma = a+b
    resta = a-b
    return suma,resta

print(suma_y_resta(1,2))

#%%
suma_lambda = lambda a,b: a+b
print(suma_lambda(1,3))