# simular un coche que acelera y frena
velocidad=0
opcion = " ";

while opcion !="4":
    print("1. Acelerar")
    print("2. Frenar")
    print("3. Ver velocidad actual")
    print("4. Terminar")
    opcion = input("Elige opcion (1,2,3,4):")


match opcion:
    case "1":
        velocidad = velocidad+10
    case "2":
        velocidad = velocidad-10
    case "3":
        print("Mi coche va a ",velocidad,"km/h")
    case _:
        print("Opcion incorrecta")

print("HASTA PRONTO")
