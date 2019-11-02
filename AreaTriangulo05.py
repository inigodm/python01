def esDecimal(numero):
    try:
        float(numero)
        return True
    except:
        return False

def obtenerNumericoDeUsuario(mensajeIntroduccion):
    resultado = input(mensajeIntroduccion)
    while not esDecimal(resultado):
        print(resultado, "no es un valor numérico")
        resultado = input(mensajeIntroduccion)
    return resultado
    
strBase = obtenerNumericoDeUsuario("Introduzca la base del triángulo: ")
strAltura = obtenerNumericoDeUsuario("Introduzca la altura del triángulo: ")
    
b = float(strBase)
h = float(strAltura)

area = b * h / 2

print("Superficie del triángulo: ", round(area,2))