
# No conviene crear funciones con nombre y se simpplifican a una sola funcion 

# delacracion de la funcion lambda

mi_funcion = lambda: print("Hola mundo")

mi_funcion()

# Paso de variables mediante el empleo y uso de la funcion 

cuadrado = lambda x: print(f"El cuadrado de el numero {x} es {x**2}")

cuadrado(10)

# Paso de 2 variables 

suma = lambda x,y: print(f"La suma de los numerosa {x} y {y} es {x+y}")

suma(10,5)


# Paso de creacion de funciones lambda mediante listas iterables

numeros = [1,2,3,4,5]

cubos = list(map(lambda x: x**3, numeros)) # la funcion map necesita como requisisto una funcion y una condicion iterable como lo puede ser una lista

print(cubos)

# Muestra del uso de la funcion filter en relacion a las funciones lambda

Numeros1 = [1,2,3,4,5,6,7,8,9]

impares = list(filter(lambda x: x % 2 != 0, Numeros1)) # Lo que hace la funcion filter es que toma y returna los valores que establezcan como true la condicion que se cumpla

print(impares)       

# Rutilizacion de los elementos dados con las funciones de reduce 

from functools import reduce

ONumeros = [1,2,3,4,5]

multiplicacion = reduce(lambda x,y: x*y, ONumeros) # la funcion reduce reutiliza los valoes resultado y los guarda en la primera variable, iterando en la segunda

print(multiplicacion)



