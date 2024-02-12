""" Write a Python program that takes a list of numbers and returns a new list containing only the even elements. """

def isEven(n):
    return [num for num in n if num % 2 == 0]
            
print(isEven([1,2,3,4,5,6,7,8,9,10]))