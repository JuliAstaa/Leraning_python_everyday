#to access tuples item by referring number index, inside square bracket. like list
# ex:
myTuple = ('mobil', 'motor', 'acumalaka')
print(myTuple[1]) #output: motor

# negative index, -1 will be return the last item in tuples, -2 the second last item, etc.
# ex:
myTuple = ('mobil', 'motor', 'acumalaka')
print(myTuple[-1]) #output: acumalaka

# range of index
# ex:
foods = ('nasi goreng', 'sushi', 'pizza', 'burger', 'pasta')
print(foods[1:3]) # output: ('sushi', 'pizza')

#By leaving out the start value, the range will start at the first item:
foods = ('nasi goreng', 'sushi', 'pizza', 'burger', 'pasta')
print(foods[:3]) # output: ('nasi goreng', 'sushi', 'pizza')

#By leaving out the end value, the range will go on to the end of the tuple:
foods = ('nasi goreng', 'sushi', 'pizza', 'burger', 'pasta')
print(foods[2:]) # output: ('pizza', 'burger', 'pasta')

# negative index:
foods = ('nasi goreng', 'sushi', 'pizza', 'burger', 'pasta')
print(foods[-4:-1]) #output: ('sushi', 'pizza', 'burger')


# check item if exist
foods = ('nasi goreng', 'sushi', 'pizza', 'burger', 'pasta')
if 'sushi' in foods:
    print('Ada sushi coy')
else :
    print('gada sushi coy')

