# Inicializamos una lista vacía para guardar los números
numeros = []

# Solicitamos los 5 números al usuario mediante un bucle
for i in range(1, 6):
    numero = float(input(f"Introduce el número {i}: "))
    numeros.append(numero)

# Encontramos el número mayor utilizando la función max()
mayor = max(numeros)

print(f"\nEl número mayor de los introducidos es: {mayor}")
