# Funcionan para iterar sobre listas, ciclos etc


names = ["marcelo", "hacker", "devops", "thegoodhacker"]

for i in range(5): # Utilizar Secuenciadores, se cuenta el 0 siempre
    print(i)

for name in names:
    print(f"el nombre de esta secuencia es de {name}")

# Modo de utilizacion de Whil, bucles condicionados

i = 0

while i < 5:
    print(i)
    i += 1

# Modo de utilizacion de la funcion enumerate 

for posicion,name in enumerate(names):
    print(f"{posicion+1} - {name}")

# Iteracion de items mediante el uso de diccionarios

frutas = {"manzanas":1, "platanos":5, "kiwis":10}

for fruta, cantidad in frutas.items():
    print(f"hay {cantidad} unidades de {fruta}")

# Anidacion de Bucles

my_list=[[1,2,3],[2,4,6],[4,7,8]]

b=0
for element in my_list:
    print(f"El grupo # {b} es.")
    b += 1
    for elements_in_list in element:
        print(elements_in_list)



# Listas de Comprension (for)

odd_list = {1,3,5,7,9}
cuadrado = [ i ** 2 for i in odd_list] # En la lista cuadrado se deja el cuadrado del numero dado en su posicion respectiva


print(cuadrado)

# break and continue 

for i in range(10):

    if i == 5:
        break # rompe el bucle y termina el recorrido

    print(i)

for i in range(10):

    if i == 5:
        continue # salta el bucle en este momento pero continua ejecutandose la intruccion 

    print(i)