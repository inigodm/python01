texto = "Tres pelos tiene mi barba."

frecuencias = dict()

for caracter in texto:
    if caracter in frecuencias: # es lo mismo que abajo pero usando una funcionalidad de python
#    if frecuencias.get(caracter) != None:
        frecuencias[caracter] += 1
    else:
        frecuencias[caracter] = 1

for letra in frecuencias.keys():
    print(letra, "-", frecuencias[letra])