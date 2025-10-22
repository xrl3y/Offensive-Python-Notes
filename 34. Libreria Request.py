
import requests

respuesta =requests.get("https://google.es") # Genera una peticion a un dominio dado

Codigo_de_estado = respuesta.status_code # Almacena el codigo de estado de una peticion 

print(Codigo_de_estado)

print(respuesta.text) # Con esto puedes ver el codigo que manda la pagina por detras

with open("Index.html","w") as f:
 f.write(respuesta.txt) # Con esto creamos un archivo html que guarde el contenido de la respuesta de google  


 # De la siguiente manera podemos enviar y modificar los datos a uana url dada

 values = {'key1':'value1', 'key2':'value2', 'key3':'value3'} # Definimos un diccionario de envio de datos

 respuesta = requests.get("https://httpbin.org/get", params=values) # Se define la direccion de url de destino y los parametros que se vana  enviar , en este caso el diccionario de values

print(respuesta.url) # De esta manera vemos lo que se esta tramitando en la url
print(respuesta.text) # De esta manera vemos lo que se esta tramitando en el codigo de la pagina

# De esta manera se hace el envio de los datos a traves de post

payload = {'key1':'value1', 'key2':'value2', 'key3':'value3'} 
respuesta = requests.post("https://httpbin.org/post", params=payload)

print(respuesta.text)

# Tambien se pueden cambiar los headers de la misma forma headers 

# Limitacion de tiempo de respuesta de una pagina web 

try:    
    respuesta = requests.get("https://google.es", timeout=8) # tiempo de 8 segundos 
    respuesta.raise_for_status()

except requests.Timeout:
   print(f"La peticion ha excedido el limite de espera")

except requests.HTTPError:
   
   print(f"Error http: {requests.HTTPError}")

except requests.RequestException as err:
   
   print(f"Ha ocurrido el siguient error: {err}")

   
   # Para convertir los datos a una respuesta de json se puede usar la funcion de 

respuesta.json() 