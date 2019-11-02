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

for precio, unidades in zip(listaPrecios, listaUnidades):
    print(precio,"€ -", unidades, "unidades -", totalUnitario,"€")
   
print("--------------------")
print("Total: ", precioTotal)
print("Unidades: ", totalUnidades)

