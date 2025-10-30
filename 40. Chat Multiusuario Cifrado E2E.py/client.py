
import socket
import threading

def client_program():

    host = 'localhost'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.accept((host,port))

    username = input(f"Introduce tu usuario = ")
    client_socket.sendall(f"{username.encode()} se ha conectado")


if __name__ == '__main__':
    client_program()