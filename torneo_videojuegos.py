mario_kart = {"Ana", "Luis", "Pedro", "Marta", "Hugo"}
minecraft = {"Luis", "Marta", "Sara", "David"}
rocket_league = {"Pedro", "Marta", "David", "Elena"}

opcion = 0

while opcion != 9:
    print("\n--- TORNEOS DE VIDEOJUEGOS ---")
    print("1. Mostrar todos los participantes")
    print("2. Participantes comunes a Mario Kart y Minecraft")
    print("3. Participantes inscritos en los tres torneos")
    print("4. Participantes de Mario Kart que no están en Minecraft")
    print("5. Participantes de Minecraft o Rocket League, pero no en ambos")
    print("6. Añadir un participante a un torneo")
    print("7. Eliminar un participante de un torneo")
    print("8. Consultar los torneos de una persona")
    print("9. Terminar")

    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        todos = mario_kart | minecraft | rocket_league
        print("Todos los participantes:", todos)

    elif opcion == 2:
        comunes = mario_kart & minecraft
        print("Participantes comunes:", comunes)

    elif opcion == 3:
        comunes = mario_kart & minecraft & rocket_league
        print("Inscritos en los tres torneos:", comunes)

    elif opcion == 4:
        participantes = mario_kart - minecraft
        print("Solo en Mario Kart:", participantes)

    elif opcion == 5:
        participantes = minecraft ^ rocket_league
        print("Participantes en uno solo de los dos torneos:", participantes)

    elif opcion == 6:
        nombre = input("Nombre del participante: ")
        print("1. Mario Kart")
        print("2. Minecraft")
        print("3. Rocket League")
        torneo = int(input("Elige el torneo: "))

        if torneo == 1:
            mario_kart.add(nombre)
            print("Participante añadido a Mario Kart.")
        elif torneo == 2:
            minecraft.add(nombre)
            print("Participante añadido a Minecraft.")
        elif torneo == 3:
            rocket_league.add(nombre)
            print("Participante añadido a Rocket League.")
        else:
            print("Torneo no válido.")

    elif opcion == 7:
        nombre = input("Nombre del participante: ")
        print("1. Mario Kart")
        print("2. Minecraft")
        print("3. Rocket League")
        torneo = int(input("Elige el torneo: "))

        if torneo == 1:
            mario_kart.discard(nombre)
            print("Operación realizada en Mario Kart.")
        elif torneo == 2:
            minecraft.discard(nombre)
            print("Operación realizada en Minecraft.")
        elif torneo == 3:
            rocket_league.discard(nombre)
            print("Operación realizada en Rocket League.")
        else:
            print("Torneo no válido.")

    elif opcion == 8:
        nombre = input("Nombre de la persona: ")
        encontrado = False

        if nombre in mario_kart:
            print("Está inscrito en Mario Kart.")
            encontrado = True

        if nombre in minecraft:
            print("Está inscrito en Minecraft.")
            encontrado = True

        if nombre in rocket_league:
            print("Está inscrito en Rocket League.")
            encontrado = True

        if not encontrado:
            print("La persona no está inscrita en ningún torneo.")

    elif opcion == 9:
        print("Programa terminado.")

    else:
        print("Opción no válida.")
