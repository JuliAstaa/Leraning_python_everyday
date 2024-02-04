"""
Encapsulation is an important concept in object-oriented programming that helps in hiding certain details of an object's implementation and exposing only essential functionality through public methods.
"""

class User:
    def __init__(self, name:str, username:str, password:str):
        self.name = name
        self.username = username
        self.__password = password

    def userInformation(self):
        print(F"Name: {self.name}")
        print(F"Username: {self.username}")

    def passwordInformation(self):
        print(F"Password: {self.__password}")

    def resetPassword(self, newPassword:str):
        self.__password = newPassword
    
User1 = User(name='Budi Budiono', username='budiono123', password='sukablyatt')
User1.userInformation()
User1.passwordInformation()
User1.resetPassword(newPassword='aowowowo')
User1.passwordInformation()