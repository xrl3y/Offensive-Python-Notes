
# Es otra alternativa a la ibreria request, destinadas al mismo tramite de peticiones 

# La complejidad de uso , esta libreria es mucho mas profunda y a bajo nivel de la maquina con mayor complejidad 


import urllib3

http = urllib3.PoolManager # Controlador de conexiones


data = {"atribututo":"valor"} # The same passw : value 
respuesta = http.request('GET','https://ejemplo.com/get', body=data) 

print(respuesta.data.decode())

# Para post lo mismo pero con el cambio de variables 


# Tambien se puede modificar el conten type y demas cabeceras que se pueden realizar 

# headers = {'NuevaCabecera': 'SeTensa'}


# Se pueden controlar las redirecciones con redirect = False si no quiero mostrar redireccionamientos  y con True Redirige y se puede ver con un .status 


# Si tratamos con un certificados de autofirmado ssl, en maquinas o proyectos de ctfs, si queremos entrar y no carga bien la pagina, debemos colocar el certificado autofirmado y su forma es modificando los valores del controlador de conexiones 


