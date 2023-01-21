# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 18:49:32 2020

@author: EspinoLeandroo
"""

"""
creacion de carpetas
"""

import os
os.makedirs("./data/working_with_files/", exist_ok=True)


"""
Listar archivos
"""


archivos_carpeta_actual = os.listdir('.')
print(archivos_carpeta_actual)
"""
Escribir archivos
"""


archivo_para_escribir = open('./data/working_with_files/usuarios.txt', 'w')
archivo_para_escribir.write('hola ')
archivo_para_escribir.write('mundo ')
archivo_para_escribir.write('!')
archivo_para_escribir.close()


archivo_para_escribir = open('./data/working_with_files/usuarios.txt', 'a')
archivo_para_escribir.write('hola ')
archivo_para_escribir.write('mundo ')
archivo_para_escribir.write('!')
archivo_para_escribir.close()


usuarios = {'leandro', 'Espino'}
with open('./data/working_with_files/usuarios.txt', 'w') as fname:
    for usuario in usuarios:
        fname.write(usuario)
        fname.write("\n")


"""
Lectura de archivos
"""
with open('./data/working_with_files/usuarios.txt',) as fname:
    datos = fname.readlines()
    
print(datos)


"""
Usando pathlib
"""

from pathlib import Path
carpeta = Path('./data/working_with_files/')
archivo = carpeta / "usuarios.txt"
print(archivo)

archivo.read_text()
archivo.write_text('hola')


archivo = carpeta / "usuarios_2.txt"
archivo.write_text('hola!')
print(archivo.read_text())

usuarios=['Leandro', 'Itzel']
carpeta = Path('./data/working_with_files/')
archivo = carpeta / "usuarios_2.txt"

with open(archivo, "a") as fname:
    for usuario in usuarios:
        fname.write(usuario)
        fname.write("\n")

archivo.read_text()











