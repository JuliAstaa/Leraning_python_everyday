"""
Python Classes/Objects
Python is an object oriented programming language.

Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects.
"""

class MyClass:
    x = 5;

x = MyClass()
print(x.x) #output: 5

"""
The __init__() Function
The examples above are classes and objects in their simplest form, and are not really useful in real life applications.

To understand the meaning of classes we have to understand the built-in __init__() function.

All classes have a function called __init__(), which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
"""

class Person:
    def __init__(self, name, age) :
        self.name = name
        self.age = age

person1 = Person('John', 25)

print(person1.name) #ouput: John
print(person1.age) #output: 25



"""
The __str__() function controls what should be returned when the class object is represented as a string.

If the __str__() function is not set, the string representation of the object is returned:
"""

class Greeting:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self) -> str:
        return F"Hello my name is {self.name}, and i am {self.age} y.o"

juli = Greeting('Juli', 18)
print(juli) #output: Hello my name is Juli, and i am 18 y.o


class oldOrYoung:
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Nama kamu {self.name}, dan umur kamu {self.age}, berarti kamu {'sudah tua' if self.age > 18 else 'masih muda'}"
    
Yaoming = oldOrYoung('Yaoming', 20)
Xiao = oldOrYoung(name='Xiao', age=15)

print(Yaoming) #output: Nama kamu Yaoming, dan umur kamu 20, berarti kamu sudah tua
print(Xiao) #output: Nama kamu Xiao, dan umur kamu 15, berarti kamu masih muda


class LuasPersegi:
    def __init__(self, sisi:int):
        self.sisi = sisi

    def luasPersegi(self):
        return f"Luas persegi dengan sisi {self.sisi} adalah {self.sisi * self.sisi}"

persegi1 = LuasPersegi(sisi=10)
print(persegi1.luasPersegi()) #output Luas persegi dengan sisi 10 adalah 100