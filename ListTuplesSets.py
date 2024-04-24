fruits = ['Grapes', 'Strawberry', 'Guava', 'Banana', 'Mango']
fruits2 = ['Apple']
print(fruits)
#Finding Length of a list
print(len(fruits))
#Accessing elements of list
print(fruits[3])
print(fruits[:2])
#Append(Adding at back)
fruits.append('Musk Melon')
print(fruits)
#Insert(Adding in front)
fruits.insert(2,'Lichi')
print(fruits)
#List within list
#fruits.insert(2,fruits2)
#print(fruits)
#fruits.extend(fruits2)
#Removing specified items from list
fruits.remove('Grapes')
print(fruits)
#removing last item from a list
fruits.pop()
print(fruits)
#Sorting lists
fruits.sort()
print(fruits)
nums = [1,2,3,4,5]
nums.reverse()
print(nums)
#Find index of a particular element in a list
print(fruits.index('Banana'))
#Check for elements in list
print('Kiwi' in fruits)
print('Guava' in fruits)
#looping through lists
for index,item in enumerate(fruits):
    print(index,item)
#LISTS ARE MUTABLE AND TUPLES ARE IMMUTABLE
#WHEN TO USE TUPLES AND LISTS?
#TO LOOP THROUGH AND ACCESS USE TUPLES
#TO MODIFY AND MAKE CHANGES USE LISTS
#Tuple
fruits_tuple = ('Kiwi', 'Banana', 'Apple','Cherry')
#SETS
#VERY DIFFERENT PURPOSE FROM LISTS AND TUPLES
#PURPOSE
#TO FILTER OUT DUPLICATE VALUES
#TO CHECK IF A VALUE IS PRESENT IN A SET
#AT EACH RUNTIME THE ORDER OF THE ELEMENT WILL BE DIFFERENT
fruits_set = {'Apple', 'Mango', 'Kiwi', 'Jam', 'Blueberry','Tomato'}
#Same in tuples but sets does it more efficiently
print('Mango' in fruits_set)
#Intersection
vegetable_set = {'Tomato','Raddish','Brinjal'}
print(fruits_set.intersection(vegetable_set))
print(fruits_set.difference(vegetable_set))
print(fruits_set.union(vegetable_set))
#Empty
#Empty list
empty_list = []
#Empty set
empty_set = set()
#empty tuple
empty_tuple = ()
