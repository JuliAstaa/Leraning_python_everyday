# foor loop
"""
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
"""

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print( fruit)
"""
output:
apple
banana
cherry
"""

# Even strings are iterable objects, they contain a sequence of characters:
# ex:
for letter in 'I Made Juli Astawa':
    print(letter)
"""
output:
I

M
a
d
e

J
u
l
i

A
s
t
a
w
a
"""

listPerempuan = ["Hana", "Sofia", "Aisha", "Bella", "Jasmine",]

for nama in listPerempuan:
    print(nama)
    if nama== 'Sofia':
        break
"""
output:
Hana
Sofia
"""

listMakanan = ["Sushi", "Pizza", "Nasi Goreng", "Pad Thai", "Spaghetti Carbonara"]
for makanan in listMakanan:
    print(makanan)
    if makanan == 'Pizza':
        continue
"""
output: 
Sushi
Pizza
Nasi Goreng
Pad Thai
Spaghetti Carbonara
"""

# the range() function
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

for x in range(10):
    print(x)
"""
output:
0
1
2
3
4
5
6
7
8
9
"""

# The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):
for z in range(2, 6):
    print(z)
"""
output:
2
3
4
5
"""

# The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):
# Increment the sequence with 3 (default is 1)
for y in range(0, 60, 5):
    print(y)
"""
output:
5
10
15
20
25
30
35
40
45
50
55
"""

# nested for loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for ad in adj:
    for fruit in fruits:
        print(ad, fruit)
"""
output:
red apple
red banana
red cherry
big apple
big banana
big cherry
tasty apple
tasty banana
tasty cherry
"""
