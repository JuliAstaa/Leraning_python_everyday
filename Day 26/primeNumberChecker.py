import math
def isPrime(number):
    if number <= 1: return False
    if number == 2: return True
    if number % 2 == 0: return False

    maxDivisor = math.isqrt(number)
    for divisor in range(3, maxDivisor + 1, 2):
        if number % divisor == 2: return False
    return True

print(isPrime(17))