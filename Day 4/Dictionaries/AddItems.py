# Adding an item to the dictionary is done by using a new index key and assigning a value to it:
# ex:
car = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}

car['color'] ='yellow'
print(car) #output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'yellow'}

# update dictionary, The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.
# ex:
myFood = {
    'name': 'Nasi Goreng',
    'hot': False,
    'portion': 'large'
}
myFood.update({"price": 18000})
print(myFood) #output: {'name': 'Nasi Goreng', 'hot': False, 'portion': 'large', 'price': 18000}