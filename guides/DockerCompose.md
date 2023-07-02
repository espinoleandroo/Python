# Docker compose

## Ejecuta el proceso de construcción de una imagen
 que va a ser usado en el docker-compose.yml a partir de los ficheros Dockerfile que se indican.

    docker-compose build



##  Crear los contenedores 
que están descritos en el docker-compose.yml.
    
    docker-compose up




##  Crear en modo detach los contenedores 
que están descritos en el docker-compose.yml. Eso significa que no muestran mensajes de log en el terminal y que se nos vuelve a mostrar un prompt.
    
    docker-compose up -d




## Enlista contenedores
Lista los contenedores de un proyecto Compose, con el estado actual y los puertos expuestos.
    
    docker-compose ps




## Ejecuta una orden
En este caso bash en un contenedor llamado web-server que estaba descrito en el docker-compose.yml
    
    docker-compose exec web-server bash




## Para los contenedores
los borra y también borra las redes que se han creado con
    
    docker-compose down
