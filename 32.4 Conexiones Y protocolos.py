
# Creacion del script de cliente para que la conexion no se efectue por consola 


import socket

def start_client():

    host = 'localhost'
    port = 1234

    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.connect((host,port))

        while True:
            message = input("\n Introduce tu mensaje = ")
            s.sendall(message.encode())
            
            if message == 'bye':
                break

            data = s.recv(1024)

            print(f"Mensaje de respuesta del servidor = {data.decode}")


start_client()

# Se puede usar para la creacion de chats interactivos entre servidor y cliente