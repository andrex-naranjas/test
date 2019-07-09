#Strings in python are sorrounded by either single or double quotation marks.
#lets look at string formatting and some strings methods

name = 'Andres'
age = 31


#Concatenate
print('Hello, my name is ' + name + ' and I am ' + str(age))

# better way

#strin formmating

#arguments by position
print('My name is {name} and I am {age}'.format(name=name, age=age))
#{}== basically place holders


#another way to do it (python 3.6 and after)
#F-Strings
print(f'Hello, my name is {name} and I am {age}')


#String methods

s = 'hello world'

#capitilize string
print(s.capitalize())


#more methods
#Get lenght
print(len(s))


#revisar las demas funciones
