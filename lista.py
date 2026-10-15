almacen = [
    ["Coca Cola", 15, 1.50],
    ["Fanta Naranja", 10, 1.40],
    ["Fanta Limón", 8, 1.40],
    ["Sprite", 12, 1.50],
    ["Agua", 20, 1.00],
    ["Zumo de naranja", 7, 1.30],
    ["Té frío", 9, 1.60],
    ["Café", 14, 1.20],
    ["Chocolate", 6, 1.80],
    ["Bebida energética", 5, 2.00]
]

print(almacen)
print(almacen[2])
print(almacen[2][0])

for producto in almacen:
    print(producto[0],"en stock a",producto[1],producto[2],"euros")