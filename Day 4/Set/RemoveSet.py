# To remove an item in a set, use the remove(), or the discard() method.
# ex:
set_hewan = {"Singa", "Gajah", "Jerapah", "Harimau", "Kuda"}
set_hewan.remove('Singa')
print(set_hewan) #output: {"Gajah", "Jerapah", "Harimau", "Kuda"}
# Note: If the item to remove does not exist, remove() will raise an error.

# Remove "banana" by using the discard() method:
# ex:
set_buah = {"Apel", "Jeruk", "Anggur", "Pisang", "Strawberi"}
set_buah.discard('Jeruk')
print(set_buah) #output: {"Apel", "Anggur", "Pisang", "Strawberi"}
# Note: If the item to remove does not exist, discard() will NOT raise an error.

# remove random item using method pop(), because set is unordered so we do not know which item that gets removed
# ex:
set_warna = {"Merah", "Biru", "Hijau", "Kuning", "Ungu"}
set_warna.pop()
print(set_warna) #output: {'Kuning', 'Merah', 'Ungu', 'Hijau'}, note! the output is random

# clear(), to clear the set
set_benda = {"Meja", "Kursi", "Lampu", "Buku", "Jam"}
set_benda.clear()
print(set_benda) #output: set()

# delete set use del
set_mata_uang = {"Dolar", "Euro", "Yen", "Poundsterling", "Rupiah"}
del set_mata_uang # if we print it, it will be return 'set_mata_uang' is not defined, because we deletes the set


