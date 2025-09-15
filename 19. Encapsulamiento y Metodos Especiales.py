
# Es un metodo o estrategia para la restriccion de componentes de un objeto

# Serie de atributos definidos en metodos de construccion


# Definicion de atributos privados y atributos publicos de referencian, seguimiento de convenios a la hora de la elaboracion del area de desarollo



class Ejemplo:

    def __init__(self):

        # Atributo Protegido
        self._atributo_protegido = "Soy un atributo protegido y no deberias poder verme"  #Variable interna con uso protegido, se referencia con una raya baja al inicio del nombre de la variable

        # Atributo Privado

        self.__atributo_privado = "Soy un atributo Privado y no  deberias poder verme" # Se referencia con doble raya baja al inicio del nombre

Ejemplo1 = Ejemplo()

print(Ejemplo1._atributo_protegido)

# print(Ejemplo1.__atributo_privado) # No se podria ejecutar porque el atributo es privado y el objeto no puede acceder

# El convenio para el uso de variables privadas en las clases es el siguiente : _CLASE__VARIABLE PRIVADA

print(Ejemplo1._Ejemplo__atributo_privado) # La referencia se hace inaccesible pero no inexistente



# EJEMPLO DE ENCAPSULAMIENTO

class coche:

    def __init__(self,marca,modelo):

        self.marca = marca
        self.modelo = modelo
        self.__kilometraje = 0 # Atributo Privado 

    def conducir(self, kilometros):
        if kilometros >= 0:
            self.__kilometraje += kilometros
        else:
            print(f"Los kilometros deben ser mayores a cero")

    def mostrar_kilometros(self):

        return f"El coche de la marca {self.marca} del modelo {self.modelo} tiene {self.__kilometraje} kilometraje"

coche1 = coche("Toyota","Coroya")

coche1.conducir(150)

print(coche1.mostrar_kilometros()) 

# Metodos Especiales


class Libro:
    def __init__(self,autor,titulo):

        self.autor = autor
        self.titulo = titulo

    def __str__(self): # Metodo que te permite imprimir informacion que quieras en el objeto deseado

        return f"El libro {self.titulo} es de {self.autor}"
    
    def __eq__(self, Valor_del_segundo_Objeto): # Funcion que te permite realizar la comparacion de 2 objetos

        return self.autor == Valor_del_segundo_Objeto.autor and self.titulo == Valor_del_segundo_Objeto.titulo  # Se realiza la comprobacion de que los atributos de ambos libros son iguales


Libro1 = Libro("Marcelo","Como ser un lammer")
Libro2 = Libro("Marcelo","Como ser un lammer")

print(Libro1)

print(f"Son iguales estos libros -> {Libro1==Libro2}")


class CuentaBancaria:
    def __init__(self, num_cuenta , titular, saldo_inicial =0):

        self.num_cuenta = num_cuenta
        self.titular = titular
        self.__saldo = saldo_inicial

    def depositar_dinero(self, cantidad):

        if cantidad > 0:
            self.__saldo += cantidad
            return self.__saldo
        else:
            print(f"La cantidad indicada tiene que ser mayor que cero")

    def retirar_dinero(self,cantidad):

        if cantidad <= self.__saldo:
                if cantidad > 0:
                    if self.__saldo > 0:
                        self.__saldo -= cantidad
                        return self.__saldo
                    else:
                        print(f"No tiene dinero para retirar")
                else:
                    print(f"La cantidad a retirar debe ser mayor a 0")
        else:
            print(f"La cantidad a retirar exede el saldo existente en la cuenta")

    def mostrar_dinero(self):

        print(f"El dinero actual que tiene en la cuenta numero: {self.num_cuenta} es de : {self.__saldo}")

        


manolo = CuentaBancaria("1726569", "Manolo Vieria",1500)

manolo.depositar_dinero(500)
manolo.retirar_dinero(500)
manolo.mostrar_dinero()


# Otro Ejercicio de aplicacion 

class caja:
    def __init__(self,*items): # Se almacena en una sola variable como si fuera una tupla

        self.items = items
    
    def mostrar_items(self):


        for item in self.items:
            print(f"Los items son {item}")

    def __len__(self):

        return len(self.items)

caja1 = caja("manzana","kiwi","platano","pera","Melecoton") # El total de elementos o atributos que se establezcan se puede guardar en una sola variable con el *variable


caja1.mostrar_items()

print((len(caja1.items)))
print(len(caja1)) # Impresion con el metodo len definido en la longitud de los caracteres


# Para la iteracion un objeto el cual esta modificado como una lista se puede usar el siguiente metodo especial

class Mi_lista:

    def __init__(self):

        self.data = [1,2,3,4,5] # setear por defecto los elemntos con cualquier tipo de dato que se quiera

    def __getitem__(self,index):

        return self.data[index] # Retorna el valor del elemento que se ejecuta en el indice prorporcionado 

        
lista = Mi_lista()
print(lista[2])


# Metodo Especial Call

class Saludo:

    def __init__(self,saludo):

        self.saludo = saludo

    def __call__(self,nombre): # Definicion de un metodo call para llamar a las variables

        return f"{self.saludo} {nombre}"

saludo1 = Saludo("¡Hola ")

print(saludo1("luis!"))