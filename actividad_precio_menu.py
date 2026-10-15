edad_src = input("¿Qué edad tienes? ")
dia = input("¿Qué día es hoy? ")

edad = int(edad_src)

if dia == "sabado" or dia == "domingo":
    precio = 20
else:
    precio = 15

if edad < 18:
    descuento = precio * 0.30
    precio_final = precio - descuento
    print("El precio final es:", precio_final, "€")
else:
    precio_final = precio

print("El precio final es:", precio_final, "€")