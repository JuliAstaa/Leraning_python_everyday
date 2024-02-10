class Car:
    def color(self):
        pass

    def carInformation(self):
        return NotImplementedError("Pakai kelas turunan woiii")


class Ford(Car):
    def __init__(self, model, color):
        super().__init__()
        self.model = model
        self.carColour = color
    
    def color(self):
        return self.carColour
    
    def carInformation(self):
        return F"Name: {self.model}\nColor: {self.carColour}"
    
mustang = Ford(model="Mustang", color='Red')
print(mustang.carInformation())
car = Car()
print(car.carInformation())