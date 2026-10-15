
talleres = [
    ("Fotografía", ["Ana", "Luis"], {"aula": 12, "plazas": 4}, {"cámara", "tarjeta de memoria"}),
    ("Robótica", ["Marta"], {"aula": 15, "plazas": 3}, {"portátil", "cable USB"}),
    ("Pintura", [], {"aula": 8, "plazas": 5}, {"pinceles", "acuarelas", "papel"})
]

opcion = 0

while opcion != 6:
    print("\n1. Mostrar talleres")
    print("2. Inscribir alumno")
    print("3. Cancelar inscripción")
    print("4. Cambiar aula")
    print("5. Añadir material")
    print("6. Terminar")

    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        for t in talleres:
            print(t[0], "Aula:", t[2]["aula"],
                  "Alumnos:", t[1],
                  "Plazas libres:", t[2]["plazas"] - len(t[1]),
                  "Materiales:", t[3])

    elif opcion == 2:
        nombre = input("Taller: ")
        alumno = input("Alumno: ")
        for t in talleres:
            if t[0].lower() == nombre.lower():
                if len(t[1]) < t[2]["plazas"] and alumno not in t[1]:
                    t[1].append(alumno)
                    print("Inscripción realizada")
                else:
                    print("No hay plazas o ya está inscrito")

    elif opcion == 3:
        nombre = input("Taller: ")
        alumno = input("Alumno: ")
        for t in talleres:
            if t[0].lower() == nombre.lower() and alumno in t[1]:
                t[1].remove(alumno)
                print("Inscripción cancelada")

    elif opcion == 4:
        nombre = input("Taller: ")
        aula = int(input("Nueva aula: "))
        for t in talleres:
            if t[0].lower() == nombre.lower():
                t[2]["aula"] = aula

    elif opcion == 5:
        nombre = input("Taller: ")
        material = input("Material: ")
        for t in talleres:
            if t[0].lower() == nombre.lower():
                t[3].add(material)

    elif opcion == 6:
        print("Fin del programa")
