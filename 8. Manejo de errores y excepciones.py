
# La idea es de probar una accion y en caso de que pase algo, o da un error, se pueden manejar las ecepciones y dar control a las salidas

# Ejemplo 1

# Una biblioteca de manejo y muestra de errores podria ser la siguiente:
 

try: 
    num = 5/2

except ZeroDivisionError: # Ejemplo de ecepcion mencionada de division entre 0

    print("No se puede dividir un numero entre 0 ")

except TypeError: # Solo es posible la division entre numeros

    print("Solo es posible la division entre numeros") # Para que esto funcione se debe instalar la libreria ppwntools


else:

    print(f" La division de los 2 numeros da como resultado = {num}")    

finally: # Bloque de codigo que siempre se va a ejecutar en las exepciones

    print("Esto siempre se va a ejecutar ")

# Tambien se pueden lanzar excepciones sin que necesariamente necesiten existir errores

n = -5

if n < 0:
    raise Exception("No se puede utilizar numero negativos") # Linea de Traza que simula un error real





