# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 18:49:32 2020

@author: EspinoLeandroo
"""

"""
creacion de carpetas
"""
#%%
import os
os.makedirs("./nombres/", exist_ok=True)


"""
Listar archivos
"""

#%%
archivos_carpeta_actual = os.listdir('.')
print(archivos_carpeta_actual)
"""
Escribir archivos
"""
#%%

archivo_para_escribir = open('./nombres/usuarios.txt', 'w')
archivo_para_escribir.write('hola ')
archivo_para_escribir.write('mundo ')
archivo_para_escribir.write('!')
archivo_para_escribir.close()

#%%
archivo_para_escribir = open('./nombres/usuarios.txt', 'a')
archivo_para_escribir.write('hola ')
archivo_para_escribir.write('mundo ')
archivo_para_escribir.write('!')
archivo_para_escribir.close()

#%%
usuarios = {'leandro', 'Espino'}
with open('./nombres/usuarios.txt', 'w') as fname:
    for usuario in usuarios:
        fname.write(usuario)
        fname.write("\n")

#%%
"""
Lectura de archivos
"""
with open('./nombres/usuarios.txt',) as fname:
    datos = fname.readlines()
    
print(datos)

#%%
"""
Usando pathlib
"""

from pathlib import Path
carpeta = Path('./nombres/')
archivo = carpeta / "usuarios.txt"
print(archivo)

archivo.readtext();
archivo.write_text('hola')













