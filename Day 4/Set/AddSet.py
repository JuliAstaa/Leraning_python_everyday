# Once a set is created, you cannot change its items, but you can add new items.
# To add one item to a set use the add() method.
# ex:
setBunga = {"Mawar", "Melati", "Anggrek", "Tulip"}
setBunga.add('Lavender')
print(setBunga) #output: {'Tulip', 'Lavender', 'Mawar', 'Melati', 'Anggrek'}

# To add items from another set into the current set, use the update() method.
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset) #outpu: {'apple', 'pineapple', 'mango', 'papaya', 'cherry', 'banana'}