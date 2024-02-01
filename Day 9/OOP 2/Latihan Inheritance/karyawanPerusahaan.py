"""
2.
Andi adalah seorang manajer HR di sebuah perusahaan besar. Dia ingin membuat program untuk mengelola data karyawan. Setiap karyawan memiliki atribut seperti nama, usia, dan gaji pokok.

1. Buatlah sebuah kelas Karyawan yang memiliki atribut-atribut tersebut dan metode informasi() untuk menampilkan informasi tentang karyawan.
2. Andi juga memiliki karyawan-karyawan yang memiliki jabatan spesifik. Buatlah beberapa subclass dari kelas Karyawan dengan nama Manajer, Staf, dan Magang. Setiap subclass memiliki atribut tambahan seperti departemen untuk Manajer, posisi untuk Staf, dan lama magang untuk Magang.
3. Implementasikan metode informasi() di setiap subclass agar mencakup informasi tambahan tentang atribut tambahan yang relevan.
4. Buatlah beberapa objek karyawan dengan berbagai jabatan, lalu tampilkan informasi tentang karyawan-karyawan tersebut.
"""

class Karyawan():
    def __init__(self, nama:str, usia:int, gaji:int):
        self.nama = nama
        self.usia = usia
        self.gaji = gaji
        pass

    def informasi(self):
        print(F"Nama: {self.nama}")
        print(F"Usia: {self.usia}")
        print(F"Gaji: {self.nama}")
        pass


class Manajer(Karyawan):
    def __init__(self, nama: str, usia: int, gaji: int, departemen: str):
        self.departemen = departemen
        super().__init__(nama, usia, gaji)
        pass

    def informasi(self):
        super().informasi()
        print(F"Departemen: {self.departemen}")
        pass

class Staff(Karyawan):
    def __init__(self, nama: str, usia: int, gaji: int, posisi: str):
        self.posisi = posisi
        super().__init__(nama, usia, gaji)
        pass

    def informasi(self):
        super().informasi()
        print(F"Posisi: {self.posisi}")
        pass
    
class Magang(Karyawan):
    def __init__(self, nama: str, usia: int, gaji: int, awalMagang: str, akhirMagang: str):
        self.awalMagang = awalMagang
        self.akhirMagang = akhirMagang
        super().__init__(nama, usia, gaji)
        pass

    def informasi(self):
        super().informasi()
        print(F"Awal magang: {self.awalMagang}")
        print(F"Akhir magang: {self.akhirMagang}")
        pass

manajer = Manajer(nama="Wahyudi", usia=34, gaji=10000000, departemen='Keuangan')
manajer.informasi()

print('\n')

staff = Staff(nama='Johny', usia=28, gaji=8000000,posisi='Supervisor')
staff.informasi()

print('\n')

magang = Magang(nama='Iso', usia=17, gaji=1000000, awalMagang='12 Januari 2023', akhirMagang='12 Juli 2023')
magang.informasi()