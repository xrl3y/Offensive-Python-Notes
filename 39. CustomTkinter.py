
import customtkinter as ctk  # Importar la biblioteca

# Configuración global de la apariencia
ctk.set_appearance_mode("Dark")  # Modos: "Dark", "Light", "System"
ctk.set_default_color_theme("blue")  # Temas: "blue", "green", "dark-blue"

# Crear la ventana principal
root = ctk.CTk()
root.geometry("500x400")
root.title("CustomTkinter Example")

# Etiqueta
label = ctk.CTkLabel(root, text="¡Bienvenido a CustomTkinter!", font=("Arial", 16))
label.pack(pady=10)

# Entrada de texto
entry = ctk.CTkEntry(root, placeholder_text="Escribe algo...")
entry.pack(pady=10)

# Botón de acción
def on_button_click():
    label.configure(text=f"Texto: {entry.get()}")

button = ctk.CTkButton(root, text="Mostrar texto", command=on_button_click)
button.pack(pady=10)

# Slider
slider = ctk.CTkSlider(root, from_=0, to=100)
slider.pack(pady=10)

# Checkbox
checkbox = ctk.CTkCheckBox(root, text="Activar opción")
checkbox.pack(pady=10)

# Switch
toggle = ctk.CTkSwitch(root, text="Modo activado")
toggle.pack(pady=10)

# Menú desplegable
combobox = ctk.CTkComboBox(root, values=["Opción 1", "Opción 2", "Opción 3"])
combobox.pack(pady=10)

# Iniciar la aplicación
root.mainloop()
