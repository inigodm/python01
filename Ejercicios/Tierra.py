mensaje = (90, 180, 135, 337, 135, 270, 135, 225)
base16 = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f") 
angulo = 360/16
listaHex = []

for caracter in mensaje:
    indiceBase16 = int(round(caracter / angulo, 1))
    
    valorHexadecimal = base16[indiceBase16]
      
    listaHex.append(valorHexadecimal)
    
while listaHex != []:
    elemento1 = listaHex.pop(0)
    elemento2 = listaHex.pop(0)
    print(elemento1 + elemento2)
    ordinal = ord(int(elemento1 + elemento2))
    print(ordinal)
