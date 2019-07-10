#create a class
import datetime
miFecha= datetime.date.today()

class Usuario:
     def __init__(self,nombre,edad,fecha):
        self.nombre = nombre
        self.edad = edad
        self.fecha=miFecha
     def saludos(self,fecha):
	print(fecha)
        return "Me llamo {0} y tengo:{1} y llegue a las {2}".format(nombre,edad,fecha)

#init un objeto para el usuario
Leslie= Usuario("Leslie Mayte",18,miFecha)

