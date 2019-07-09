#A tuple is a collection which is ordered and unchangable. Allows duplicate members

#Create a tuple

fruits = ('Apples', 'Oranges', 'Grapes')
#fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

#single value need trailing comma
fruits2 = ('Apples',)

#get a value from a tuple
print(fruits[1])

# with tuples you can't change value
#fruits[0]='Pears'

#Delete tuple
del fruits2
#print(fruits2)

#Get the length of a tuple
print(len(fruits))


# A set is a collection which is unordered and unidexed. No duplicate members

#Create a set

fruits_set = {'Apples','Oranges','Mango'}

#Check if in set
print('Apples' in fruits_set)

#Add to set
fruits_set.add('Grape')
print(fruits_set)

#Remove from set
fruits_set.remove('Grape')
print(fruits_set)

#Clear set
fruits_set.clear()
print(fruits_set)

#clear is different to delete

#delete
del fruits_set
print(fruits_set)
