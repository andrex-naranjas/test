#A list is a collection which is ordered and changable. Allows duplicate membe
#Prueba de git

#Create a list, 1st way to do it
numbers = [1,2,3,4,5]
fruits = ['Apples','Oranges', 'Grapes','Pears']

#Create a list, use a constructor
numbers2 = list((1,2,3,4,5))

print(numbers,fruits)

#Get a value of a list
print(fruits[0])

#Get length

print(len(fruits))

#Append to the list

fruits.append('Mangos')
print(fruits)

#Remove from the list
fruits.remove('Grapes')
print(fruits)

#Insert to position
fruits.insert(2,"Strawberries")
print(fruits)

#Remove from a position, with pop
fruits.pop(2)
print(fruits)

#Reverse the list
fruits.reverse()
print(fruits)

#sort alphbetically
fruits.sort()
print(fruits)

#Reverse sort
fruits.sort(reverse=True)
print(fruits)

#change a value

fruits[0]='Blueberries'
print(fruits)
