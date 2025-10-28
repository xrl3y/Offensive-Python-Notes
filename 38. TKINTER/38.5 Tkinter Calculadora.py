
# Creation of an a calculator with tkinter

import tkinter as tk

root = tk.Tk() # mainly window
root.title("Calculator")
root.resizable(False, False)
root.attributes('-alpha', 1) 


# root.wm_attributes('-transparentcolor', 'white') translucides


# 🔹 Cambiar color de fondo
root.configure(bg="#ddf3ff")  # Color oscuro moderno



class calculator:
    def __init__(self, root):

        self.root = root # mainly window
        self.display = tk.Entry(
                    self.root,
                    width=15,
                    font=("Verdana", 18, "bold"),  # Fuente más moderna y legible
                    bd=5,  # Bordes más pronunciados para un mejor efecto visual
                    relief="ridge",  # Efecto 3D sutil
                    insertwidth=2,  # Hace que el cursor sea más visible
                    bg="#009ef9",  # Color de fondo atractivo (puedes probar con tonos más oscuros)
                    fg="white",  # Texto en blanco para buen contraste
                    insertbackground="white",  # Cursor en blanco para mejor visibilidad
                    justify="right",  # Alinea los números a la derecha
                    highlightthickness=3,  # Borde extra alrededor del widget
                    highlightbackground="#0078d7",  # Color del borde cuando no está seleccionado
                    highlightcolor="#00c3ff"  # Borde iluminado al seleccionar
                )

        self.display.grid(row=0, column=0, columnspan=4) # Location of the display, u can use columspan to determinate the lenght of de spaces 
        self.op_verification = False
        self.current = ''
        self.op = ''
        self.total = ''


        # List of the buttons that u can see in the calculator

        # Location with grid method 

        row = 1
        col = 0



        buttons = [ 

            "7","8","9","/",
            "4","5","6","*",
            "1","2","3","-",
            "C","0",".","+",
            "="

        ]

        for button in buttons:

            #Call the buil button method

            self.build_button(button, row, col)

            col += 1

            if col > 3:
                col = 0
                row += 1

        self.root.bind("<Key>", self.key_press)

    def key_press(self, event):
        key = event.char

        if key == "\r":
            self.calculate()
            return
        elif key == "\x08":
            self.clear_display()
            return
        elif key == "\x1b":
            self.root.quit()
            return
        
        self.click(key)

    
    def clear_display(self):
        self.display.delete(0, tk.END)
        self.op=''
        self.op_verification=False
        self.total=0
        self.current=''

    def calculate(self):
        
        if self.current and self.op:

            if self.op == "/":

                self.total /= float(self.current)

            if self.op == "*":

                self.total *= float(self.current)

            if self.op == "+":

                self.total += float(self.current)

            if self.op == "-":

                self.total -= float(self.current)

        self.display.delete(0,tk.END)
        self.display.insert(tk.END, round(self.total,3))



    def click(self, key):
        if self.op_verification:
            self.op_verification = False

        self.display.insert(tk.END, key)

        if key in "1234567890" or key ==".":
            self.current += key # Son strings asi que se añade a la lista del numero como string
        else:
            if self.current:
                if not self.op:
                    self.total = float(self.current)
                    
            self.current = ''
            self.op_verification = True
            self.op = key 
            




    def build_button(self, button, rows , cols):

        if button == "C":
                b = tk.Button(
                    self.root,
                    text=button,
                    width=8,  
                    bd=3,  # Borde ligeramente resaltado
                    relief="ridge",  # Agrega un efecto 3D sutil
                    font=("Arial",9,"bold"),  # Fuente moderna y legible
                    bg="#006d93",  # Fondo oscuro para un look elegante
                    fg="white",  # Texto en color blanco para buen contraste
                    activebackground="#555",  # Cambio de color al presionar
                    activeforeground="white",  # Mantiene el texto blanco en hover
                    cursor="hand2",  # Cambia el cursor a una mano al pasar sobre el botón
                    command= lambda: self.clear_display() # Con lambda se evita que se llame al metodo una vez se tenga que ingresar ahi
                )
        elif button == "=":
            b = tk.Button(
                    self.root,
                    text=button,
                    width=8,  
                    bd=3,  # Borde ligeramente resaltado
                    relief="ridge",  # Agrega un efecto 3D sutil
                    font=("Arial",9,"bold"),  # Fuente moderna y legible
                    bg="#006d93",  # Fondo oscuro para un look elegante
                    fg="white",  # Texto en color blanco para buen contraste
                    activebackground="#555",  # Cambio de color al presionar
                    activeforeground="white",  # Mantiene el texto blanco en hover
                    cursor="hand2",  # Cambia el cursor a una mano al pasar sobre el botón
                    command= lambda: self.calculate() # Con lambda se evita que se llame al metodo una vez se tenga que ingresar ahi
                )
        else:
             
             b = tk.Button(
                    self.root,
                    text=button,
                    width=8,  
                    bd=3,  # Borde ligeramente resaltado
                    font=("Arial",9,"bold"),  # Fuente moderna y legible
                    bg="#b0e2ff",  # Fondo oscuro para un look elegante
                    fg="black",  # Texto en color blanco para buen contraste
                    activebackground="#555",  # Cambio de color al presionar
                    activeforeground="white",  # Mantiene el texto blanco en hover
                    cursor="hand2",  # Cambia el cursor a una mano al pasar sobre el botón
                    command= lambda: self.click(button) # Con lambda se evita que se llame al metodo una vez se tenga que ingresar ahi
                )
        
        
        b.grid(row=rows, column=cols)





my_gui =  calculator(root) # object instance
root.mainloop()