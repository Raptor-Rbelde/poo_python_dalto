from abc import ABC, abstractmethod

class Persona(ABC):
    @abstractmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad

    def saludar(self):
        print(f'Hola, mi nombre es {self.nombre} y tengo {self.edad} años.')
    
    @abstractmethod
    def hacer_actividad(self):
        pass


class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
    
    def hacer_actividad(self):
        print(f"Hola, soy {self.nombre} y estoy estudiando {self.actividad}.")


class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
    
    def hacer_actividad(self):
        print(f"Actualmente estoy trabajando en el rubro de: {self.actividad}.")
    


jose = Estudiante("Michael", 17, "Masculino", "Programacion")
jose.saludar()
jose.hacer_actividad()

mario = Trabajador("Mario", 25, "Masculino", "Ingenieria")
mario.saludar()
mario.hacer_actividad()


# No se puede instanciar una clase abstracta
# La diferencia entre una clase abstracta y una clase normal es que la clase abstracta no se puede instanciar,
# es decir, no se puede crear un objeto de esa clase.
# La clase abstracta solo sirve para heredar sus atributos y métodos a otras clases.