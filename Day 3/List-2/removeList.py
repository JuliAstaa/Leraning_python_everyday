#remove an item in list

#remove specified item use remove()
# ex:
fruits = ["banana", "kiwi", "apple"]
fruits.remove("banana")
print(fruits) #output:  ["kiwi", "apple"]

#remove speficied index, the pop() method remove specified index
# ex
animals = ['dog', 'monkey', 'elephant']
animals.pop(2) #will be remove item at index 2 
print(animals) #output ['dog', 'monkey']

# if pop() doesnt have specified index, it will remove the last item in list
# ex
flowers = ['rose', 'jasmine','lotus']
flowers.pop()
print(flowers) #output ['rose', 'jasmine']

# the del keyword also removes the specified index
# ex:
phones = ['xiaomi', 'samsung', 'huawei']
del phones[1]
print(phones) #outut ['xiaomi', 'huawei']

# the del keyword also can remove the list completly
# ex:
tv = ['LG', 'Samsung', 'TCL']
del tv # output: tv is not defined

# the clear() method empties the list, the list still exist but it has no content
colours = ['red', 'green', 'blue']
colours.clear()
print(colours) #output []