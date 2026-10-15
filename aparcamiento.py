horas = float(input("Introduce el número de horas que el vehículo ha permanecido aparcado: "))

if horas <= 2:
    importe = horas * 2
elif horas <= 5:
    importe = horas * 1.50
else:
    importe = horas * 1

print(f"El importe total a pagar es: {importe:.2f} €")