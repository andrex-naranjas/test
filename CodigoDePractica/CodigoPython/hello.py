#This is a small program to practice python

"""
VARIABLE RULES
-Variable names are case sensitive (name and NAME are different)
-Must start with a letter or an underscore
-Can have numbers but can not start with one
"""

#print function
print('Hello cold world')


x = 1           # int
y = 2.5         # float
name = 'Andres' # str
is_cool = True  # bool

#Multiple definicion
x, y, name, is_cool = (1,2.5, 'Andres', True)



#matematicas basicas
a = x + y

print(x,y,name,is_cool,a)

#checar el tipo de x
print(type(x))

#cast, e.g. x to string

x = str(x) #passing x
y = int(y)  # passing y
z = float(y)

print(type(y),y)
print(type(z),z)
