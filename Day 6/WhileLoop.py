# while loop, with the while loop we can execute a set of statements as long as a condition is true.
# ex:
i = 0
while i < 10:
    print(i)
    i+=1
"""
output:
0
1
2
3
4
5
6
7
8
9
"""

# With the break statement we can stop the loop even if the while condition is true:
# ex
j = 0
while j < 10:
    print(j)
    if j == 3:
        break
    j+=1
"""
output:
0
1
2
3
"""
print('\n')
# With the continue statement we can stop the current iteration, and continue with the next:
# ex:
k = 0
while k < 10:
    k+=1
    if k == 3:
        continue
    print(k)
"""
output: 
1
2
4
5
6
7
8
9
10
"""

l = 0
while l < 10:
    print(l)
    l+=1
else:
    print('l is no longer than 6')
"""
output:
0
1
2
3
4
5
6
7
8
9
l is no longer than 6
"""