import random

total_puntos = 0
tiradas = 0

while tiradas <= 10:
    dado = random.randint(1, 6)
    print(f"Tirada {tiradas + 1}: Ha salido un {dado}")
    
    if dado == 6:
        total_puntos += 12
    else:
        total_puntos += dado
        
    tiradas += 1

print(f"\nPuntuación total obtenida: {total_puntos}")
