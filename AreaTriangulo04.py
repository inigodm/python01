def esDecimal(numero):
    try:
        float(numero)
        return True
    except:
        return False
    
strBase = input("Intruduzca la base del triángulo: ")
while not esDecimal(strBase):
    print(strBase, "no es un valor numérico")
    strBase = input("Intruduzca la base del triángulo: ")

strAltura = input("Introduzca la altura del triángulo: ")
while not esDecimal(strAltura):
    print(strAltura, "no es un valor numérico")    
    strAltura = input("Introduzca la altura del triángulo: ")
    
b = float(strBase)
h = float(strAltura)

area = b * h / 2

print("Superficie del triángulo: ", round(area,2))
    
    