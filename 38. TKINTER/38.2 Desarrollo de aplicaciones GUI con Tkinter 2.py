
# Aislado a esto metodos tenemos otra variante con el metodo de place con posiciones absolutas y relativas de la ventana 


import tkinter as tk

root = tk.Tk()
root.geometry("500x400")

root.title("Ejemplo Place")

# Metodo de posicionamiento place
label1 = tk.Label(root, text="Pobando Metodo Place", bg="green")

label2 = tk.Label(root, text="Place con medidas Relativas", bg="green")

# Se referencian coordenadas de pocicionamiento
# Los posicionamientos son absolutos y se miden las unidades con respecto al eje 

label1.place(x=20,y=20)

label2.place(relx=0.5, rely=0.5, anchor=tk.CENTER) # Se toma como referencia la unidad osea 1 para dar referencia al totalidad del contenedor # Se basa en que porcentaje de la ventana se debe ocupar

# Para centrar se usa el anchor=tk.center

def get_data():

    Nombre = entry1.get("1.0",tk.END) # Funcion para la entrada de datos a traves de un widget, get solo funciona para entry , con text tienes que decirle desde donde hasta donde quieres almacenar texto
    # 1.0 siginifa hasta la 1 primera linea caracter 0 , es decir todo el imput 
    print(f"Hola mi nombre es {Nombre}")

  

# WIDGET ENTRY 

# Almacenar datos de entrada del usuario

entry1 = tk.Text(root) # Existen las funciones tanto ENTRY para una sola linea y TEXT para varias lineas de input
entry1.place(relx=0.8, rely=0.8, anchor=tk.CENTER, relwidth=0.2,  relheight=0.1)

boton1= tk.Button(root,text= "Nombre",  command=get_data)
boton1.place(relx=0.9, rely=0.9, anchor=tk.CENTER)

root.mainloop()

