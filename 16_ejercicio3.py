class Personaje:
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad
    
    def __repr__(self):
        return f"{self.nombre}( Fuerza: {self.fuerza}, Velocidad: {self.velocidad})"
    
    def __add__(self, otro_personaje):
        nuevo_nomrbre = self.nombre + "-" + otro_personaje.nombre
        nueva_fuerza = round(((self.fuerza + otro_personaje.fuerza)/2)**1.5)
        nueva_velocidad = round(((self.velocidad + otro_personaje.velocidad)/2)**1.5)
        return Personaje(nuevo_nomrbre, nueva_fuerza, nueva_velocidad)

goku = Personaje("Goku", 100, 50)
vegeta = Personaje("Vegeta", 80, 60)

gogeta = goku + vegeta
print(gogeta) # Personaje(Goku-Vegeta, 90, 55)