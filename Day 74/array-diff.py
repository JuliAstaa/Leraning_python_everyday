""" 
Your goal in this kata is to implement a difference function, which substracts one list from another and returns the result.

It should remove all values from list a, which are present in list b keeping their order.

array_diff([1, 2], [1]) -> [2]

If value in present in b, all of its occurences must be removed from the other:
array_diff([1,2,2,2,2,3], [2]) -> [1, 3]
"""

def array_diff(a:list[int], b:list[int]) -> list[int]:
    for digit in b:
        if digit in a:
            a = [x for x in a if x != digit]

    
    
    return a



#one line enjoyer
def array_diff(a:list[int], b:list[int]) -> list[int]:
    return [x for x in a if x not in b]

print(array_diff([1,2,2,2,2,3], [2]))