
peliculas = [
    ("Shrek", 90),
    ("Toy Story", 81),
    ("Buscando a Nemo", 100)
]

print("Películas iniciales:")
for pelicula in peliculas:
    print("Título:", pelicula[0], "- Duración:", pelicula[1], "minutos")

peliculas.append(("Los Increíbles", 115))

print("\nPelículas después de añadir una:")
for pelicula in peliculas:
    print("Título:", pelicula[0], "- Duración:", pelicula[1], "minutos")