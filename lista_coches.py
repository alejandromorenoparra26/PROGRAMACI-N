coches = []

coche = ""

while coche != "FIN":
    coche = input("¿Qué modelo de coche es? ")

    if coche != "FIN":
        coches.append(coche)
        print("Hay", len(coches), "coches")

posicion = 0

for coche in coches:
    print(posicion, coche)
    posicion = posicion + 1