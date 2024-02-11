class Kontak:
    def __init__(self, nama:str, nomorTelepon:int):
        self.nama = nama
        self.nomorTelepon = nomorTelepon

    def tampilkanInfo(self):
        print(f"Nama: {self.nama}, Nomor Telepon: {self.nomorTelepon}")
    
class DaftarKontak:
    def __init__(self):
        self.daftarContact = []

    def tambahKontak(self, nama:str, nomorTelepon:int):
        newKontak = Kontak(nama=nama, nomorTelepon=nomorTelepon)
        self.daftarContact.append(newKontak)

    def showDaftarKontak(self):
        print("Daftar kontak:\n")
        for kontak in self.daftarContact:
            kontak.tampilkanInfo()

    def searchKontak(self, nama:str):
        ditemukan = False
        for kontak in self.daftarContact:
            if kontak.nama.lower() == nama.lower():
                print(f"Kontak dengan nama '{nama}' ditemukan:")
                kontak.tampilkanInfo()
                ditemukan = True
                break
        
        if not ditemukan:
            print(f"Kontak dengan nama '{nama}' tidak ditemukan.")


# Membuat objek daftar_kontak
daftar_kontak = DaftarKontak()

# Menambahkan kontak
daftar_kontak.tambahKontak("John", "123456789")
daftar_kontak.tambahKontak("Alice", "987654321")

# Menampilkan semua kontak
daftar_kontak.showDaftarKontak()

# Mencari kontak berdasarkan nama
daftar_kontak.searchKontak("John")