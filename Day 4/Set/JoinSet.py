# join set
# You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another

# union() ex:
setBuah1 = {"Apel", "Jeruk", "Anggur"}
setBuah2 = {"Pisang", "Strawberi"}

setBuah3 = setBuah1.union(setBuah2)
print(setBuah3) #output: {'Pisang', 'Apel', 'Anggur', 'Jeruk', 'Strawberi'}

# update() ex:
setWarna1 = {"Merah", "Biru"}
setWarna2 = {"Hijau", "Kuning", "Ungu"}
setWarna1.update(setWarna2)

print(setWarna1) #output: {'Ungu', 'Kuning', 'Merah', 'Hijau', 'Biru'}

# Keep ONLY the Duplicates
# The intersection_update() method will keep only the items that are present in both sets.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}
set1.intersection_update(set2)
print(set1) #output: {4,5}

# The intersection() method will return a new set, that only contains the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z) #output: {'apple'}

# keep all, except the duplicate
# The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
setBuahBuahan1 = {"Apel", "Jeruk", "Pisang", "Anggur", "Melon"}
setBuahBuahan2 = {"Jeruk", "Anggur", "Mangga", "Pepaya", "Durian"}
setBuahBuahan1.symmetric_difference_update(setBuahBuahan2)
print(setBuahBuahan1) #output: {'Apel', 'Pisang', 'Mangga', 'Pepaya', 'Melon', 'Durian'}

# The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.
setHewanSatu = {"Singa", "Harimau", "Gajah", "Jerapah"}
setHewanDua = {"Singa", "Jerapah", "Zebra", "Kuda"}
setHewanTiga = setHewanSatu.symmetric_difference(setHewanDua)
print(setHewanTiga) #output: {'Gajah', 'Zebra', 'Kuda', 'Harimau'}
