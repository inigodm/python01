notas = (2,4,6,8)

def contenido(lista, indice):
    try:
        resultado = lista [indice]
    except:
        resultado = None

    return resultado

def longitud(lista):
    indice = 0
    while contenido(lista, indice) != None:
        indice = indice + 1
    
    return indice

# Calcular media
suma = 0
for indice in range(0, longitud(notas)):
    suma = suma + notas[indice]
    
media = suma / longitud(notas)

print("Número de items: ", longitud(notas))    
print("Nota Total.....: ", suma)
print("Nota Media.....: ", media)

# Cada vez que invoca logitud entra en un bucle y hace el programa mas lento. Hay que hacerlo más eficiente.

    
