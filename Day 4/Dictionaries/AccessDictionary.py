# access item in dictioanry, you can access the items of a dictionary by referring to its key name, inside square brackets:
# ex:
people = {
    'name': 'John Doe',
    'age': 23,
    'email': 'johndoe@gmail.com',
    'single': True
}

print(people['single']) #output: True

# There is also a method called get() that will give you the same result:
car = dict(brand= 'Ford', model='Mustang', year=1964, colors=['red', 'yellow', 'blue'])
print(car.get('colors')) #output: ['red', 'yellow', 'blue']

# The keys() method will return a list of all the keys in the dictionary.
siswa = {
    "nama": "Andi",
    "umur": 17,
    "kelas": "XI IPA 1",
    "nilai": {
        "matematika": 90,
        "bahasa_inggris": 85,
        "fisika": 88
    }
}

key = siswa.keys()
print(key) #output: dict_keys(['nama', 'umur', 'kelas', 'nilai'])

# The values() method will return a list of all the values in the dictionary.
buku = {
    "judul": "Python Programming for Beginners",
    "penulis": "John Smith",
    "tahun_terbit": 2022,
    "penerbit": "Tech Books",
    "harga": 150000
}

ValueOfBook = buku.values()
print(ValueOfBook) #output: dict_values(['Python Programming for Beginners', 'John Smith', 2022, 'Tech Books', 150000])

# check if key exists
makanan = {
    "nama": "Nasi Goreng",
    "jenis": "Makanan Utama",
    "harga": 25000,
    "rating": 4.5,
    "bahan": ["nasi", "telur", "udang", "bawang merah", "bawang putih", "saus tiram", "kecap", "garam", "merica"],
    "resep": "Tumis bawang merah dan bawang putih hingga harum, masukkan telur dan aduk hingga setengah matang. Tambahkan udang dan aduk hingga matang. Masukkan nasi, saus tiram, kecap, garam, dan merica. Aduk rata hingga nasi terasa panas. Sajikan."
}

if 'resep' in makanan : #output: Ya makanan itu ada resepnya
    print('Ya makanan itu ada resepnya')