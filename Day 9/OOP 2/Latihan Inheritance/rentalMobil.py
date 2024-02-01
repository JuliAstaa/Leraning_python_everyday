"""
1.
Andi memiliki sebuah perusahaan rental mobil. Dia ingin membuat program untuk mengelola data mobil yang tersedia untuk disewakan. Setiap mobil memiliki atribut seperti merek, model, tahun pembuatan, dan harga sewa per hari.

1. Buatlah sebuah kelas Mobil yang memiliki atribut-atribut tersebut dan metode informasi() untuk menampilkan informasi tentang mobil.
2. Andi juga memiliki mobil-mobil premium yang memiliki fitur tambahan. Buatlah sebuah subclass dari kelas Mobil dengan nama MobilPremium. Mobil premium memiliki atribut tambahan berupa biaya tambahan per hari.
3. Implementasikan metode informasi() di kelas MobilPremium agar mencakup informasi tambahan tentang biaya tambahan per hari.
4. Buatlah beberapa objek mobil dan mobil premium, lalu tampilkan informasi tentang mobil-mobil tersebut.
"""


class Mobil:
    def __init__(self, merek:str, model:str, tahunPembuatan:int, hargaSewaPerHari:int):
        self.merek = merek
        self.model = model
        self.tahunPembuatan = tahunPembuatan
        self.hargaSewaPerHari = hargaSewaPerHari

    def informasi(self):
        print(F"Merek: {self.merek}")
        print(F"model: {self.model}")
        print(F"tahunPembuatan: {self.tahunPembuatan}")
        print(F"hargaSewaPerHari: {self.hargaSewaPerHari}")
       

class MobilPremium(Mobil):
    def __init__(self, merek: str, model: str, tahunPembuatan: int, hargaSewaPerHari: int, biayaTambahanSewaPerHari: int):
        self.biayaTambahanSewaPerHari = biayaTambahanSewaPerHari
        super().__init__(merek, model, tahunPembuatan, hargaSewaPerHari)

    def informasi(self):
        super().informasi()
        print(F"Biaya tambahan harga sewa per hari: {self.biayaTambahanSewaPerHari}")

mobil = Mobil(merek='Ford', model='Mustang', tahunPembuatan=1964, hargaSewaPerHari=10000000)
mobil.informasi()

print('\n')

mobilPremium = MobilPremium(merek='Toyota', model='Supra', tahunPembuatan=1970, hargaSewaPerHari=1200000, biayaTambahanSewaPerHari=1000000)
mobilPremium.informasi()








