class Auto:
    def __init__(self):
        self._estado = "apagado"
    
    def encender(self):
        self._estado = "encendido"

    def conducir(self):
        if self._estado == "apagado":
            self._estado = "encendido"
        print("Conduciendo")


carro = Auto()
carro.encender()
carro.conducir()