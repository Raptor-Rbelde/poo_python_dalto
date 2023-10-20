# Los getters y setters son decoradores que nos permiten acceder y modificar atributos de una clase.
# Estos con la finalidad de proteger los datos de la clase.


class Persona:
    def __init__(self, nombre, apellido):
        self.__nombre = nombre
        self.apellido = apellido
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre




michael = Persona('Michael', 'Jordan')
print(michael.get_nombre())
michael.set_nombre('Mike')
persona = michael.get_nombre()
print(persona)