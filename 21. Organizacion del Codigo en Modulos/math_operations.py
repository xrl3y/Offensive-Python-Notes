

# Codigo mas manejable y reutilizable

# Un modulo es un simple archuvo de python que contiene variables, funciones, estructuraas que puedes importar entre archivo y archivo


# Modulo de math operations

def suma(x,y):

    return x+y

def resta(x,y):

    return x-y

def multiplicacion(x,y):

    return x*y

def division(x,y):

    if y == 0:

        raise ValueError("No se puede dividir entre 0")
    else:
        return x/y 
    


