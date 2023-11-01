import random

class Pokemon:
    def __init__(self, nombre, tipo, hp):
        self.nombre = nombre
        self.tipo = tipo
        self.hp = hp

    def __str__(self):
        return f"{self.nombre} ({self.tipo}) {self.hp}"

class Ataque:
    def __init__(self, nombre, power):
        self.nombre = nombre
        self.power = power

    def atacar(self, user, target):
        target.hp -= self.power

class AtaqueFuego(Ataque):
    def __init__(self, nombre):
       super().__init__(nombre, 0)
       self.power = self.set_power(nombre)

    def set_power(self, nombre):
        if nombre == "Ember":
            return 40
        elif nombre == "Fire Blast":
            return 120
        elif nombre == "Flamethrower":
            return 90
        else:
            raise ValueError("Ataque no válido")

class AtaqueAgua(Ataque):
    def __init__(self, nombre):
        super().__init__(nombre, 0)
        self.power = self.set_power(nombre)

    def set_power(self, nombre):
        if nombre == "Surf":
            return 60
        elif nombre == "Hydro Pump":
            return 110
        elif nombre == "Aqua Jet":
            return 40
        else:
            raise ValueError("Ataque no válido")


class AtaquePlanta(Ataque):
    def __init__(self, nombre):
        super().__init__(nombre, 0)
        self.power = self.set_power(nombre)

    def set_power(self, nombre):
        if nombre == "Vine Whip":
            return 45
        elif nombre == "Razor Leaf":
            return 55
        elif nombre == "Solar Beam":
            return 120
        else:
            raise ValueError("Ataque no válido")

usuario = input("Ingrese el nombre del Pokémon con el que desea jugar: ")
tipo_usr = input("Ingrese el tipo de Pokémon: ")
pokemon_usuario = Pokemon(usuario, tipo_usr, 100)

pokemon_en = {"charmander": ["fuego", 100], "squirtle": ["agua", 100], "bulbasaur": ["planta", 100]}
seleccion = random.choice(list(pokemon_en.keys()))
pokemon_enemigo = Pokemon(seleccion, pokemon_en[seleccion][0], pokemon_en[seleccion][1])
print("el tipo de pokemon enemigo es: ", pokemon_enemigo.tipo)

while pokemon_usuario.hp > 0 and pokemon_enemigo.hp > 0:
    # Turno Enemigo


    if pokemon_enemigo.tipo == "fuego":
        ataque_enemigo = ["Ember", "Fire Blast", "Flamethrower"]
    elif pokemon_enemigo.tipo == "agua":
        ataque_enemigo = ["Surf", "Hydro Pump", "Aqua Jet"]
    elif pokemon_enemigo.tipo == "planta":
        ataque_enemigo = ["Vine Whip", "Razor Leaf", "Solar Beam"]
    
    eleccion = random.choice(ataque_enemigo)
    ataque_enemigo = None

    if pokemon_enemigo.tipo == "fuego":
        ataque_enemigo = AtaqueFuego(eleccion)
    elif pokemon_enemigo.tipo == "agua":
        ataque_enemigo = AtaqueAgua(eleccion)
    elif pokemon_enemigo.tipo == "planta":
        ataque_enemigo = AtaquePlanta(eleccion)
    
    ataque_enemigo.atacar(pokemon_enemigo, pokemon_usuario)
    print(f"El Pokémon enemigo atacó con {ataque_enemigo.nombre}")
    print(f"{pokemon_usuario.nombre} tiene {pokemon_usuario.hp} de vida")

    # Turno Usuario
    if pokemon_usuario.tipo == "fuego":
        print("Los ataques disponibles son: Ember, Fire Blast, Flamethrower")
        eleccion_usr = input("Ingrese el ataque: ")
    elif pokemon_usuario.tipo == "agua":
        print("Los ataques disponibles son: Surf, Hydro Pump, Aqua Jet")
        eleccion_usr = input("Ingrese el ataque: ")
    elif pokemon_usuario.tipo == "planta":
        print("Los ataques disponibles son: Vine Whip, Razor Leaf, Solar Beam")
        eleccion_usr = input("Ingrese el ataque: ")

    if pokemon_usuario.tipo == "fuego":
        ataque_usuario = AtaqueFuego(eleccion_usr)
    elif pokemon_usuario.tipo == "agua":
        ataque_usuario = AtaqueAgua(eleccion_usr)
    elif pokemon_usuario.tipo == "planta":
        ataque_usuario = AtaquePlanta(eleccion_usr)
    
    ataque_usuario.atacar(pokemon_usuario, pokemon_enemigo)
    print(f"El Pokémon usuario atacó con {ataque_usuario.nombre}")
    print(f"{pokemon_enemigo.nombre} tiene {pokemon_enemigo.hp} de vida")

print("El juego ha terminado")