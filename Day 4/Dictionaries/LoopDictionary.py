#loop dictionary
# You can loop through a dictionary by using a for loop. When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.

makanan = {
    "nama": "Nasi Goreng",
    "jenis": "Makanan Utama",
    "harga": 25000,
    "rating": 4.5,
    "bahan": ["nasi", "telur", "udang", "bawang merah", "bawang putih", "saus tiram", "kecap", "garam", "merica"],
    "resep": "Tumis bawang merah dan bawang putih hingga harum, masukkan telur dan aduk hingga setengah matang. Tambahkan udang dan aduk hingga matang. Masukkan nasi, saus tiram, kecap, garam, dan merica. Aduk rata hingga nasi terasa panas. Sajikan."
}

# Print all key names in the dictionary, one by one:
for maem in makanan:
    print(maem)
"""
output:
nama
jenis
harga
rating
bahan
resep
"""

#  print all value in the dictionary, one by one
anak_anak_dict = {
    "Ali": {
        "usia": 8,
        "jenis_kelamin": "laki-laki",
        "hobi": ["main sepak bola", "membaca buku cerita"]
    },
    "Bella": {
        "usia": 6,
        "jenis_kelamin": "perempuan",
        "hobi": ["mewarnai", "bermain boneka"]
    },
    "Citra": {
        "usia": 9,
        "jenis_kelamin": "perempuan",
        "hobi": ["berkebun", "menggambar"]
    }
}

for nama in anak_anak_dict:
    print(anak_anak_dict[nama])
"""
output:
{'usia': 8, 'jenis_kelamin': 'laki-laki', 'hobi': ['main sepak bola', 'membaca buku cerita']}        
{'usia': 6, 'jenis_kelamin': 'perempuan', 'hobi': ['mewarnai', 'bermain boneka']}
{'usia': 9, 'jenis_kelamin': 'perempuan', 'hobi': ['berkebun', 'menggambar']}
"""

# u also can use keys() to print all keys in the dictionary
ceweJepang={
    "Aiko": True,
    "Yumi": True,
    "Haruka": True,
    "Sakura": True,
    "Hina": True
}
for ceweJp in ceweJepang.keys():
    print(ceweJp)
"""
output:
Aiko
Yumi
Haruka
Sakura
Hina
"""

# u also can use  values() to print all values in the dictionary
film_dict = {
    "judul": "Inception",
    "genre": ["Action", "Adventure", "Sci-Fi", "Thriller"],
    "tahun_rilis": 2010,
    "rating_imdb": 8.8,
    "durasi": 148  # dalam menit
}

for film in film_dict.values():
    print(film)
"""
output:
Inception
['Action', 'Adventure', 'Sci-Fi', 'Thriller']
2010
8.8
148
"""

# loop through keys and values, by using item() method:
animeDict = {
    "One Piece": {
        "rating": 8.58,
        "genre": ["Action", "Adventure", "Comedy", "Drama", "Fantasy", "Shounen"]
    },
    "Attack on Titan": {
        "rating": 8.52,
        "genre": ["Action", "Drama", "Fantasy", "Military", "Mystery", "Shounen", "Super Power"]
    },
    "Naruto": {
        "rating": 7.93,
        "genre": ["Action", "Adventure", "Comedy", "Super Power", "Martial Arts", "Shounen"]
    },
    "Death Note": {
        "rating": 8.63,
        "genre": ["Mystery", "Psychological", "Supernatural", "Thriller"]
    },
    "My Hero Academia": {
        "rating": 8.38,
        "genre": ["Action", "Comedy", "School", "Shounen", "Super Power"]
    }
}

for key, value in animeDict.items():
    print(key, value)
"""
output:
One Piece {'rating': 8.58, 'genre': ['Action', 'Adventure', 'Comedy', 'Drama', 'Fantasy', 'Shounen']}
Attack on Titan {'rating': 8.52, 'genre': ['Action', 'Drama', 'Fantasy', 'Military', 'Mystery', 'Shounen', 'Super Power']}
Naruto {'rating': 7.93, 'genre': ['Action', 'Adventure', 'Comedy', 'Super Power', 'Martial Arts', 'Shounen']}
Death Note {'rating': 8.63, 'genre': ['Mystery', 'Psychological', 'Supernatural', 'Thriller']}       
My Hero Academia {'rating': 8.38, 'genre': ['Action', 'Comedy', 'School', 'Shounen', 'Super Power']}
"""