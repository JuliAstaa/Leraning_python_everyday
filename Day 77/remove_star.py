""" 
Example:
input: "leet*co**de"
output: "leede

input: "secret*****"
output: ""
"""

def erase_star(s: str) -> str:
    stack = []
    for c in s:
        if c is not "*":
            stack.append(c)
        else:
            if stack[-1] and c == "*":
                stack.pop()
    
    return "".join(stack)

print(erase_star("leet*co**de"))