""" 
As part of this kata, you need to create a function that when provided with a triplet, return the middle index of the numerical element that lies between the other two elements.

The input to the function will be an list of three distinct number (Haskell: a tuple)

Example:
input: [2,3,1]
output: 0
explanation:
2 is the number that fits between 1 and 3 and the index of 2 in the input array is 0

input: [5, 10, 14]
output: 1

"""

def gimme(num_arr: list[int]) -> int:
    sorted_num = sorted(num_arr)
    return num_arr.index(sorted_num[1])

print(gimme([5, 10, 14]))