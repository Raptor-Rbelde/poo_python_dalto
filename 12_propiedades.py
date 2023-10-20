class Persona:
    def __init__(self, nombre, apellido):
        self.__nombre = nombre
        self.apellido = apellido
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @nombre.deleter
    def nombre(self):
        del self.__nombre


michael = Persona('Michael', 'Jordan')
nombre = michael.nombre
print(nombre)

nombre = michael.nombre = 'Mike'
print(nombre)

del michael.nombre
print(michael.nombre)