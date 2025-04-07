
# No estan enumerados y son Mutables 
# Pares de clave - valor 

mi_diccionario = {"Nombre":"Arley", "Edad":"22", "Ciudad":"Bogota" }

print(mi_diccionario)
print(type(mi_diccionario)) # Tipo de dato : dictionary


print(mi_diccionario["Edad"]) # Se lista El valor de la clave

# Mutabilidad


mi_diccionario["Nombre"] = "Lobotec" # Cambio de valor en la Propiedad Nombre

print(mi_diccionario["Nombre"])

mi_diccionario["Profesion"] = "Hacker" # Añadir propiedades y valores a un diccionario 

print(mi_diccionario)

# Eliminacion de elementos del diccionario dado

del mi_diccionario["Edad"] # Eliminacion de la propiedad Edad

print(mi_diccionario)

# Busquedad de propiedades o valores en el registro de todo el diccionario de la siguiente forma 

if "Nombre" in mi_diccionario:
    print("Esta propiedad existe en el diccionario")

# Iteracion sobre un diccionario podriamos hacer lo siguiente:


for Propiedad, Valor in mi_diccionario.items(): # Con la funcion items
    print(f"El {Propiedad} es: {Valor}")


# Diccionarios de comprension 


cuadrados = {x: x**2 for x in range(6)} # Sacar el cuadrado de cada valor en el rango dado

print(cuadrados) # Genera un diccionario con clave - valor correspondiente


print(cuadrados.keys()) # Print de Claves
print(cuadrados.values()) # Print Valores

# Busqueda con manejo de ecepcion

print(mi_diccionario.get("Nombre","No Encontrado")) # Busca el valor de la propiedad Nombre y si no aparece entonces genera un mensaje de ecepcion


# Actualizacion de diccionarios e inclusion de nuevas propiedades y valores asignados

mi_diccionario2={"color":"Azul","Mascota":"Perro"}

mi_diccionario.update(mi_diccionario2)
print(mi_diccionario)

# Existencia de diccionarios anidados con sub claves

my_dict = {

    "nombre" : "S4vitar",
    "Hobbies" : {"Primero":"Musica", "Segundo":"Futbol"} ,
    "Edad" : 28

}


# Valor de la subclave 

print(my_dict["Hobbies"]["Primero"]) # Impresion de la subclave de Primnero de la Propiedad de Hobbies

