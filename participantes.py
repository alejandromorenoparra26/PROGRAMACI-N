participantes = ["Luis", "Marta", "Pablo", "Luis", "Ana"]
print("Luis aparece", participantes.count("Luis"), "veces")

print("Marta está en la posición", participantes.index("Marta"))

participantes.append("Sara")
print(participantes)

participantes.insert(2, "Elena")
print(participantes)

participantes.remove("Pablo")
print(participantes)

participantes.sort()
print(participantes)
participantes.reverse()
print(participantes)

ultimo = participantes.pop()
print("El último participante era:", ultimo)

print("Lista final:", participantes)