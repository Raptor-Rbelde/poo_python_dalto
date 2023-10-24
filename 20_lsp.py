# El lsp o principio de sustitución de Liskov, es un principio que
# nos dice que una clase base debe poder ser sustituida por cualquier clase derivada
# de esta, sin alterar el comportamiento del programa.
# Es decir, que una clase derivada debe poder ser sustituida por su clase base.

# class Pajaro:
#     def volar(self):
#         print("El pajaro está volando")

# class Pinguino(Pajaro):
#     def volar(self):
#         print("El pinguino no puede volar")


# def hacer_volar(ave):
#     return ave.volar()

# pajaro = Pajaro()
# pinguino = Pinguino()
# hacer_volar(pajaro)
# hacer_volar(pinguino)

class Ave:
    def __init__(self, especie):
        self.especie = especie

class AveVoladora(Ave):
    def volar(self):
        print(f"El ave {self.especie} está volando")

class AveNoVoladora(Ave):
    def volar(self):
        print(f"El ave {self.especie} no puede volar")


tucan = AveVoladora("Tucan")
pinguino = AveNoVoladora("Pinguino")
tucan.volar()
pinguino.volar()