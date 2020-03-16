FROM python:3.7-alpine  #Se construye la imagen empezando con python
WORKDIR /code           #Se establece el directorio de trabajo
ENV FLASK_APP app.py    #Se establecen las variables de entorno usadas por flask
ENV FLASK_RUN_HOST 0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers #Se instala gcc para que algunos paquetes de python puedan compilar speedups
COPY requirements.txt requirements.txt  #Copia requirements.txt e installa las dependencias de python
RUN pip install -r requirements.txt     
COPY . . #Copia el directorio actual . en el proyecto al directorio de trabajo . en la imagen
CMD ["flask", "run"]    #Establece el comando por defecto del contenedor.