a = 5
b = 32

print("Suma: ", a+b)
print("Division:", b/a)
print("Division entera:", b//a)
print("Resto:", b%a)
print("Potencia: ", a**2)

nombre = input("¿Cómo te llamas?")
edad = input("¿Cuántos años tienes?")
edad = int(edad)
# mensaje = "Hola {0}, tienes {1} años".format(nombre, edad)
mensaje = f"Hola {nombre}, tienes {edad} años"
print(mensaje)
