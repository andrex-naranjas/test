#Un modulo es basicamente un archivo que contiene un conjunto de funciones para incluir en tu aplicacion. Hay modulos basicos en el nucleo de python, tambien modulos que puedes instalar usando el administrador "pip" y finalmente modulos personalizados

#importar un modulo de python que tiene por default

import datetime
hoy = datetime.date.today()
print(hoy)

from datetime import date
hoy2 = date.today()
print(hoy2)

import time
estampatemporal = time.time()
print(estampatemporal)


from time import time
estampatemporal2 = time()
print(estampatemporal2)


#administrador para instalar modulos externos
#modulo camel case
#pip --version
#pip install camel case
#pip freeze

#from camelcase import CamelCase

#instancion o instancia de camel case
#c = CamelCase()
#print(c.hump('hola otra vez mundo'))


# #Modulo personalizado
import validator
from validator import validate_email

email = 'prueba@prueba.com'
if validate_email(email):
    print('El correo esta bien escrito')
else:
    print('El correo esta mal escrito')

