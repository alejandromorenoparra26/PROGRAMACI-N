numero = int(input("Introduce un número entero: "))


suma_total = 0

print("Secuencia numérica:")


if numero >= 0:

    for i in range(numero, -1, -1):
        print(i)
        suma_total += i
else:
    for i in range(numero, 1):
        print(i)
        suma_total += i

print(f"La suma de todos los números es: {suma_total}")