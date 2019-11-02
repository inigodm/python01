import random

saludos = ["Hola, {}", "Buenas, {}", "{}, ¿Que tal estas?", "Zer moduz, {}?"]
saludo = saludos[random.randint(0,3)]

nombre = input("¿Cómo te llamas? ")

print(saludo.format(nombre))
