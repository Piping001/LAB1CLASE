# Fill in this file with the code from parsing YAML exercise

import json
import yaml

# Abrir y parsear el archivo YAML (se convierte en dict de Python)
with open('myfile.yaml', 'r') as yaml_file:
    ouryaml = yaml.safe_load(yaml_file)

# Ver el diccionario completo
print(ouryaml)

# Extraer valores específicos
print("The access token is {}".format(ouryaml['access_token']))
print("The token expires in {} seconds.".format(ouryaml['expires_in']))

# Convertir y mostrar el YAML en formato JSON (con indentación)
print("\n\n")
print(json.dumps(ouryaml, indent=4))
