strUnidades = input("Unidades: ")
unidades = float(strUnidades)

strPrecio = input("Precio (€): ")
precio = float(strPrecio)

totalUnidades = 0
precioTotal = 0

while unidades > 0 and precio > 0:
    totalUnitario = precio * unidades
    print(precio,"€ -", unidades, "unidades -", totalUnitario,"€")
    
    totalUnidades += unidades # es lo mismo que decir totalUnidades = totalUnidades + unidades
    precioTotal += totalUnitario
    
    strUnidades = input("Unidades: ")
    unidades = float(strUnidades)
    strPrecio = input("Precio (€): ")
    precio = float(strPrecio)
    
print("--------------------")
print("Total: ", precioTotal)
print("Unidades: ", totalUnidades)


