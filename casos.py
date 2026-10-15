numero1 = int(input("Introduce primer numero"))
numero2 = int(input("Introduce segundo numero "))

resultado = 0

print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")
opcion = input("¿Que opcion eliges? (1, 2, 3, 4)")

match opcion:
    case 1:
        resultado = numero1 + numero2;
    case 2:
        resultado = numero1 - numero2;
    case 3:
        resultado = numero1 * numero2;
    case 4:
        resultado = numero1 / numero2;
    case _:
        print("No es un número válido")
print("Resultado de la operacion: ", resultado)
print("Fin del programa")
