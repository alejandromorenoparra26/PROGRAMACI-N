equipajes = []

numero = int(input("¿Cuántos equipajes vas a facturar? "))

for i in range(numero):
    peso = float(input("Introduce el peso del equipaje: "))

    if peso <= 20:
        precio = 0
    elif peso <= 30:
        precio = 20
    else:
        precio = 35

    equipaje = {
        "peso": peso,
        "precio": precio
    }

    equipajes.append(equipaje)

print("\nEquipajes registrados:")

total = 0

for equipaje in equipajes:
    print("Peso:", equipaje["peso"], "kg")
    print("Precio:", equipaje["precio"], "€")
    
    total = total + equipaje["precio"]

print("\nImporte total:", total, "€")
