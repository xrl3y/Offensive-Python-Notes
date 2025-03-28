
# Datos mas versatiles de python que facilmente pueden mutar

puertos_tcp = [21,22,25,80, 443, 444, 8080, 445, 69]

puertos_tcp.append(1337)


for puerto in puertos_tcp:
    print(puerto)

# Ejemplo con vulnerabilidades CVES

cve_list =  ['CVE-2024-1477', 'CVE-2023-1122', 'CVE-1999-5670']

cve_list.remove(cve_list[0]) # remover datos de una lista

print(cve_list)

# Ordenamient de listas

puertos_tcp.sort() # esto es una funcion que se le aplica a la variable puertos_tcp y que modifica el valor de la variable ordenando sus datos de manera acendente

print(puertos_tcp)

# Inversion de elementos con la funcion reverse

Ataques = ["ramsoware", "SQLinyection", "Cross-Site-Scripting", "XSS", "Man-In-the-Middle"]

Ataques.reverse() # funcion de reversa

print(Ataques)

#Proceso de enumeracion de ataques

for i, attack in enumerate(Ataques):
    print(f"{i}. {attack}")

# Para colocar todo en  mayusculas de una secuencia de strings podriamos hacerlo de la siguiente forma

Ataques_Upper_Case = [ attack.upper() for attack in Ataques] # funcion de mayusculas y lower es funcion de minusculas

print(Ataques_Upper_Case)

# Para usar combinatoria de listas podremos hacer lo siguiente

names = ["s4vitar", "xrl3y", "fabi0n", "hackavis","xrl3y"]
edades = [19,20,31,45]

for name, edad in zip(names, edades): # combinacion de listas 
    print(f"{name} tiene {edad} años")

del names[2]

for name in names:
    names.remove("xrl3y") # remover por nombre, puede ser usado en listas gigantes 

print(names)

# Otro ejemplo de litas puede ser la eliminacion o la limpieza de las listas de la siguiente forma

animales = ["perro", "gato", "oso" , "avestruz"]

# animales.clear() # con esta funcion se pueden vaciar y limpiar listas 

print(animales)

# Otro ejemplo que se puede usar es acerca del uso del pop 

animal_eliminado = animales.pop(1) 

print(animales)
print(animal_eliminado)

# La mutabilidad se trata de cambiar datos que estan asignados a otros segun el valor que desees 

# Ademas de las funciones insert y extend que es para la insercion de datos y listas en una misma lista 