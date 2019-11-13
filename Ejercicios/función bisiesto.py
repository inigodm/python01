'''
Función con parametro de entrada AÑO,  que devuelva TRUE si es bisiesto y FALSE si no lo es.
Condiciones:
Cualquier año dividido entre 400 es bisiesto.
De los restantes, cualquier año dividido entre 100 no lo es.
De los restantes, cualquier año dividido entre 4 es bisiesto.
Los demás, no lo son.
'''

def annoBisiesto(anno):
    if anno % 400 == 0:
        anno = True
        print(anno)
    elif anno % 100 == 0:
        anno = False
        print(anno)
    elif anno % 4 == 0:
        anno = True
        print(anno)
    else:
       anno = False
       print(anno)









    