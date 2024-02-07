class Employe:
    def __init__(self, name, salary) -> None:
        self.name = name
        self.salary = salary
    
    def __str__(self):
        return F"Name: {self.name}, salary: {self.salary}"


class Manager(Employe):
    def __init__(self, name, salary,departement) -> None:
        super().__init__(name, salary)
        self.departement = departement

    def __str__(self):
         return F"Name: {self.name}, salary: {self.salary}, departement: {self.departement}"

John = Employe(name='John Doe', salary=500)
skirk = Manager(name='Skirk', salary=1000, departement='Sneznaya')
print(John)
print(skirk)