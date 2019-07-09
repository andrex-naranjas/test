#If/Else son condiciones que se usan para decidir de hacer algo basado en en algo que es verdadero o falso (boleanos)

x = 10
y = 5

#Poder usar operadores de comparacion (==, !=, >, <, >=, <=)

#simple if
if x > y:
   print('{0} es mas grande que {1}'.format(x,y))
else:
   print('{0} es mas grande que {1}'.format(y,x))

print('-----------')
    
if x > y:
    print('{0} es mas grande que {1}'.format(x,y))
elif x==y:
    print('{0} es igual que {1}'.format(y,x))    
else:
    print('{0} es menor que {1}'.format(x,y))
    

#if anidados

if x > 2:
  if x <= 10:
    print('{0} es mas grande que 2 e igual/menor a 10'.format(x))


#Una forma mejor de hacerlo: usar operadores logicos (and, or, not) se usan para combinar condicionales

#and
if x > 2 and x <= 10:
  print('{0} es mas grande que 2 e igual/menor a 10'.format(x))

#or  
if x > 2 or x <= 10:
  print('{0} es mas grande que 2 e igual/menor a 10'.format(x))

if not(x==y):
    print('{0} no es igual a {1}'.format(x,y))


#Operadores de membresia (not, not in) son usados para verificar si algo esta presente en un objeto

numbers = [1,2,3,4,5]
z = 5

# in
if z in numbers:
    print(z in numbers)

# not in
if z not in numbers:
    print(z not in numbers)

# is

if z is y:
    print(x is y)
