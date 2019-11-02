# Entrada de datos
strNumero1 = input("Introduzca un número: ")
strNumero2 = input("Introduzca otro número: ")

if strNumero1.isdigit():
    numero1 = int(strNumero1)
elif strNumero1[0] == "-" and strNumero1[1:].isdigit():
        numero1 = int(strNumero1)
else:
    print(strNumero1, "debe ser un entero.")
    quit()

if strNumero2.isdigit():
    numero2 = int(strNumero2)
elif strNumero2[0] == "-" and strNumero2[1:].isdigit():
        numero2 = int(strNumero2)
else:
    print(strNumero2, "debe ser un entero.")
    quit()

# Procesamiento de datos
divisor = 10

numero1 = numero1 / divisor
numero2 = numero2 / divisor

suma = round(numero1 + numero2,2)
resta = round(numero1 - numero2,2)
multiplicacion = round(numero1 * numero2,2)
division = round(numero1 / numero2,2)

# Salida de datos
print(numero1, " + ", numero2, " = ", suma)
print(numero1, " - ", numero2, " = ", resta)
print(numero1, " x ", numero2, " = ", multiplicacion)
print(numero1, " / ", numero2, " = ", division)
