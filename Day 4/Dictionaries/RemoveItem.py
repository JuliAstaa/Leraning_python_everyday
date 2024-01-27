# remove item
# There are several methods to remove items from a dictionary:
# The pop() method removes the item with the specified key name:
# ex:
buahDict = {
    "apel": True,
    "pisang": True,
    "jeruk": True,
    "mangga": True,
    "semangka": True
}

buahDict.pop('mangga')
print(buahDict) #output: {'apel': True, 'pisang': True, 'jeruk': True, 'semangka': True}

# The popitem() method removes the last inserted item
ceweJepang={
    "Aiko": True,
    "Yumi": True,
    "Haruka": True,
    "Sakura": True,
    "Hina": True
}

ceweJepang.popitem()
print(ceweJepang) #output: {'Aiko': True, 'Yumi': True, 'Haruka': True, 'Sakura': True}

# The del keyword removes the item with the specified key name:
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

del animeDict['One Piece']
print(animeDict) #output: {'Attack on Titan': {'rating': 8.52, 'genre': ['Action', 'Drama', 'Fantasy', 'Military', 'Mystery', 'Shounen', 'Super Power']}, 'Naruto': {'rating': 7.93, 'genre': ['Action', 'Adventure', 'Comedy', 'Super Power', 'Martial Arts', 'Shounen']}, 'Death Note': {'rating': 8.63, 'genre': ['Mystery', 'Psychological', 'Supernatural', 'Thriller']}, 'My Hero Academia': {'rating': 8.38, 'genre': ['Action', 'Comedy', 'School', 'Shounen', 'Super Power']}}

# The del keyword can also delete the dictionary completely:
film_dict = {
    "judul": "Inception",
    "genre": ["Action", "Adventure", "Sci-Fi", "Thriller"],
    "tahun_rilis": 2010,
    "rating_imdb": 8.8,
    "durasi": 148  # dalam menit
}

del film_dict #output: 'film_dict' is not defined


# The clear() method empties the dictionary:
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
anak_anak_dict.clear()
print(anak_anak_dict) #output: {}