
import tkinter as tk

root = tk.Tk() # Se crea la ventana principal de la app
root.title("Mi Primera Aplicacion") # Titulo de la Ventana
root.geometry("500x400") # Medidas de la Ventana principal


# Los label son widgets(mostrar info o interactuar) que permiten mostrar texto o imagen

                #Hay que pasarle la ventana principal
#labelejemplo = tk.Label(root, text="Hola mundo",bg="green") # Aqui solamente se define
#labelejemplo.pack(side="left",fill=tk.Y) # Con esta funcion se puede presentar el label que queremos, tambien se puede con grid() , place(), el fill = tk.X es para presentar el label en todo el eje de X

#Side es para elegir el lado de pegado
#Fill es para hasta donde se va a llenar


#Funciones 

def accion_de_boton():
    print(f"Se ha presionado el boton")


# Botones 


#BotonPrincipal = tk.Button(root, text="Click", border=5, command=accion_de_boton,bg="red") # Con la opcion de # Command puedo elegir la funcion que quiero desplegar
#BotonPrincipal.pack()




# Metodo grid 

label2 = tk.Label(root, text="Ejemplo grid", bg="green")
label2.grid(row=0, column=0) # Se indican filas y columnas , para usar este metodo de posicionamiento, no se pueden usar los otros al tiempo
label3 = tk.Label(root, text="Ejemplo otro", bg="red")
label3.grid(row=2,column=1,columnspan=3,)

# rowspan=,columnspan= , sirven para entablillar cuantos espacios de casillas queremos ocupar 

root.mainloop() # Para ver la ventana de la aplicacion y se crea el loop de la aplicacion 