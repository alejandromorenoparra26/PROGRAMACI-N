nombre = input("¿Cómo te llamas?")
edad_str = input("¿Qué edad tienes?")
edad = int(edad_str)
if edad<17:
    print("Eres menor de edad")
    print("No puedes votar")
else:
    if edad<65:
        print("Eres mayor de edad")
        print("Ya puedes votar")
    else:    
        print("Jubilado")
print("Hasta pronto")


