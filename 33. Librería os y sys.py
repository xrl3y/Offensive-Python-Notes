
# Ver cuales son las librerias os y sys 

import os 

directorio_actual = os.getcwd() # Lo que te permite es reconocer la ruta absoluta del directorio actual de trabajo

print(directorio_actual)

files = os.listdir(directorio_actual) # Se guarda como una lista todos los elementos que esten en el listado del directorio 
print(files)

os.mkdir("Mi_directorio") # Crear directorio

os.makedirs("Directorio1/direcotrio2") # Crear una ruta de directorios

os.path.exists("ejemplo.txt") # Prueba si un archivo o directorio existe 

variable_de_entorno = os.getenv('VARIABLEDEENTORNO') # Lo que hace es obtener el valor de una variable de entorno


import sys 

sys.argv[0] # Forma de poder recoger o recopilar el nombre del script 

sys.argv[1] # Hace referencia al primer argumento que se le pase al script por consola durante su ejecucion y asi sucecivamente 

sys.path # Rutas del sistema

sys.exit(1) # Control de los codigos de estado, 1 erroneo, 0 exitoso




 
