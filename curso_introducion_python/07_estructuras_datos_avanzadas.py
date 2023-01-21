# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 17:13:09 2020

@author: EspinoLeandroo
"""

#%%
grupo_amigos = set(['Vale', 'koke', 'fely', 'yo'])
print(type(grupo_amigos))

grupo_amigos2 = {'manuel', 'fernando', 'andres', 'yo'}
print(type(grupo_amigos2))

#%%
todos_amigos = grupo_amigos.union(grupo_amigos2)
print(todos_amigos)

amigos_comun = grupo_amigos.intersection(grupo_amigos2)
print(amigos_comun)

grupo_amigos2.add('martin')
print(grupo_amigos2)

grupo_amigos2.remove('yo')
print(grupo_amigos2)