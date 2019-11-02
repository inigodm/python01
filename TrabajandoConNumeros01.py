# Entrada de datos
strNumero1 = input("Intruduzca un número: ")
strNumero2 = input("Introduzca otro número: ")

# Procesamiento de datos
numero1 = float(strNumero1)
numero2 = float(strNumero2)

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






