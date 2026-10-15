edad = int(input("¿Que edad tienes?"))
altura = int(input("¿Cuanto mides?"))
acompañado = (input("¿Vas acompañado de un adulto?"))

if altura <= 120: 
    print("No puedes subir a la atraccion")
else:
    if edad >= 12:
        print("Puedes subir a la atraccion")
    else:
        if acompañado == "si":
            print("Puedes subir a la atraccion")
        else:
            print("no puedes subir a la atraccion")