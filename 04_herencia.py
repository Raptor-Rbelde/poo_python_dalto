# La herencia es una forma de crear una clase usando otra clase como base.
# Es decir, una clase hija hereda todos los atributos y métodos de la clase padre.
# Esto es muy útil porque podemos crear una clase padre con atributos y métodos genéricos y
#luego crear clases hijas más específicas con sus propios atributos y métodos.

class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años")
    

class Empleado(Persona): # La clase Empleado hereda de la clase Persona
    def __init__(self, nombre, edad, nacionalidad, trabajo, sueldo):
        super().__init__(nombre, edad, nacionalidad) # Con super() llamamos al constructor de la clase padre
        self.trabajo = trabajo
        self.sueldo = sueldo
        

class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, notas, universidad):
        super().__init__(nombre, edad, nacionalidad)
        self.notas = notas
        self.universidad = universidad


michael = Empleado("Michael", 20, "Colombiano", "Programador", 1000000)
print(michael.sueldo)
michael.saludar() 