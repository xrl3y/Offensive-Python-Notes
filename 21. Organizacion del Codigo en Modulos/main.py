
import math_operations # Se busca en el directorio actual de trabajo


print(math_operations.suma(2,4)) # Se llama al modulo a la funcion suma, dando asi la organizacion del codigo

# Tambien se puede indicar las funciones o clases que quieres importar del mismo script


from math_operations import suma, resta,multiplicacion,division # De esta manera especificas que es lo que quieres importar del modulo existente


print(suma(2,4))
print(resta(2,4))
print(division(2,4))
print(multiplicacion(2,4))

# Tambien existen bibliotecas , modulos y librerias estandas incorporadas en python que puedes utilizar

import math

from math import * # De esta forma podrias importar todo # Afecta el rendimiento

print(dir(math)) # De la siguiente manera puede ver que puedes realizar con la libreria que quieres utilizar

print(math.sqrt(16))


# De la siguiente forma podrias ver todos los modulos que por defecto vienen con python

import sys

print(sys.builtin_module_names)


# Libreria de hasheo

import hashlib

print(hashlib.md5(b"Hola").hexdigest()) # Permite hashear una cadena a md5 

# para listar una ruta del sistema se podria usar

print(hashlib.__file__) 