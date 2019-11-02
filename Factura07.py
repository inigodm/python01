strUnidades = input("Unidades: ")
unidades = float(strUnidades)

strPrecio = input("Precio (€): ")
precio = float(strPrecio)

totalUnidades = 0
precioTotal = 0

listaLineasFact = []

while unidades > 0 and precio > 0:
    totalUnitario = precio * unidades
    item = dict()
    item["unidades"] = unidades
    item["precio"] = precio
    
    listaLineasFact.append (item)
    
    totalUnidades += unidades # es lo mismo que decir totalUnidades = totalUnidades + unidades
    precioTotal += totalUnitario
    
    strUnidades = input("Unidades: ")
    unidades = float(strUnidades)
    strPrecio = input("Precio (€): ")
    precio = float(strPrecio)

for item in listaLineasFact:
    print(item.get("precio"), "€ - ", item.get("unidades"), " unidades - ", item.get("precio") * item.get("unidades"), "€")
        
print("--------------------")
print("Total: ", precioTotal)
print("Unidades: ", totalUnidades)


