
# Comprendiendo mejor el uso de la secuencia self en los modelos contructores de las clases dadas


class  Persona:

    def __init__(self,nombre,edad): 

        self.nombre = nombre
        self.edad = edad

    def informacion(self):

        print(f"La persona es {self.nombre} y tiene la edad de {self.edad}")   


Persona1 = Persona("Marcelo",27)
 

Persona1.informacion()

# Referencia a Metodos estaticos sin depender de atributos de objetos 

class Calculadora:

    def __init__(self, numero):

        self.numero = numero
        Calculadora.numero = numero
    
    @staticmethod
    def suma(valor):
        return valor + Calculadora.numero
    
    def suma_doble(self, num1, num2):
        return self.suma(num1) + self.suma(num2)

Calc = Calculadora(5)

print(Calc.suma(8))

print(Calc.suma_doble(2,9))