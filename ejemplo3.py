texto = "tres tristes 'tigres' comian trigo en un trigal"
print(texto)
print(texto[0])
print(texto[1])
print(texto[2])
ultimo = len(texto)-1
print(texto [ultimo])
# Extrae la subcadena que esta entre las posiciones 0 a 3.
print(texto [0:3])
# Extrae la subcadena que está entre las posiciones 2 a 5.
print(texto [2:5])
# Extrae los 5 últimos caracteres.
print(texto [5:])

texto1 = "Hola \"Mundo\" de Python"
texto2 = "Lun\tMar\tMie\tJue\tVie"
texto3 = "Pepe\nJuan\nLuis"
#Métodos de las cadenas
print(texto.upper())
print(texto.lower())
print(texto.capitalize())
print(texto.title())
print(texto.count("t"))
print(len(texto))
subcadena = "tigres"
print(texto.index(subcadena))
#Cadenas multilínea
texto_grande = """
    Hola, este es un texto grande puedo usar retornos de carro  Adios """
print(texto_grande)
