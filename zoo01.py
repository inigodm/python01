'''grupos = {
    "baby": {
        "numPersonas": 0,
        "precioEntradas": 0
        },
    "menores": {
        "numPersonas": 0,
        "precioEntradas": 14
        },
    "normal": {
        "numPersonas": 0,
        "precioEntradas": 23
        },
    "jubilados": {
        "numPersonas": 0,
        "precioEntradas": 18
        }
    }

grupos = {}
grupos["baby"] = {}
grupos["baby"]["numPersonas"] = 0
grupos["baby"]["precioEntradas"] = 0
hacer lo mismo con todos los grupos. Las tres formas son equivalentes. Distintas formas de escribir lo mismo.
'''
# Creo un diccionario de diccionarios con el número de personas en cada grupo y el precio por entrada de cada grupo.
grupos = {}
grupos["baby"] = {"numPersonas": 0,"precioEntradas": 0}
grupos["menores"] = {"numPersonas": 0,"precioEntradas": 14}
grupos["normal"] = {"numPersonas": 0,"precioEntradas": 23}
grupos["jubilados"] = {"numPersonas": 0,"precioEntradas": 18}

import screen

# pedir edad. Obtener edad asegurándome de que meten un número entero
def obtenerEdad():
    screen.locate(1,1)
    screen.clearLine()
    strEdad = input("Edad (años): ")

    while not strEdad.isdigit():
        print("Dato incorrecto. Edad (años) debe ser un número entero.")
        strEdad = input("Edad (años): ")
        
    return int(strEdad)

# meter a las personas en distinto grupo según su edad. Tengo que crear los grupo (arriba) y los inicializo en 0
def agruparPorEdad(edad):
    if edad <= 2:
        grupos["baby"]["numPersonas"] += 1
    elif edad <= 12:
        grupos["menores"]["numPersonas"] += 1
    elif edad < 65:
        grupos["normal"]["numPersonas"] += 1
    else:
        grupos["jubilados"]["numPersonas"] +=1
    
# multiplicar el precio de las entradas por las personas de cada grupo, obteniendo el precio que tiene que pagar cada grupo
def precioGrupo(tipo):
    precioGrupo = grupos[tipo]["precioEntradas"] * grupos[tipo]["numPersonas"]
    return precioGrupo     

# hacer la suma total a pagar
def sumaTotal():
    total = precioGrupo("baby") + precioGrupo("menores") + precioGrupo("normal") + precioGrupo("jubilados")
    return total

def lineasImpresion(tipo):
    return"{0:2} entradas de {1:10} ({2:2}€):{3:5}€".format(grupos[tipo]["numPersonas"],tipo, grupos[tipo]["precioEntradas"] ,precioGrupo(tipo))
   

