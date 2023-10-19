# Los atributos en POO son variables que pertenecen a una clase.

class Celular:
    def __init__(self, marca, modelo, precio): # Init es el constructor de la clase y se ejecuta al crear un objeto.
        self.marca = marca
        self.modelo = modelo
        self.precio = precio


celular = Celular("Apple", "iPhone 12", 1000)
celular2 = Celular("Samsung", "Galaxy S20", 800)
print(celular.marca)
print(celular.modelo)
print(celular2.precio)