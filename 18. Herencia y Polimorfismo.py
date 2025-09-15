# Explicacion de clases padre e hijos referente al uso de la programacion

class Animal:

    def __init__(self,especie,nombre):

        self.especie = especie  
        self.nombre = nombre
    
    def saludo(self):

        pass  # No hace nada y deja documentado   que se tiene que codificar algo aca
        raise NotImplementedError("Las Subclases definidas deben implementar este metodo") # Una condicion de error que le dice al desarrollador lo que se debe implementar a la hora de realizar la programacion

class Gato(Animal): # Clase Gato que hereda de la clase animal

    def hablar(self):

        return f"MIAU"  

class Perro(Animal):

    def hablar(self):

        return f"GUAU"


Animal1 = Gato("Gato Siames", "Firulais")
Animal2 = Perro("Perro Aleman", "Roberto")

# iNSTANCIA PARA MOSTRAR EL ERROR QUE SE DEFINIO EN LA FUNCION SALUDO DE LA CLASE PADRE ANIMAL

# Animal3 = Animal("Rinoceornte","Andres")
# Animal3.saludo()


Animal1.hablar()
Animal2.hablar()



# Defeiniciond e un metodo de Polimorfismo que simplifica las funciones 

def hacer_hablar(objeto): # Un mismo metodo puede comportarse de maneras distintas para una misma clase con diferentes subclases

    print(f"Soy un {objeto.especie} y mi nombre es {objeto.nombre} y digo {objeto.hablar()}") #El objeto que se le pase se debe definir y sus variables a traer deben estar en salida como returns


hacer_hablar(Animal1)
hacer_hablar(Animal2)



class Automovil:

    def __init__(self, marca, modelo):

        self.marca = marca
        self.modelo = modelo

    def describir(self):

        print(f"La Marca es {self.marca} y el modelo es {self.modelo}")

class moto(Automovil):

    def describir(self):
        
        print(f"Moto: Marca: {self.marca}, Modelo: {self.modelo}")

class carro(Automovil):

    def describir(self):
        
        print(f"Carro: Marca: {self.marca}, Modelo: {self.modelo}")


def descripcion_Automovil(objeto): # Concepto de polimorfismo, entrando a la funciones especificas dadas de cada de una de las subclases 

    objeto.describir()

Automovil1 = carro("Toyota", "Corola")
Automovil2 = moto("Honda","CBR")


descripcion_Automovil(Automovil1)
descripcion_Automovil(Automovil2)




class Dispositivo:

    def __init__(self, modelo):

        self.modelo = modelo 

    def escanear_vulnerabilidades(self):

        raise NotImplementedError("Este metodo debe de ser definido para el resto de subclases existentes")


class Ordenador(Dispositivo): 

    def escanear_vulnerabilidades(self):

        return f"[+] Analisis de Vulnearabilidades Concluido, Actualizacion de software necesaria, Multiples desactuañizaciones de software Detectadas"

class Router(Dispositivo): 

    def escanear_vulnerabilidades(self):

        return f"[+] Analisis de Vulnearabilidades Concluido: Multiples puertos criticos detectados como abiertos, es recomendable cerrar estos puertos"            

class TelefonoMovil(Dispositivo): 

    def escanear_vulnerabilidades(self):

        return f"[+] Analisis de Vulnearabilidades Concluido: Apps detectadas, Multiples aplicaciones detectadas con permisos excesivos"


def Escanear_vulnerabilidades(objeto):

    print(objeto.escanear_vulnerabilidades())

Dispositivo1 = Ordenador("DELL XPS") 
Dispositivo2 = Router("INTEL")
Dispositivo3 = TelefonoMovil("POCO C3 PRO")


Escanear_vulnerabilidades(Dispositivo1)
Escanear_vulnerabilidades(Dispositivo2)
Escanear_vulnerabilidades(Dispositivo3)

# Consideraciones dispuestas debido al uso de  Contructores en cada funcion 

class A:

    def __init__(self):
        print("Inicializando A")


class B(A): # Sobre incripcion del constructor asi que prevalece el constructor del cual se sobrescribe
    def __init__(self):
        print("Inicializando B")

class C(A):
    def __init__(self):
        print("Inicializando C") 
        super().__init__() # Como tenemor el super init, quiere decir que le damos mas importancia al constructor de la clase padre que al de la clase especificada

b = B() # Este tendria como prioridad el contructor de la clase B
c=C() 


# Otra instancia utilizando funcionalidades de uso de super podria ser la siguiente definiendo metodos en la super clase y que se dieran en la subclase definiendo otros modelos de constructores

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludo(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años"

class Empleado(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self.salario = salario

    def saludo(self):
        return f"{super().saludo()}, y cobro {self.salario} euros brutos anuales"

persona = Empleado("Alicia", 23, 35000)
print(persona.saludo())

