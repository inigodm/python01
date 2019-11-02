strUnidades = input("Unidades: ")
unidades = float(strUnidades)

strPrecio = input("Precio (€): ")
precio = float(strPrecio)

strAImprimir = "\n"
totalUnidades = 0
precioTotal = 0

while unidades > 0 and precio > 0:
    totalUnitario = precio * unidades
    
    strAImprimir += str(precio) + "€ - " + str(unidades) + " unidades - " + str(totalUnitario) + "€\n"
    # strAImprimir += "{}€ - {} unidades - {}€\n".format(precio, unidades, totalUnitario) 
    
    totalUnidades += unidades # es lo mismo que decir totalUnidades = totalUnidades + unidades
    precioTotal += totalUnitario
    
    strUnidades = input("Unidades: ")
    unidades = float(strUnidades)
    strPrecio = input("Precio (€): ")
    precio = float(strPrecio)

print(strAImprimir)
print("--------------------")
print("Total: ", precioTotal)
print("Unidades: ", totalUnidades)




