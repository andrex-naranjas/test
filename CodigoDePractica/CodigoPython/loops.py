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
# print('****Continue loop****')
# for person in people:
#     if person == 'Benito':
#         continue
#     print(f'Current Person: {person}')


# print('****Range loop****')
# #range
# for i in range(len(people)):
#     print(people[i])

# for i in range(0,11):
#     print(f'Number: {i}')

    
# #While loops: hasta que se cumpla una condicion

# count = 0
# while count <= 10:
#     print(f'Count: {count}')
#     count+=1
