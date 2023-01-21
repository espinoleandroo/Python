# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 17:29:11 2020

@author: espinoLeandroo
"""
"""
hacer una funcion que toma una frase y devulve las 5 letras mas comunes
"""

from collections import Counter

frase = 'Hola mi nombre es leandroo'

def contar_letrar(frase):
    contador = Counter([letra for letra in frase if letra not in " ,.\n"])
    return contador.most_common(5)

print(contar_letrar(frase))