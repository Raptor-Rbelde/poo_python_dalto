# OCP o principio de abierto/cerrado, es un principio que nos dice que una clase debe\
# estar abierta para su extensión, pero cerrada para su modificación.

class Usuario:
    def __init__(self, nombre, email, sms):
        self.nombre = nombre
        self.email = email
        self.sms = sms

class Notificador():

    def notificar(self, usuario):
        raise NotImplementedError("Notificar no implementado")

class NotificadorEmail(Notificador):

    def notificar(self):
        print(f"Enviando email a {self.email}")
    

class NotificadorSMS(Notificador):
    def __init__(self, nombre, sms):
        self.nombre = nombre
        self.sms = sms
    
    def notificar(self):
        print(f"Enviando sms a {self.sms}")

Michael = Usuario("Michael", "micapor5@gmail.com", 73019931)

NotificadorEmail.notificar(Michael)
NotificadorSMS.notificar(Michael)

#Version ChatGPT
# class Usuario:
#     def __init__(self, nombre, email, sms):
#         self.nombre = nombre
#         self.email = email
#         self.sms = sms

# class Notificador:
#     def notificar(self, usuario):
#         raise NotImplementedError("Notificar no implementado")

# class NotificadorEmail(Notificador):
#     def notificar(self, usuario):
#         print(f"Enviando email a {usuario.email}")

# class NotificadorSMS(Notificador):
#     def notificar(self, usuario):
#         print(f"Enviando sms a {usuario.sms}")

# Michael = Usuario("Michael", "micapor5@gmail.com", 73019931)

# notificador_email = NotificadorEmail()
# notificador_sms = NotificadorSMS()

# notificador_email.notificar(Michael)
# notificador_sms.notificar(Michael)
