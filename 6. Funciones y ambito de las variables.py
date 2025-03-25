
# Las funciones son bloques de codigo con intrucciones reutilizables 

def saludo():
    print("\n Hola Mundo")


saludo()


# Funcion con parametros de inicio de variabales 

def saludo1(nombre):
    print(f"Hola {nombre}")

saludo1("xrl3y")

# Funciones de retorno de resultados 

def suma(numero1, numero2):
    return numero1 + numero2

resultado = suma(3,4)

print(f"El resultado es {resultado}")

# ambitos de las variables 

def mi_funcion():
    variable_local = "soy local"
    print(variable_local) # La variable solo existe en la funcion pero no es de ambito global 


mi_funcion()

# De la siguiente forma podemos hacer a una variable global dentro de una funcion

def mi_funcion2():
    global variable_local
    variable_local = "Soy una variable global"
    print(variable_local) # La variable solo existe en la funcion pero no es de ambito global 


mi_funcion2()