""" 
A format for expressing an ordered list of integers is to use a comma separated list of either
    - individual integers
    - or a range of integers denoted by the starting integer separated frim the end integer in the range by a dash "-". The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"

Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format

Example
input: [-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 20]
output: "-10--8, -6, -3, -1-3, 3-5, 7-11, 14, 15, 17, 20"
"""

def solution(numbers):
    if not numbers:
        return []
    
    result = []
    start = numbers[0]
    end = numbers[0]

    for i in range(1, len(numbers)):
        if numbers[i] == end + 1:
            end = numbers[i]
        else:
            if start == end or start == start + 1:
                result.append(str(start))
            elif start + 1 == end:
                result.append(f"{start},{end}")    
            else:
                result.append(f"{start}-{end}")    
            start = numbers[i]
            end = numbers[i]
                

    
    if start == end:
        result.append(str(start))
    elif start + 1 == end:
        result.append(f"{start},{end}")   
    else:
        result.append(f"{start}-{end}")


    
    return ",".join(result)

print(solution([-35, -34]))

