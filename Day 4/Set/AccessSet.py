"""
You cannot access items in a set by referring to an index or a key.

But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
"""

setBunga = {"Mawar", "Melati", "Anggrek", "Tulip", "Lavender"}
for bunga in setBunga:
    print(bunga) #output: Tulip Mawar Anggrek Lavender Melati

# check item in set
setBunga = {"Mawar", "Melati", "Anggrek", "Tulip", "Lavender"}
if 'Mawar' in setBunga: #output: ya ada
    print('Ya ada')
else:
    print('tidak ada')
 

