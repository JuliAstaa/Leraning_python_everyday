"""  
Description:
Define a function that takes an intefer argument and returns a logical value True or False depending on if the integer is a prime.

per Wikipediam, a prime number  ( or a prime ) is a natural number greater than 1 that has no positive disivors other than 1 and itself

Requirements:
1. You can assume you will be given an integer input.
2. You can't assume that the interger will be only positive. You may be given negative numbers as well ( or 0)
3. NOTE on performance: There are no fancy optimizations required, but still the most trivial solutions might time out. Number go up to 2^31(or similiar, depending on language). Looping all the way up to n or n/2, will be too slow.

Example:
input: 1
output: False

input: 2
output: True

input: -1 
output: False
"""
from math import sqrt

def is_prime(num):
    if num <= 1: return True
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0: return False
    return True

print(is_prime(17))