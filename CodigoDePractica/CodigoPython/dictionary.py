# A dictionary is a collection which is unordered, changable and indexed. No duplicated members

#Create dict
person = {
    'first_name': 'Andres',
    'last_name': 'Ramirez',
    'age': 30
    }

#use constructor
person2 = dict(first_name='Rufina', last_name='Max')

print(person,type(person))
print(person2,type(person2))

#get value
print(person['first_name'])
print(person.get('last_name'))

#Add key value
person['telefono'] = '4925448852'
print(person)

#Get dict keys and items
print(person.keys())
print(person.items())

#Copy dict
person2 = person.copy()
person2['ciudad'] = 'Zacatecas'
print(person2)

#remove an item
del(person['age']) #or pop
print(person)

#Clear
person.clear()
print(person)

#Get lenght
print(len(person2))



#List of dictionaries

people = [

    {'nombre': 'Andres', 'edad': 31},
    {'nombre': 'Rufina', 'edad': 2}

    ]

print("---------")
print(people)

print("---------")
print(people[1]['nombre'])
