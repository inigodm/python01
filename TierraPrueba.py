# mensaje = (90, 180, 135, 337, 135, 270, 135, 22.5)
base16 = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f") 
angulo = 360/16
listaHex = []

def obtenerMensaje():
    mensajeRecibido = []
    angulosRecibidos = input("Introduzca los ángulos recibidos separados por comas: ")
    angulosSeparados = angulosRecibidos.split(",")
    for angulo in angulosSeparados:
        mensajeRecibido.append(float(angulo))
    return mensajeRecibido

def tierra(angulos):
    for caracter in angulos:
        indiceBase16 = int(round(caracter / angulo, 1))
        valorHexadecimal = base16[indiceBase16]
        listaHex.append(valorHexadecimal)  

    mensajeDecodificado = ""
    
    if len(listaHex) %2 != 0:
        listaHex.append("0")
        
    while listaHex != []:
        elemento1 = listaHex.pop(0)
        elemento2 = listaHex.pop(0)
        caracHex = elemento1 + elemento2
        mensajeDecodificado += chr(int(caracHex, 16)) 
    
    print(mensajeDecodificado)

mensaje = obtenerMensaje()

if len(mensaje) % 2 != 0:
    print("Número de ángulos introducido incorrecto. Tenga en cuenta que el mensaje puede ser erróneo.")
    tierra(mensaje)

   
