# docker-compose
# Docker Command to Docker Compose Converter

This project is a Docker command to Docker Compose converter that allows you to take existing Docker commands and generate the equivalent YAML format for Docker Compose.

## Inspiration

This project was inspired by the [magicmark/composerize](https://github.com/magicmark/composerize) project, which also tackles the conversion of Docker commands to Docker Compose. However, this project was written from scratch in Python to create a lighter Docker image with the same functionalities.

## Features

The Docker command to Docker Compose converter is capable of parsing existing Docker commands and extracting relevant information such as the image, ports, volumes, restart, logging options, among others. Based on this information, it generates a valid YAML file for Docker Compose that reflects the configuration of the original Docker command.

## Usage

To use this converter, simply paste the Docker command into the provided text box in the web interface. The converter will analyze the command and generate the equivalent Docker Compose YAML. You can copy the result and use it in your Docker Compose project.

## Contributions

This project was developed as a personal contribution, but contributors are encouraged to participate and enhance the functionality of the converter. If you wish to contribute, you can submit pull requests through GitHub.

## Acknowledgements

I would like to thank the [magicmark/composerize](https://github.com/magicmark/composerize) project for their inspiration and focus on converting Docker commands to Docker Compose. Their contributions are valuable to the developer community and have been an important reference for this project.


# Convertidor de Comandos Docker a Docker Compose

Este proyecto es un convertidor de comandos de Docker a Docker Compose, que te permite tomar comandos de Docker existentes y generar el equivalente en formato YAML para Docker Compose. 

## Inspiración

Este proyecto se inspiró en el proyecto [magicmark/composerize](https://github.com/magicmark/composerize), el cual también aborda la conversión de comandos Docker a Docker Compose. Sin embargo, este proyecto fue escrito desde cero en Python, con el objetivo de crear una imagen Docker más liviana y ofrecer las mismas funcionalidades.

## Funcionalidades

El convertidor de comandos Docker a Docker Compose es capaz de analizar los comandos Docker existentes y extraer información relevante como la imagen, puertos, volúmenes, reinicio, opciones de registro, entre otros. A partir de esta información, genera un archivo YAML válido para Docker Compose que refleja la configuración del comando Docker original.

## Uso

Para utilizar este convertidor, simplemente pega el comando Docker en el cuadro de texto proporcionado en la interfaz web. El convertidor analizará el comando y generará el equivalente en YAML de Docker Compose. Puedes copiar el resultado y utilizarlo en tu proyecto de Docker Compose.

## Contribuciones

Este proyecto fue desarrollado como una contribución personal, pero se anima a los colaboradores a participar y mejorar la funcionalidad del convertidor. Si deseas contribuir, puedes enviar solicitudes de extracción a través de GitHub.

## Agradecimientos

Quiero agradecer al proyecto [magicmark/composerize](https://github.com/magicmark/composerize) por su inspiración y enfoque en la conversión de comandos Docker a Docker Compose. Sus contribuciones son valiosas para la comunidad de desarrolladores y han sido una referencia importante para este proyecto.

