# El srp o principio de responsabilidad única, es un principio que nos
#dice que una clase debe tener una única responsabilidad, es decir, una única razón para cambiar.

class Auto:
    def __init__(self, tanque):
        self.tanque = tanque
        self.posicion = 0
    
    def mover(self, distancia):
        if self.tanque.obtener_combustible >= distancia / 2:
            self.posicion += distancia
            self.tanque.consumir_combustible(distancia / 2)
        else:
            print("No hay combustible suficiente")
    
    @property
    def obtener_posicion(self):
        return self.posicion


class GasolinaAuto:
    def __init__(self):
        self.combustible = 0
    
    def agregar_combustible(self, cantidad):
        self.combustible += cantidad
    
    @property
    def obtener_combustible(self):
        return self.combustible
    
    def consumir_combustible(self, cantidad):
        self.combustible -= cantidad

ferrari = Auto(GasolinaAuto())
ferrari.tanque.agregar_combustible(100)

ferrari.mover(10)
print(ferrari.obtener_posicion)
ferrari.mover(20)
print(ferrari.obtener_posicion)
ferrari.mover(80)
print(ferrari.obtener_posicion)
ferrari.tanque.agregar_combustible(100)
ferrari.mover(100)
print(ferrari.obtener_posicion)
ferrari.mover(100)
print(ferrari.obtener_posicion)