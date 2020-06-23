# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 17:37:12 2020

@author: EspinoLeandroo
"""
#%%
"""
IF ELSE
"""
edad = 23
if edad >= 18:
    print ("eres mayor de edad")
else:
    print ("eres menor de edad")

#%%
"""
FOR
"""
numeros = [1, 2, 3, 4, 5, 6, 11, 13, 23, 56]

for numero in numeros:
    if numero == 11:
        print (11)
        pass
    
    if numero < 10:
        print("numero valido")
    else:
        print("numero invalido")
        
#%%
"""
Try Except
"""
numero_str = '10.5'
try:
    numero_int = int(numero_str)
except Exception as e:
    print (e)


#%%
"""
WHILE
"""
n_elefante = 2
print("1 elefante se columpiaba sobre la tela de una ara;a")
while n_elefante <= 10:
    print("{} elefante se columpiaba sobre la tela de una ara;a".format(n_elefante))
    n_elefante += 1
#%%
while 1:
    input_usuario = input('dime un numero del 1 al 10, ("exit") para salir: ')
    try:
        if(input_usuario == 'exit'):
            print('adios')
            break
        elif int(input_usuario) <= 10:
            print('valor correcto')
        else:
            print('valor incorrecto')
    except ValueError as e:
        print('Error: {}'.format(e))
