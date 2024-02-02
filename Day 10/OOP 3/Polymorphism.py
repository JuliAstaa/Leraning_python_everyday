"""
Polymorphism is one of the concepts in programming that allows objects of different classes to have different behaviors on the same method. In other words, polymorphism allows a function or method to behave differently depending on the data type or class of the object being operated on.
"""


class Hero:
    def __init__(self, name:str, role:str, atk:int, magic:int, health:int, armor:int):
        self.name = name
        self.role = role
        self.atk = atk
        self.magic = magic
        self.health = health
        self.armor = armor

    def heroInfo(self):
        print(F"Name: {self.name}")
        print(F"Role: {self.role}")
        print(F"Attack: {self.atk}")
        print(F"Magic Power: {self.magic}")
        print(F"Health: {self.health}")
        print(F"Armour: {self.armor}")

    def attackType(self):
        print('Melee and Range')


class Mage(Hero):
    def __init__(self, name: str, role: str, atk: int, magic: int, health: int, armor: int):
        self.range = 'Range'
        super().__init__(name, role, atk, magic, health, armor)

    def heroInfo(self):
        return super().heroInfo()
    
    def attackType(self):
        print(F"Attack Type: {self.range}")


class Fighter(Hero):
    def __init__(self, name: str, role: str, atk: int, magic: int, health: int, armor: int):
        self.range = 'Melee'
        super().__init__(name, role, atk, magic, health, armor)

    def heroInfo(self):
        return super().heroInfo()
    
    def attackType(self):
        print(F"Attack Type: {self.range}")
        


Lunox = Mage(name='Lunox', role='Mage', atk=143, magic=400, health=3400, armor=30)
Alucard = Fighter(name='Aluacrd', role='Fighter', atk=300, magic=0, health=5000, armor=50)

for hero in (Lunox, Alucard):
    hero.heroInfo()
    hero.attackType()
    print('\n')