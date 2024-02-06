import math

class Calculator:
    def __init__(self, num1: int, num2: int) -> None:
        self.num1 = num1
        self.num2 = num2

    def sum(self):
        print(F"{self.num1} + {self.num2} = {self.num1 + self.num2}")
    
    def substract(self):
        print(F"{self.num1} - {self.num2} = {self.num1 - self.num2}")

    def multiply(self):
        print(F"{self.num1} x {self.num2} = {self.num1 * self.num2}")

    def divided(self):
        if self.num2 == 0 : print(F"Undefined")
        print(F"{self.num1} / {self.num2} = {self.num1 / self.num2}")
    
    def power(self):
        print(F"{self.num1}^{self.num2} = {self.num1 ** self.num2}")

    def square_root(self):
        if self.num1 < 0 : print("Cannot calculate square root of a negative number")
        print(F"Square root of {self.num1} = {math.sqrt(self.num1)}")


calc = Calculator(7, 8)
calc.sum()
calc.substract()
calc.multiply()
calc.divided()
calc.power()
calc.square_root()



def factorial(num):
    if num == 0: 
        return 1
    else:
        return num * factorial(num - 1)
    
print(factorial(5))
