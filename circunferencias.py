import math

for radio in range(10, 101, 10):
    longitud = 2 * math.pi * radio
    area = math.pi * radio ** 2

    print("Radio:", radio)
    print("Longitud:", longitud)
    print("Área:", area)
    print("----------------")