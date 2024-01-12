# Lista
pokemones = ["Charizard", "Mimikyu", "Pikachu", "Snorlax", "Arcanine"]
print (pokemones[1])
pokemones [1] = "I pick U"
print (pokemones [-4])
print (pokemones [1:4])
print (pokemones [:4])
print (pokemones [1:])

# Tupla 
pokemones = ("Charizard", "Mimikyu", "Pikachu", "Snorlax", "Arcanine")

# Diccionarios 
pokemones = {
    "Charizard": "Fuego",
    "Mimikyu": "Fantasma",
    "Pikachu": "Eléctrico",
    "Snorlax": "Normal",
    "Arcanine": "Fuego"
}
print(pokemones)
print(pokemones["Snorlax"])

# Conjuntos
pokemones = ["Charizard", "Mimikyu", "Pikachu", "Snorlax", "Arcanine"]
pokemones.insert (4, "I pick U")
pokemones.insert (0, "Trabbish")
pokemones.remove ("Pikachu")

print("Mimikyu" in pokemones)

print(len (pokemones))

# Estructuras Mixtas 
equipo_pokemon = [
    {"nombre": "Charizard", "Tipo": ["Fuego"]},
    {"nombre": "Mimikyu", "Tipo": ["Fantasma"]},
    {"nombre": "Pikachu", "Tipo": ["Eléctrico"]},
    {"nombre": "Snorlax", "Tipo": ["Normal"]},
    {"nombre": "Arcanine", "Tipo": ["Fuego"]}
]
print(equipo_pokemon[2]["nombre"])

# Recursividad
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
resultado = factorial(4)
print("El factorial es:", resultado)

print("hello world")