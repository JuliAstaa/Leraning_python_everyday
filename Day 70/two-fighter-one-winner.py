""" 
Each fighter takes turns attacking the other and whoever kills the other first is victorious. Death is defined as having healt <= 0

Each fighter will be a fighter object/instance. See the fighter class bellow in  your choosen languange

Both health  and damage_per_attack will be integers larger than 0. You can mutate the FIghter object

Your function also receives a third argument, a strinh, with the name of the fighter that attack first

Example:
declare_winner(Fighter("lew", 10, 2), Fighter("Hary", 5, 4), "Lew") -> "Lew"

Lew attacks harry, now Harry has 3 health
Harry attacks Lew, Lew now has 6 health
Lew attacks harry, harry now has 1 health
Harry attacks lew, lew now has 2 health
Lew attacks Harry, Harry now has -1 health
"""

class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack
        
    def __str__(self): return "Fighter({}, {}, {})".format(self.name, self.health, self.damage_per_attack)
    __repr__=__str__

def declare_winner(fighter1, fighter2, first_attacker):


    attacker, defender = (fighter1, fighter2) if fighter1.name == first_attacker else (fighter2, fighter1)

    while attacker.health > 0 and defender.health > 0:
        defender.health -= attacker.damage_per_attack
        attacker, defender = defender, attacker
    
    return defender.name




print(declare_winner(Fighter("Jerry", 30, 3), Fighter("Harald", 20, 5), "Jerry"))