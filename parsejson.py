# Fill in this file with the code from parsing JSON exercise

import json
import yaml

# Abrir y parsear el archivo JSON (se convierte en dict de Python)
with open('myfile.json', 'r') as json_file:
    ourjson = json.load(json_file)

# Ver el diccionario completo
print(ourjson)

# Extraer valores específicos por clave
print("The access token is: {}".format(ourjson['access_token']))
print("The token expires in {} seconds.".format(ourjson['expires_in']))

# Convertir y mostrar el JSON en formato YAML
print("\n\n---")
print(yaml.dump(ourjson))
