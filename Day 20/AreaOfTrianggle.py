""" 
Write a Python program to calculate the area of a triangle based on its base and height.
"""

class Triangle:
    def __init__(self, base:int, height:int):
        self.base = base
        self.height = height
    
    def areaOfTriangle(self):
        return 1/2 * self.base * self.height
    

triangle = Triangle(base=14, height=20)
print(triangle.areaOfTriangle())
