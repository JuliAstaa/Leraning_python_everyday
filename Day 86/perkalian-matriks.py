"""  
Perkalian skalar pada matriks
"""

A = [[4, 2],
     [-1, 3]]

for i in range(len(A)):
    for j in range(len(A[i])):
        A[i][j] *= 5
        
print(A)