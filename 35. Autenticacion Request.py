
# Formas de Autenticarse mediante el empleo de la libreria request 

import requests 

respuesta = requests.get("https://ejemplo.com", auth=("Usuario","contraseña")) # Autenticacion con credenciales en paneles basicos de autenticacion , panel super basico 

print(respuesta.text)


# Cambios de cookies de session tambien se puede 

ValorCookie = dict(cookies_are='Valor de la cookie')
respuesta = requests.get("https://ejemplo.com", cookies=ValorCookie)

# Otro campo que se puede editar para la subida de arvhivos puede ser "files"


# Se puede evaluar una sesion de la siguiente forma para el guardado de cookies 

s = requests.Session()

# De la siguiente manera podemos preparar una peticion:

from requests import Session, Request

url = 'https://httpbin.org/get'
s = Session()

headers = {'Custom-Header': 'my_custom_header'}
req = Request('GET', url, headers=headers)
prepped = req.prepare()

prepped.headers['Custom-Header'] = 'my_header_changed'
response = s.send(prepped)

print(response.text)


# Historico de urls de redireccionamiento por los que ha pasado un pagina 


url = 'http://github.com'

r = requests.get(url, allow_redirects=False) # No se aplican redirects


print(r.url)

print(r.history) # Se pueden ver todos los dominios por los que se ha pasado y ver un historico 

