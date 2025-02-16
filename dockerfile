#Usar la imagen de Python 
FROM python:3.10

#Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

#Copiar todos los archivos del proyecto al contenedor
COPY . /app

#Instalar Flask (y cualquier otra dependencia)
RUN pip install flask

#Exponer el puerto 5000 para acceder a la aplicación
EXPOSE 5000

#Comando para ejecutar la aplicación
CMD ["python", "app.py"]