# Fill in this file with the code from parsing XML exercise

import xml.etree.ElementTree as ET
import re
 
# Parsear el archivo XML
xml = ET.parse("myfile.xml")
root = xml.getroot()
 
# Extraer el namespace con regex  (ej: {urn:ietf:params:xml:ns:netconf...})
ns = re.match('{.*}', root.tag).group(0)
 
# Navegar el arbol: rpc > edit-config > default-operation / test-option
editconf = root.find("{}edit-config".format(ns))
defop    = editconf.find("{}default-operation".format(ns))
testop   = editconf.find("{}test-option".format(ns))
 
# Imprimir los valores extraidos
print("The default-operation contains: {}".format(defop.text))
print("The test-option contains: {}".format(testop.text))

