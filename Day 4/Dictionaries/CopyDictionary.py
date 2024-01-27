# copy dictionary

#You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.
# There are ways to make a copy, one way is to use the built-in Dictionary method copy().
galaxy_dict = {
    "Andromeda": {
        "tipe": "Spiral",
        "jarak": "2.537 juta tahun cahaya",
        "ukuran": "sekitar 220.000 tahun cahaya diameter"
    },
    "Bima Sakti": {
        "tipe": "Spiral",
        "jarak": "sekitar 100.000 tahun cahaya",
        "ukuran": "sekitar 100.000 tahun cahaya diameter"
    },
    "Sombrero": {
        "tipe": "Spiral",
        "jarak": "28 juta tahun cahaya",
        "ukuran": "sekitar 50.000 tahun cahaya diameter"
    },
    "Elips": {
        "tipe": "Elipsoidal",
        "jarak": "2 juta tahun cahaya",
        "ukuran": "sekitar 700.000 tahun cahaya diameter"
    }
}

copyOfGalaxy = galaxy_dict.copy()
copyOfGalaxy.update({
    "Whirlpool": {
        "tipe": "Spiral",
        "jarak": "23 juta tahun cahaya",
        "ukuran": "sekitar 60.000 tahun cahaya diameter"
    },
    "Triangulum": {
        "tipe": "Spiral",
        "jarak": "sekitar 3 juta tahun cahaya",
        "ukuran": "sekitar 50.000 tahun cahaya diameter"
    },
    "Cigar": {
        "tipe": "Elipsoidal",
        "jarak": "12 juta tahun cahaya",
        "ukuran": "sekitar 30.000 tahun cahaya diameter"
    },
    "Cartwheel": {
        "tipe": "Ring",
        "jarak": "500 juta tahun cahaya",
        "ukuran": "sekitar 150.000 tahun cahaya diameter"
    }
})
print('Galaxy 1: \n', galaxy_dict, '\n')
print('Copy of galaxy and add more galaxy: \n',copyOfGalaxy)
"""
output:

Galaxy 1: 
 {'Andromeda': {'tipe': 'Spiral', 'jarak': '2.537 juta tahun cahaya', 'ukuran': 'sekitar 220.000 tahun cahaya diameter'}, 'Bima Sakti': {'tipe': 'Spiral', 'jarak': 'sekitar 100.000 tahun cahaya', 'ukuran': 'sekitar 100.000 tahun cahaya diameter'}, 'Sombrero': {'tipe': 'Spiral', 'jarak': '28 juta tahun cahaya', 'ukuran': 'sekitar 50.000 tahun cahaya diameter'}, 'Elips': {'tipe': 'Elipsoidal', 'jarak': '2 juta tahun cahaya', 'ukuran': 'sekitar 700.000 tahun cahaya diameter'}}

Copy of galaxy and add more galaxy:
 {'Andromeda': {'tipe': 'Spiral', 'jarak': '2.537 juta tahun cahaya', 'ukuran': 'sekitar 220.000 tahun cahaya diameter'}, 'Bima Sakti': {'tipe': 'Spiral', 'jarak': 'sekitar 100.000 tahun cahaya', 'ukuran': 'sekitar 100.000 tahun cahaya diameter'}, 'Sombrero': {'tipe': 'Spiral', 'jarak': '28 juta tahun cahaya', 'ukuran': 'sekitar 50.000 tahun cahaya diameter'}, 'Elips': {'tipe': 'Elipsoidal', 'jarak': '2 juta tahun cahaya', 'ukuran': 'sekitar 700.000 tahun cahaya diameter'}, 'Whirlpool': {'tipe': 'Spiral', 'jarak': '23 juta tahun cahaya', 'ukuran': 'sekitar 60.000 tahun cahaya diameter'}, 'Triangulum': {'tipe': 'Spiral', 'jarak': 'sekitar 3 juta tahun cahaya', 'ukuran': 'sekitar 50.000 tahun cahaya diameter'}, 'Cigar': {'tipe': 'Elipsoidal', 'jarak': '12 juta tahun cahaya', 'ukuran': 'sekitar 30.000 tahun cahaya diameter'}, 'Cartwheel': {'tipe': 'Ring', 'jarak': '500 juta tahun cahaya', 'ukuran': 'sekitar 150.000 tahun cahaya diameter'}}

"""