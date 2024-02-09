class User:
    def __init__(self, name:str, username:str, password:str):
        self.name = name
        self.username = username
        self.__password = password

    def UserInformation(self):
        return F"Name: {self.name}\nUsername: {self.username}"
    
    def getNewPassword(self, newPassword:str):
        self.__password = newPassword
    

def addUser():
    print("Tambahkan user")
    name = input("Masukkan nama anda: ")
    username = input("Masukkan username anda: ")
    password = input("Masukkan password anda: ")
    return User(name=name, username=username, password=password)

def readUser(users):
    print("Data User")
    for user in users:
        print(user.UserInformation())
        print()

def updateUser(user):
    print("Perbarui data user, kosongkan data jika tidak ingin merubahnya")
    user.username = input("Masukkan username baru: ") or user.username
    newPassword = input ("Masukkan password baru: ") or user.__password
    user.getNewPassword(newPassword=newPassword)


def deleteUser(users, id):
    for index, user in enumerate(users):
        if user.id == int(id) :
            del users[index]
            print(f"User dengan ID {id} berhasil dihapus.")
            return
    print(f"Tidak ada user dengan ID {id}.")


def main():
    users = []
    while True:
        print("\nMenu")
        print("1. Add new user")
        print("2. Get users information")
        print("3. Edit user")
        print("4. Delete user")
        print("5. Exit")
        choice = input("Pilih menu: ")

        if choice == "1":
            newUser = addUser()
            newUser.id = len(users) + 1
            users.append(newUser)

        elif choice == "2":
            readUser(users)
        
        elif choice == "3":
            id = input("Masukkan id user: ")
            for user in users:
                if user.id == int(id):
                    updateUser(user)
                else:
                    print(F"User dengan id {id} tidak ditemukan")
        elif choice == "4":
            id = input("Masukkan id user: ")
            deleteUser(users=users, id=id)
        elif choice == "5":
            print("Terimakasih")
            break
        else:
            print("Input tidak valid")


if __name__ == "__main__":
    main()