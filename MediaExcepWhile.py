notas = (2,4,6,8)


def contenido(lista, indice):
    try:
        resultado = lista [indice]
    except:
        resultado = None

    return resultado

# Contar items de notas
indice = 0

while contenido(notas, indice) != None:
        indice = indice + 1
        
print("Número de items: ", indice)

# Suma notas
indice = 0
suma = 0

while contenido(notas, indice) != None:
    suma = suma + notas[indice]
    indice = indice + 1
    
print("Nota Total: ", suma)

# Calcular media
media = suma / indice

print("Nota Media: ", media)

# El programa está hecho pero es feo como el demonio. Ahora lo mejoramos.


