# Los metodos en POO son funciones que pertenecen a una clase.
# Estos metodos pueden ser llamados desde los objetos creados a partir de la clase.

class Celular:
    def __init__(self, marca, modelo, precio): # Init es el constructor de la clase y se ejecuta al crear un objeto.
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def llamar(self):
        print(f"Llamando... desde un {self.marca} {self.modelo}")
    
    def colgar(self):
        print(f"Colgando... desde un {self.marca} {self.modelo}")


celular = Celular("Apple", "iPhone 12", 1000)
celular.llamar()
celular.colgar()