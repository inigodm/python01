base16 = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f")
angulo = 360 / 16

cadena = input("Mensaje: ")

for caracter in cadena:
    hexadecimal = hex(ord(caracter))
    
    digito1 = hexadecimal[2]
    indiceDe1 = base16.index(hexadecimal[2])
    angulo1 = angulo * indiceDe1
    
    digito2 = hexadecimal[3]
    indiceDe2 = base16.index(hexadecimal[3])
    angulo2 = angulo * indiceDe2
    
    print(digito1, "-", angulo1)
    print(digito2, "-", angulo2)