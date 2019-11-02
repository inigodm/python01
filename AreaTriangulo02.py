def esDecimal(numero):
    try:
        float(numero)
        return True
    except:
        return False
    
strBase = input("Intruduzca la base del triángulo: ")
if esDecimal(strBase):
    b = float(strBase)
else:
    print(strBase, "no es numérico.")
    quit()
       
strAltura = input("Introduzca la altura del triángulo: ")    
if esDecimal(strAltura):
    h = float(strAltura)
else:
    print(strAltura, "no es numérico.")
    quit()

area = b * h / 2

print("Superficie del triángulo: ", round(area,2))