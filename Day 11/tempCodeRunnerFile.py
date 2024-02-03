
    def CharacterInformation(self):
        super().CharacterInformation()


Ilnisiya = Mage(name='Ilnisiya', attack=120, magicPower=300, armour=35, health=3000)
print(F"{Ilnisiya.name} - {Ilnisiya.role}")
print('\b')
Ilnisiya.CharacterInformation()
print('\b')
Ilnisiya.basicAttack()