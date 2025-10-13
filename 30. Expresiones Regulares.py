

#  El uso de los rejex, encontrar un patron de caracteres para hacer match con parametros de busqueda 

# Mas usualmente llamadas como expresiones regulares 

import re

text = "Mi gato esta en el tejado y mi otro gato esta en el jardin"

matches = re.findall("gato", text) # Se filtra en formato lista con los matches que se encuentren

print(matches) 


text2 = "Hoy estamos a la fecha de 10/10/2023 y mañana es el dia de 11/10/2023"

matches = re.findall("10/10/2023",text2)

print(matches)
# Si queremos bucar por un formato dado como lo puede ser la fecha podemos hacer lo siguiente

matches = re.findall("\d{2}\/\d{2}\/\d{4}",text2) #Se usan caracteres especiales para denotar 2 caracteres en dia y mes y 4 en año 

print(matches)


# Con la funcion de sub puedes realizar remplazos en el texto

modificada=re.sub("fecha","remplazo", text2)
print(modificada)


# se pueden crear funciones para validar un correo 
