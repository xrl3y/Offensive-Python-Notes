
# Se van a aprender a operar y leer archivos 

# vamos a crear un archivo exmaple.txt("Hola mundo")

f = open("example.txt","a") # creacion de un archivo con permisos de escritura write, no se guarada lo escrito sino que se borra para iniciar un archuvo nuevo


# r - Lectura 
# a - Escritura con incorporacion, sin perdida de datos 


f.write("Hola mundo") # Para escribir lo que queramos en nuestro archivo dado

# El archivo queda abierto, asi que lo mas conveniente es que cerremos el archivo de la siguiente manera
f.close()

f.write("Hasta luego")


# Otra manera de instanciar esto puede ser lo siguiente:

with open("example.txt","w") as f:
    f.write("HOLA mundo ")   # De esta forma python se encarga de cerrar el archivo de forma automatica en cara a posibles errores que se asocien en el futuro 


# Otra manera para realizar la lectura de archivos puede ser de la siguiente forma

with open("/etc/hosts","r") as f:
    file_content = f.read()


print(file_content) # Se guarda en una variable para despues imprimirla


# si queremos iterar linea por linea podremos hacer lo siguiente

with open("/etc/hosts","r") as f: # De esta forma no se carga el archivo en memoria 
    for line in f:             
        print(line.strip)

# Para procesamiento de imagenes se puede con:

# Copiar el archivo subido a una nueva ubicación
with open("/mnt/data/image.png", "rb") as f_in, open("/mnt/data/copied_image.png", "wb") as f_out:
    file_content = f_in.read()
    f_out.write(file_content)

print("El archivo se ha copiado correctamente como 'copied_image.png'")



