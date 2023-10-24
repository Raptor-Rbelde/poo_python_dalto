# El isp o principio de segregación de interfaces, es un principio que
# nos dice que una clase no debe depender de métodos que no utiliza.
# Es decir, que una clase no debe depender de interfaces que no utiliza.

from abc import ABC, abstractmethod

class trabajar(ABC):
    @abstractmethod
    def trabajar(self):
        pass

class comer(ABC):
    @abstractmethod
    def comer(self):
        pass

class dormir(ABC):
    @abstractmethod
    def dormir(self):
        pass

class Persona(trabajar, comer, dormir):

    def trabajar(self):
        return "El humano esta trabajando"
    
    def comer(self):
        return "El humano esta comiendo"
    
    def dormir(self):
        return "El humano esta durmiendo"

class Robot(trabajar):
    def trabajar(self):
        return "El robot esta trabajando"
    

arturito = Robot()
print(arturito.trabajar())
# print(arturito.comer())

# En este caso, la clase Robot no puede comer ni dormir, por lo que no
# debería heredar de las clases comer y dormir, ya que no utiliza sus

Pedro = Persona()
print(Pedro.trabajar())
print(Pedro.comer())
print(Pedro.dormir())
