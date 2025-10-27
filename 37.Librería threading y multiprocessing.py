
# Los hilos nos permiten ejecutar tareas en paralelo en un proceso 

import threading
import time

def tarea(num_tarea):
    print(f"Iniciando Tarea {num_tarea}")

    time.sleep(2)

    print(f"Finalizando Tarea {num_tarea}")

                #Funcion 
thread1 = threading.Thread(target=tarea, args=(1,))
thread2 = threading.Thread(target=tarea, args=(2,))


thread1.start()
thread2.start() # Iniciado de los hilos

thread1.join()
thread2.join() # Espera a que finalicen los hilos 

print(f"Los hilos han finalizado correctamente")



#tarea(1)
#tarea(2) # Hasta que no finalice la tarea 1 entonces la tarea anterior no va a empezar y para eso es el concepto de hilos



# Otra libreria podria ser multiprocesing

# No comparten memoria ni variables de los hilos, resulta util para el manejo de la cpu 

import multiprocessing

proceso1 = multiprocessing.Process(target=tarea, args=(1,))
proceso2 = multiprocessing.Process(target=tarea, args=(2,))


proceso1.start()
proceso2.start()

proceso1.join()
proceso2.join()
print(f"Los procesos han finalizado exitosamente")


# Ejercicio de hilos ----------------------------------------------------------------------------------------------------

#!/usr/bin/env python3

import requests
import threading
import time

def realizar_peticion(url):
    response = requests.get(url)
    print(f"\n[+] URL [{url}]: {len(response.content)} bytes")

dominios = [
    "https://google.es",
    "https://xvideos.com",
    "https://wikipedia.org",
    "https://yahoo.com"
]

start_time = time.time()

hilos = []
for url in dominios:
    hilo = threading.Thread(target=realizar_peticion, args=(url,))
    hilo.start()
    hilos.append(hilo)

for hilo in hilos:
    hilo.join()

end_time = time.time()

print(f"\n[+] Tiempo total transcurrido: {round(end_time - start_time, 2)} segundos")
