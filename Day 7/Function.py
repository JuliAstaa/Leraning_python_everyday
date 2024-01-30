# python function

def greeting ():
    print('Hello there')

greeting() #output: Hello there

def helloMyNameIs (name):
    print('Hello my name is ', name)
helloMyNameIs('Kirei D. Hana') #output: Hello my name is  Kirei D. Hana

# By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.

def people(name, age):
    greeting = str('Hello my name is {}, and i am {} y.o')
    print(greeting.format(name, age))
people('John Doe', 25) #output: Hello my name is John Doe, and i am 25 y.o

def myChild(*name):
    print('My youngest child is', name[len(name)-1])
myChild('Sasa', 'Skye', 'Obi One', 'Anakin') #output: My youngest child is Anakin

# keyword arguments
def heroes (jungler, midlaner, goldlane):
    print(F'Hyper carry is {jungler}')
heroes(midlaner='Lunox', goldlane='Claude', jungler='Ling') #outpu: Hyper carry is Ling


def echantingBooks(**book):
    print(F"I think i need { book['mending'] if book['mending'] == 'mending' else 'another'} enchanting books")
echantingBooks(mending='mending', silkTouch='silk touch') #output: I think i need mending enchanting books

def whereAreYouFrom(country = 'Indonesian'):
    print(F"Hello there, i'm from {country}")
whereAreYouFrom(country='Swedan') #output: Hello there, i'm from Swedan
whereAreYouFrom() #output: Hello there, i'm from Indonesian

# passing a list to function
def myCars(cars):
    for car in cars:
        print(F"i have {car} in my garage")

cars = ['Porche', 'Lamborginy', 'Supra']
myCars(cars)

"""
output:
i have Porche in my garage
i have Lamborginy in my garage
i have Supra in my garage
"""

# return value
def circle(r):
    return 3.14 * r ** 2
print(circle(7)) #output: 153.86

# the pass statement
# function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
def asalole():
    pass #output: no output

"""
Positional-Only Arguments
You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.

To specify that a function can have only positional arguments, add , / after the arguments:
"""

def myNum(num, /):
    print(F"My number is {num}")
myNum(4) #outpot: My number is 4

"""
Keyword-Only Arguments
To specify that a function can have only keyword arguments, add *, before the arguments:
"""

def myFavFood(*, food='Steak'):
    print(F"My favorite food is {food}")
myFavFood(food='Chicken Nugget') #output: My favorite food is Chicken Nugget

"""
Combine Positional-Only and Keyword-Only
You can combine the two argument types in the same function.

Any argument before the / , are positional-only, and any argument after the *, are keyword-only.
"""
def student(number, /, *, name):
    print(F"hello my name is {name}, and my number is {number}")
student(10, name='Hanamizaka') #output: hello my name is Hanamizaka, and my number is 10

# Recursion
"""
Python also accepts function recursion, which means a defined function can call itself.

Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.

The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.
"""

def factorial(n):
    result = 0
    if n == 1:
        return 1
    else:
        result = n * factorial(n - 1)
    return result

print(factorial(5))


