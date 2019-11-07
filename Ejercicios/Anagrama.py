def stringContieneCaracter(string, caracter):
    for letra in string:
        if letra == caracter:
            return True 
    return False

def esAnagrama(p1, p2):
    if len(p1)!= len(p2):
        return False
    if not stringContieneTodosCaracteres(p1, p2):
        return False
    if not stringContieneTodosCaracteres(p2, p1):
        return False
    return True

def stringContieneTodosCaracteres(p1, p2):
    for letra in p1:
        if not stringContieneCaracter(p2, letra):
            return False
    return True

p1 = input("Palabra 1: ")
p2 = input("Palabra 2: ")

print(esAnagrama(p1, p2))