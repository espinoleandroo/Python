# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 17:08:08 2020

@author: EspinoLeandroo
"""
frutas = ['naranjas', 'manzana', 'pera', 'fresa']

print(frutas)
print(type(frutas))

print(frutas[0])
#podemos aceder aun rango de elementos con [inicio:final-1:orden]
print(frutas[:2])
print(frutas[2:])

print(len(frutas))

frutas[0]='mango'
print(frutas)

frutas[3:] = ['uva', 'higo', 'sandia', 'pomelo']
print(frutas)
#%%
print ('uva' in frutas)
print ('patata' in frutas)
print (frutas.index('pera'))

#%%
print (frutas)
a = frutas.pop(2)
print (frutas)

#%%
edades = [49,47, 23,20,17,14]
edades.sort()
print(edades)


#%%
"""
Diccionarios
"""
inventario = {
     'melocotones':3,
     'fresas': 1,
     'manzanas': 4}
print(type(inventario))
print(inventario['fresas'])
 