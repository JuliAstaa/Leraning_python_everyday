class Buku:
    def __init__(self, judul, penulis, tahun_terbit, harga):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit
        self.harga = harga
        pass

    def tampilkan_info(self):
        print(f"Judul: {self.judul}")
        print(f"Penulis: {self.penulis}")
        print(f"Tahun Terbit: {self.tahun_terbit}")
        print(f"Harga: {self.harga}")
        pass

class TokoBuku:
    def __init__(self):
        self.daftarBuku = []
        pass

    def tambahkan_buku(self, buku):
        self.daftarBuku.append(buku)
        pass

    def cari_buku(self, judul):
        for buku in self.daftarBuku:
            if buku.judul == judul:
                return buku
        pass

    def tampilkan_semua_buku(self):
        for buku in self.daftarBuku:
            buku.tampilkan_info()
        pass

    def hapus_buku(self, judul):
        buku = self.cari_buku(judul)
        if buku:
            self.daftarBuku.remove(buku)
            print(f"Buku dengan judul '{judul}' telah dihapus dari daftar.")
        else:
            print(f"Buku dengan judul '{judul}' tidak ditemukan")
        pass

# Potongan kode di bawah ini merupakan contoh penggunaan kelas yang telah dibuat
toko_buku = TokoBuku()

buku1 = Buku("Harry Potter", "J.K. Rowling", 1997, 150000)
buku2 = Buku("The Lord of the Rings", "J.R.R. Tolkien", 1954, 200000)

toko_buku.tambahkan_buku(buku1)
toko_buku.tambahkan_buku(buku2)

print("Semua buku yang tersedia:")
toko_buku.tampilkan_semua_buku()

print("\nMencari buku dengan judul 'Harry Potter':")
hasil_cari = toko_buku.cari_buku("Harry Potter")
if hasil_cari:
    print("Buku ditemukan:")
    hasil_cari.tampilkan_info()
else:
    print("Buku tidak ditemukan.")

print("\nMenghapus buku dengan judul 'The Lord of the Rings'")
toko_buku.hapus_buku("The Lord of the Rings")

print("\nSemua buku setelah penghapusan:")
toko_buku.tampilkan_semua_buku()
