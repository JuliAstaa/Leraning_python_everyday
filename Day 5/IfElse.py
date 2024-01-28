"""
Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
"""


# ex
a = 10
b = 20
print(a > b) #output: false
print(a < b) #output: true
print( a== b) #output: false
print(a != b) #output: true
print(a <= b) #output: true
print(a >= b) #output: false


# if statement
x = 10
y = 15
if x > y: #output: Y greater than X
    print('X greater than Y')
else:
    print('Y greater than X')


# elif
c = 25
d = 20
if c < d : #output: C greater than D
    print('C less than D')
elif c > d:
    print('C greater than D')
else :
    print('Both are has same value')

# short hand if
e = 10
f = 11
if f > e: print('F greater than E') #output: F greater than E

# short hand if else
g = 2
h = 200
print('G greater than H') if g > h else print('H greater than G') #output: H greater than G


# ternary operator
h = 32  
i = 30
print('H') if h == i else print('>') if h > i else print('I') #output: >

# conditional expression
# and
j = 5
k = 5
l = 5
if j == k and k == l:
    print('They are same') #output: they are same


# or
m = 5
n = 6
o = 7
if m > n or n < o: print('At least one of them true') #outout: At least one of them true

# not
p = 25
q = 30

if not p > q: print('P is NOT greater than Q') #output: P is NOT greater than Q

r = 50
if r > 20:
    print('more than 20')
    if r > 40:
        print('more than 40')
    else:
        print('Not more than 40')
"""
output:
more than 20
more than 40
"""

# the past statement
# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.

s = 20
t = 25
if s < t:
    pass #output: no output