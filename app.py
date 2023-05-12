from flask import Flask, render_template, request
import re
import yaml
from options import options, options_dict

app = Flask(__name__)

# Ruta principal para mostrar el formulario y el resultado
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        docker_command = request.form['docker_command']
        docker_compose_yaml = convert_to_docker_compose(docker_command)
        return docker_compose_yaml

    return render_template('index.html')

def find_options(command):
    # separa las palabras de command para obtener luego la imagen
    command_sep = command.split()
    # Expresión regular para buscar opciones en el comando
    pattern = r"-(\w+)|--(\w+[-\w]+)|--(\w+)"
    # Buscar coincidencias de opciones en el comando
    matches = re.findall(pattern, command)
    # Lista para almacenar las opciones encontradas
    found_options = []
    # Procesar las coincidencias y compararlas con el diccionario de opciones
    for match in matches:
        option = match[0] or match[1] or match[2] # El resultado puede estar en una de las tres posiciones

        if f"--{option}" in options:
            value=''
            value_index = command.index(option) + len(option) + 1
            if value_index < len(command):
                for i in range(value_index, len(command)):
                    value += command[i]
                    if command[i].startswith(' '):
                        break
                value = value.strip()
            found_options.append((option, value))
        elif f"-{option}" in options:
            value=''
            value_index = command.index(option) + len(option) + 1
            if value_index < len(command):
                for i in range(value_index, len(command)):
                    value += command[i]
                    if command[i].startswith(' '):
                        break
                value = value.strip()
            found_options.append((option, value))

    for word in command_sep:
        if any(word in option for option in found_options) or word.lower() in ['docker', 'run']:
            continue
        if not word.startswith('-'):
            image = word
            break
    if image is not None:
        found_options.append(("image", image))


    return found_options


def convert_to_docker_compose(command):
    # Obtener las opciones encontradas
    options_found = find_options(command)

    # Extraer la imagen de las opciones encontradas
    image_name = None
    for option, value in options_found:
        if option == 'image':
            image_name = value
            break

    # Construir el fragmento de texto de Docker Compose
    docker_compose_text = f'version: "3.3"\n' \
                          f'services:\n' \
                          f'  {image_name}:\n' \
                          f'    image: {image_name}\n'

    # Agregar las opciones al fragmento de texto de Docker Compose
    for option, value in options_found:
        if option != 'image' and option in options_dict:
            compose_key = options_dict[option]
            if '/' in compose_key:
                compose_key, sub_key = compose_key.split('/')
                docker_compose_text += f"    {compose_key}:\n" \
                                       f"      {sub_key}:\n" \
                                       f"        {value}\n"
            else:
                docker_compose_text += f"    {compose_key}: {value}\n"

    # Generar el YAML de Docker Compose
    docker_compose_yaml = yaml.safe_dump(docker_compose_text, sort_keys=False, default_style='|')
    docker_compose_yaml = docker_compose_yaml.strip('|')
    return docker_compose_yaml

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
