# Una clase es como un plano para crear objetos. Un objeto tiene propiedades y metodos (funciones) asociadas a el. Casi todo en python es un objeto (clase)

#Create a class
class Usuario:
    #Constructor (funcion que corre cuando haces una instanciacion d una clase)
    def __init__(self, nombre, email, edad):
        self.nombre = nombre
        self.email = email
        self.edad = edad

    def saludos(self):
        return f'Me llamo {self.nombre} y tengo {self.edad}'

    def tengo_cumple(self):
        self.edad+=1

#Extender la clase Usuario
class Cliente(Usuario):
    #Constructor (funcion que corre cuando haces una instanciacion d una clase)
    def __init__(self, nombre, email, edad):
        self.nombre = nombre
        self.email = email
        self.edad = edad
        self.saldo = 0

    def establecer_saldo(self,saldo):
        self.saldo = saldo
        
    def saludos(self):
        return f'Me llamo {self.nombre}, tengo {self.edad} y mi saldo es {self.saldo}'

        
#Init un objeto para el usuario
Andres = Usuario('Andres Ramirez','andres@gmail.com',31)
print(type(Andres))
print(Andres.nombre)
print(Andres.saludos())

Andres.tengo_cumple()
print(Andres.saludos())

print('--------------------------')

#Init un Cliente
Rufina = Cliente('Rufina Madrid', 'rufina@yahoo.com',2)
Rufina.establecer_saldo(500)
print(Rufina.saludos())
