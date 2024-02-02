"""
Anda memiliki sebuah program yang mengelola data berbagai bentuk geometri, seperti persegi, lingkaran, dan segitiga. Setiap bentuk memiliki metode hitungLuas(). Implementasikan kelas-kelas untuk masing-masing bentuk geometri dengan metode hitungLuas() yang sesuai. Kemudian, buat sebuah fungsi totalLuas() yang menerima sebuah daftar berisi objek-objek bentuk geometri dan mengembalikan total luas dari semua bentuk tersebut.
"""

class hitungLuas:
    def __init__(self, name: str) -> None:
        self.name = name

    def namaGeometri(self):
        print(F"Nama geometri: ${self.name}")

class segitiga(hitungLuas):
    def __init__(self, name: str, alas:int, tinggi:int) -> None:
        self.alas = alas
        self.tinggi = tinggi
        super().__init__(name)

    def hitungLuasSegitiga(self):
        return 1/2 * self.alas * self.tinggi
    

class persegi(hitungLuas):
    def __init__(self, name: str, sisi: int) -> None:
        self.sisi = sisi
        super().__init__(name)

    def hitungLuasPersegi(self):
        return self.sisi ** 2

class lingkaran(hitungLuas):
    def __init__(self, name: str, jariJari: int) -> None:
        self.jariJari = jariJari
        super().__init__(name)

    def hitungLuasLingkaran(self):
        return 3.14 * self.jariJari ** 2




def totalLuasGeometri(daftarGeometri):
    result = 0
    for geometri in daftarGeometri:
        if isinstance(geometri, segitiga):
            result += geometri.hitungLuasSegitiga()
        elif isinstance(geometri, persegi):
            result += geometri.hitungLuasPersegi()
        elif isinstance(geometri, lingkaran):
            result += geometri.hitungLuasLingkaran()
    
    return result



segitigaKecil = segitiga(name='Segitiga', alas=10, tinggi=8)
persegiKecil = persegi(name='Persegi', sisi=5)
lingkaranKecil = lingkaran(name='Lingkaran', jariJari=7)

daftarGeometri = [segitigaKecil, persegiKecil, lingkaranKecil]

total = totalLuasGeometri(daftarGeometri=daftarGeometri)

print(F"Total luas dari geometri tersebut adalah {total}")