
# Ahora veremos el siguiente widget que es frame 

# Funciona para dentro del contenedor podamos representar frames o contenedores 

import tkinter as tk


# root = tk.Tk()
# root.geometry("500x200")
# root.title("Prueba de Conceptos Frame")
#                                     #Borde en px
# frame1 = tk.Frame(root, bg="blue")
# frame1.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=100, height=100) # No se muestra hasta que se inserte un label


# label1 = tk.Label(frame1, bg="green", text="Hola soy Arley")
# label1.pack(fill=tk.X)


# # Otro WIdeget es Canvas

# canvas1 = tk.Canvas(root,width=200, height=200, bg="white")
# canvas1.pack()
#                             #Radio #Distancia
# ovalo = canvas1.create_oval(50,50,150,150,fill= "red")
# rectangulo = canvas1.create_rectangle(100,100,150,150,fill= "green")
# linea = canvas1.create_line(150,150,20,20, fill="black" , width=20)



#root.mainloop()


#--------------------- RECORDAR CAMBIAR LA CONFIGURACION DEL PICOM Y BSPWN COMO EL TUTORIAL DE S4VITAR ------------------------------

# Creacion de la barra de un menu
from tkinter import messagebox

root2 = tk.Tk()
root2.title("barra del menu")
root2.geometry("500x200")

def hablar():
                       #Ventana #Texto
    messagebox.showinfo("Menu", "Se ha tensado la cosa")

barra_menu = tk.Menu(root2)
root2.config(menu=barra_menu) # Configuracion de la ventana root para la eleccion de la barra del menu

                            # Quitar la fragmentacion del menu
menu1 = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Menu", menu=menu1) # Con esta funcion te sirve para añadir el menu a la barra de menu

menu1.add_command(label="Opcion1", command=hablar) # Añadir opciones al menu 
menu1.add_command(label="Opcion2")

# Para la incorporacion de cuadros de dialogo esta lo siguiente





root2.mainloop()