
# Tambien se asemejan a sets 

# lA dIFERENCIa es que los conjuntos no estan enumerados al igual que las listas y las tuplas

# Asi que los elementos de un conjunto no tienen un orden especifico al igual que por ejemplo las listas y las tuplas


mi_conjunto = {1,2,3}

print(mi_conjunto)

# A los conjuntos se les pueden añadir datos de la siguiente forma 

mi_conjunto.add(8)

print(mi_conjunto) # Python organiza la forma mas optimizada en los conjuntos porque no tienen orden especificos

# Tambien esta la secuencia de update 

mi_conjunto.update({7,8,9})

print(mi_conjunto)

# Tambien se puede remover y otras asiganiciones como en las listas, propiedades de edicion 

mi_conjunto.discard(7) # Funcion para eleminar elementos de un conjunto

print(mi_conjunto)

# Se puedem crear intersecciones entre conjuntos 

mi_primer_conjunto ={1,2,3,4,5,6,7,9}
mi_segundo_conjunto = {2,6,9}

mi_conjunto_final = mi_primer_conjunto.intersection(mi_segundo_conjunto) # Fucion de interseccion de conjuntos

print(mi_conjunto_final)

mi_conjunto_final = mi_primer_conjunto.union(mi_segundo_conjunto) # Funcion de union sin que se repitan los elementos

print(mi_conjunto_final)

# Podemos verificar si un conjunto es subconjunto de otro conjunto

print(mi_segundo_conjunto.issubset(mi_primer_conjunto)) # Te devuelve un estado booleano que te dice si un conjunto pertenece a otro


# Los conjuntos no pueden tener elementos repetdos

mi_lista = [1,2,3,4,5,6,8,64,6,4,64,6,4,6,1,61,6,1,61,61,1]

Conjunto_Sin_Repeticiones = set(mi_lista) # funcion set usada para no repeticiones de elementos

print(Conjunto_Sin_Repeticiones) # Te imprime la variable de tipo conjunto ya que no proporciona repeticiones de elementos 

# Busqueda de valores mediante los conjuntos

mi_conjunto = set(range(10000)) # Establece un conjunto con los numeros del 0 al 9999

print(1234 in mi_conjunto) # Devuelve un estado booleano si es veridica la confirmacion de que ese numero se encuentra en el conjunto

# Operaciones entre conjuntos

usuarios_facebook = {"ana","JUAN","luis","pepe"}
usuarios_twitter = {"pepe","ama","luis","arley"}

print(usuarios_facebook.intersection(usuarios_twitter)) # Rpresentacion de interseccion asi como tambien se puede hacer la union si la repeticion de valores 

# La diferecia se realiza con .difference 


