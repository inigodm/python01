def validacion(mensaje):
    strNumero = input(mensaje)
    isvalid = False

    while not isvalid:
        if strNumero.isdigit():
            numero = int(strNumero)
            isvalid = True
        elif strNumero != " " and strNumero[0] == "-" and strNumero[1:].isdigit():
            numero = int(strNumero1)
            isvalid = True
        else:
            print(strNumero, "debe ser un número entero.")
            strNumero = input(mensaje)

    return strNumero

strNumero01 = validacion("Introduzca un número: ")

strNumero02 = validacion("Introduzca otro número: ")

# Procesamiento de datos
numero01 = int(strNumero01)
numero02 = int(strNumero02)

divisor = 10

numero01 = numero01 / divisor
numero02 = numero02 / divisor

suma = round(numero01 + numero02,2)
resta = round(numero01 - numero02,2)
multiplicacion = round(numero01 * numero02,2)
division = round(numero01 / numero02,2)

# Salida de datos
print(numero01, " + ", numero02, " = ", suma)
print(numero01, " - ", numero02, " = ", resta)
print(numero01, " x ", numero02, " = ", multiplicacion)
print(numero01, " / ", numero02, " = ", division)


