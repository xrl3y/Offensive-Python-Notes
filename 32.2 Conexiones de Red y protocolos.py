
# Jugaremos con otras utilidades utilizando conexxiones de udp

import socket

# Archivo de creacion del server.py

def start_udp_server():

    host = 'localhost'
    port = 1234

    #Udp 

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s: # Asi se realiza para conexiones udp 
        s.blind(host, port)
        print(f"\n Sevidor Udp iniciado en {host} y {port}")

        while True:
            data, addrs = s.recvfrom(1024) # No se necesita conectar al sock sino que de una vez ya se gestiona la data
            print(f" Mensaje enviado por el cliente = {data.decode}")
            print(f"Informacion del cliente = {addrs}")

# Se haria lo mismo para entablar la conexion del cliente, y para conectarse se juega con s.sendto