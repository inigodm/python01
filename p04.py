diasMes = (31,28,31,30,31,30,31,31,30,31,30,31)

nombre = input("¿Cómo te llamas? ")
print("Hola, ", nombre)

strEdad = input("¿Cuántos años tienes? ")
strAnno = input("¿En qué año estamos? ")
strMes = input("¿En qué número de mes estamos? ")
strDia = input("¿Qué día del mes es hoy? ")

edad = int(strEdad)
anno = int(strAnno)
mes = int(strMes)
dia = int(strDia)

transcurridos = 0
if mes > 1:
    transcurridos = transcurridos + diasMes[0]
if mes > 2:
    transcurridos = transcurridos + diasMes[1]
if mes > 3:
    transcurridos = transcurridos + diasMes[2]
if mes > 4:
    transcurridos = transcurridos + diasMes[3]
if mes > 5:
    transcurridos = transcurridos + diasMes[4]
if mes > 6:
    transcurridos = transcurridos + diasMes[5]
if mes > 7:
    transcurridos = transcurridos + diasMes[6]
if mes > 8:
    transcurridos = transcurridos + diasMes[7]
if mes > 9:
    transcurridos = transcurridos + diasMes[8]
if mes > 10:
    transcurridos = transcurridos + diasMes[9]
if mes > 11:
    transcurridos = transcurridos + diasMes[10]
    
transcurridos = transcurridos + dia
    
prob = transcurridos / 365 * 100
nacimiento = anno - edad

    
print(nombre, "naciste en", nacimiento, "con una probabilidad de", prob, "%")
print("o en", nacimiento -1 , "con una probabilidad de", 100 - prob, "%")

