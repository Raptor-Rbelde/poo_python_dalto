#Primer ejercicio para poner en practica lo aprendido hasta ahora.

class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    
    def estudiar(self):
        print(f"El estudiante {self.nombre} esta estudiando")


estudiante = Estudiante(input("Ingrese el nombre del estudiante: "), input("Ingrese la edad del estudiante: "),
                         input("Ingrese el grado del estudiante: "))

while True:
    print("Escriba 'estudiar' para que el estudiante estudie")
    estudiar = input("")
    if estudiar.lower() == "estudiar":
        estudiante.estudiar()
        break

# class Personaje:
#     def __init__(self, nombre, vida, ataque, defensa, estilo):
#         self.nombre = nombre
#         self.vida = vida
#         self.ataque = ataque
#         self.defensa = defensa
#         self.estilo = estilo
    
#     def atacar(self):
#         print(f"El personaje {self.nombre} esta atacando y le quita {self.ataque} de vida al enemigo")
#         print("\n")
    
#     def defender(self):
#         print(f"El personaje {self.nombre} esta defendiendo y se protege {self.defensa} del ataque del enemigo")
#         print("\n")




# personaje1 = Personaje("Goku", 100, 100, 100, "Saiyajin")
# personaje2 = Personaje("Pablo", 120, 121, 60, "Mago")

# personaje1.atacar()
# personaje2.defender()
# personaje2.atacar()