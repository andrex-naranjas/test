# Un for loop es utilizado para iterar sobre una secuencia (puede ser una lista, un diccionario, un conjunto o una string)

#Simple loop
people = ['Andres', 'Alejandra', 'Benito', 'Jose']

print('****Simple loop****')
for person in people:
  print('Current Person: {0}'.format(person))

#Break
print('****Break loop****')
for person in people:
    if person == 'Benito':
        break
    print('Current Person: {0}'.format(person))

#Continue
print('****Continue loop****')
for person in people:
    if person == 'Benito':
       continue
    print('Current Person: {0}'.format(person))
    print('Esta orden tiene que estar indentada')


print('****Range loop****')
#range
for i in range(len(people)):
    print(people[i])

for i in range(0,len(people)):
    print('Number: {0}'.format(i))
    print('Orden extra para ver la importancia de indentacion')

    
#While loops: hasta que se cumpla una condicion

count = 0
while count <= 10:
    print('Count: {0}'.format(count))
    count+=1
