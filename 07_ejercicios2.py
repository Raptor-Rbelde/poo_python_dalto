# Ejercicios para practicar

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def datos(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")


class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
    
    def fgrado(self):
        print(f"Grado: {self.grado}")

michael = Estudiante("Michael", 25, "10mo")
michael.datos()
michael.fgrado()


# class Animal:
#     def comer(self):
#         print("Comiendo")


# class Ave(Animal):
#     def volar(self):
#         print("Volando")

# class Mamifero(Animal):
#     def correr(self):
#         print("coriendo")

# class Murcielago(Mamifero, Ave):
#     pass

# murcielago = Murcielago()

# murcielago.comer()
# murcielago.correr()
# murcielago.volar()
