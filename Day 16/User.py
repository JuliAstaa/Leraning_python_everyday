class User:
    def __init__(self, username:str, email:str,  password:str, firstPetName):
        self.user_Id = 0
        self.username = username
        self.email = email
        self.__password = password
        self.__firstPetName = firstPetName
    

    def UserInformation(self):
        return F"Username: {self.username}\nEmail: {self.email}\n"


def addUser():
    userList = []
    print("Masukkan user")
    while True:
        username = input("Masukkan username atau ketik 'selesai' untuk berhenti: ")
        if username.lower() == 'selesai':
            break

        email = input("Masukkan email: ")
        password = input("Masukkan password: ")
        firstPetName = input("Masukkan nama hewan peliharaan anda: ")
        user = User(username=username, email=email, password=password, firstPetName=firstPetName)
        userList.append(user)
        print("\b")
    return userList

userList = addUser()
print("\n")
print("Informasi User")
for user in userList:
    print(user.UserInformation())




