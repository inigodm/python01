strUnidades = input("Unidades: ")
unidades = float(strUnidades)

strPrecio = input("Precio (€): ")
precio = float(strPrecio)

totalUnidades = 0
precioTotal = 0

listaUnidades = []
listaPrecios = []

while unidades > 0 and precio > 0:
    totalUnitario = precio * unidades
    listaUnidades.append(unidades)
    listaPrecios.append(precio)
    
    totalUnidades += unidades # es lo mismo que decir totalUnidades = totalUnidades + unidades
    precioTotal += totalUnitario
    
    strUnidades = input("Unidades: ")
    unidades = float(strUnidades)
    strPrecio = input("Precio (€): ")
    precio = float(strPrecio)

indice = 0
while indice < len(listaPrecios):
    print(listaPrecios[indice], "€ - ", listaUnidades[indice], " unidades - ", listaPrecios[indice] * listaUnidades[indice], "€")
    indice = indice + 1
    
print("--------------------")
print("Total: ", precioTotal)
print("Unidades: ", totalUnidades)
