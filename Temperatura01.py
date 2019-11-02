tipo = input("Salida de grados (F/C): ")

def aCelsius(fahren):
    return round((fahren - 32) * 5 / 9, 2)

def aFahren(celsius):
    return round(celsius + 9 / 5 + 32, 2)

if tipo.upper() == "C":
    for grados in range(0, 240, 10):
        print(grados, "ºF -----> ", aCelsius(grados), "ºC")
elif tipo.upper() == "F":
    for grados in range(0, 100, 10):
        print(grados, "ºC -----> ", aFahren(grados), "ºF")
else:
    print ("Tipo de salida incorrecta.")