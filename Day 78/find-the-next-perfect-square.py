""" 
You might know some pretty large perfect squares. But what about the next one?

Complete the find_next_squares method that finds the next intergral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer

If the argument is itself not a perfect square then return either -1 or an empty value like None or null, depending on your language. You may assumne the argument is non-negative

EXAMPLE:
Input: 121
Output: 144
"""
import math
def find_next_square(sq: int) -> int:
    sqrt = math.sqrt(sq)
    perfect_sqrt = int(sqrt)

    return -1 if sqrt != perfect_sqrt else (perfect_sqrt + 1) ** 2

print(find_next_square(15241383936))
