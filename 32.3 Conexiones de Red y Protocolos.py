import threading
import socket
import pdb


class ClientThread(threading.Thread):
    def __init__(self, client_sock, client_addr):
        super().__init__()
        self.client_sock = client_sock
        self.client_addr = client_addr

        print(f"\n[+] Nuevo cliente conectado: {client_addr}")

    def run(self):
        message = ''

        while True:
            data = self.client_sock.recv(1024)
            message = data.decode()

            pdb.set_trace() # Break Point


            if message.strip() == 'bye': # Con la funcion de strip se le quita el espaciado y salto de linea a la cadena de string 
                break

            print(f"\n[+] Mensaje enviado por el cliente: {message.strip()}")
            self.client_sock.send(data)

        
        print(f"El cliente {self.client_addr} se ha desconectado") # desconcexion del cliente 

        self.client_sock.close()

HOST = 'localhost'
PORT = 1234

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # TIME_WAIT
    server_socket.bind((HOST, PORT))

    print("\n[+] En espera de conexiones entrantes...")

    while True:
        server_socket.listen()
        client_sock, client_addr = server_socket.accept()
        new_thread = ClientThread(client_sock, client_addr)
        new_thread.start() # run()
