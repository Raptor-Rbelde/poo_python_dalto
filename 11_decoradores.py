# Los decoradores son funciones que reciben como parámetro una función y retornan otra función.
# Son muy útiles para agregar funcionalidades a una función sin modificarla.

def decorador(funcion):
    def funcion_modificada():
        print('Antes de ejecutar la función')
        funcion()
        print('Después de ejecutar la función')
    return funcion_modificada

# def saludo():
#     print('Hola')

# decorador(saludo)()

@decorador
def saludo():
    print('Hola')

saludo()