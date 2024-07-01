""" 
Digital root is the recursive sum of all the digits in a number

Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way utnuk a single digit number is produced. The input will be a non-negative integer:

Example:
input: 16
output: 7
explanation: 16 -> 1 + 6 -> 7

input: 942
output: 6
explanation: 942  ->  9 + 4 + 2 = 15  ->  1 + 5 = 6
"""

def digital_root(n: int) -> int:
   if n < 10: return n
   n = sum([int(digit) for digit in str(n)])
   return digital_root(n)
   

print(digital_root(972))

      
