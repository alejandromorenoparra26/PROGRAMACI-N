planta_actual = int(input("en que planta estas??"))
planta_destino = int(input("a que planta deseas ir"))

if planta_actual>planta_destino:
    print("bajando")
elif planta_actual<planta_destino:
    print("ya estas en la planta")
    print("subiendo")