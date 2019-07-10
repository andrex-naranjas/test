# Una clase es como un plano para crear objetos. Un objeto tiene propiedades y metodos (funciones) asociadas a el. Casi todo en python es un objeto (clase)

#Create a class
class Usuario:
    #Constructor (funcion que corre cuando haces una instanciacion d una clase)
    def __init__(self, nombre, email, edad):
        self.nombre = nombre
        self.email = email
        self.edad = edad

    def saludos(self,num1=1):
        print(num1)
        return 'Me llamo {0} y tengo {1}'.format(self.nombre,self.edad)

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
        return 'Me llamo {0}, tengo {1} y mi saldo es {2}'.format(self.nombre,self.edad,self.saldo)
        
        
#Init un objeto para el usuario
Andres = Usuario('Andres Ramirez','andres@gmail.com',31)
print(type(Andres))
print(Andres.nombre)
print(Andres.saludos('d'))

Andres.tengo_cumple()
print(Andres.saludos())

print('--------------------------')

#Init un Cliente
Rufina_usuario = Usuario('Rufina Madrid', 'rufina@yahoo.com',2)
Rufina_cliente = Cliente('Rufina Madrid', 'rufina@yahoo.com',2)
Rufina_cliente.establecer_saldo(5e10)
print(Rufina_cliente.saludos())
print(Rufina_usuario.saludos())
