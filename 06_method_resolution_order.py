# MRO

# El metodo de resolucion de orden es el orden en el que se van a ejecutar los metodos
# cuando se hace una llamada a un metodo de una clase que hereda de otras clases
# en python se puede ver el orden de resolucion de orden con el metodo mro


class F():
    def hablar(self):
        print('Soy de clase F')


class A (F):
    pass

class B(A):
    pass



class C(A):
    pass

class D(B, C):
    pass

class E(D, F):
    pass

e = E()
e.hablar()

C.hablar(e)

# MRO
print(E.mro())