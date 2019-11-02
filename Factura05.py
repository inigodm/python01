_UNIDADES = 0
_PRECIO = 1

strUnidades = input("Unidades: ")
unidades = float(strUnidades)

strPrecio = input("Precio (€): ")
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
    
    strUnidades = input("Unidades: ")
    unidades = float(strUnidades)
    strPrecio = input("Precio (€): ")
    precio = float(strPrecio)

indice = 0
while indice < len(listaLineasFact):
    item = listaLineasFact[indice]
    print(item[_PRECIO], "€ - ", item[_UNIDADES], " unidades - ", item[_PRECIO] * item[_UNIDADES], "€")
    indice = indice + 1
    
print("-------------------------------")
print("Total: ", precioTotal)
print("Unidades: ", totalUnidades)

