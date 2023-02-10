# Entornos Virtuales

Un entorno virtual, es un directorio que contiene una instalación de Python de una versión en particular, además de unos cuantos paquetes adicionales.

## Instalar en WSL
    sudo apt install -y python3-venv

## Crear un entorno virtual
    python3 -m venv env

## Activar Entorno Virtual en WSL
    source env/bin/activate

## Activar Entorno Virtual en Windows
    env\Scripts\activate.bat

## Salir del Entorno Virtual
    deactivate
