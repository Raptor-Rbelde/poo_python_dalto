# Los metodos dunder son metodos especiales que tienen doble guion bajo al inicio
# y al final del nombre del metodo
# Estos metodos son llamados automaticamente por python dependiendo de la accion
# que se este realizando con el objeto

# __init__ es un metodo dunder que se ejecuta automaticamente al crear un objeto
# __str__ es un metodo dunder que se ejecuta automaticamente al imprimir el objeto
# __len__ es un metodo dunder que se ejecuta automaticamente al usar la funcion len() con el objeto
# __del__ es un metodo dunder que se ejecuta automaticamente al eliminar el objeto
# __add__ es un metodo dunder que se ejecuta automaticamente al sumar el objeto con otro objeto

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"

    def __len__(self):
        return self.edad

    def __del__(self):
        print("Se ha eliminado el objeto")

    def __add__(self, other):
        return self.edad + other.edad

persona1 = Persona("Juan", 28)
persona2 = Persona("Carlos", 30)

print(persona1 + persona2)