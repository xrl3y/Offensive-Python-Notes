
# Creacion del primer proyecto de practica, editor de texto 

import tkinter as tk

                    #explorador #mensajes
from tkinter import filedialog, messagebox

class SimpleTextEditor():

    def __init__(self, root):

        self.root = root # recibe la venta de root como variable
        self.text_area = tk.Text(self.root) # Definimos la creacion de un metodo de tkinter de text para poner el imput en nuestra ventana
        self.text_area.pack(fill=tk.BOTH, expand=1)
        self.current_open_file = ''
    
    def quit_confirm(self):

        if messagebox.askokcancel("Salir","Estas Seguro que quieres salir ?"):
            self.root.destroy()
    
    def open_confirm(self):
        file_name = filedialog.askopenfilename()

        if file_name:
            self.text_area.delete("1.0", tk.END) # Cantidad de texto que se quiere borrar antes de insertar el nuevo texto
            with open(file_name, 'r') as file:
                self.text_area.insert("1.0", file.read())

            self.current_open_file = file_name
    def new_file(self):
        self.text_area.delete("1.0", tk.END)
        self.current_open_file=''
    
    def safe_file(self):

        if not self.current_open_file:
            self.current_open_file=filedialog.asksaveasfilename()
        
        with open(self.current_open_file,'w') as file:
            file.write(self.text_area.get("1.0",tk.END))

 

root = tk.Tk()
root.geometry("700x500")

editor = SimpleTextEditor(root)

menu_bar = tk.Menu(root)

menu_options = tk.Menu(menu_bar, tearoff=0)

menu_options.add_command(label="Nuevo", command=editor.new_file)
menu_options.add_command(label="Abrir", command=editor.open_confirm)
menu_options.add_command(label="Guardar", command=editor.safe_file)
menu_options.add_command(label="Salir", command=editor.quit_confirm)


root.config(menu=menu_bar)
menu_bar.add_cascade(label="Archivo", menu=menu_options)


root.mainloop()

