"""
Buatlah sebuah kelas BankAccount yang merepresentasikan sebuah rekening bank dengan atribut account_number, holder_name, balance, dan pin. Implementasikan encapsulation untuk memastikan bahwa nilai balance dan pin hanya dapat diakses dari dalam kelas BankAccount dan tidak dapat diubah secara langsung dari luar kelas. Berikan juga metode deposit() untuk menambahkan saldo dan withdraw() untuk menarik saldo, dengan memerlukan PIN untuk validasi.

1. Buat kelas BankAccount dengan atribut account_number, holder_name, balance, dan pin. Pastikan nilai balance dan pin tidak bisa diakses secara langsung dari luar kelas.
2. Berikan metode deposit(amount) untuk menambahkan saldo.
3. Berikan metode withdraw(amount, pin) untuk menarik saldo dengan memerlukan PIN untuk validasi. Pastikan saldo mencukupi sebelum melakukan penarikan.
"""


class BankAccount:
    def __init__(self, account_number:int, holder_name:str, balance:int, pin:int):
        self.__account_number = account_number
        self.holder_name = holder_name
        self.__balance = balance
        self.__pin = pin

    def UserInformation(self):
        print("Bank Accout: ")
        print(F"Account Number: {self.__account_number}")
        print(F"Holder Name: {self.holder_name}")
        print(F"Balance: ${self.__balance}")
        print()

    def deposit(self, ammount:int):
        print(F"Deposit ${ammount}")
        self.__balance += ammount
        print(F"Balance: ${self.__balance}")
        print()
    
    def withdraw(self, ammount:int, pin:int):
        print(F"Withdrawing {ammount} from the account")
        if pin != self.__pin:
            print(F"Wrong Pin, Withdrawal failed")
        else:
            self.__balance -= ammount
            print(F"Withdrawal successful. Remaining balance: {self.__balance}")


John = BankAccount(account_number=1432432343212341, holder_name='John Doe', balance=5000, pin=254313)
John.UserInformation()
John.deposit(ammount=3000)
John.withdraw(ammount=100, pin=254313)