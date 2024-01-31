"""
A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.
"""
"""
syntax
lambda arguments: expressionKO
"""

x = lambda x: x* 5

print(x(10)) #output: 50

"""
Why Use Lambda Functions?
The power of lambda is better shown when you use them as an anonymous function inside another function.

Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number
"""

def sum(n):
    return lambda a: a+n

sumTheNumber = sum(4)
print(sumTheNumber(5)) #output: 9
