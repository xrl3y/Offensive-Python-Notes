

# Una propiedad @property, tiene la capacidad de alterar una funcion o una clase, se puede decorar para  que realice mas operaciones

# Funcion de orden superior para crear un decorador

def mi_decorador(funcion): # Funcion de orden superior
    def envoltura():

        print("estoy saludando antes de la funcion")

        funcion()

        print("estoy saludando despues de llamar a la envoltura de la funcion")

    return envoltura

@mi_decorador
def saludo():

    print(f"Hola estoy saludando dentro de la funcion")  

saludo()

# @property # Getters y Setters

class Persona:

    def __init__(self, nombre, edad):

        self._nombre = nombre
        self._edad = edad # Variable protegidas

    @property
    def edad(self):

        return self._edad # Metodo para obtener la edad con una funcion get
    @edad.setter    
    def edad(self,valor):
        if valor > 0:
            self._edad=valor
        else:
            raise ValueError("[!] La Edad no puede ser un numero negativo")

Persona1 = Persona("Manolo",23)

 
 # Setters y Getters

 # Siempre para asignar un valor a un atributo, hablamos de set o settear
 # Siempre para obtener o traer un valor o un atributo, hablamos de gettear

Persona1.edad = 2
print(Persona1.edad)


# Otro Ejemplo de jugar con getters y Setters

import time # Libreria para meter tiempo

time.sleep(5)

def cronometro(funcion):
    def envoltura():
        inicio = time.time()
        funcion()
        final = time.time()

        print(f"Tiempo total transcurrido de la funcion {funcion.__name__}: {final - inicio}")

    return envoltura
        



@cronometro
def pausa_corta():

    time.sleep(0)

@cronometro
def pausa_larga():

    time.sleep(0)

pausa_corta()
pausa_larga()


# Nomenclatura de python:

# *args = Define todos los valores dados individuales en una tupla
# **kwargs = Define todos los valores en pares de clave valor como si fuera un diccionario


# Ejemplo de las nomenclatura 


def suma(*args):

    return sum(args) # Sum es una funcion ya establecidad en python que suma todos los elemntos iterables

print(suma(1,2,3,4)) # Los elementos tienen que ser enviados desde la llamada de la funcion 

# **kwargs

def presentacion(**kwargs):

    return kwargs


print(presentacion(nombre = "Marcelo", edad = 21 , Nacionalidad = "Colombiana", Empleo = "Hacker"))


