# El polimorfismo es la habilidad de tomar varias formas y es una de las caracteristicas de la POO
# En python se puede implementar de varias formas, una de ellas es la sobrecarga de operadores
# La sobrecarga de operadores permite cambiar el comportamiento de un operador
# Por ejemplo, el operador suma (+) puede sumar dos enteros o concatenar dos cadenas

class Gato:
    def sonido(self):
        print("Miau")

class Perro:
    def sonido(self):
        print("Guau")

def hacer_sonido(animal):
    animal.sonido()

gato = Gato()
perro = Perro()

hacer_sonido(gato)
perro.sonido()