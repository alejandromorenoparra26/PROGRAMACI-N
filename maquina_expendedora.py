bebidas = [
    ["Coca Cola", 15, 1.50],
    ["Fanta naranja", 10, 1.40],
    ["Agua", 20, 1.00],
    ["Nestea", 8, 1.60],
    ["Aquarius", 12, 1.70]
]

ventas = []

opcion = ""

while opcion != "OFF":

    print("\nMÁQUINA EXPENDEDORA")

    print("0. Coca Cola")
    print("1. Fanta naranja")
    print("2. Agua")
    print("3. Nestea")
    print("4. Aquarius")
    print("OFF = Apagar máquina")

    opcion = input("Teclea opción deseada: ")

    if opcion == "OFF":
        break

    opcion = int(opcion)

    if opcion >= 0 and opcion <= 4:

        bebida = bebidas[opcion]

        if bebida[1] > 0:

            bebida[1] = bebida[1] - 1
            ventas.append([bebida[0], bebida[2]])

            print("Aquí tiene su", bebida[0])
            print("Han sido", bebida[2], "euros.")

        else:
            print("El producto está agotado.")

    else:
        print("Opción no válida.")


print("\nVENTAS DEL DÍA")

recaudacion = 0

for venta in ventas:

    print(venta[0], "-", format(venta[1], ".2f"), "euros")

    recaudacion = recaudacion + venta[1]


print("\nRecaudación total:", format(recaudacion, ".2f"), "euros")