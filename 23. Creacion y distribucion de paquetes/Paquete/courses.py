
class curso:

    def __init__(self,name, duracion, link):

        self.name = name
        self.duracion = duracion
        self.link = link

    def __repr__(self): # Toca definir este metodo cuando queremos llamar a un objeto definido desde la clase, si queremos llamar a la lista sin tener que iterar podremos hacer los siguienbte 
        
        return f"{self.name}, [{self.duracion}] horas, {self.link}"


cursos = [

    curso("Introduccion a Linux", 15, "Link1"),
    curso("Personalizacion de linux",3 , "Link2"),
    curso("Introduccion al hacking", 53, "Link3")

]

# print(cursos[0]) # Printeado con el metodo especial repr

# Defincion de la Funcion que se encargara de la impresion de los cursos

def listar_cursos():
    for curso in cursos:
        print(curso)

def search_course_by_name(name):
    for curso in cursos:
        if curso.name == name:
            print(curso)
    
    return None 



