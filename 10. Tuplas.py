
# lAS tuplas son similares a las litas y son inmutables y se definene con parentesis ()


example = (1,2,3,4,5)

print(type(example))


# Print de elementos

print(example[0]) # Para seleccionar el primer elemento si se debe realizar con parentesis cuadrados la eleccion

# No se puedem realizar cambios a la tupla, ni cambio de valores, ni añadicion de valores 

# Otro ejemplo puede ser

mi_tupla = (1,2,3,4)

a,b,c,d = mi_tupla

print(a)
print(b)
print(c)
print(d)

# Si se puede hacer sumatorias entre las tuplas como la siguiente forma 

mi_primera_tupla = (1,2,3,4,5)
mi_segunda_tupla = (6,7,8,9,10)

mi_tercera_tupla = mi_primera_tupla + mi_segunda_tupla

print(mi_tercera_tupla)