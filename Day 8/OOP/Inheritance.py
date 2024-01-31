"""
Inheritance, is a concept in object-oriented programming where a class can inherit attributes and methods from another class called the parent class or superclass. The class that inherits is referred to as the subclass or child class.
"""

class Hewan:
    def __init__(self, nama:str):
        self.nama = nama
    
    def namaHewan(self):
        return f"{self.nama}"


class HewanBerkakiEmpat(Hewan):
    def __init__(self, nama: str):
        super().__init__(nama)
        self.jumlah_kaki = 4
    def namaHewan(self):
        return F"{super().namaHewan()}, {self.nama} adalah hewan berkaki {self.jumlah_kaki}"

class HewanBerkakiDua(Hewan):
    def __init__(self, nama: str):
        super().__init__(nama)
        self.jumlah_kaki = 2
    def namaHewan(self):
        return F"{super().namaHewan()}, {self.nama} adalah hewan berkaki {self.jumlah_kaki}"
        
    

sapi = HewanBerkakiEmpat(nama='Sapi')
print(sapi.namaHewan()) #output: Sapi, Sapi adalah hewan berkaki 4

ayam = HewanBerkakiDua(nama='Ayam')
print(ayam.namaHewan()) #output: Ayam, Ayam adalah hewan berkaki 2

kucing = Hewan('Kucing')
print(kucing.namaHewan()) #output: Kucing
