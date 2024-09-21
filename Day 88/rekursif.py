def fibbonaci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibbonaci(n-1) + fibbonaci(n-2)

print(fibbonaci(5))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
  
print(factorial(5))

class Recursive:
    def __init__(self, n):
        self.n = n
  
    def fibbonaci(self):
        if self.n == 0:
            return 0
        elif self.n == 1:
            return 1
        else:
            return fibbonaci(self.n-1) + fibbonaci(self.n-2)
  
    def factorial(self):
        if self.n == 0:
            return 1
        else:
            return self.n * factorial(self.n-1)

nilai = 5
recursive = Recursive(nilai)
print(f"Fibonaci dari {nilai} adalah {recursive.fibbonaci()}")
print(f"Faktorial dari {nilai} adalah {recursive.factorial()}")