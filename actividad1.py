nota_str = input("¿Qué nota has sacado?")

nota = float(nota_str) #conversion a numero

if nota < 6:
    if nota < 5:

        if nota < 3:
            print("Muy deficiente")
        else:
            print("Insuficiente")

    else:
        print("Suficiente")

else:

    if nota < 7:
        print("Bien")

    else:

        if nota < 9:
            print("Notable")
        else:
            print("Sobresaliente")

print("Hasta pronto")