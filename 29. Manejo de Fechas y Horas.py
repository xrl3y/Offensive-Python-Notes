
# Se emplea el uso de la libreria datetime 

import datetime

ahora = datetime.datetime.now() # Se deriva del formato y de los conceptos de poo

print(ahora)


fecha = datetime.date(2023,6,14) # creacion de un formato especifico de fecha 

hora = datetime.time(14,15,15) # formato de hora 

FechaHora = datetime.datetime(2023,6,12,14,15,15) # Formato de fecha y hora ambos incluidos

Nuevoahora = datetime.datetime.now()

año = ahora.year
mes = ahora.month
dia = ahora.day
horas = ahora.hour
minutos = ahora.minute
segundos = ahora.second

print(f"Año: {año}, mes: {mes}, día: {dia}, {horas}:{minutos}:{segundos}")
