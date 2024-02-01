"""
3.
Andi memiliki sebuah toko online yang menjual berbagai macam produk. Dia ingin membuat program untuk mengelola data produk-produk yang tersedia untuk dijual. Setiap produk memiliki atribut seperti nama, harga, dan stok.

1. Buatlah sebuah kelas Produk yang memiliki atribut-atribut tersebut dan metode informasi() untuk menampilkan informasi tentang produk.
2. Andi juga memiliki produk-produk unggulan yang memiliki fitur tambahan. Buatlah sebuah subclass dari kelas Produk dengan nama ProdukUnggulan. Produk unggulan memiliki atribut tambahan berupa diskon harga.
3. Implementasikan metode informasi() di kelas ProdukUnggulan agar mencakup informasi tambahan tentang diskon harga.
4. Buatlah beberapa objek produk dan produk unggulan, lalu tampilkan informasi tentang produk-produk tersebut.
"""

class Toko:
    def __init__(self, nama:str, harga:int, stok:int):
        self.nama = nama
        self.harga = harga
        self.stok = stok
        pass

    def informasi(self):
        print(F"Nama: {self.nama}")
        print(F"Harga: {self.harga}")
        print(F"Stok: {self.stok}")

class ProdukUnggulan(Toko):
    def __init__(self, nama: str, harga: int, stok: int, diskon: int):
        self.diskon = diskon
        super().__init__(nama, harga, stok)
        pass

    def informasi(self):
        super().informasi()
        print(F"Diskon: {self.diskon}")
        pass


aqua = Toko(nama='Aqua', harga=5000, stok=50)
aqua.informasi()

print("\n")

produkUnggulan = ProdukUnggulan(nama='Sendok sop abad-17', harga=100000000, stok=1, diskon=2)
produkUnggulan.informasi()