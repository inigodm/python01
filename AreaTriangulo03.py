def esDecimal(numero):
    try:
        float(numero)
        return True
    except:
        return False
    
strBase = input("Intruduzca la base del triángulo: ")
if esDecimal(strBase):
    b = float(strBase)
   
    strAltura = input("Introduzca la altura del triángulo: ")
    if esDecimal(strAltura):
        h = float(strAltura)
    
        area = b * h / 2

        print("Superficie del triángulo: ", round(area,2))
    
    else:
        print(strAltura, "no es numérico.")

else:
    print(strBase, "no es numérico.")
 

