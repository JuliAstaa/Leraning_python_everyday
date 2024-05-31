""" 
The fibbonacci numbers, commonly denoted F(n) from sequence, called the fibonnaci sequence, such that each number is the sum if the two preceding number ones, starting from 0 and 1. That is

 F(0) = 0, F(1) = 1
 F(n) = F(n-1) + F(n-2), for n > 1

 Given n, calculate F(n)

 Example:
 Input: n = 2
 Output: 1
 Explanation: F(2) = F(2-1) + f(2-2) = 1 + 0 = 1
 """

def fib(n: int) -> int:
    memo = {0: 0, 1: 1}

    def f(x):
        if x in memo:
            return memo[x]
        else :
            memo[x] = f(x-1) + f(x-2)
            return memo[x]
        
    return f(n)


def fib(n: int) -> int :
    if n == 0: 
        return 0
    if n == 1:
        return 1
    
    prev = 0
    cur = 1

    for i in range(2, n+1):
        prev, cur = cur, prev+cur
    
    return cur


print(fib(5))