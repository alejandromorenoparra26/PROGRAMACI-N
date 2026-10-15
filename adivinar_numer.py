import random  

numero = random.randint(1, 10)

intentos = 0

acertado = False

while intentos < 5 and acertado == False:

    apuesta = int(input("Adivina el número (1-10): "))
    intentos = intentos + 1

    if apuesta == numero:

        print("¡Has acertado!")

        acertado = True
    elif apuesta < numero:

        print("El número es mayor.")

    else:
        print("El número es menor.")

if acertado == False:
    print("Has perdido. El número era", numero)