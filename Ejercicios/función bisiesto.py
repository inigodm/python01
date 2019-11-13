'''
Función con parametro de entrada AÑO,  que devuelva TRUE si es bisiesto y FALSE si no lo es.
Condiciones:
Cualquier año dividido entre 400 es bisiesto.
De los restantes, cualquier año dividido entre 100 no lo es.
De los restantes, cualquier año dividido entre 4 es bisiesto.
Los demás, no lo son.
'''
anno = int(input("Año: "))

def annoBisiesto(anno):
    resultado = False
    if anno % 400 == 0:
        resultado = True
    elif anno % 100 == 0:
        resultado = False
    elif anno % 4 == 0:
        resultado = True
    return resultado

print("El año {} es bisiesto: {}". format(anno, annoBisiesto(anno)))


       









    