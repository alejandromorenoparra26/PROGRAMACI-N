nombre = input("¿Cómo te llamas? ")
estado_civil = input("Tu estado civil (S,C,V,D): ")
sueldo_str = input("Sueldo: ")

sueldo = float(sueldo_str)

print("Es casado: ", estado_civil == "C")
print("Sueldo alto: ", sueldo >= 3000)