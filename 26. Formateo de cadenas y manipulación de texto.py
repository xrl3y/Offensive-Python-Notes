
cadena =  "HOLA MUNDO"


print(cadena.strip()) # Quita todos los espacios y las tabulaciones que pueda quitar una cadena


print(cadena.lower()) # Coloca todo en minusculas 
print(cadena.upper()) # coloca todo en mayusculas


print(cadena.replace('O','x')) # remplaza el primer item con el segundo item 


nueva_cadena = cadena.split()

print(nueva_cadena) # crea una lista con limitador de espacion o 2 puntos

# Prueba del contenido de una cadena en booleano 

s = "Hola mundo"

print(s.startswith('Hola')) # verifica si es true or false donde limita donde epieza la cadena

print(s.endswith('mundo')) # terminaciones 

print(s.find("ola")) # Posicion dond eempieza la cadena , si la cadena no existe te va a a devolver -1

print(s.index("H")) # si el elemento no existen entonces lo que te devolver es un error en vez de un -1


frase = "Esto es una prueba para contar el totald e caracteres que hay en una frase"

print(frase.count('e')) # Cuenta el numero segun la condicion que se le asigne
