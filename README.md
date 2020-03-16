
 #DOCKER Y DOCKER COMPOSE
 
 En el ejemplo de Docker-compose (composet) se construye una aplicación web en Pyhton que se ejecuta en Docker Compos.
 La aplicación usa el framework **Flask** y mantiene un contador de visitas en **Redis**.
 
 
 **Flask** -> Framework para aplicaciones web en Python.
 **Redis** -> Motor de base de datos en memoria, basado en el almacenamiento en tablas de hashes (clave/valor) pero que opcionalmente puede ser usada como una base de datos durable o persistente. 
**Dockerfile** -> Se usa para construir una imagen Docker.
**Docker image** -> contiene todas las dependencias que necesita la aplicación.
**docker-compose.yml** -> Define servicios
    **web service** -> Utiliza una imagen creada a partir del Dockerfile en el directorio actual. Luego conecta el contendor y la máquina host al puerto indicado.
    **redis service** -> Utiliza una imagen pública de Redis extraida Docker Hub.

 ## Comando para ejecutar la aplicación -> docker-compose up 
 ## Comando para listar las imagenes -> docker images ls

 

