# Utiliza la imagen base de Alpine Linux
FROM python:3.9-alpine

# Actualiza los paquetes en la imagen base
RUN apk update && apk upgrade

# Crea el directorio de la aplicación
RUN mkdir /app

# Copia los archivos necesarios a la imagen
COPY app.py /app/app.py
COPY options.py /app/options.py
COPY templates /app/templates
COPY requirements.txt /app/requirements.txt

# Establece el directorio de trabajo
WORKDIR /app

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt


# Especifica el comando que se ejecutará al iniciar el contenedor
CMD ["python3", "app.py"]
