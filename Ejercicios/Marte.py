base16 = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f")
angulo = 360 / 16

def anguloHex(digito):
    encontrado = False
    indice = 0 
    while not encontrado:
        if digito == base16[indice]:
            return indice * angulo
        else:
            indice += 1    

cadena = input("Mensaje: ")

for caracter in cadena:
    hexadecimal = hex(ord(caracter))
    
    digito1 = hexadecimal[2]
    angulo1 = anguloHex(digito1)
    
    digito2 = hexadecimal[3]
    angulo2 = anguloHex(digito2)
    
    print(digito1, "-", angulo1)
    print(digito2, "-", angulo2)
    
