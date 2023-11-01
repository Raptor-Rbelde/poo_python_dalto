# El dip o principio de inversión de dependencias, es un principio que
# nos dice que las clases de alto nivel no deben depender de las clases de bajo nivel.

from abc import ABC, abstractmethod

class VerificadorOrtografico(ABC):
    @abstractmethod
    def verificar_palabra(self, palabra):
        pass

class Diccionario(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        # Logica para verificar en diccionario
        pass

class CorrectorOrtografico:
    def __init__(self, verificador):
       self.verificador = verificador
    
    def corregir_texto(self, texto):
        # Usamos el verificador para corregir el texto
        pass
    

corrector = CorrectorOrtografico(Diccionario())