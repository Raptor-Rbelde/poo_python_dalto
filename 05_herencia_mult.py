# La herencia múltiple es una característica de los lenguajes de programación orientados a objetos
#en la que una clase puede heredar comportamiento y características de más de una clase base.

class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    
    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años"
    

class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
    
    def mostrar_habilidad(self):
        return f"Soy {self.nombre} y sé {self.habilidad}"


class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, trabajo, sueldo):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.trabajo = trabajo
        self.sueldo = sueldo
    
    def mostrar_habilidad(self):
        return "XD"
    
    def presentarse(self):
        return f"{super().mostrar_habilidad()}"
    

persona = EmpleadoArtista("Michael", 20, "Colombiano", "Programar", "Programador", 1000000)
print(persona.presentarse())


herencia = issubclass(EmpleadoArtista, Persona)
print(herencia)

instancia = isinstance(persona, Persona)
print(instancia)