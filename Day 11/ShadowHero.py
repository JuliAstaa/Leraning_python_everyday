"""
Anda sedang mengembangkan permainan video yang melibatkan berbagai jenis karakter. Setiap karakter memiliki kemampuan khususnya sendiri yang memengaruhi cara mereka berinteraksi dengan lingkungan dalam permainan.

Implementasikan struktur kelas untuk karakter-karakter berikut:

1. Character: Kelas dasar untuk semua karakter. Setiap karakter memiliki atribut name dan metode special_ability() yang mencetak kemampuan khusus karakter tersebut.

2. Mage: Subkelas dari Character. Mage memiliki kemampuan khusus untuk melemparkan sihir yang dapat mengubah lingkungan sekitarnya. Implementasikan metode special_ability() untuk mage.

3. Warrior: Subkelas dari Character. Warrior memiliki kemampuan khusus dalam bertarung dan meningkatkan kekuatan saat melawan musuh. Implementasikan metode special_ability() untuk warrior.

4. Archer: Subkelas dari Character. Archer memiliki kemampuan khusus dalam menembakkan panah yang dapat menghancurkan rintangan dalam lingkungan. Implementasikan metode special_ability() untuk archer.

Selain itu, buatlah sebuah fungsi use_special_ability() yang menerima objek karakter dan memanggil metode special_ability() pada objek tersebut.
"""

class Character:
    def __init__(self, name:str, attack:int, magicPower:int, armour:int, health:int):
        self.name = name
        self.attack = attack
        self.magicPower = magicPower
        self.armour = armour
        self.health = health

    def CharacterInformation(self):
        print(F"Character Name: {self.name}")
        print(F"Attack: {self.attack}")
        print(F"Magic Power: {self.magicPower}")
        print(F"Armour: {self.armour}")
        print(F"Health: {self.health}")


class Mage(Character):
    def __init__(self, name: str, attack: int, magicPower: int, armour: int, health: int):
        self.role = 'Mage'
        super().__init__(name, attack, magicPower, armour, health)

    def basicAttack(self):
        print("Basic attack")
        print(F"{self.name} attacks enemies with light waves, and deals 100% physical damage")

    def firstSkill(self):
        print("First skill")
        print(F"{self.name} with the power of light, marks the enemy area with starlight, and deals 150+ (100% magic power) magic power continuously in area")
    
    
    def secondSkill(self):
        print("Second skill")
        print(F"{self.name} heal 50 + (50% magic power) for herself")

    def ultimate(self):
        print("Third skill / Ultimate")
        print(F"{self.name} with her light power, dropped a giant ball of light from the sky, deals 500 + (300% magic power) magic power, and causing darkness for 5 seconds")

    def CharacterInformation(self):
        super().CharacterInformation()

class Warrior(Character):
    def __init__(self, name: str, attack: int, magicPower: int, armour: int, health: int):
        self.role = 'Warrior'
        super().__init__(name, attack, magicPower, armour, health)

    def basicAttack(self):
        print("Basic attack")
        print(F"{self.name} attacks enemies with a giant sword, and deals 100 + (150%) physical damage")

    def firstSkill(self):
        print("First skill")
        print(F"{self.name} leaps forward with his sword, and deals 300 + (150%) physical damage")
    
    def secondSkill(self):
        print("Second skill")
        print(F"{self.name} releases darkness energy from his sword, and deals 150 + (300%) physical damage, and stun enemies for 0.8 seconds")

    def ultimate(self):
        print("Third skill / Ultimate")
        print(F"{self.name} marks all enemies, reducing enemy armor by 50% and increasing his physical attack by 120%")

    def CharacterInformation(self):
        super().CharacterInformation()


class Archer(Character):
    def __init__(self, name: str, attack: int, magicPower: int, armour: int, health: int):
        self.role = 'Archer'
        super().__init__(name, attack, magicPower, armour, health)

    def basicAttack(self):
        print("Basic attack")
        print(F"{self.name} attack the enemy with arrows, and deals 100 + (300%) physical damage")

    def firstSkill(self):
        print("First skill")
        print(F"{self.name} arrows can strike multiple targets (max 5 targets), tapi serangannya berkurang menjadi 100 + (120%)")
    
    def secondSkill(self):
        print("Second skill")
        print(F"{self.name} shoots out a giant arrow, can destroy obstacles, and pierce through enemies deals 300 + (300%) pysical damage")

    def ultimate(self):
        print("Third skill / Ultimate")
        print(F"{self.name} summons a rain of arrows, and deals 100 + (150%) physical damage every 0.5 seconds, for 5 seconds")

    def CharacterInformation(self):
        super().CharacterInformation()


Ilnisiya = Mage(name='Ilnisiya', attack=120, magicPower=300, armour=35, health=3000)
print(F"{Ilnisiya.name} - {Ilnisiya.role}")
print('\b')
Ilnisiya.CharacterInformation()
print('\b')
Ilnisiya.basicAttack()
print('\b')
Ilnisiya.firstSkill()
print('\b')
Ilnisiya.secondSkill()
print('\b')
Ilnisiya.ultimate()

print(F"---------------------------------------------------------------------------------------------------")

Kirei = Warrior(name='Kirei', attack=200, magicPower=0, armour=100, health=4000)
print(F"{Kirei.name} - {Kirei.role}")
print('\b')
Kirei.CharacterInformation()
print('\b')
Kirei.basicAttack()
print('\b')
Kirei.firstSkill()
print('\b')
Kirei.secondSkill()
print('\b')
Kirei.ultimate()

print(F"---------------------------------------------------------------------------------------------------")

Sakura = Archer(name='Sakura', attack=300, magicPower=0, armour=20, health=2800)
print(F"{Sakura.name} - {Sakura.role}")
print('\b')
Sakura.CharacterInformation()
print('\b')
Sakura.basicAttack()
print('\b')
Sakura.firstSkill()
print('\b')
Sakura.secondSkill()
print('\b')
Sakura.ultimate()

print(F"---------------------------------------------------------------------------------------------------")



