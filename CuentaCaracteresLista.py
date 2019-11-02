def existe(letra, lista):
    posicion = 0
    while posicion < len(lista):
        if lista[posicion] == letra:
            return posicion
        posicion += 1
    return None

texto = "Tres pelos tiene mi barba."

letras = []
frecuencias = []

for caracter in texto:
    posicion = existe(caracter, letras)
    if posicion != None:
        frecuencias[posicion] += 1
    else:
        letras.append(caracter)
        frecuencias.append(1)

indice = 0
while indice < len(letras):
    print (letras[indice], "-", frecuencias[indice])
    indice += 1