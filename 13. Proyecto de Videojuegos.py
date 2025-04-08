
tope = 923

# Generos

juegos = ["Super Mario Bros", "Zelda: Breath of the Wild", "Cyberpunk 2077", "Final Fantasy VII"]

# Para expresar los generos lo haremos con funciones de diccionarios
generos = {

    "Super Mario Bros": "Aventura",
    "Zelda: Breath of the Wild": "Aventura",
    "Cyberpunk 2077": "Rol",
    "Final Fantasy VII": "Rol"

}


# Ventas y STOCK 


Ventas_Stock = {

#Respresentadno como tuplas

    "Super Mario Bros": (400,200),
    "Zelda: Breath of the Wild": (600,20),
    "Cyberpunk 2077": (60,120),
    "Final Fantasy VII": (924,3)
}

# Clientes 

# Clientes
clientes = {
    "Super Mario Bros": {"Marcelo", "Hackermate", "Hackavis", "Securiters", "Lobotec"},
    "Zelda: Breath of the Wild": {"Hackermate", "Hackavis", "Lucía", "Manolo", "Pepe"},
    "Cyberpunk 2077": {"Hackermate", "Lobotec", "Pepe", "Raquel", "Albert"},
    "Final Fantasy VII": {"Lucía", "Manolo", "Pepe", "Securiters", "Patricia", "Moisés"}
}




#Sumario 

def sumario(juego):

    print(f"\n[i] Resumen del Juego {juego} \n")
    print(f"\t[+] Genero del Juego: {generos[juego]}\n")
    print(f"\t[+] Total de Ventas para este juego: {Ventas_Stock[juego][0]}")
    print(f"\t[+] Total de Stock para este juego: {Ventas_Stock[juego][1]}")
    print(f"\t[+] Clientes del Juego : {', '.join(clientes[juego])}") 
    # La funcion de ', '.join() , funciona para limpiar la salida de los conjuntos y que queden separados con una coma sin que como impresion salgan las llaves de los conjutnos dadas 

def Ventas_Totales(juego):
    Ventas=0
    for juego in juegos:
        
        if Ventas_Stock[juego][0] > tope:
            Ventas+=Ventas_Stock[juego][0]
    
    return(Ventas)

# Funcion para iterar sobre cada uno de los juegos en la lista Juegos

Ventas=0

for juego in juegos:
    

    if Ventas_Stock[juego][0] > tope: # Condicion para mostrar solo los juegos con ventas mayores a 500 u 
        ventas=Ventas_Totales(Ventas_Stock[juego][0])
        sumario(juego)
    else:
        ventas = 0
        
if ventas == 0:
    print(f"\n\n No hay Juegos con ventas Mayores a {tope}")

print(f"\n\n\t:.:. VENTAS TOTALES .:.:")
print(f"\n Las ventas Totales de todos los juegos fue de: {ventas}\n")

