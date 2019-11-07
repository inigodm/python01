def cuentaLetras(palabra):
    frecuencias = dict() # o lo que es lo mismo: frecuencias = {}
    for letra in palabra:
        if letra in frecuencias:
            frecuencias[letra] += 1
        else:
            frecuencias[letra] = 1
    return frecuencias
            
def esAnagrama(p1,p2):
    dP1 = cuentaLetras(p1)
    dP2 = cuentaLetras(p2)
    
    if len(dP1) != len(dP2):
        return False
    
    for letra in dP1:
        if letra in dP2 and dP1[letra] == dP2[letra]:
            pass
        else:
            return False
    return True

p1 = input("Introduzca una palabra: ")
p2 = input("Introduzca otra plabra: ")

print(esAnagrama(p1, p2))
