
# Proyecto de Creacion de una biblioteca, herencia, polimorfismo, etc


class libro:

    def __init__(self,id, autor, titulo, disponibilidad = True , es_para_niños= False):

        self.id = id
        self.autor = autor
        self.titulo = titulo
        self.disponibilidad = disponibilidad # De inicio entonces el libro no estaria prestado
        self.es_para_niños = es_para_niños

    def __str__(self):

        return f"\n ID: {self.id} \n AUTOR: {self.autor} \n NOMBRE: {self.titulo} \n DISPONIBILIDAD: {self.disponibilidad} \n "
        


class biblioteca:

    def __init__(self):
        self.libros = [] # Diccionario de CLAVE : VALOR = {1: Print(Libro1), 2: Print(Libro2) } / Modificados para que funciones como una lista

    def agregar_libro(self, libro):

        if libro.id not in self.libros: # Se busca el id de la lista si no esta se incorpora
            self.libros.append(libro)
            self.libros.sort(key=lambda libro: libro.id) # Forma de ordenar una lista de objetos por el parametro ID
            
        else:
            print(f"\n [!] No es Posible agregar el libro con id {libro.id}")

    def mostrar_libros(self):

        print("\n \t :. LISTA DE LIBROS .: \n")
        
        for i, libro in enumerate(self.libros):
            print(f"\n \t [--{i+1}--] \n {self.libros[i]}")

    def mostrar_libros_disponibles(self):

        print("\n \t :. LISTA DE LIBROS DISPONIBLES  .: \n")
        
        for i, libro in enumerate(self.libros):
            if libro.disponibilidad == True:
                print(f"\n \t [--{i+1}--] \n {self.libros[i]}")
            
            else: 
                print(f"\n \t [--{i+1}--] NO SE ENCUENTRA DISPONIBLE: \n {self.libros[i]}")

    def prestar_libro(self, id):

        id -=1
        try:
                if  self.libros[id].disponibilidad == True:

                    print(f"\n \t El libro siguiente Libro fue Prestado Correctamente: \n {self.libros[id]}")
                    
                    self.libros[id].disponibilidad = False
                
            
                else:

                    print(f"\n \t [!] El libro no se encuentra Disponible \n")     

        except:

            print(f"\n \t [!] El id numero {id+1} del Libro No se Encuentra Registrado en el Sistema \n ")

    
    def Es_para_niños(self, id):

        id -=1
        try:
             if self.libros[id]:
                if self.libros[id].es_para_niños == True:
                    print(f"\n [+] El libro {id+1} Con nombre {self.libros[id].titulo} Es para Niños")
                
                else:
                    print(f"\n [+] El libro {id+1} Con nombre {self.libros[id].titulo} NOO es para Niños")

        except:

            print(f"\n \t [!] El id numero {id+1} del Libro No se Encuentra Registrado en el Sistema \n ")
             
        
if __name__  == '__main__': # Se usa para sentenciar el inicio del programa                   

    libro1 = libro(1, "Marcelo Vazquez", "¿Como ser un Lammer?",False)
    libro2 = libro(2,"Pepito Manolete","Aprende a colorear desde 0",True)
    libro3 = libro(3, "Arley GARZON", "Tecnicas de Hacking",True)


    
    biblioteca1 = biblioteca()

    biblioteca1.agregar_libro(libro3)
    biblioteca1.agregar_libro(libro1)
    biblioteca1.agregar_libro(libro2)

    biblioteca1.prestar_libro(1)

    biblioteca1.Es_para_niños(1)

    biblioteca1.mostrar_libros_disponi  