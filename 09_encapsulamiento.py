# El encapsulaiento es una forma de proteger los datos de una clase
# para que no puedan ser accedidos desde fuera de la clase.
# En Python no existe el encapsulamiento como tal, pero se puede simular
# usando convenciones de nombres.

class MiClase:
    def __init__(self):
        self.__atributo_privado = 5
        self._atributo_semiprivado = 10


objeto = MiClase()
print(objeto._atributo_semiprivado)
print(objeto.__atributo_privado)