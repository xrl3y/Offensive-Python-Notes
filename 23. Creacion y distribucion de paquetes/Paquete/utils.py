
from courses import *


def total_duration():

    total = 0

    for curso in cursos:
        total += curso.duracion

    return total


print(total_duration())