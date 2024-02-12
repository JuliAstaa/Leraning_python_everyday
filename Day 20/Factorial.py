""" 
Create a Python program to calculate the factorial of a given number.
 """

def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n -1)
    
print(factorial(5))