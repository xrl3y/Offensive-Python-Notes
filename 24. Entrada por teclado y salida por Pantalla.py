
# Entrada y salida de datos 

# Los scripts pueden solicitar datos y eso se referencias con los user input


# nombre = input("Cual es tu nombre = ") # Nomenclatura para el ingreso de datos

# print(f"perfecto ahora se que te llamas {nombre}")


while True:

    try:
        edad = int(input("Dime cual es tu edad = "))  # Hay que seleccionar el tipo de dato que esperamos 

        print(f"Perfecto, el otro año vas a cumplir {edad+1}")
        break
    except ValueError:
        print("El dato Ingresado no es correspondiente")

# Para ocultar salidas del output podremos hacer lo siguiente:

from getpass import getpass # Modulo para la definicion 

password = getpass("Introduce tu contraseña = ")

print(f" tu contraseña es = {password}")


