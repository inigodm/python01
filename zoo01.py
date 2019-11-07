grupo = {}
grupo["baby"] = 0
grupo["menores"] = 0
grupo["normal"] = 0
grupo["jubilados"] = 0

precioEntradas = {}
precioEntradas["baby"] = 0
precioEntradas["menores"] = 14 
precioEntradas["normal"] = 23
precioEntradas["jubilados"] = 18 


# pedir edad. Obtener edad asegurándome de que meten un número entero
def obtenerEdad():
    strEdad = input("Edad (años): ")

    while not strEdad.isdigit():
        print("Dato incorrecto. Edad (años) debe ser un número entero.")
        strEdad = input("Edad (años): ")
        
    return int(strEdad)

# meter a las personas en distinto grupo según su edad. Tengo que crear los grupo (arriba) y los inicializo en 0
def agruparPorEdad(edad):
    if edad <= 2:
        grupo["baby"] += 1
    elif edad <= 12:
        grupo["menores"] += 1
    elif edad < 65:
        grupo["normal"] += 1
    else:
        grupo["jubilados"] +=1
    
# multiplicar el precio de las entradas por las personas de cada grupo, obteniendo el precio que tiene que pagar cada grupo
def precioGrupo(tipo):
    precioGrupo = precioEntradas[tipo] * grupo[tipo]
    return precioGrupo     

# hacer la suma total a pagar
def sumaTotal():
    total = precioGrupo("baby") + precioGrupo("menores") + precioGrupo("normal") + precioGrupo("jubilados")
    return total

def lineasImpresion(tipo):
    return"{0:2} entradas de {1:10} ({2:2}€):{3:5}€".format(grupo[tipo],tipo, precioEntradas[tipo] ,precioGrupo(tipo))
   

