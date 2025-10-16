
# A la hora de explotar servicios de alguna forma se debe entablar la conexion de puertos en servicios tanto por udp como de tcp 

# El socket es un proceso en el cual se pueden comunicar 2 maquinas, descriptores de archivos 


# Con netcat se entablan las conexiones , creando un cliente y simulandolo con una conexion de atacante


# Crearemos una especie de chat, entre servidor y cliente

import socket

# Crear un socket del servidor 


server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # El Af inet es el que acepta la familia de conexiones con ipv4, y el sock stream se solicita a las conexiones tcp 

server_adress = ('localhost',1234) # Se define la direccion del socket

server_socket.bind(server_adress) # Utilidad que dada una direccion te permite ponerte en modo de escucha

# Se va a crear una cola de espera, dado por la conexion de cliente por cliente

server_socket.listen(1) # Se limita el numero de conexiones a 1 a la vez

while True:
    client_socket, client_adress = server_socket.accept() # Primeramente necesitamos el socket del cliente y su direccion asi que de esa forma, primeramente se inicializan estos valores para que la conexion se realice por un puerto aleatorio
    data = client_socket.recv(1024) # se guarda un mensaje del cliente que se almacena en formato de bytes y se almacena en una variable data, se elige 1024 por el tamaño del mensaje pero puede ser cualquier valor 

    print(f"\n \t El mensaje del cliente es : {data.decode()}") # Se tiene que decodear para poder pasar de bytes a string y asi hacer suceptible su lectura en texto claro
    print(f"\n Informacion del cliente : {client_adress}") # Informacion de la conexion que se realiza del servicio del cliente dado

    client_socket.sendall(f"Un saludo amigo \n".encode()) # Con esta funcion lo que se realiza es que la cadena de texto que vamos a enviar se decodea a bytes para poder ser recivida por el cliente y de esa manera que el cliente pueda decodearla

    client_socket.close() # Se cierra la conexion del cliente



# Ahora haremos el script del cliente dado que ya se realizo el script de conexiones dentro del servidor

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_adress = ('localhost', 1234)

client_socket.connect(server_adress) # Se conecta la conexion del cliente hacia el servidor 

try:
    message = "Un saludo amigo"
    client.socket.sendall(message)
    data = client.socker.recv(1024)

finally:
    client.socker.close() # Se realiza para evitar fugas de conexxion y asi cerrar todas las conexiones pertinentes




# Una forma de poder crear y entabablar un socket sin un bucle infinito de while, podria ser la siguiente:

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s : # Asi se cierra solo y no se precede a un bucle infinito de la siguiente forma 
    s.bind(host, port) # Entablas la conexion 
    s.listen(1)
    conn, addres = s.accept() 

    with conn:
        print(f"Se ha concetdo un nuevo cliente: {addr}")
        while true:
            data = conn.recv(1024) # Se realiza el recibo de data de mensaje en bytes 
            break
            conn.sendall(data)


# Se entabla una conexion de socket como el SYN SYNACK ACK