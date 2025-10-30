
# Se debe represntar que clientes ingresan y que clientes salen del chat multiusuario 

# Recurso que va estar constante en escucha para conexiones entrantes

import socket # Conexiones 
import threading # Hilos de conexiones multiples 


def client_thread(client_socket, clients, usernames):

    username = client_socket.recv(1024).decode() # Recoger la informacion del cliente 
    usernames[client_socket] = username

def server_program():


    host = 'localhost'
    port = 12345

    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1) # Time wait del tiempo de espera 
    server_socket.bind((host,port))
    server_socket.listen()

    print(f"[*] El servidor esta en escucha de conexiones entrantes")


    clients = []
    usernames = []

    while  True:

        client_socket, adress = server_socket.accept() # Aceptacion del socket del cliente
        clients.append(client_socket) 

        print(f"se ha conectado un nuevo cliente, {adress}")

        thread = threading.Thread(target=client_thread, args=(client_socket, clients, usernames))
        thread.daemon = True
        thread.start()

    server_socket.close()


if __name__ == 'main':
    server_program()