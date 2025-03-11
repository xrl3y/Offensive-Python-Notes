

# La cuestion al definir variables de string es que se ubiquen con dobles comillas para resaltar ese tipo de dato como una cadena 

# Si las dobles comillas no se colocan por ejemplo en un numero, este se tomara como dato entero 
ip_address = "192.168.20.16"

print(ip_address)
print(type(ip_address))

# Para convertir los tipos de datos lo podemos hacer de la siguiente forma

number = float(4)

print(type(number))


# Listas: Estrutura de Datos de Alamacenamiento en contenedores 

my_ports = [] #Creacion de la lista
my_ports.append(22) #Agregar elementos
my_ports.append(80)
my_ports.append(443)

print(my_ports[0])

# Para recorrer una lista lo podremos hacer de la siguiente forma utilizando los bucles, escalable con un numero infinito de datos en los elementos de la lista


for port in my_ports:
    print(port)

# Para dar salida de strings con el tipo de puerto podemos hacer lo siguiente:

for port in my_ports:
    print("puerto: " + str(port))

# Otra forma para hacer ese bucle podria ser de la siguiente manera con la intruccion de formatear

for port in my_ports:
    print(f"puerto: {port}")


# Para ver cuantos datos hay en el bucle se podria hacer de la siguiente forma:

print(f"\n [+] la lista tiene un total de {len(my_ports)} elementos")

# Para añadir mas de un solo elemento podmeos utilizar la siguiente forma con el comando extend de la siguiente manera

my_ports.extend([22,33,44,55,66])

my_ports += [101,102]

for port in my_ports:
    print(f"puerto: {port}")

# Funcion para ordenar datos de numeros

my_ports=sorted(my_ports)

print(f"\n la lista ordenada de puertos es {[my_ports]}")

# La forma de eliminar datos de una lista puede ser de la siguiente forma

del my_ports[0]

# Mostrar los elementos de una lista 

print(my_ports[:6])

# Mostrar un rango de elementos en especifico

print(my_ports[2:4])

# Para mostrar el rango de elementos despues de dado una variale lo podemos hacer de la siguente forma

print(my_ports[3:])

# Para agregar datos tambien se podria hacer 

my_ports.insert(2,9) # El primer numero estable la posicion y el segundo numero el valor que se va a insertar

print(my_ports)

# Para eliminar los ultimos datos de una lista se puede usar la siguiente funcion 

my_ports.pop

# Para conocer la posicion de un elemento podemos hacer lo siguiente: 

print(my_ports.index(80))

# Cantidad de veces que un elemento esta en una lista 

print(my_ports.count(22))

# Para quitar las repeticiones de numeros de una lista se podria hacer de la siguiente forma:

set(my_ports)