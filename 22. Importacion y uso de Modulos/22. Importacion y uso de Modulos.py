
# DETALLES adicionales de importacion y uso de modulos 

# Ataque de secuestro de librerias en python 

import math as m # Puedes llamar a las librerias tal como tu quieras


print(m.sqrt(16)) # Se puede ajustar a la necesidad para que sea intuitivo y facil de usar 

# Una biblioteca son varios modulos y paquetes asociados en una proyecto en comun 


# -    ---      --------------------  Python library hyjacking

import sys

print(sys.path) # para saber cual es el path de esta libreria


import os 

os.system("whoami")