# to add an item to the end of the list use the append()
# ex:

fruits = ['cocoa', 'banana', 'orange']
fruits.append('jackfruits')
print(fruits)


# to add an item at specific index, use insert(), insert have 2 parameter, 1st one is for where we want to add the item, secondly what we want to add
# ex:

flowers = ['rose', 'violet', 'tulip']
flowers.insert(2, 'jasmine')
print(flowers)


# to appends element from another list, use extend()
# ex:

dogs = ['cihuaha', 'pitbull', 'golden']
cats = ['persia', 'anggora', 'totol']
dogs.extend(cats)
print(dogs)

