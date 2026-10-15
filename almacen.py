almacen = []

while True:

    print("\n--- MENÚ DEL ALMACÉN ---")
    print("1. Añadir nuevo producto")
    print("2. Listar todos los productos")
    print("3. Mostrar valor del almacén")
    print("4. Salir del programa")

    opcion = input("Elige una opción: ")

    if opcion == "1":

        nombre = input("Introduce el nombre del producto: ")
        cantidad = int(input("Introduce la cantidad en stock: "))
        precio = float(input("Introduce el precio por unidad: "))

        producto = [nombre, cantidad, precio]

        almacen.append(producto)

        print("Producto añadido correctamente.")

    elif opcion == "2":

        print("\n--- PRODUCTOS DEL ALMACÉN ---")

        for producto in almacen:
            print("Nombre:", producto[0])
            print("Cantidad:", producto[1])
            print("Precio:", producto[2], "€")
            print("--------------------")

    elif opcion == "3":

        total = 0

        for producto in almacen:

            valor = producto[1] * producto[2]

            total = total + valor

        print("Valor total del almacén:", total, "€")

    elif opcion == "4":

        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Elige entre 1 y 4.")