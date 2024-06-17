""" 
Given an array of integers yout solution find th esmallest integer

Example:
input: [34, 25, 88, 2]
output: 2

 """

def find_smallest_int(arr: list[int]) -> int:
    
    # return int(min(arr))

    smallest = None

    for i in arr:
        if smallest is None or smallest > i:
            smallest = i
    
    return smallest

print(find_smallest_int([34, 25, 88, 2]))