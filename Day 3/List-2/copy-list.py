#copy list
#ex:
list1 = ['rose', 'jasmine', 'orchid', 'lotus', 'cherry blossom', 'dahlia']
list2 = list1.copy()
list2.append('hibiscus')
print('Ini list 1', list1)
print('Ini list 2', list2)

#use built in func
#ex:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruits2 = list(fruits)
fruits2.insert(1, 'starfruit')
print('Ini list fruit ke-1 ',fruits)
print('Ini list fruit ke-2 ',fruits2)