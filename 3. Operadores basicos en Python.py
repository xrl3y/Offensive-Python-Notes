

# Demostracion de calculos con diferentes tipos de variables

first_number = 6
second_number = 8.54444 

result = first_number + second_number

print(result)

# Para redondear un numero flotante se podria hacer lo siguiente:

print(round(result,2)) # la segunda posicion clasifica la idea de cuantos decimales se establecen despues del punto decimal 

# La potencia se establece como **

# De la siguiente manera puedes establecer un formato a los datos que se asignan eventualmente de la siguiente manera

print("{:,}".format(result).replace(",",".")) # la funcion de replace hace que el caracter de (,) se remplace por otro caratcter a nuestra conveniencia

# El operador de % es la divicion exacta o el modulo, donde no quedan residuos 


# _____________________________________________________________________________________


# Operadores entre cadenas

first_stdr = "Hola"
second_stdr = "  "
tird_stdr = "Mundo"

result_stdr = first_stdr +  second_stdr +  tird_stdr

print(result_stdr)
print(first_stdr*3)
print(first_stdr[0]*8)

# Operaciones entre listas

firs_elements = [1,3,5,7,9]
second_elements = [2,4,6,8,10]

result_elements = firs_elements + second_elements

print(result_elements)
print(sorted(result_elements))

result_elements = zip(firs_elements,second_elements) # la funcion zip se reconoce por asignar duplas a conjuntos de listas que se entrelazan entre si 

for element in result_elements: # iteracion de elementos en las lisas dadas
    print(element)

# Para operaciones entre esas tuplas se puede hacer lo siguiente:

suma_tuplas = map(sum, zip(firs_elements,second_elements))

for element in suma_tuplas:
    print(element)