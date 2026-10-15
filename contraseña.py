CLAVE = "campusfp"
intentos = 0
while intentos <= 4:
    if input("Introduce la contraseña: ") == CLAVE:
        print("BIENVENIDO AL SISTEMA")
        break
else:
    print("ACCESO DENEGADO")
