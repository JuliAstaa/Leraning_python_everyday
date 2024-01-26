# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
# syntax = newlist = [expression for item in iterable if condition == True]
# ex

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruitsWithLetterA = []

for fruit in fruits:
    if 'a' in fruit:
        fruitsWithLetterA.append(fruit)

print(fruitsWithLetterA)

# one line
print('\b')
print('One line')
flowers = ['rose', 'jasmine', 'orchid', 'lotus', 'cherry blossom', 'hibiscus', 'dahlia']
flowerWithLetterO = [flower for flower in flowers if 'o' or 'a' in flower]
print(flowerWithLetterO)
flowerWithoutRoseAnfJasmine = [flower for  flower in flowers if flower not in ['rose', 'jasmine']]
print('Flower without Rose and Jasmine', flowerWithoutRoseAnfJasmine)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evenNumber = [number for number in numbers if number % 2 == 0]
print(evenNumber)