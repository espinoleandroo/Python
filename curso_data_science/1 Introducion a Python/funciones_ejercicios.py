# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 18:50:14 2020

@author: EspinoLeandroo
"""

#%%
"""
Crear una funcion resta que reste dos numero y regrese el resultado
"""
def resta(a, b):
    return a - b

print(resta(11,1))

#%%
"""
Crear una funcion lambda que convierta una string a minusculas
"""
minusculas = lambda string:string.lower()
print(minusculas("LEANDRO"))

""""
Crear una funcion que acepte 3 argumentos 2 numeros y 1 string
si el string es "suma" regresar la suma de los numeros
si el string es "resta" regresar la resta de los numeros
"""
def operaciones(a, b, operacion):
    if operacion == 'resta' :
        return a - b
    elif operacion == 'suma' :
        return a + b

print(operaciones(1,1,'suma'))
print(operaciones(11,1,'resta'))

#%%
"""
Crear una funcion que pregunte al usuario una frase, 
y la funcion debera retornar las palabras de la frase en orden inverso
"""
def frase_inversa():
    frase = input('Frase: ')
    palabras = list(frase.split(" ")) 
    inversa = ''
    for palabra in palabras:
        inversa = palabra + ' ' + inversa
    return inversa

print(frase_inversa())

#%%
"""
Crear una funcion que detecte si una palabra o frase es palindromo
"""
def es_palindromo(string):
    palindromo = ''
    string = string.replace(' ', '')
    
    for letra in string:
        palindromo = letra + palindromo
    
    if palindromo == string:
        print ('Es palindromo')
    else:
        print('NO es palindromo')
        
frase = input('frase: ')
es_palindromo(frase)


#%%
"""
Crear una funcion que reciba una lista de listas y retorne una lista simple
"""
def listas_to_lista(listas):
    lista_simple = []
    for lista in listas:
        for elemento in lista:
            lista_simple.append(elemento)
    print(lista_simple)

listas = [
    [1,2,3,4,5],
    ['a', 'b', 'c'],
    ["Leandro", "Espino"]]
print(listas)
listas_to_lista(listas)
    