# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 19:54:22 2020

@author: EspinoLeandroo
"""

#%%
class CocheBasico:
    
    def girar_izquierda(self):
        print('girando izquierda')
        
    def girar_derecha(self):
        print('girando derecha')
    
    def acelerar(self):
        pass
    
    def frenar(self):
        pass
    
print(CocheBasico)

#%%
coche_de_leandro = CocheBasico()
print(coche_de_leandro)

#%%
print(coche_de_leandro.girar_derecha())


#%%
class CocheColor:
    
    def __init__(self, color):
        self.color = color
        
    def describir(self):
        print("coche de color {}".format(self.color))
        
coche_rojo = CocheColor(color='rojo')
coche_rojo.describir()

#%%
"""
Herencia
"""

class Taxi(CocheColor):
    
    def acelerar2(self):
        pass
    
