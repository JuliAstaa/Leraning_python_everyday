def fibbonaci(n: int) -> int:
    prev, curr = 0, 1

    for i in range(2, n+1):
        prev, curr = curr, prev + curr
    
    return curr

print(fibbonaci(100))