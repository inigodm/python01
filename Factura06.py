def esDecimal(numero):
    try:
        float(numero)
        return True
    except:
        return False
    
def obtenerNumeroInput(texto):
    dato = input(texto)
    while not esDecimal(dato):
        print("Dato incorrecto. Introduzca un valor numérico: ")
        dato = input(texto)
    return dato    
    
_UNIDADES = 0
_PRECIO = 1

strUnidades = obtenerNumeroInput("Unidades: ")
unidades = float(strUnidades)

strPrecio = obtenerNumeroInput("Precio (€): ")
precio = float(strPrecio)

totalUnidades = 0
precioTotal = 0

listaLineasFact = []

while unidades > 0 and precio > 0:
    totalUnitario = precio * unidades
    item = []
    item.append(unidades)
    item.append(precio)
    
    listaLineasFact.append (item)
    
    totalUnidades += unidades # es lo mismo que decir totalUnidades = totalUnidades + unidades
    precioTotal += totalUnitario
    
    strUnidades = obtenerNumeroInput("Unidades: ")
    unidades = float(strUnidades)
    strPrecio = obtenerNumeroInput("Precio (€): ")
    precio = float(strPrecio)

for it in listaLineasFact:
    print(it[_PRECIO], "€ - ", it[_UNIDADES], " unidades - ", it[_PRECIO] * it[_UNIDADES], "€")
        
print("--------------------")
print("Total: ", precioTotal)
print("Unidades: ", totalUnidades)

