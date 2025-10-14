

# Escalamiento de scripts para que otros usuarios puedan usar la modalidad

# se usa la libreria os 

import os

if os.path.exists("Mi archivo.txt"):

    print("El archivo existe") # Realiza una comprobacion de existencia del archivo en la ruta actual 

if not os.path.exists("Mi_directorio"):
    os.mkdir("Mi_Directorio") # Crea un directorio nuevo depues de realizar una comprobacion de existencia del mismo 


# Tambien se puede realizar con directorios anidados de la siguiente forma:

if not os.path.exists("PrimerDirectorio/SegundoDirectorio"):
    os.makedirs("PrimerDirectorio/SegundoDirectorio") # Creacion de directorios anidados

# fUNCION para listar direcotorios es la siguiente 

recursos = os.listdir()

for recurso in recursos:
    print(recursos)


# Para la eliminacion tambien se puede hacer de la siguiente forma



if os.path.exists("Prueba.txt"):
    os.remove("Prueba.txt")


# Eliminacion de directorios se vincula de la siguiente forma 

os.removedirs("Mis_Directorios") 