""" 
Given an array of integers.

Return an array, where the first element is the count of positive numbers and the second element is sum of negative numbers. 0 is neither positive nor netagive.

If the input is an empty array or is null, return an empty array

Example:
input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
output: [10, -65]
"""

def count_positives_sum_negatives(arr: list[int]) -> list[int]:
    if len(arr) == 0: return []
    positive = 0
    negative = 0
    for num in arr:
        if num > 0:
            positive += 1
        if num < 0:
            negative += num
        
        

    return [positive, negative]




#one line enjoyer
def count_positives_sum_negatives(arr: list[int]) -> list[int]:
    return [sum(n > 0 for n in arr), sum(n for n in arr if n < 0) if arr else []]

print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))