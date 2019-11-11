# importo modulo (zoo01) y llamo las funciones
from zoo01 import obtenerEdad, agruparPorEdad, sumaTotal, lineasImpresion, grupos
import screen

screen.clear()

edad = obtenerEdad()

while edad != 0:
    agruparPorEdad(edad)
    edad = obtenerEdad()
screen.clear()
    
total = sumaTotal()

print(lineasImpresion("baby"))
print(lineasImpresion("menores"))
print(lineasImpresion("normal"))
print(lineasImpresion("jubilados"))
print("--------------------------------------\nTotal:{0:31}€".format(total))

