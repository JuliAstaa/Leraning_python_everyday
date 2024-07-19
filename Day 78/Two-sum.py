"""  
should find two different items in the array that, when added together, give the target value, THe indices of these items should then be returned in a tupple or list like so: (index1, index2)

For the purpose of this kata, some tests may habe multiple aswers: any valid solution will be accepted.

The input will always be valid (numbers will be an array of length 2 or greater, and all of the items will be numbers: target will always be the sum of two different items from that array).

Example:
two_sum([1, 2, 3], 4) # returns (0, 2) or (2, 0)
two_sum([3, 2, 4], 6) # returns (1, 2) or (2, 1)

link question : https://www.codewars.com/kata/52c31f8e6605bcc646000082/train/python
"""

def two_sum(numbers, target):
    checked = {}
    for i, num in enumerate(numbers):
        complement = target - num

        if complement in checked:
            return (checked[complement], i)
        
        
        checked[num] = i


            

print(two_sum([2,2,3], 4))
