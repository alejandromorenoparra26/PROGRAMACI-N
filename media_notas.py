# Pedimos las 10 notas en una sola línea usando una lista de comprensión
notas = [float(input(f"Introduce la nota {i+1}: ")) for i in range(10)]

# Calculamos los aprobados y la media directamente
aprobados = sum(1 for n in notas if n >= 5)
media = sum(notas) / len(notas)

# Mostramos los resultados
print(f"\nNúmero de aprobados: {aprobados}")
print(f"La media es: {media:.2f}")
