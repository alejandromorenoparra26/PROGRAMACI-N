lado1 = int(input("Introduce el 1º lado"))
lado2 = int(input("Introduce el 2º lado"))
lado3 = int(input("Introduce el 3º lado"))

if lado1 == lado2 and lado2 == lado3:
    print("Equilatero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Isosceles")
else:
    print("Escaleno")